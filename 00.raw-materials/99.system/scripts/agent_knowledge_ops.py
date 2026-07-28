from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

VAULT = Path(__file__).resolve().parents[3]
OPS = VAULT / "30.areas" / "agent-knowledge-ops"
PROCESSED = VAULT / "00.raw-materials" / "90.processed" / "agent-knowledge-ops"
STATE_DIR = PROCESSED / "state"
TASK_QUEUE_JSON = PROCESSED / "agent-dispatch-queue.json"

WATCH_DIRS = [
    VAULT / "00.raw-materials" / "00.inbox",
    VAULT / "00.raw-materials" / "10.sources" / "images",
    VAULT / "00.raw-materials" / "20.metadata",
    VAULT / "00.raw-materials" / "90.processed" / "dispatch-requirements-notes",
    VAULT / "00.raw-materials" / "90.processed" / "weekly-knowledge-distill",
    VAULT / "30.areas" / "ai-agent-intel" / "inbox",
    VAULT / "30.areas" / "semiconductor-dispatch-intel" / "inbox",
]

TEXT_EXTS = {".md", ".txt", ".json", ".csv", ".yml", ".yaml"}
EXCLUDED_PARTS = {".git", ".obsidian", ".venv", "__pycache__", "node_modules", "99.system"}


def rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def read_text(path: Path, limit: int = 120_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except Exception:
        return ""


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def load_existing_task_statuses() -> dict[tuple[str, str], str]:
    if not TASK_QUEUE_JSON.exists():
        return {}
    try:
        existing_tasks = json.loads(TASK_QUEUE_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    statuses: dict[tuple[str, str], str] = {}
    for task in existing_tasks:
        if not isinstance(task, dict):
            continue
        task_text = str(task.get("task", "")).strip()
        source = str(task.get("source", "")).strip()
        status = str(task.get("status", "todo")).strip().lower()
        if task_text and source and status in {"doing", "done", "blocked", "cancelled"}:
            statuses[(task_text, source)] = status
    return statuses


def ensure_dirs() -> None:
    for d in [
        OPS / "01.task-queue",
        OPS / "02.evidence",
        OPS / "03.testcases",
        OPS / "04.telemetry",
        OPS / "05.mcp-server",
        OPS / "06.memory",
        OPS / "07.hooks",
        PROCESSED,
        STATE_DIR,
    ]:
        d.mkdir(parents=True, exist_ok=True)


def latest_file(folder: Path, pattern: str = "*.md") -> Path | None:
    if not folder.exists():
        return None
    files = [p for p in folder.glob(pattern) if p.is_file()]
    return max(files, key=lambda p: p.stat().st_mtime) if files else None


def iter_text_files(base: Path) -> list[Path]:
    if not base.exists():
        return []
    out: list[Path] = []
    for p in base.rglob("*"):
        if not p.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in p.parts):
            continue
        if p.suffix.lower() in TEXT_EXTS and p.stat().st_size > 0:
            out.append(p)
    return sorted(out, key=lambda x: rel(x).lower())


def infer_category(text: str) -> str:
    low = text.lower()
    if "mcp" in low or "model context protocol" in low:
        return "MCP / 工具接口"
    if "testcase" in low or "test case" in low or "测试" in text or "验证" in text:
        return "TestCase"
    if "evidence" in low or "证据" in text:
        return "Evidence"
    if "telemetry" in low or "看板" in text or "dashboard" in low:
        return "Telemetry"
    if "hook" in low or "新增文件" in text or "扫描" in text:
        return "Hooks"
    if "memory" in low or "记忆" in text:
        return "Memory"
    if "安全" in text or "guardrail" in low or "preflight" in low or "权限" in text:
        return "安全预检"
    if "waferbalance" in low or "qsort" in low or "pm_control" in low or "wphloss" in low:
        return "派工规则"
    return "知识整理"


def infer_priority(text: str) -> str:
    low = text.lower()
    if any(k in low for k in ["mcp", "testcase", "evidence", "security", "guardrail", "waferbalance", "overqtime"]):
        return "P1"
    if any(k in low for k in ["telemetry", "hook", "memory", "优化", "待澄清", "todo"]):
        return "P2"
    return "P3"


def recommend_executor(category: str, text: str) -> str:
    if category in {"TestCase", "派工规则", "Hooks", "Telemetry"}:
        return "Codex"
    if category in {"Evidence", "知识整理", "Memory"}:
        return "Codex + 人工复核"
    if category == "MCP / 工具接口":
        return "Codex（先本地只读）"
    if category == "安全预检":
        return "人工确认 + Codex"
    return "Codex"


def infer_output(category: str) -> str:
    return {
        "TestCase": "30.areas/agent-knowledge-ops/03.testcases/",
        "Evidence": "30.areas/agent-knowledge-ops/02.evidence/",
        "Telemetry": "30.areas/agent-knowledge-ops/04.telemetry/",
        "Hooks": "30.areas/agent-knowledge-ops/07.hooks/",
        "Memory": "30.areas/agent-knowledge-ops/06.memory/",
        "MCP / 工具接口": "30.areas/agent-knowledge-ops/05.mcp-server/",
        "派工规则": "00.raw-materials/90.processed/dispatch-requirements-notes/",
    }.get(category, "00.raw-materials/90.processed/agent-knowledge-ops/")


def extract_tasks_from_text(text: str, source: Path, max_tasks: int = 25) -> list[dict[str, Any]]:
    keywords = [
        "MCP", "Agent", "TestCase", "Evidence", "Telemetry", "Hooks", "Memory",
        "WaferBalance", "Qsort", "PM_Control", "WPHLoss", "OverQtime",
        "待澄清", "优化空间", "TODO", "Action Preflight", "guardrail",
        "工具调用", "证据", "看板", "安全", "测试", "验证",
    ]
    action_prefixes = (
        "整理", "处理", "研究", "评估", "阅读", "优先阅读", "将", "把", "对",
        "检查", "补充", "补齐", "建立", "申请", "填写", "更新", "优化",
        "验证", "确认", "跟进",
    )
    ignored_prefixes = (
        "type:", "tags:", "source:", "date:", "updated:", "- 分类：",
        "- 来源：", "- 原文摘要：", "- 中文导读：", "- 本简报",
    )
    tasks: list[dict[str, Any]] = []
    seen: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.lower().startswith(tuple(prefix.lower() for prefix in ignored_prefixes)):
            continue
        checkbox = line.startswith("- [ ]")
        heading_link = bool(re.match(r"^#{2,4}\s+.*\[[^\]]+\]\([^)]+\)", line))
        action_text = line.lstrip("-* ").strip()
        action_line = action_text.startswith(action_prefixes)
        keyword_hit = any(k.lower() in line.lower() for k in keywords)
        if not checkbox and not (heading_link and keyword_hit) and not action_line:
            continue
        clean = line.replace("|", "｜")
        if clean.startswith("- [ ]"):
            clean = clean[5:].strip()
        clean = " ".join(clean.split())[:220]
        if len(clean) < 8 or clean in seen:
            continue
        seen.add(clean)
        category = infer_category(clean)
        tasks.append(
            {
                "status": "todo",
                "priority": infer_priority(clean),
                "category": category,
                "task": clean,
                "recommended_executor": recommend_executor(category, clean),
                "trigger": "brief_or_note_scan",
                "evidence": rel(source),
                "output": infer_output(category),
                "next_action": "人工确认后执行",
                "source": rel(source),
            }
        )
        if len(tasks) >= max_tasks:
            break
    return tasks


def load_hook_state() -> dict[str, dict[str, Any]]:
    path = STATE_DIR / "hooks_state.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_hook_state(state: dict[str, dict[str, Any]]) -> None:
    write(STATE_DIR / "hooks_state.json", json.dumps(state, ensure_ascii=False, indent=2))


def scan_hooks() -> tuple[list[dict[str, Any]], bool]:
    previous = load_hook_state()
    first_run = not previous
    current: dict[str, dict[str, Any]] = {}
    events: list[dict[str, Any]] = []

    watch_files: list[Path] = []
    for d in WATCH_DIRS:
        if d.exists():
            for p in d.rglob("*"):
                if p.is_file() and not any(part in EXCLUDED_PARTS for part in p.parts):
                    watch_files.append(p)

    for p in sorted(watch_files, key=lambda x: rel(x).lower()):
        stat = p.stat()
        key = rel(p)
        info = {"mtime": stat.st_mtime, "size": stat.st_size}
        current[key] = info
        old = previous.get(key)
        if first_run:
            continue
        if old is None:
            events.append({"event": "created", "path": key, "size": stat.st_size})
        elif old.get("mtime") != stat.st_mtime or old.get("size") != stat.st_size:
            events.append({"event": "modified", "path": key, "size": stat.st_size})

    if not first_run:
        for key in sorted(set(previous) - set(current)):
            events.append({"event": "deleted", "path": key, "size": 0})

    save_hook_state(current)
    return events, first_run


def build_hooks(events: list[dict[str, Any]], first_run: bool) -> Path:
    out = OPS / "07.hooks" / "Hooks扫描器.md"
    lines = [
        "---",
        "type: hooks-scanner",
        f"updated: {datetime.now().isoformat(timespec='seconds')}",
        "tags: [Agent, Hooks, 自动触发]",
        "---",
        "",
        "# Hooks 扫描器",
        "",
        "## 作用",
        "",
        "扫描关键目录的新增、修改、删除事件，并把事件转成可进入 Dispatch 队列的候选任务。当前版本只生成任务，不自动修改业务资料。",
        "",
        "## 监听目录",
        "",
    ]
    for d in WATCH_DIRS:
        lines.append(f"- `{rel(d)}`")
    lines += ["", "## 本次扫描结果", ""]
    if first_run:
        lines.append("- 首次运行：已建立文件状态基线，本次不把历史文件全部塞进任务队列。")
    elif not events:
        lines.append("- 未发现新增、修改或删除事件。")
    else:
        lines += ["| 事件 | 文件 | 大小 | 建议动作 |", "|---|---|---:|---|"]
        for e in events[:100]:
            path = e["path"]
            action = "检查是否需要 OCR / 整理 / 更新 Evidence / 生成 TestCase"
            lines.append(f"| {e['event']} | [[{path}]] | {e['size']} | {action} |")
    lines += [
        "",
        "## 触发规则草案",
        "",
        "| 事件 | 自动生成任务 |",
        "|---|---|",
        "| `00.inbox` 新增文件 | 分类原始资料，必要时移动到 `10.sources` |",
        "| `10.sources/images` 新增图片 | OCR 并建立资料卡 / 需求单整理 |",
        "| AI 简报新增 | 抽取可借鉴 Agent 应用 |",
        "| 半导体派工简报新增 | 抽取派工相关条目 |",
        "| processed 笔记修改 | 更新 Evidence 和 Telemetry |",
        "",
    ]
    write(out, "\n".join(lines))
    write(PROCESSED / "hook-events.json", json.dumps(events, ensure_ascii=False, indent=2))
    return out


def build_memory(events: list[dict[str, Any]], tasks: list[dict[str, Any]]) -> list[Path]:
    memory_dir = OPS / "06.memory"
    outputs: list[Path] = []
    outputs.append(
        write(
            memory_dir / "系统约定记忆.md",
            "\n".join(
                [
                    "---",
                    "type: agent-memory",
                    "tags: [Agent, Memory, 系统约定]",
                    "---",
                    "",
                    "# 系统约定记忆",
                    "",
                    "- Obsidian 是长期知识中枢。",
                    "- `00.raw-materials/10.sources/` 存放原始资料。",
                    "- `00.raw-materials/90.processed/` 存放加工后知识。",
                    "- Agent Knowledge Ops 负责 Dispatch、Evidence、TestCase、Telemetry、MCP 原型、Memory 和 Hooks。",
                    "- 删除或移动文件前必须检查引用。",
                    "- Token 不在回答中回显。",
                    "- 涉及敏感资料时默认只做本地处理。",
                    "",
                ]
            ),
        )
    )
    outputs.append(
        write(
            memory_dir / "任务执行记忆.md",
            "\n".join(
                [
                    "---",
                    "type: agent-memory",
                    "tags: [Agent, Memory, 任务执行]",
                    "---",
                    "",
                    "# 任务执行记忆",
                    "",
                    f"- 最近刷新时间：{datetime.now().isoformat(timespec='seconds')}",
                    f"- 本次 Hook 事件数：{len(events)}",
                    f"- 本次 Dispatch 候选任务数：{len(tasks)}",
                    "",
                    "## 最近事件",
                    "",
                    *[f"- {e['event']}：[[{e['path']}]]" for e in events[:20]],
                    "",
                ]
            ),
        )
    )
    outputs.append(
        write(
            memory_dir / "错误与修复记录.md",
            "\n".join(
                [
                    "---",
                    "type: agent-memory",
                    "tags: [Agent, Memory, 错误修复]",
                    "---",
                    "",
                    "# 错误与修复记录",
                    "",
                    "- 中文乱码：优先使用 UTF-8 写入；PowerShell 控制台显示异常不等于文件损坏。",
                    "- X API：当前 Recent Search 返回 402，说明 API 套餐 / 权限不足。",
                    "- OCR：自动识别结果可能有错字，关键业务结论必须回看原图。",
                    "- 计划任务：注册或读取状态可能需要管理员 / 系统权限。",
                    "",
                ]
            ),
        )
    )
    outputs.append(
        write(
            memory_dir / "高价值来源记录.md",
            "\n".join(
                [
                    "---",
                    "type: agent-memory",
                    "tags: [Agent, Memory, 来源]",
                    "---",
                    "",
                    "# 高价值来源记录",
                    "",
                    "- GitHub：适合发现 Agent 框架、MCP、工具调用、开源实现。",
                    "- arXiv / RSS：适合发现 Agent 评测、多智能体、RAG / Memory 研究。",
                    "- 原始需求单图片：适合沉淀自动派工业务规则。",
                    "- 每周知识提纯报告：适合发现 processed 笔记优化空间。",
                    "",
                ]
            ),
        )
    )
    return outputs


def build_task_queue(hook_events: list[dict[str, Any]]) -> tuple[Path, list[dict[str, Any]]]:
    existing_statuses = load_existing_task_statuses()
    sources: list[Path] = []
    for folder in [
        VAULT / "30.areas" / "ai-agent-intel" / "inbox",
        VAULT / "30.areas" / "semiconductor-dispatch-intel" / "inbox",
        VAULT / "00.raw-materials" / "90.processed" / "weekly-knowledge-distill",
        VAULT / "00.raw-materials" / "90.processed" / "dispatch-requirements-notes",
    ]:
        latest = latest_file(folder)
        if latest:
            sources.append(latest)

    tasks: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for src in sources:
        for t in extract_tasks_from_text(read_text(src), src):
            key = (t["task"], t["source"])
            if key not in seen:
                seen.add(key)
                tasks.append(t)

    for e in hook_events:
        category = "Hooks"
        path = e["path"]
        task = f"处理 Hook 事件：{e['event']} {path}"
        tasks.append(
            {
                "status": "todo",
                "priority": "P2",
                "category": category,
                "task": task,
                "recommended_executor": recommend_executor(category, task),
                "trigger": e["event"],
                "evidence": path,
                "output": infer_output(category),
                "next_action": "判断是否需要 OCR、整理、Evidence 或 TestCase",
                "source": path,
            }
        )

    for task in tasks:
        key = (task["task"], task["source"])
        task["status"] = existing_statuses.get(key, task["status"])

    tasks.sort(key=lambda x: (x["priority"], x["category"], x["task"]))

    out = OPS / "01.task-queue" / "Agent任务队列.md"
    lines = [
        "---",
        "type: agent-task-queue",
        f"updated: {datetime.now().isoformat(timespec='seconds')}",
        "tags: [Agent, Dispatch, 任务队列, 自动化]",
        "---",
        "",
        "# Agent Dispatch 任务队列",
        "",
        "> 这是 Dispatch 中枢：把简报、Hooks、Memory、Evidence、TestCase 中出现的事项，整理成可执行任务。当前默认人工确认后再执行。",
        "",
        "## 字段说明",
        "",
        "- 推荐执行者：建议由哪个 Agent / 人类角色处理。",
        "- 触发来源：brief、note_scan、hook created / modified 等。",
        "- Evidence：任务依据，优先指向原始资料或 processed 笔记。",
        "- 输出位置：完成后建议写到哪里。",
        "",
        "## 任务列表",
        "",
        "| 状态 | 优先级 | 分类 | 任务 | 推荐执行者 | 触发来源 | Evidence | 输出位置 | 下一步 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    active_tasks = [task for task in tasks if task["status"] != "cancelled"]
    closed_task_count = sum(task["status"] == "cancelled" for task in tasks)
    for t in active_tasks[:120]:
        evidence = f"[[{t['evidence']}]]" if t.get("evidence") else ""
        lines.append(
            f"| {t['status']} | {t['priority']} | {t['category']} | {t['task']} | {t['recommended_executor']} | {t['trigger']} | {evidence} | `{t['output']}` | {t['next_action']} |"
        )
    if not active_tasks:
        lines.append("| — | — | — | 当前没有自动生成的待办任务 | — | — | — | — | 新任务将在后续刷新时加入 |")
    lines += [
        "",
        "## 已关闭自动任务",
        "",
        f"- 已关闭：{closed_task_count} 条。",
        "- 明细保存在 [[00.raw-materials/90.processed/agent-knowledge-ops/agent-dispatch-queue.json]]。",
        "",
        "## 人工追加任务",
        "",
        "- [ ] 把 Qsort 需求单整理成通俗介绍和 TestCase。",
        "- [ ] 把 PM_Control 需求单整理成通俗介绍和 TestCase。",
        "- [ ] 将 X Article 里提到的 Codex + Claude Code 工作系统拆成可执行蓝图。",
        "",
    ]
    write(out, "\n".join(lines))
    write(TASK_QUEUE_JSON, json.dumps(tasks, ensure_ascii=False, indent=2))
    return out, tasks


def build_evidence_index() -> Path:
    evidence_files: list[Path] = []
    for root in [VAULT / "00.raw-materials", VAULT / "30.areas"]:
        for p in iter_text_files(root):
            text = read_text(p, limit=50_000)
            if any(k in text for k in ["WaferBalance", "Qsort", "PM_Control", "OverQtime", "QZone", "RTD", "DSP", "TestCase", "MCP", "Agent"]):
                evidence_files.append(p)
    evidence_files = sorted(set(evidence_files), key=lambda x: rel(x).lower())[:250]

    out = OPS / "02.evidence" / "Evidence索引.md"
    lines = [
        "---",
        "type: evidence-index",
        f"updated: {datetime.now().isoformat(timespec='seconds')}",
        "tags: [Evidence, 证据层, Agent, 自动派工]",
        "---",
        "",
        "# Evidence 证据索引",
        "",
        "## 设计目的",
        "",
        "每个结论都尽量追溯到原图、OCR、需求单、简报或整理笔记。Evidence 层负责回答：这个说法的出处在哪里？可信度如何？是否需要人工复核？",
        "",
        "## 证据资料清单",
        "",
        "| 资料 | 类型 | 大小 | 说明 |",
        "|---|---|---:|---|",
    ]
    for p in evidence_files:
        lines.append(f"| [[{rel(p)}]] | {p.suffix.lower().lstrip('.')} | {p.stat().st_size} | 自动识别为可能包含 Agent / 派工 / TestCase 证据 |")
    lines += [
        "",
        "## 证据引用模板",
        "",
        "```markdown",
        "## 结论",
        "",
        "## 证据",
        "- 原始资料：[[路径]]",
        "- OCR / 原文摘录：",
        "- 可信度：高 / 中 / 低",
        "- 需要人工复核：是 / 否",
        "```",
        "",
    ]
    write(out, "\n".join(lines))
    write(PROCESSED / "evidence-index.json", json.dumps([rel(p) for p in evidence_files], ensure_ascii=False, indent=2))
    return out


def read_scheduled_tasks() -> list[dict[str, Any]]:
    try:
        proc = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                "Get-ScheduledTask | Where-Object {$_.TaskName -like 'Obsidian*'} | Select-Object TaskName,State | ConvertTo-Json -Compress",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            return []
        data = json.loads(proc.stdout)
        return [data] if isinstance(data, dict) else data
    except Exception:
        return []


def build_telemetry() -> Path:
    key_dirs = [
        VAULT / "30.areas" / "ai-agent-intel" / "inbox",
        VAULT / "30.areas" / "semiconductor-dispatch-intel" / "inbox",
        VAULT / "00.raw-materials" / "90.processed" / "weekly-knowledge-distill",
        VAULT / "00.raw-materials" / "90.processed" / "dispatch-requirements-notes",
        OPS / "01.task-queue",
        OPS / "02.evidence",
        OPS / "03.testcases",
        OPS / "06.memory",
        OPS / "07.hooks",
    ]
    logs = [p for p in VAULT.rglob("*.log") if "99.system/.venv" not in rel(p)]
    tasks = read_scheduled_tasks()

    out = OPS / "04.telemetry" / "Agent自动化运行看板.md"
    lines = [
        "---",
        "type: agent-telemetry-dashboard",
        f"updated: {datetime.now().isoformat(timespec='seconds')}",
        "tags: [Agent, Telemetry, 自动化看板]",
        "---",
        "",
        "# Agent 自动化运行看板",
        "",
        "## 计划任务",
        "",
        "| 任务 | 状态 |",
        "|---|---|",
    ]
    if tasks:
        for t in tasks:
            lines.append(f"| {t.get('TaskName','')} | {t.get('State','')} |")
    else:
        lines.append("| 未读取到 | 可能是权限限制；不代表任务不存在 |")
    lines += ["", "## 关键输出目录", "", "| 目录 | 文件数 | 最新文件 |", "|---|---:|---|"]
    for d in key_dirs:
        latest = latest_file(d)
        count = len([p for p in d.glob("*.md")]) if d.exists() else 0
        latest_link = f"[[{rel(latest)}]]" if latest else ""
        lines.append(f"| `{rel(d)}` | {count} | {latest_link} |")
    lines += ["", "## 日志健康度", "", "| 日志 | 大小 | Warning / Error 计数 |", "|---|---:|---:|"]
    for p in sorted(logs, key=lambda x: rel(x).lower()):
        text = read_text(p, limit=200_000)
        warnings = text.count("[WARN]") + text.lower().count("error")
        lines.append(f"| [[{rel(p)}]] | {p.stat().st_size} | {warnings} |")
    lines += ["", "## 建议", "", "- [ ] Warning / Error 大于 0 的日志优先检查。", "- [ ] 如果某个简报目录没有新文件，检查计划任务。", ""]
    write(out, "\n".join(lines))
    write(PROCESSED / "telemetry.json", json.dumps({"tasks": tasks}, ensure_ascii=False, indent=2))
    return out


def main() -> int:
    ensure_dirs()
    hook_events, first_run = scan_hooks()
    hook_note = build_hooks(hook_events, first_run)
    task_note, tasks = build_task_queue(hook_events)
    memory_notes = build_memory(hook_events, tasks)
    evidence_note = build_evidence_index()
    telemetry_note = build_telemetry()
    outputs = [task_note, evidence_note, telemetry_note, hook_note, *memory_notes]
    print("Generated:")
    for p in outputs:
        print(rel(p))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
