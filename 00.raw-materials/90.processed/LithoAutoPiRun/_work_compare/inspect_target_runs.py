from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.text.paragraph import Paragraph


TARGETS = (
    "从 UI.RTDConfig",
    "（2）判断 Lot 的片数",
    "⑦Min(lotid)",
    "将排序第一的 Lot+Context",
    "以上五项为",
    "若 Context 对应的 pi_splitcnt",
    "对于需 TransferFOUP",
    "拿取 2.1 中的 LithoPilot",
    "通过表fabfutureaction拿取",
    "1.2.1 执行前复核",
    "（1）分批 Lot 属于本厂",
    "（2）Lot 当前状态",
    "（3）Lot 当前站点",
    "（4）Lot 当前 Capability",
    "（5）CarrierKind",
    "（6）Report 中选中",
    "仅检查 Wafer 归属",
    "1.2.2 空FOUP",
    "当 IsNeedSplit=T 时",
    "获取 Report：LithoPiLotAutoDoAdhocSorter",
)


def iter_paragraphs(doc: Document):
    for p_element in doc.element.body.iter():
        if p_element.tag.endswith("}p"):
            yield Paragraph(p_element, doc)


def main() -> None:
    doc = Document(Path(sys.argv[1]))
    for index, paragraph in enumerate(iter_paragraphs(doc)):
        if any(paragraph.text.startswith(prefix) for prefix in TARGETS):
            print(f"\n[{index}] {paragraph.text}")
            for run_index, run in enumerate(paragraph.runs):
                print(f"  run {run_index}: {run.text!r}")


if __name__ == "__main__":
    main()
