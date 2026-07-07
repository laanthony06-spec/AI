from __future__ import annotations

import json
import re
import time
from collections import defaultdict
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[2]
IMG_BASE = ROOT / "10.sources" / "images"
OCR_BASE = ROOT / "90.processed" / "dispatch-requirements-ocr"
NOTE_BASE = ROOT / "90.processed" / "dispatch-requirements-notes"
META_BASE = ROOT / "80.metadata"

EXCLUDE_DIRS = {"dsp-dispatch-system-intro"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def natural_key(p: Path):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", p.name)]


def get_requirement_folders() -> list[Path]:
    out = []
    for d in sorted([p for p in IMG_BASE.rglob("*") if p.is_dir()], key=lambda x: x.as_posix().lower()):
        rel_parts = d.relative_to(IMG_BASE).parts
        if not rel_parts:
            continue
        if rel_parts[0] in EXCLUDE_DIRS:
            continue
        imgs = [p for p in d.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES]
        if imgs:
            out.append(d)
    return out


def lines_from_result(result) -> list[str]:
    if not result:
        return []
    items = []
    for box, text, score in result:
        text = (text or "").strip()
        try:
            score = float(score)
        except Exception:
            score = 0.0
        if not text or score < 0.42:
            continue
        xs = [pt[0] for pt in box]
        ys = [pt[1] for pt in box]
        items.append({"text": text, "score": score, "x": min(xs), "y": min(ys), "h": max(ys) - min(ys)})
    items.sort(key=lambda a: (a["y"], a["x"]))
    groups = []
    for it in items:
        placed = False
        for g in groups:
            if abs(g["y"] - it["y"]) <= max(12, min(32, it["h"] * 0.75)):
                g["items"].append(it)
                g["y"] = (g["y"] + it["y"]) / 2
                placed = True
                break
        if not placed:
            groups.append({"y": it["y"], "items": [it]})
    lines = []
    for g in sorted(groups, key=lambda x: x["y"]):
        parts = [it["text"] for it in sorted(g["items"], key=lambda a: a["x"])]
        line = " ".join(parts).strip()
        if line and line not in {"动画", "评论", "编辑"}:
            lines.append(line)
    return lines


def infer_topic(folder: str, text: str) -> str:
    folder_low = folder.lower()
    low = f"{folder} {text}".lower()
    # 优先使用文件夹名判断主题，避免 OCR 内容中的 PM、Qsort 等词干扰。
    if "waferbalance" in folder_low or ("wafer" in folder_low and "balance" in folder_low):
        return "Wafer Balance / 晶圆均衡"
    if "wphloss" in folder_low or ("wph" in folder_low and "loss" in folder_low):
        return "WPH Loss / 产能损失"
    if "qsort" in folder_low or "q-sort" in folder_low or "q_sort" in folder_low:
        return "Qsort / 派工排序"
    if "testcase" in folder_low or "sop" in folder_low:
        return "TestCase / SOP / 验证规范"
    if "pm" in folder_low:
        return "PM 管控 / 设备保养约束"

    if "pm" in low:
        return "PM 管控 / 设备保养约束"
    if "qsort" in low or "q-sort" in low or "q sort" in low:
        return "Qsort / 派工排序"
    if "testcase" in low or "test case" in low or "sop" in low or "测试" in low or "验证" in low:
        return "TestCase / SOP / 验证规范"
    if "wafer" in low and "balance" in low:
        return "Wafer Balance / 晶圆均衡"
    if "wph" in low or "loss" in low:
        return "WPH Loss / 产能损失"
    return "自动派工需求"


def extract_signals(text: str) -> dict[str, list[str]]:
    keys = {
        "系统对象": ["Lot", "FOUP", "Tool", "EQP", "Machine", "Chamber", "Port", "Recipe", "Route", "Step"],
        "派工逻辑": ["dispatch", "Dispatch", "派工", "Reserve", "Pre-reserve", "Sorting", "Qsort", "Prefer", "Filter", "Rule", "规则", "排序"],
        "约束条件": ["PM", "WPH", "Capability", "QTime", "QZone", "Hold", "Inhibit", "Constraint", "Down", "Idle", "Loss", "Balance"],
        "系统接口": ["MES", "RTD", "AMA", "EAP", "MCS", "APC", "PMS", "Scheduler", "FABScheduler"],
        "验证信息": ["需求", "测试", "Test", "Case", "SOP", "验收", "结果", "异常", "原因"],
    }
    found = {}
    for group, terms in keys.items():
        hits = []
        for t in terms:
            if t.lower() in text.lower():
                hits.append(t)
        if hits:
            found[group] = sorted(set(hits), key=lambda x: x.lower())
    return found


def pick_lines(lines: list[str], limit: int = 12) -> list[str]:
    keywords = [
        "需求", "目的", "背景", "逻辑", "规则", "条件", "判断", "派工", "排序",
        "PM", "Qsort", "WPH", "Loss", "Wafer", "Balance", "Filter", "Prefer",
        "MES", "RTD", "AMA", "EAP", "MCS", "Recipe", "Capability", "QTime", "QZone",
        "测试", "Case", "异常", "原因", "结果",
    ]
    selected = []
    for line in lines:
        if any(k.lower() in line.lower() for k in keywords):
            selected.append(line)
        if len(selected) >= limit:
            break
    if len(selected) < max(4, min(limit, len(lines))):
        for line in lines:
            if line not in selected:
                selected.append(line)
            if len(selected) >= limit:
                break
    return selected


def make_safe_slug(name: str) -> str:
    # Keep CJK characters so folders like TestCase示例 and TestCase要求 do not collide.
    return re.sub(r"[^\w_.-]+", "-", name, flags=re.UNICODE).strip("-") or "requirement"


def folder_id(folder: Path) -> str:
    return folder.relative_to(IMG_BASE).as_posix()


def folder_slug(folder_name: str) -> str:
    parts = [make_safe_slug(p) for p in folder_name.split("/")]
    return "__".join([p for p in parts if p]) or "requirement"


def ocr_all() -> list[dict]:
    OCR_BASE.mkdir(parents=True, exist_ok=True)
    ocr = RapidOCR()
    records = []
    start = time.time()
    folders = get_requirement_folders()
    for folder in folders:
        imgs = sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES], key=natural_key)
        fid = folder_id(folder)
        out_dir = OCR_BASE / folder_slug(fid)
        out_dir.mkdir(parents=True, exist_ok=True)
        folder_pages = []
        for idx, img in enumerate(imgs, 1):
            result, elapse = ocr(str(img))
            lines = lines_from_result(result)
            rec = {
                "folder": fid,
                "page": idx,
                "file": img.name,
                "image_path": img.relative_to(ROOT.parent).as_posix(),
                "lines": lines,
                "raw": result,
                "elapsed": elapse,
            }
            (out_dir / f"p{idx:03d}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
            (out_dir / f"p{idx:03d}.txt").write_text("\n".join(lines), encoding="utf-8")
            folder_pages.append(rec)
            records.append(rec)
            print(f"OCR {fid} p{idx:03d}/{len(imgs)} lines={len(lines)}")
        (out_dir / "index.json").write_text(json.dumps(folder_pages, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"DONE folders={len(folders)} images={len(records)} seconds={time.time()-start:.1f}")
    return records


def load_records() -> list[dict]:
    records = []
    for idx in sorted(OCR_BASE.glob("*/index.json")):
        records.extend(json.loads(idx.read_text(encoding="utf-8")))
    return records


def write_folder_notes(records: list[dict]) -> list[Path]:
    NOTE_BASE.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        grouped[r["folder"]].append(r)

    outputs = []
    for folder, pages in sorted(grouped.items(), key=lambda x: x[0].lower()):
        pages = sorted(pages, key=lambda r: r["page"])
        all_text = "\n".join("\n".join(p["lines"]) for p in pages)
        topic = infer_topic(folder, all_text)
        signals = extract_signals(all_text)
        note = NOTE_BASE / f"{folder_slug(folder)}-需求单整理.md"
        md = [
            "---",
            "type: dispatch-requirement-note",
            f"source_folder: {folder}",
            f"topic: {topic}",
            "tags: [自动派工, 需求单, OCR, 需求整理]",
            "---",
            "",
            f"# {folder} - 需求单整理",
            "",
            "## 资料概况",
            "",
            f"- 原始图片目录：[[00.raw-materials/10.sources/images/{folder}]]",
            f"- OCR 输出目录：[[00.raw-materials/90.processed/dispatch-requirements-ocr/{folder_slug(folder)}]]",
            f"- 图片数量：{len(pages)}",
            f"- 初步主题：{topic}",
            "- 处理状态：已 OCR，已建立初步结构化笔记",
            "- 注意：本笔记基于 OCR 自动识别，关键需求点需回看原图确认。",
            "",
            "## 自动识别到的关键信号",
            "",
        ]
        if signals:
            for group, hits in signals.items():
                md.append(f"- {group}：{', '.join(hits)}")
        else:
            md.append("- 暂未识别到明显关键词，建议人工复核原图。")

        md += [
            "",
            "## 需求理解（初稿）",
            "",
        ]
        if "PM" in topic:
            md += [
                "- 该组资料疑似围绕 PM（Preventive Maintenance）对自动派工的影响展开。",
                "- 需要重点确认：PM 前后是否允许派工、Prefer 是否考虑 PM、PM 造成的机台可用性变化如何进入排序或过滤逻辑。",
                "- 对派工系统的影响：PM 约束通常应进入 Tool 可作业性过滤、Prefer 计算或 WPH / Capacity 评估。",
            ]
        elif "Qsort" in topic:
            md += [
                "- 该组资料疑似围绕 Qsort 或派工排序值计算展开。",
                "- 需要重点确认：排序因子、权重、优先级、Tie-breaker、与 QTime / WIP / Due Date / Hot Lot 的关系。",
                "- 对派工系统的影响：Qsort 决定候选 Lot 通过过滤后的最终派工顺序。",
            ]
        elif "Wafer Balance" in topic:
            md += [
                "- 该组资料疑似围绕 Wafer Balance 或晶圆数量均衡展开。",
                "- 需要重点确认：均衡对象是设备、Chamber、Recipe、产品、Monitor Wafer 还是批次内 wafer 分布。",
                "- 对派工系统的影响：Wafer Balance 可能影响设备选择、批次组合、WPH 损失和后续站点负载均衡。",
            ]
        elif "WPH Loss" in topic:
            md += [
                "- 该组资料疑似围绕 WPH Loss 或产能损失分析展开。",
                "- 需要重点确认：Loss 的定义、计算窗口、归因规则、是否用于派工排序或异常提醒。",
                "- 对派工系统的影响：WPH Loss 可作为派工策略评估指标，也可反馈到瓶颈机台优先级或设备选择逻辑。",
            ]
        else:
            md += [
                "- 该组资料与自动派工需求有关，需进一步人工复核 OCR 结果。",
                "- 建议从输入、处理逻辑、输出、异常、验收标准五个角度补全需求。",
            ]

        md += [
            "",
            "## 待澄清问题",
            "",
            "- [ ] 需求目标是什么：提升产能、降低 Cycle Time、减少 OverQtime、降低 WPH Loss，还是提升自动化率？",
            "- [ ] 输入数据来自哪些系统：MES、RTD、AMA、EAP、MCS、APC、PMS？",
            "- [ ] 规则属于 Global Rule、Local Rule，还是排序 / Prefer 逻辑？",
            "- [ ] 需要新增哪些异常原因码或查询页面？",
            "- [ ] 验收标准是什么：测试 Case、前后对比指标、上线影响范围？",
            "",
            "## 分页 OCR 摘录",
            "",
        ]
        for p in pages:
            md += [
                f"### 第 {p['page']:03d} 张：{p['file']}",
                "",
                f"![[{p['image_path']}]]",
                "",
                "关键 OCR 行：",
            ]
            for line in pick_lines(p["lines"]):
                md.append(f"- {line}")
            md += [
                "",
                "<details>",
                "<summary>展开完整 OCR</summary>",
                "",
                "```text",
                *p["lines"],
                "```",
                "",
                "</details>",
                "",
            ]
        note.write_text("\n".join(md), encoding="utf-8")
        outputs.append(note)
    return outputs


def write_index(notes: list[Path], records: list[dict]) -> Path:
    NOTE_BASE.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        grouped[r["folder"]].append(r)

    out = NOTE_BASE / "自动派工需求单图片-OCR索引.md"
    md = [
        "---",
        "type: dispatch-requirements-index",
        "tags: [自动派工, 需求单, OCR, 索引]",
        "---",
        "",
        "# 自动派工需求单图片 - OCR 索引",
        "",
        "## 汇总",
        "",
        f"- 已处理文件夹数量：{len(grouped)}",
        f"- 已处理图片数量：{len(records)}",
        "- 空文件夹未生成 OCR 笔记，例如当前 `TestCase_SOP` 下暂无图片。",
        "",
        "## 文件夹清单",
        "",
        "| 文件夹 | 图片数 | 初步主题 | 整理笔记 |",
        "|---|---:|---|---|",
    ]
    note_map = {n.stem.replace("-需求单整理", ""): n for n in notes}
    for folder, pages in sorted(grouped.items(), key=lambda x: x[0].lower()):
        text = "\n".join("\n".join(p["lines"]) for p in pages)
        topic = infer_topic(folder, text)
        note = note_map.get(folder_slug(folder))
        note_link = f"[[{note.relative_to(ROOT.parent).as_posix()}]]" if note else ""
        md.append(f"| {folder} | {len(pages)} | {topic} | {note_link} |")

    md += [
        "",
        "## 建议后续处理",
        "",
        "- [ ] 人工复核每个需求单的 OCR 结果。",
        "- [ ] 将需求拆解为：背景、目标、输入、规则、输出、异常、验收标准。",
        "- [ ] 对涉及生产内部规则的内容标记敏感级别。",
        "- [ ] 将成熟需求沉淀到正式专题笔记或项目文档。",
    ]
    out.write_text("\n".join(md), encoding="utf-8")
    return out


def main() -> None:
    records = ocr_all()
    if not records:
        records = load_records()
    notes = write_folder_notes(records)
    index = write_index(notes, records)
    print("NOTES")
    for n in notes:
        print(n.relative_to(ROOT.parent).as_posix())
    print(index.relative_to(ROOT.parent).as_posix())


if __name__ == "__main__":
    main()
