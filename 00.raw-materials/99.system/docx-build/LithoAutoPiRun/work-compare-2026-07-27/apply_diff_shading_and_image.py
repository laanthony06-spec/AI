from __future__ import annotations

import hashlib
import zipfile
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph


BASE = Path(r"D:\Obsidian\work\OBSidianCodex\00.raw-materials\90.processed\LithoAutoPiRun")
INPUT = BASE / "LithoAutoPiRun_需求申请单_最终版_流程图更新.docx"
OUTPUT = BASE / "LithoAutoPiRun_需求申请单_最终版_流程图更新_差异标注.docx"
NEW_IMAGE = BASE / "_work_compare" / "03_WaitPilotChangeFOUP_修复.png"
MEDIA_TARGET = "word/media/image6.png"
YELLOW = "FFFF00"


FULL_PARAGRAPHS = {
    "⑦Min(lotid)",
    "以上五项为“或”关系，任一项成立时将整批设为 Pilot。",
    "1.2.1 执行前复核",
    "（1）分批 Lot 属于本厂，即 FAB6 或 FAB8；",
    "（2）Lot 当前状态为 WaitForJobPrep；",
    "（3）Lot 当前站点的 runcardid 为空；",
    "（4）Lot 当前 Capability 为 LithoCapability、L-BARCO-L 或 L-BARCO-S；",
    "（5）CarrierKind='FOUP'；",
    "（6）Report 中选中的 Wafer 确实存在于该 Lot 中。",
    "仅检查 Wafer 归属关系，不额外检查 Wafer 状态、Slot 或 Chuck。任一复核项不满足时，停止处理该 Lot，记录失败原因并等待下一轮重新计算，不回退为整批 Pilot。",
    "1.2.2 空FOUP与MES物理分批",
    "当 IsNeedSplit=T 时，先执行上述六项复核。复核通过后，先获取并预占空 Foup，再给 MES 物理分批接口，将 pi_splitwafer 从 Lot 中分出。若未拿到可用空 Foup，则不执行物理分批，将整批 Lot 传给 R2R；若分批接口 Fail，则立即释放预占的空 Foup，并将整批 Lot 传给 R2R；否则将分出的子批 pilot 传给 R2R。",
}

PARTIAL_PARAGRAPHS = {
    "从 UI.RTDConfig-LITHOLotAssignment-LithoAssignCapability 中获取 LithoCapability；BARCO Capability 固定为 L-BARCO-L、L-BARCO-S。": [
        "；BARCO Capability 固定为 L-BARCO-L、L-BARCO-S。"
    ],
    "（2）判断 Lot 的片数是否大于等于 Pi_splitcnt（默认为4），若是则 SplitCntMatched=1，否则为0；Pi_splitcnt 为空、为0、为负数或大于25时使用默认值4；": [
        "；Pi_splitcnt 为空、为0、为负数或大于25时使用默认值4；"
    ],
    "将排序第一的 Lot+Context 固定，作为已选 Pilot 的 Context，并去除 lot/Context 与已选 Context 相同的其他 Lot+Context，在更新 ReticleSTNRank、ContextCandidateCount、ActualSTNPilotCount 指标后，进入下一轮循环，直至无可用 Context 或无可用 Lot 后，结束循环。每个 Context 最多选择一个 Pilot。": [
        "每个 Context 最多选择一个 Pilot。"
    ],
    "若 Context 对应的 pi_splitcnt 有值，则按排序顺序挑选 pi_splitcnt 片 Wafer 作为 pi_splitwafer；pi_splitcnt 为空、为0、为负数或大于25时，使用默认值4。若选片数大于 Lot 当前可用 Wafer 数，则不执行物理分批，改为整批 Pilot。": [
        "；pi_splitcnt 为空、为0、为负数或大于25时，使用默认值4。若选片数大于 Lot 当前可用 Wafer 数，则不执行物理分批，改为整批 Pilot。"
    ],
    "对于需 TransferFOUP 的 LithoPilot 进行排序，拿取 LithoPilot 的 RemainQ、Priority、componentqty 指标，并按照 Min(RemainQ)、Min(Priority)、Max(componentqty)、Min(lotid)排序，根据排序建立 AdhocSorterJob。": [
        "、Min(lotid)"
    ],
    "通过表fabfutureaction拿取和lot有FutureMerge关系的子批/母批lot，从表r2r_lot_history中（匹配Lotid、productid、layerid）获取最新一笔子批/母批在待判断lot当前layer的作业机台toolid（按实际作业完成时间、记录ID降序取最新记录）。": [
        "（按实际作业完成时间、记录ID降序取最新记录）"
    ],
    "获取 Report：LithoPiLotAutoDoAdhocSorter 栏位信息，并按顺序给 MES 打 TransferFOUP 接口，将 Pilot 导到空 FOUP 中，若拿取可用的空 Foup 失败或空 Foup 数量为0，或 MES TransferFOUP 接口失败，则在 AMALog 中记录 Fail 信息。": [
        "，或 MES TransferFOUP 接口失败"
    ],
}


def iter_paragraphs(doc: Document):
    for element in doc.element.body.iter():
        if element.tag == qn("w:p"):
            yield Paragraph(element, doc)


def make_run_like(source_run, text: str, shaded: bool):
    run = OxmlElement("w:r")
    if source_run._r.rPr is not None:
        run.append(deepcopy(source_run._r.rPr))
    if shaded:
        rpr = run.get_or_add_rPr()
        for old in list(rpr.findall(qn("w:shd"))):
            rpr.remove(old)
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), YELLOW)
        rpr.append(shd)
    text_element = OxmlElement("w:t")
    if text[:1].isspace() or text[-1:].isspace():
        text_element.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    text_element.text = text
    run.append(text_element)
    return run


def shade_whole_paragraph(paragraph: Paragraph) -> None:
    for run in paragraph.runs:
        if run.text:
            rpr = run._r.get_or_add_rPr()
            for old in list(rpr.findall(qn("w:shd"))):
                rpr.remove(old)
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), YELLOW)
            rpr.append(shd)


def shade_substrings(paragraph: Paragraph, substrings: list[str]) -> None:
    if len(paragraph.runs) != 1 or paragraph.runs[0].text != paragraph.text:
        raise ValueError(f"目标段落不是单一文本 Run，无法安全拆分：{paragraph.text}")
    source_run = paragraph.runs[0]
    spans = []
    for substring in substrings:
        start = paragraph.text.index(substring)
        spans.append((start, start + len(substring)))
    spans.sort()

    segments: list[tuple[str, bool]] = []
    cursor = 0
    for start, end in spans:
        if start > cursor:
            segments.append((paragraph.text[cursor:start], False))
        segments.append((paragraph.text[start:end], True))
        cursor = end
    if cursor < len(paragraph.text):
        segments.append((paragraph.text[cursor:], False))

    parent = source_run._r.getparent()
    insertion_index = parent.index(source_run._r)
    parent.remove(source_run._r)
    for offset, (text, shaded) in enumerate(segments):
        parent.insert(insertion_index + offset, make_run_like(source_run, text, shaded))


def replace_media(docx_path: Path, media_path: str, image_path: Path) -> None:
    temp = docx_path.with_suffix(".media.tmp.docx")
    with zipfile.ZipFile(docx_path, "r") as source, zipfile.ZipFile(
        temp, "w", compression=zipfile.ZIP_DEFLATED
    ) as target:
        found = False
        for item in source.infolist():
            if item.filename == media_path:
                target.writestr(item, image_path.read_bytes())
                found = True
            else:
                target.writestr(item, source.read(item.filename))
        if not found:
            raise FileNotFoundError(f"未找到文档媒体：{media_path}")
    temp.replace(docx_path)


def validate(docx_path: Path) -> None:
    with zipfile.ZipFile(docx_path) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"DOCX ZIP 校验失败：{bad}")
        media_bytes = archive.read(MEDIA_TARGET)
        if hashlib.sha256(media_bytes).digest() != hashlib.sha256(NEW_IMAGE.read_bytes()).digest():
            raise ValueError("3.1 流程图替换后校验失败")

    doc = Document(docx_path)
    paragraphs = list(iter_paragraphs(doc))
    yellow_runs = 0
    for paragraph in paragraphs:
        for run in paragraph.runs:
            rpr = run._r.rPr
            if rpr is None:
                continue
            shd = rpr.find(qn("w:shd"))
            if shd is not None and shd.get(qn("w:fill")) == YELLOW:
                yellow_runs += 1
    if yellow_runs < len(FULL_PARAGRAPHS) + len(PARTIAL_PARAGRAPHS):
        raise ValueError(f"黄色底纹数量异常：{yellow_runs}")
    print(f"输出：{docx_path}")
    print(f"黄色底纹 Run：{yellow_runs}")
    print(f"文档段落：{len(paragraphs)}")


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(INPUT)
    if not NEW_IMAGE.exists():
        raise FileNotFoundError(NEW_IMAGE)

    doc = Document(INPUT)
    seen_full: set[str] = set()
    seen_partial: set[str] = set()

    for paragraph in iter_paragraphs(doc):
        if paragraph.text in FULL_PARAGRAPHS:
            if paragraph.text in seen_full:
                raise ValueError(f"整段标注目标重复：{paragraph.text}")
            shade_whole_paragraph(paragraph)
            seen_full.add(paragraph.text)
        elif paragraph.text in PARTIAL_PARAGRAPHS:
            if paragraph.text in seen_partial:
                raise ValueError(f"局部标注目标重复：{paragraph.text}")
            shade_substrings(paragraph, PARTIAL_PARAGRAPHS[paragraph.text])
            seen_partial.add(paragraph.text)

    missing_full = FULL_PARAGRAPHS - seen_full
    missing_partial = set(PARTIAL_PARAGRAPHS) - seen_partial
    if missing_full or missing_partial:
        raise ValueError(
            f"未找到全部目标段落：full={sorted(missing_full)} partial={sorted(missing_partial)}"
        )

    doc.save(OUTPUT)
    replace_media(OUTPUT, MEDIA_TARGET, NEW_IMAGE)
    validate(OUTPUT)


if __name__ == "__main__":
    main()
