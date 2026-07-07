from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VAULT = ROOT.parent

RAW_DIRS = [
    "00.inbox",
    "10.sources/images",
    "10.sources/videos",
    "10.sources/documents",
    "10.sources/presentations",
    "10.sources/pdfs",
    "10.sources/spreadsheets",
    "10.sources/audio",
    "10.sources/web-clips",
    "10.sources/datasets",
    "10.sources/archives",
    "10.sources/sensitive",
    "20.metadata",
]

PROCESSED = ROOT / "90.processed"
WEEKLY_DIR = PROCESSED / "weekly-knowledge-distill"
MANIFEST_DIR = PROCESSED / "inventory"
LOG_DIR = ROOT / "99.system" / "cache"

TEXT_EXTS = {".md", ".txt", ".csv", ".tsv", ".json", ".yaml", ".yml", ".html", ".htm", ".xml"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}
DOC_EXTS = {".doc", ".docx", ".ppt", ".pptx", ".pdf", ".xls", ".xlsx"}

CATEGORY_RULES = {
    "派工规则": ["派工", "dispatch", "dispatching", "sorting", "qsort", "prefer", "reserve", "pre-reserve", "rule", "规则"],
    "WIP / Cycle Time": ["wip", "cycle time", "queue time", "qtime", "qzone", "overqtime", "堆货", "断线", "在制品"],
    "AMHS / 搬送": ["amhs", "mcs", "oht", "stocker", "ohb", "foup", "搬送", "存储", "load port"],
    "MES / 系统集成": ["mes", "rtd", "ama", "eap", "apc", "pms", "scheduler", "接口", "回写", "状态"],
    "NPW / Monitor": ["npw", "monitor", "dummy", "season", "reuse", "recycle", "downgrade", "dummy"],
    "设备与工艺约束": ["recipe", "capability", "chamber", "tool", "eqp", "pm", "wph", "r2r", "reticle", "机台", "设备"],
    "验证与 SOP": ["testcase", "test case", "sop", "测试", "验证", "验收", "case"],
}


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def sha256_file(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            data = f.read(chunk)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


def iter_raw_files() -> list[Path]:
    files: list[Path] = []
    for d in RAW_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file():
                continue
            if ".venv" in p.parts:
                continue
            if p.name == ".gitkeep":
                continue
            files.append(p)
    return sorted(files, key=lambda p: rel(p).lower())


def build_inventory(files: list[Path]) -> list[dict]:
    inventory = []
    for p in files:
        stat = p.stat()
        suffix = p.suffix.lower()
        if suffix in IMAGE_EXTS:
            kind = "图片"
        elif suffix in {".mp4", ".mov", ".avi", ".mkv", ".wmv"}:
            kind = "视频"
        elif suffix in {".mp3", ".wav", ".m4a", ".flac"}:
            kind = "音频"
        elif suffix in {".pdf"}:
            kind = "PDF"
        elif suffix in {".ppt", ".pptx"}:
            kind = "演示文档"
        elif suffix in {".doc", ".docx"}:
            kind = "文档"
        elif suffix in {".xls", ".xlsx", ".csv", ".tsv"}:
            kind = "表格/数据"
        elif suffix in {".zip", ".rar", ".7z"}:
            kind = "压缩包"
        elif suffix in TEXT_EXTS:
            kind = "文本"
        else:
            kind = "其他"
        inventory.append(
            {
                "path": rel(p),
                "name": p.name,
                "folder": rel(p.parent),
                "suffix": suffix,
                "kind": kind,
                "size": stat.st_size,
                "mtime": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
                "sha256": sha256_file(p) if stat.st_size <= 50 * 1024 * 1024 else "",
            }
        )
    return inventory


def read_text_file(path: Path, max_chars: int = 20000) -> str:
    for enc in ["utf-8", "utf-8-sig", "gb18030", "latin-1"]:
        try:
            return path.read_text(encoding=enc, errors="ignore")[:max_chars]
        except Exception:
            continue
    return ""


def collect_text_corpus(files: list[Path]) -> dict[str, str]:
    corpus = {}
    # raw text files
    for p in files:
        if p.suffix.lower() in TEXT_EXTS and p.stat().st_size > 0 and p.stat().st_size < 5 * 1024 * 1024:
            corpus[rel(p)] = read_text_file(p)
    # processed OCR / notes are important distilled sources too.
    for p in PROCESSED.rglob("*"):
        if not p.is_file() or ".venv" in p.parts:
            continue
        if p.suffix.lower() in {".md", ".txt"} and p.stat().st_size > 0 and p.stat().st_size < 5 * 1024 * 1024:
            corpus[rel(p)] = read_text_file(p)
    return corpus


def score_categories(text: str) -> Counter:
    low = text.lower()
    scores = Counter()
    for cat, terms in CATEGORY_RULES.items():
        for t in terms:
            if t.lower() in low:
                scores[cat] += 1
    return scores


def extract_key_lines(text: str, limit: int = 20) -> list[str]:
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    selected = []
    keywords = [t for terms in CATEGORY_RULES.values() for t in terms]
    for line in lines:
        if len(line) > 240:
            line = line[:240] + "..."
        if any(k.lower() in line.lower() for k in keywords):
            if line not in selected:
                selected.append(line)
        if len(selected) >= limit:
            break
    return selected


def run_image_ocr_pipeline(logs: list[str]) -> None:
    """Run existing image OCR pipeline if dependencies are available."""
    script = ROOT / "99.system" / "scripts" / "ocr_dispatch_requirements.py"
    py = ROOT / "99.system" / ".venv" / "Scripts" / "python.exe"
    if not script.exists():
        logs.append("未找到需求单图片 OCR 脚本，跳过图片 OCR。")
        return
    if not py.exists():
        logs.append("未找到 00.raw-materials/99.system/.venv，跳过图片 OCR。")
        return
    try:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        proc = subprocess.run(
            [str(py), str(script)],
            cwd=str(VAULT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            timeout=900,
        )
        logs.append("图片 OCR 脚本已运行。")
        if proc.stdout:
            logs.append(proc.stdout[-3000:])
        if proc.stderr:
            logs.append("STDERR:\n" + proc.stderr[-2000:])
    except Exception as e:
        logs.append(f"图片 OCR 脚本运行失败：{e}")


def detect_processed_optimization(corpus: dict[str, str]) -> list[dict]:
    suggestions = []
    for path, text in corpus.items():
        if not path.startswith("00.raw-materials/90.processed/"):
            continue
        if not path.endswith(".md"):
            continue
        issues = []
        if "待澄清" in text or "TODO" in text or "- [ ]" in text:
            issues.append("存在待办 / 待澄清项，可继续补全。")
        if "OCR 自动识别" in text or "关键需求点需回看原图确认" in text or "可能存在错字" in text:
            issues.append("依赖 OCR 自动识别，建议人工复核关键页面。")
        if len(text) > 30000:
            issues.append("笔记较长，建议拆分为专题页和索引页。")
        if len(text) < 800:
            issues.append("内容较短，可能只是索引或初稿，可补充摘要、结论和后续行动。")
        if "## 结论" not in text and "## 知识提取" not in text and "## 需求理解" not in text:
            issues.append("缺少明确的结论 / 知识提取 / 需求理解章节。")
        if issues:
            suggestions.append({"path": path, "issues": issues[:4]})
    return suggestions


def write_inventory(inventory: list[dict], stamp: str) -> tuple[Path, Path]:
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    json_path = MANIFEST_DIR / f"raw-materials-inventory-{stamp}.json"
    csv_path = MANIFEST_DIR / f"raw-materials-inventory-{stamp}.csv"
    json_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "name", "folder", "suffix", "kind", "size", "mtime", "sha256"])
        writer.writeheader()
        writer.writerows(inventory)
    return json_path, csv_path


def write_weekly_report(
    stamp: str,
    inventory: list[dict],
    corpus: dict[str, str],
    optimization: list[dict],
    logs: list[str],
    inventory_files: tuple[Path, Path],
) -> Path:
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    out = WEEKLY_DIR / f"{stamp}-每周原始资料知识提纯.md"

    kind_counter = Counter(x["kind"] for x in inventory)
    folder_counter = Counter(x["folder"] for x in inventory)

    by_cat: dict[str, list[tuple[str, int, list[str]]]] = defaultdict(list)
    for path, text in corpus.items():
        scores = score_categories(text)
        if not scores:
            continue
        cat, score = scores.most_common(1)[0]
        key_lines = extract_key_lines(text, limit=5)
        by_cat[cat].append((path, score, key_lines))

    md = [
        "---",
        "type: weekly-knowledge-distill",
        f"date: {stamp}",
        "tags: [原始资料, 每周知识提纯, 自动化]",
        "---",
        "",
        f"# 每周原始资料知识提纯 - {stamp}",
        "",
        "## 本周自动化结论",
        "",
        f"- 扫描原始资料文件数：{len(inventory)}",
        f"- 纳入文本 / OCR / 已整理笔记语料数：{len(corpus)}",
        f"- 发现可进一步优化的 processed 笔记数：{len(optimization)}",
        f"- 文件清单 JSON：[[{rel(inventory_files[0])}]]",
        f"- 文件清单 CSV：[[{rel(inventory_files[1])}]]",
        "",
        "## 原始资料类型分布",
        "",
        "| 类型 | 数量 |",
        "|---|---:|",
    ]
    for kind, count in kind_counter.most_common():
        md.append(f"| {kind} | {count} |")

    md += [
        "",
        "## 原始资料目录分布 Top 20",
        "",
        "| 目录 | 文件数 |",
        "|---|---:|",
    ]
    for folder, count in folder_counter.most_common(20):
        md.append(f"| `{folder}` | {count} |")

    md += [
        "",
        "## 知识提纯结果（按主题聚合）",
        "",
        "> 以下为规则提取的初步知识地图；涉及生产内部规则时，请人工复核原图 / 原文。",
        "",
    ]
    for cat in CATEGORY_RULES:
        items = sorted(by_cat.get(cat, []), key=lambda x: x[1], reverse=True)[:10]
        if not items:
            continue
        md += [f"### {cat}", ""]
        for path, score, lines in items:
            md.append(f"- 来源：[[{path}]]；主题命中：{score}")
            for line in lines[:3]:
                md.append(f"  - {line}")
        md.append("")

    md += [
        "## 已有知识的优化空间",
        "",
        "| 笔记 | 建议 |",
        "|---|---|",
    ]
    for item in optimization[:50]:
        issues = "<br>".join(item["issues"])
        md.append(f"| [[{item['path']}]] | {issues} |")
    if not optimization:
        md.append("| 无 | 暂未发现明显优化项 |")

    md += [
        "",
        "## 本周建议行动",
        "",
        "- [ ] 优先人工复核 OCR 标注为关键的需求单页面。",
        "- [ ] 将高价值需求拆解为：背景、目标、输入、规则、输出、异常、验收标准。",
        "- [ ] 对长笔记拆成“索引页 + 专题页”。",
        "- [ ] 对仍含待办的 processed 笔记补充结论和下一步行动。",
        "- [ ] 对敏感资料补充敏感级别和访问限制说明。",
        "",
        "## 自动化运行日志",
        "",
        "```text",
        *logs[-80:],
        "```",
        "",
    ]

    out.write_text("\n".join(md), encoding="utf-8")
    return out


def update_latest_pointer(report: Path) -> None:
    latest = WEEKLY_DIR / "最新每周知识提纯.md"
    latest.write_text(
        "\n".join(
            [
                "---",
                "type: weekly-knowledge-distill-latest",
                "tags: [原始资料, 每周知识提纯]",
                "---",
                "",
                "# 最新每周知识提纯",
                "",
                f"- 最新报告：[[{rel(report)}]]",
                f"- 更新时间：{datetime.now().isoformat(timespec='seconds')}",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    stamp = datetime.now().strftime("%Y-%m-%d")
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logs = [f"开始时间：{datetime.now().isoformat(timespec='seconds')}"]

    # First refresh OCR-based processed notes for image demand sheets.
    run_image_ocr_pipeline(logs)

    files = iter_raw_files()
    inventory = build_inventory(files)
    inventory_files = write_inventory(inventory, stamp)
    logs.append(f"已生成文件清单：{rel(inventory_files[0])} / {rel(inventory_files[1])}")

    corpus = collect_text_corpus(files)
    optimization = detect_processed_optimization(corpus)
    report = write_weekly_report(stamp, inventory, corpus, optimization, logs, inventory_files)
    update_latest_pointer(report)

    log_path = LOG_DIR / "weekly_knowledge_distill.log"
    log_path.write_text("\n".join(logs + [f"报告：{rel(report)}", f"结束时间：{datetime.now().isoformat(timespec='seconds')}"]), encoding="utf-8")
    print(f"Wrote {rel(report)}")
    print(f"Wrote {rel(log_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
