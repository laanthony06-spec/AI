from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUTPUT_DIR = Path(__file__).resolve().parent / "generated_flowcharts"
FONT_PATH = Path(r"C:\Windows\Fonts\msyh.ttc")

BLACK = 0
WHITE = 255
STROKE = 7
ARROW_LENGTH = 25
ARROW_HALF_WIDTH = 14


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size=size)


def center_text(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    text: str,
    text_font: ImageFont.FreeTypeFont,
    max_width: int,
    line_spacing: int = 10,
) -> None:
    lines: list[str] = []
    for source_line in text.splitlines() or [""]:
        if not source_line:
            lines.append("")
            continue
        current = ""
        for character in source_line:
            candidate = current + character
            width = draw.textbbox((0, 0), candidate, font=text_font)[2]
            if current and width > max_width:
                lines.append(current)
                current = character
            else:
                current = candidate
        lines.append(current)

    boxes = [draw.textbbox((0, 0), line, font=text_font) for line in lines]
    heights = [box[3] - box[1] for box in boxes]
    total_height = sum(heights) + line_spacing * max(0, len(lines) - 1)
    y = center[1] - total_height / 2
    for line, box, height in zip(lines, boxes, heights):
        width = box[2] - box[0]
        draw.text(
            (center[0] - width / 2, y - box[1]),
            line,
            fill=BLACK,
            font=text_font,
        )
        y += height + line_spacing


def rect(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    size: tuple[int, int],
    text: str,
    text_font: ImageFont.FreeTypeFont,
) -> dict[str, tuple[int, int]]:
    cx, cy = center
    width, height = size
    left = cx - width // 2
    top = cy - height // 2
    right = cx + width // 2
    bottom = cy + height // 2
    draw.rectangle((left, top, right, bottom), outline=BLACK, width=STROKE)
    center_text(draw, center, text, text_font, width - 60)
    return {
        "center": center,
        "top": (cx, top),
        "bottom": (cx, bottom),
        "left": (left, cy),
        "right": (right, cy),
    }


def diamond(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    size: tuple[int, int],
    text: str,
    text_font: ImageFont.FreeTypeFont,
) -> dict[str, tuple[int, int]]:
    cx, cy = center
    width, height = size
    points = [
        (cx, cy - height // 2),
        (cx + width // 2, cy),
        (cx, cy + height // 2),
        (cx - width // 2, cy),
    ]
    draw.line(points + [points[0]], fill=BLACK, width=STROKE, joint="curve")
    center_text(draw, center, text, text_font, int(width * 0.62))
    return {
        "center": center,
        "top": points[0],
        "right": points[1],
        "bottom": points[2],
        "left": points[3],
    }


def arrow(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    label: str | None = None,
    label_position: tuple[int, int] | None = None,
    label_font: ImageFont.FreeTypeFont | None = None,
) -> None:
    draw.line(points, fill=BLACK, width=STROKE, joint="curve")
    start_x, start_y = points[-2]
    end_x, end_y = points[-1]
    angle = math.atan2(end_y - start_y, end_x - start_x)
    base_x = end_x - ARROW_LENGTH * math.cos(angle)
    base_y = end_y - ARROW_LENGTH * math.sin(angle)
    perp_x = ARROW_HALF_WIDTH * math.sin(angle)
    perp_y = -ARROW_HALF_WIDTH * math.cos(angle)
    head = [
        (end_x, end_y),
        (int(base_x + perp_x), int(base_y + perp_y)),
        (int(base_x - perp_x), int(base_y - perp_y)),
    ]
    draw.polygon(head, fill=BLACK)
    if label and label_position and label_font:
        draw.text(label_position, label, fill=BLACK, font=label_font)


def line(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]]) -> None:
    draw.line(points, fill=BLACK, width=STROKE, joint="curve")


def save_black_white(image: Image.Image, path: Path) -> None:
    binary = image.point(lambda pixel: WHITE if pixel >= 160 else BLACK, mode="1")
    binary.convert("RGB").save(path, dpi=(300, 300), optimize=True)


def build_pilot_selection() -> Path:
    image = Image.new("L", (2200, 2050), WHITE)
    draw = ImageDraw.Draw(image)
    node_font = font(56)
    small_font = font(48)
    branch_font = font(50)

    sort_node = rect(draw, (1100, 170), (1000, 150), "按 1.4.2 排序", node_font)
    available = diamond(
        draw,
        (1100, 500),
        (1250, 270),
        "有可用 Context\n且有可用 Lot？",
        node_font,
    )
    select = rect(
        draw,
        (1100, 815),
        (1050, 160),
        "固定首项为已选 Pilot",
        node_font,
    )
    remove = rect(
        draw,
        (1100, 1080),
        (1250, 180),
        "移除 Lot 或 Context 相同的\n其他候选",
        small_font,
    )
    update = rect(
        draw,
        (1100, 1395),
        (1450, 250),
        "更新 ReticleSTNRank\nContextCandidateCount\nActualSTNPilotCount",
        small_font,
    )
    resort = rect(
        draw,
        (1100, 1740),
        (1050, 160),
        "按最新指标重新排序",
        node_font,
    )
    finish = rect(draw, (1930, 500), (430, 150), "结束挑选", node_font)

    arrow(draw, [sort_node["bottom"], available["top"]])
    arrow(
        draw,
        [available["bottom"], select["top"]],
        "是",
        (1130, 645),
        branch_font,
    )
    arrow(
        draw,
        [available["right"], finish["left"]],
        "否",
        (1740, 425),
        branch_font,
    )
    arrow(draw, [select["bottom"], remove["top"]])
    arrow(draw, [remove["bottom"], update["top"]])
    arrow(draw, [update["bottom"], resort["top"]])
    arrow(
        draw,
        [
            resort["bottom"],
            (1100, 1940),
            (220, 1940),
            (220, 170),
            sort_node["left"],
        ],
    )

    path = OUTPUT_DIR / "01_1.4.3_Pilot挑选逻辑.png"
    save_black_white(image, path)
    return path


def build_wait_pilot_change_foup() -> Path:
    image = Image.new("L", (3800, 3560), WHITE)
    draw = ImageDraw.Draw(image)
    node_font = font(62)
    compact_font = font(56)
    branch_font = font(52)

    pilot = rect(draw, (1900, 145), (950, 140), "读取 2.1 LithoPilot", node_font)
    gate = diamond(
        draw,
        (1900, 430),
        (1350, 250),
        "Switch='Y' 且当前时间\n在 Trigger Time Slot？",
        compact_font,
    )
    no_control = rect(draw, (3450, 430), (570, 140), "不加卡控", node_font)
    at_sorter = diamond(
        draw,
        (1900, 770),
        (1320, 250),
        "adhocplanname 含\n'UnScheduleSorter'？",
        compact_font,
    )
    scope_other = rect(
        draw,
        (800, 1090),
        (1250, 190),
        "卡控同 FOUP、非 AdhocSorter 的\nOther Lot",
        compact_font,
    )
    scope_all = rect(
        draw,
        (3000, 1090),
        (1350, 190),
        "卡控 Pilot 与同 FOUP、\n非 AdhocSorter 的 Other Lot",
        compact_font,
    )
    add_reason = rect(
        draw,
        (1900, 1415),
        (1120, 145),
        "添加 WaitPilotChangeFOUP",
        node_font,
    )
    iterate = rect(draw, (1900, 1645), (1050, 135), "按对象类型判断 Remove", node_font)
    is_pilot = diamond(
        draw,
        (1900, 1925),
        (1100, 230),
        "对象是 LithoPilot？",
        node_font,
    )
    pilot_remove = diamond(
        draw,
        (800, 2285),
        (980, 240),
        "RemainQ<4H\n或触发 Qu_0？",
        compact_font,
    )
    other_litho = diamond(
        draw,
        (2850, 2285),
        (950, 230),
        "Other Lot 在 Litho？",
        compact_font,
    )
    pilot_remove_yes = rect(draw, (420, 2640), (590, 140), "Remove 卡控", node_font)
    pilot_remove_no = rect(draw, (1180, 2640), (590, 140), "保持卡控", node_font)
    litho_keep = rect(draw, (3570, 2285), (460, 140), "保持卡控", compact_font)
    other_barco = diamond(
        draw,
        (2850, 2640),
        (900, 220),
        "Other Lot 在 Barco？",
        compact_font,
    )
    barco_remove = diamond(
        draw,
        (2050, 3010),
        (1020, 230),
        "RemainQ<4H\n或触发 Qu_0？",
        compact_font,
    )
    other_remove = diamond(
        draw,
        (3300, 3010),
        (800, 220),
        "触发 Qu_0？",
        node_font,
    )
    barco_yes = rect(draw, (1770, 3380), (570, 140), "Remove 卡控", node_font)
    barco_no = rect(draw, (2320, 3380), (500, 140), "保持卡控", compact_font)
    other_yes = rect(draw, (3070, 3380), (570, 140), "Remove 卡控", node_font)
    other_no = rect(draw, (3600, 3380), (380, 140), "保持卡控", compact_font)

    arrow(draw, [pilot["bottom"], gate["top"]])
    arrow(
        draw,
        [gate["right"], no_control["left"]],
        "否",
        (3110, 345),
        branch_font,
    )
    arrow(
        draw,
        [gate["bottom"], at_sorter["top"]],
        "是",
        (1945, 585),
        branch_font,
    )
    arrow(
        draw,
        [at_sorter["left"], (800, 770), scope_other["top"]],
        "是",
        (1130, 685),
        branch_font,
    )
    arrow(
        draw,
        [at_sorter["right"], (3000, 770), scope_all["top"]],
        "否",
        (2650, 685),
        branch_font,
    )
    line(draw, [scope_other["bottom"], (800, 1280), (1900, 1280)])
    line(draw, [scope_all["bottom"], (3000, 1280), (1900, 1280)])
    arrow(draw, [(1900, 1280), add_reason["top"]])
    arrow(draw, [add_reason["bottom"], iterate["top"]])
    arrow(draw, [iterate["bottom"], is_pilot["top"]])
    arrow(
        draw,
        [is_pilot["left"], (800, 1925), pilot_remove["top"]],
        "是",
        (1190, 1840),
        branch_font,
    )
    arrow(
        draw,
        [is_pilot["right"], (2850, 1925), other_litho["top"]],
        "否",
        (2570, 1840),
        branch_font,
    )
    arrow(
        draw,
        [pilot_remove["left"], (420, 2285), pilot_remove_yes["top"]],
        "是",
        (315, 2175),
        branch_font,
    )
    arrow(
        draw,
        [pilot_remove["right"], (1180, 2285), pilot_remove_no["top"]],
        "否",
        (1240, 2175),
        branch_font,
    )
    arrow(
        draw,
        [other_litho["right"], litho_keep["left"]],
        "是",
        (3335, 2190),
        branch_font,
    )
    arrow(
        draw,
        [other_litho["bottom"], other_barco["top"]],
        "否",
        (2895, 2430),
        branch_font,
    )
    arrow(
        draw,
        [other_barco["left"], (2050, 2640), barco_remove["top"]],
        "是",
        (2260, 2545),
        branch_font,
    )
    arrow(
        draw,
        [other_barco["right"], (3300, 2640), other_remove["top"]],
        "否",
        (3210, 2545),
        branch_font,
    )
    arrow(
        draw,
        [barco_remove["left"], (1770, 3010), barco_yes["top"]],
        "是",
        (1640, 2900),
        branch_font,
    )
    arrow(
        draw,
        [barco_remove["right"], (2320, 3010), barco_no["top"]],
        "否",
        (2450, 2900),
        branch_font,
    )
    arrow(
        draw,
        [other_remove["left"], (3070, 3010), other_yes["top"]],
        "是",
        (2950, 2900),
        branch_font,
    )
    arrow(
        draw,
        [other_remove["right"], (3600, 3010), other_no["top"]],
        "否",
        (3570, 2900),
        branch_font,
    )

    path = OUTPUT_DIR / "02_3.1_WaitPilotChangeFOUP卡控逻辑.png"
    save_black_white(image, path)
    return path


def build_parent_child_same_tool() -> Path:
    image = Image.new("L", (2600, 2800), WHITE)
    draw = ImageDraw.Draw(image)
    node_font = font(58)
    compact_font = font(52)
    branch_font = font(50)

    relation = rect(
        draw,
        (1050, 150),
        (1250, 170),
        "按 Prod+Layer 匹配 relation\n获取 curr_layer",
        compact_font,
    )
    pretool = rect(
        draw,
        (1050, 430),
        (1250, 170),
        "按 Prod+curr_layer 匹配 OVL\n获取 pretool",
        compact_font,
    )
    has_pretool = diamond(
        draw,
        (1050, 735),
        (1080, 230),
        "pretool 非空？",
        node_font,
    )
    original_1 = rect(draw, (2250, 735), (600, 140), "按原逻辑判断", node_font)
    future_merge = rect(
        draw,
        (1050, 1045),
        (1300, 170),
        "从 fabfutureaction 获取\nFutureMerge 子/母批",
        compact_font,
    )
    history = rect(
        draw,
        (1050, 1365),
        (1450, 220),
        "按 Lot/Prod/Layer 查询 history\n按完成时间、记录 ID 降序\n获取最新 toolid",
        compact_font,
    )
    whitelist = rect(
        draw,
        (1050, 1690),
        (1250, 170),
        "按 productid/layerid/lotid\n匹配白名单",
        compact_font,
    )
    specify = diamond(
        draw,
        (1050, 1995),
        (1000, 220),
        "Specify Lot？",
        node_font,
    )
    original_2 = rect(draw, (2250, 1995), (600, 140), "按原逻辑判断", node_font)
    same_tool = diamond(
        draw,
        (1050, 2350),
        (1400, 250),
        "待判断机台与子/母批\n作业 toolid 一致？",
        compact_font,
    )
    original_3 = rect(draw, (2250, 2350), (600, 140), "按原逻辑判断", node_font)
    control = rect(
        draw,
        (1050, 2680),
        (1700, 160),
        "卡控 Parent&ChildLotNeedRunSameTool",
        compact_font,
    )

    arrow(draw, [relation["bottom"], pretool["top"]])
    arrow(draw, [pretool["bottom"], has_pretool["top"]])
    arrow(
        draw,
        [has_pretool["right"], original_1["left"]],
        "否",
        (1770, 645),
        branch_font,
    )
    arrow(
        draw,
        [has_pretool["bottom"], future_merge["top"]],
        "是",
        (1090, 870),
        branch_font,
    )
    arrow(draw, [future_merge["bottom"], history["top"]])
    arrow(draw, [history["bottom"], whitelist["top"]])
    arrow(draw, [whitelist["bottom"], specify["top"]])
    arrow(
        draw,
        [specify["right"], original_2["left"]],
        "是",
        (1720, 1905),
        branch_font,
    )
    arrow(
        draw,
        [specify["bottom"], same_tool["top"]],
        "否",
        (1090, 2120),
        branch_font,
    )
    arrow(
        draw,
        [same_tool["right"], original_3["left"]],
        "是",
        (1810, 2255),
        branch_font,
    )
    arrow(
        draw,
        [same_tool["bottom"], control["top"]],
        "否",
        (1090, 2490),
        branch_font,
    )

    path = OUTPUT_DIR / "03_3.2.2_ParentChildLot同机台卡控逻辑.png"
    save_black_white(image, path)
    return path


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for output in (
        build_pilot_selection(),
        build_wait_pilot_change_foup(),
        build_parent_child_same_tool(),
    ):
        print(output)


if __name__ == "__main__":
    main()
