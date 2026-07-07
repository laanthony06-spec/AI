from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REPORT = ROOT / "00.raw-materials" / "90.processed" / "agent-knowledge-ops" / "sensitive-scan-report.md"

SKIP_PARTS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
}

TEXT_EXTS = {
    ".md",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".toml",
    ".ini",
    ".ps1",
    ".py",
    ".js",
    ".ts",
    ".env",
    ".example",
    ".gitignore",
}

SENSITIVE_FILE_PATTERNS = [
    re.compile(r"(^|/|\\)\.env$", re.I),
    re.compile(r"secret", re.I),
    re.compile(r"token", re.I),
    re.compile(r"credential", re.I),
    re.compile(r"cookie", re.I),
    re.compile(r"private[_-]?key", re.I),
]

SENSITIVE_CONTENT_PATTERNS = [
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("OpenAI-like API key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("X bearer token", re.compile(r"AAAAAAAAAAAAAAAAAAAAA[A-Za-z0-9%_-]{20,}")),
    ("Generic secret assignment", re.compile(r"(?i)(api[_-]?key|secret|token|password|cookie)\s*[:=]\s*['\"]?[^'\"\s]{8,}")),
]


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def is_text_candidate(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTS:
        return True
    if path.name.lower() in {".env", ".gitignore"}:
        return True
    return False


def mask_line(line: str) -> str:
    line = re.sub(r"(github_pat_)[A-Za-z0-9_]+", r"\1***MASKED***", line)
    line = re.sub(r"(gh[pousr]_)[A-Za-z0-9_]+", r"\1***MASKED***", line)
    line = re.sub(r"(sk-)[A-Za-z0-9_-]+", r"\1***MASKED***", line)
    line = re.sub(r"(AAAAAAAAAAAAAAAAAAAAA)[A-Za-z0-9%_-]+", r"\1***MASKED***", line)
    line = re.sub(r"(?i)((api[_-]?key|secret|token|password|cookie)\s*[:=]\s*)['\"]?[^'\"\s]+", r"\1***MASKED***", line)
    return line[:240]


def main() -> int:
    suspicious_files: list[Path] = []
    content_hits: list[tuple[Path, int, str, str]] = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or is_skipped(path):
            continue
        rel = path.relative_to(ROOT)
        rel_s = rel.as_posix()

        if any(p.search(rel_s) for p in SENSITIVE_FILE_PATTERNS):
            suspicious_files.append(rel)

        if not is_text_candidate(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for label, pattern in SENSITIVE_CONTENT_PATTERNS:
                if pattern.search(line):
                    content_hits.append((rel, i, label, mask_line(line)))

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines: list[str] = [
        "---",
        "type: security-scan",
        f"updated: {now}",
        "tags: [安全, SensitiveScan, AgentKnowledgeOps]",
        "---",
        "",
        "# 敏感信息扫描报告",
        "",
        f"- 扫描时间：{now}",
        f"- 可疑文件数量：{len(suspicious_files)}",
        f"- 内容命中数量：{len(content_hits)}",
        "",
        "## 可疑文件路径",
        "",
    ]
    if suspicious_files:
        for rel in suspicious_files:
            lines.append(f"- `{rel.as_posix()}`")
    else:
        lines.append("- 未发现可疑文件路径。")

    lines += ["", "## 内容命中", ""]
    if content_hits:
        lines.append("| 文件 | 行号 | 类型 | 已脱敏片段 |")
        lines.append("|---|---:|---|---|")
        for rel, line_no, label, snippet in content_hits[:200]:
            safe = snippet.replace("|", "\\|")
            lines.append(f"| `{rel.as_posix()}` | {line_no} | {label} | `{safe}` |")
        if len(content_hits) > 200:
            lines.append(f"\n> 仅显示前 200 条，实际命中 {len(content_hits)} 条。")
    else:
        lines.append("- 未发现敏感内容命中。")

    lines += [
        "",
        "## 处理建议",
        "",
        "1. `.env` 可以存在于本地，但必须被 `.gitignore` 排除。",
        "2. 如果报告中出现真实 token，请立即轮换对应密钥。",
        "3. 不要把 Cookie、API Key、AppSecret、Bearer Token 写入 Markdown 正文。",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT.relative_to(ROOT).as_posix())
    return 1 if content_hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
