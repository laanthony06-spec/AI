from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMG_DIR = ROOT / "10.sources" / "images" / "dsp-dispatch-system-intro"
OCR_DIR = ROOT / "90.processed" / "dsp-dispatch-system-intro-ocr"
NOTE_DIR = ROOT / "90.processed" / "dsp-dispatch-system-intro-notes"
META_DIR = ROOT / "20.metadata"
NOTE_DIR.mkdir(parents=True, exist_ok=True)


def load_pages() -> list[dict]:
    pages = []
    for p in sorted(OCR_DIR.glob("p*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        pages.append(data)
    return pages


def page_link(page: dict) -> str:
    return f"![[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/{page['file']}]]"


def title_of(page: dict) -> str:
    lines = [x.strip() for x in page.get("lines", []) if x.strip()]
    noise = {"动画", "评论", "编辑", "Part", "Part/", "编辑Y式", "编辑V", "动通"}
    lines = [x for x in lines if x not in noise and not re.fullmatch(r"\d{2}", x)]
    if not lines:
        return f"第 {page['page']:03d} 页"
    t = lines[0]
    if len(t) < 4 and len(lines) > 1:
        t = lines[1]
    return t[:80]


def module_of(page: dict) -> str:
    p = int(page["page"])
    text = "\n".join(page.get("lines", []))
    if p <= 10:
        return "01 DSP 系统与自动化架构"
    if 11 <= p <= 25:
        return "02 自动化派工规则"
    if 26 <= p <= 33:
        return "03 AMHS 与搬送存储"
    if 34 <= p <= 49:
        return "04 QZone 管控"
    if 50 <= p <= 90:
        return "05 NPW 自动化处理"
    if p == 91:
        return "06 OverQtime 原因分析"
    if "QZone" in text or "Qzone" in text:
        return "04 QZone 管控"
    if "AMHS" in text or "Stocker" in text or "OHB" in text:
        return "03 AMHS 与搬送存储"
    if "NPW" in text or "Dummy" in text or "Monitor" in text:
        return "05 NPW 自动化处理"
    return "其他"


def category_of(page: dict) -> str:
    text = "\n".join(page.get("lines", [])).lower()
    if any(k.lower() in text for k in ["qzone", "qtime", "overqtime"]):
        return "QZone / QTime"
    if any(k.lower() in text for k in ["amhs", "stocker", "ohb", "mcs", "搬送", "存储"]):
        return "AMHS / 搬送"
    if any(k.lower() in text for k in ["npw", "dummy", "monitor", "reuse", "recycle", "downgrade"]):
        return "NPW 自动化"
    if any(k.lower() in text for k in ["litho", "etch", "cmp", "wet", "tf", "recipe", "r2r"]):
        return "Local 派工规则"
    if any(k.lower() in text for k in ["rtd", "ama", "global", "sorting", "wherenext"]):
        return "DSP / RTD / AMA"
    return "综合"


def pick_key_lines(page: dict, limit: int = 6) -> list[str]:
    keywords = [
        "概述", "功能描述", "主要流程", "触发条件", "管控逻辑", "Filter", "rule",
        "RTD", "AMA", "QZone", "Qtime", "NPW", "AMHS", "Stocker", "OHB",
        "派工", "管控", "筛选", "排序", "Reserve", "Reuse", "Recycle", "Downgrade",
        "断线", "堆货", "SafetyValue", "Recipe", "R2R", "Capability",
    ]
    out = []
    for line in page.get("lines", []):
        if any(k.lower() in line.lower() for k in keywords):
            out.append(line)
        if len(out) >= limit:
            break
    if not out:
        out = page.get("lines", [])[: min(limit, len(page.get("lines", [])))]
    return out


def write_ocr_markdown(pages: list[dict]) -> Path:
    out = OCR_DIR / "DSP派工系统简介-OCR原文.md"
    md = [
        "---",
        "type: ocr-result",
        "topic: DSP派工系统简介",
        "tags: [OCR, DSP, 自动派工, 派工系统]",
        "---",
        "",
        "# DSP 派工系统简介 - OCR 原文",
        "",
        f"> 图片数量：{len(pages)}。OCR 结果为自动识别，可能存在错字、漏字和表格顺序错位。",
        "",
    ]
    for page in pages:
        md += [
            f"## 第 {page['page']:03d} 页：{title_of(page)}",
            "",
            page_link(page),
            "",
        ]
        md.extend(page.get("lines", []))
        md.append("")
    out.write_text("\n".join(md), encoding="utf-8")
    return out


def write_structured_note(pages: list[dict]) -> Path:
    out = NOTE_DIR / "DSP派工系统简介-内容结构化.md"
    grouped: dict[str, list[dict]] = defaultdict(list)
    for page in pages:
        grouped[module_of(page)].append(page)

    md = [
        "---",
        "type: structured-source-note",
        "topic: DSP派工系统简介",
        "tags: [DSP, 自动派工, 结构化整理, RTD, AMA, QZone, NPW, AMHS]",
        "---",
        "",
        "# DSP 派工系统简介 - 内容结构化",
        "",
        "## 资料概况",
        "",
        f"- 原始图片数量：{len(pages)} 页",
        "- 资料形式：PPT 图片 OCR",
        "- 主题：DSP 自动派工系统、RTD、AMA、Global / Local 派工规则、AMHS、QZone、NPW 自动化",
        "- 重要提醒：本笔记基于 OCR 自动整理，涉及生产系统细节时应回看原图确认。",
        "",
        "## 总体目录",
        "",
    ]
    for module, ps in grouped.items():
        md.append(f"- {module}：第 {ps[0]['page']:03d}–{ps[-1]['page']:03d} 页")
    md.append("")

    for module, ps in grouped.items():
        md += [f"## {module}", ""]
        for page in ps:
            md += [
                f"### 第 {page['page']:03d} 页：{title_of(page)}",
                "",
                f"- 分类：{category_of(page)}",
                f"- 原图：[[00.raw-materials/10.sources/images/dsp-dispatch-system-intro/{page['file']}]]",
                "- 关键 OCR 行：",
            ]
            for line in pick_key_lines(page):
                md.append(f"  - {line}")
            md.append("")
    out.write_text("\n".join(md), encoding="utf-8")
    return out


def write_knowledge_note(pages: list[dict]) -> Path:
    out = NOTE_DIR / "DSP派工系统简介-派工系统知识提取.md"
    page_by_cat: dict[str, list[int]] = defaultdict(list)
    for page in pages:
        page_by_cat[category_of(page)].append(int(page["page"]))

    def refs(cat: str) -> str:
        nums = page_by_cat.get(cat, [])
        if not nums:
            return "未定位"
        return "、".join(f"p{n:03d}" for n in nums[:12]) + (" 等" if len(nums) > 12 else "")

    md = [
        "---",
        "type: knowledge-extraction",
        "topic: DSP派工系统简介",
        "tags: [DSP, 自动派工, 派工规则, QZone, AMHS, NPW, MES]",
        "---",
        "",
        "# DSP 派工系统简介 - 派工系统知识提取",
        "",
        "## 一句话理解",
        "",
        "DSP 派工系统围绕 RTD（实时派工）与 AMA（自动派工管理）展开：RTD 负责在实时约束下筛选、排序、推荐 Lot 与机台；AMA 负责派工触发、最终核对、NPW 自动化、搬送存储等管理流程，并与 MES、EAP、MCS、APC、PMS 等系统协同。",
        "",
        "## 系统边界与角色",
        "",
        "- **RTD / Real-Time Dispatching**：执行实时派工逻辑，处理 Lot、FOUP、Machine、Port、Recipe、Capability、QTime、QZone 等约束。",
        "- **AMA / Auto Move or Auto Dispatch Management**：承担派工触发、结果核对、Lot Pre-reserve、NPW 管理等自动化功能。",
        "- **MES**：提供 Lot 状态、工艺路线、Recipe、Hold、Comment、RTDInfo 等生产执行数据。",
        "- **EAP / MCS / AMHS**：承接设备自动化与搬送任务，影响 FOUP 到机台 Load Port 的到达效率。",
        "- **APC / PMS**：提供过程控制、设备状态、PM / Clean / R2R 等约束信息。",
        "",
        "## 核心派工链路",
        "",
        "```text",
        "触发事件 / 定时扫描",
        "  → 获取可派工 Lot 与设备状态",
        "  → Global Rule 过滤",
        "  → Local Rule 过滤",
        "  → QZone / QTime / Capacity 检查",
        "  → 排序与优先级计算",
        "  → Reserve / Pre-reserve",
        "  → 搬送与 Load Port 上料",
        "  → 异常原因回写与查询",
        "```",
        "",
        "## Global 派工规则",
        "",
        f"参考页：{refs('DSP / RTD / AMA')}、{refs('QZone / QTime')}",
        "",
        "Global Rule 是跨 Module 通用的派工过滤逻辑，关注整体控线角度，而非单一设备作业方式。典型检查包括：",
        "",
        "- Lot 状态是否 OK",
        "- FOUP 状态是否 OK",
        "- Recipe 是否被 DSP 禁止",
        "- Reticle 是否在机台或可用",
        "- Machine / Chamber 是否处于可作业状态",
        "- 是否存在 Constraint、BatchID、Runcard 指定机台、Multi Lot in One FOUP 等限制",
        "- 是否被 QZone、Capacity、Path issue、下游断线或堆货限制",
        "",
        "## Local 派工规则",
        "",
        f"参考页：{refs('Local 派工规则')}",
        "",
        "Local Rule 根据不同 Module 的设备特性与工艺限制设计。OCR 中出现的典型区域包括：",
        "",
        "- **LITHO**：Reticle、R2R、DomaPath、高低能、垂直限定、放版指导。",
        "- **ETCH**：DomaPath、R2R、Recipe 连续作业、Lot 可作业性与紧急程度。",
        "- **TF**：Recipe 连续、Film 连续、连续上限、同条件 WIP、累计膜厚 Clean、瓶颈机台、ALL-SGE。",
        "- **CMP**：Recipe 连续、R2R、PM Cycle 内同条件连续、TRIM LifeTime、CCU 错开 PM。",
        "- **WET**：Chamber / Batch 两类逻辑，以及 WET-DIFF、WET-SGE 相关派工。",
        "",
        "## QZone / QTime 管控",
        "",
        f"参考页：{refs('QZone / QTime')}",
        "",
        "QZone 管控用于判断 Q-Time loop 起始站点的 Lot 是否可以继续放货，核心是防止下游断线、堆货或 QTime 风险扩大。",
        "",
        "关键概念：",
        "",
        "- **QTime Duration**：允许等待时间窗口。",
        "- **QTime Urgency**：Lot 剩余 QTime 风险等级。",
        "- **Remain WIP / WIP Limit**：QZone 中各站点或能力组允许的放货量。",
        "- **Path issue / Capacity issue**：下游路径断线或产能不足导致的卡控。",
        "- **Safety Value**：连环 QZone 出现断线或堆货时的风险分级与特殊管控。",
        "",
        "## AMHS 与搬送存储",
        "",
        f"参考页：{refs('AMHS / 搬送')}",
        "",
        "AMHS 相关内容包括 Stocker、OHB、MCS、搬送路径、预搬送等。搬送存储的目标不是单纯移动 FOUP，而是配合派工减少设备空等、缩短搬送路径、降低搬送系统负荷并提升设备利用率。",
        "",
        "需要特别关注：",
        "",
        "- Stocker / OHB 的临时存储能力",
        "- FOUP 从当前站点到下游设备的搬送时间",
        "- Load Port 可用性",
        "- 堆货机台或瓶颈机台的预搬送策略",
        "- AMHS 派工与机台派工之间的联动",
        "",
        "## NPW 自动化",
        "",
        f"参考页：{refs('NPW 自动化')}",
        "",
        "NPW 自动化覆盖 Routine Monitor、复机 NPW、Season、Dummy、Reuse、Recycle、Downgrade、Auto Reassign、IMP Monitor、THK NPW Auto Handle 等场景。",
        "",
        "可以抽象为四类问题：",
        "",
        "1. **何时分批**：By time、weekly、apply time、WAIT MFG、PM / TRC 流程等触发条件。",
        "2. **如何筛选母批 / 子批**：按 Filter rule、产品、设备、状态、使用次数、Recipe、Monitor group 过滤。",
        "3. **如何派工或复用**：Reserve、Reuse、Recycle、Downgrade、Auto Reassign。",
        "4. **失败如何处理**：Auto Handle Fail、自动 Hold、Cancel Control ID、异常原因追踪。",
        "",
        "## OverQtime 原因分析",
        "",
        f"参考页：{refs('综合')}",
        "",
        "OverQtime 分析关注长时间未派工产品在日志中的卡控原因，重点查明：",
        "",
        "- 是否被 Assign 卡控不派工",
        "- 是否未进入预排",
        "- 是否受 QZone / QTime / Capability / Recipe / 设备状态限制",
        "- 具体 OverQtime 时间、站点和卡控原因",
        "",
        "## 可沉淀为派工系统设计原则",
        "",
        "- 派工系统不是简单排序，而是“可作业性过滤 + 风险管控 + 优先级排序 + 搬送协同”。",
        "- Global Rule 解决共性约束，Local Rule 解决 Module / Tool 特有约束。",
        "- QZone 是控线与局部最优之间的关键平衡器。",
        "- AMHS 决定派工结果能否及时落地，尤其影响瓶颈机台空等。",
        "- NPW 自动化需要把生产、设备、工艺、监控片生命周期联动起来。",
        "- 异常查询能力与派工能力同等重要；没有 reason trace，派工系统难以维护。",
        "",
        "## 后续建议建立的专题笔记",
        "",
        "- [[DSP 派工系统]]",
        "- [[RTD 实时派工逻辑]]",
        "- [[AMA 自动派工管理]]",
        "- [[QZone 管控模型]]",
        "- [[AMHS 与派工联动]]",
        "- [[NPW 自动化管理]]",
        "- [[OverQtime 原因分析]]",
    ]
    out.write_text("\n".join(md), encoding="utf-8")
    return out


def update_material_card(pages: list[dict], files: list[Path]) -> None:
    card = META_DIR / "DSP派工系统简介-资料卡.md"
    md = [
        "---",
        "type: raw-material-card",
        "status: ocr-processed",
        "topic: DSP派工系统简介",
        "tags: [原始资料, DSP, 自动派工, 派工系统, PPT图片, OCR]",
        "created: 2026-07-04",
        "---",
        "",
        "# DSP 派工系统简介 - 资料卡",
        "",
        "## 基本信息",
        "",
        "| 字段 | 内容 |",
        "|---|---|",
        "| 资料名称 | DSP 派工系统简介 |",
        "| 资料类型 | PPT 图片 |",
        f"| 图片数量 | {len(pages)} 页 |",
        "| 当前状态 | 已重命名、已 OCR、已结构化整理 |",
        "| 原始图片目录 | [[00.raw-materials/10.sources/images/dsp-dispatch-system-intro]] |",
        "| OCR 输出目录 | [[00.raw-materials/90.processed/dsp-dispatch-system-intro-ocr]] |",
        "| 结构化笔记目录 | [[00.raw-materials/90.processed/dsp-dispatch-system-intro-notes]] |",
        "| 是否敏感 | 建议按内部资料处理 |",
        "",
        "## 处理产物",
        "",
    ]
    for f in files:
        rel = f.relative_to(ROOT.parent).as_posix()
        md.append(f"- [[{rel}]]")
    md += [
        "",
        "## 原始文件命名",
        "",
        "图片已统一重命名为：",
        "",
        "```text",
        "DSP派工系统简介_p001.jpg",
        "DSP派工系统简介_p002.jpg",
        "...",
        "```",
        "",
        "旧文件名到新文件名的映射：[[00.raw-materials/20.metadata/dsp-dispatch-system-intro-rename-map.json]]",
        "",
        "## 后续建议",
        "",
        "- [ ] 人工抽查关键页面 OCR 准确性",
        "- [ ] 将知识提取内容拆分到正式专题笔记",
        "- [ ] 对涉及公司内部系统、产线、设备、规则的内容进行敏感级别标注",
        "- [ ] 结合实际工作补充本厂派工规则、异常处理 SOP 和维护经验",
    ]
    card.write_text("\n".join(md), encoding="utf-8")


def main() -> None:
    pages = load_pages()
    f1 = write_ocr_markdown(pages)
    f2 = write_structured_note(pages)
    f3 = write_knowledge_note(pages)
    update_material_card(pages, [f1, f2, f3])
    print(f"built {len(pages)} pages")
    print(f1.as_posix())
    print(f2.as_posix())
    print(f3.as_posix())


if __name__ == "__main__":
    main()
