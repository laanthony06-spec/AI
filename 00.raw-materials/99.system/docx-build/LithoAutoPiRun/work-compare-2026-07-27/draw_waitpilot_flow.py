from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 4096, 3264
LINE = 6
BLACK = "black"
WHITE = "white"
FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
OUTPUT = Path(
    r"D:\Obsidian\work\OBSidianCodex\00.raw-materials\90.processed"
    r"\LithoAutoPiRun\_work_compare\03_WaitPilotChangeFOUP_修复.png"
)

image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
draw = ImageDraw.Draw(image)
font_node = ImageFont.truetype(FONT_PATH, 58)
font_small = ImageFont.truetype(FONT_PATH, 50)
font_branch = ImageFont.truetype(FONT_PATH, 46)


def text_center(box: tuple[int, int, int, int], text: str, font=font_node) -> None:
    x1, y1, x2, y2 = box
    text_box = draw.multiline_textbbox((0, 0), text, font=font, spacing=6, align="center")
    tw = text_box[2] - text_box[0]
    th = text_box[3] - text_box[1]
    x = (x1 + x2 - tw) / 2
    y = (y1 + y2 - th) / 2 - text_box[1]
    draw.multiline_text((x, y), text, fill=BLACK, font=font, spacing=6, align="center")


def rect(box: tuple[int, int, int, int], text: str, font=font_node) -> None:
    draw.rectangle(box, outline=BLACK, fill=WHITE, width=LINE)
    text_center(box, text, font)


def diamond(
    cx: int, cy: int, w: int, h: int, text: str, font=font_node
) -> tuple[int, int, int, int]:
    points = [(cx, cy - h // 2), (cx + w // 2, cy), (cx, cy + h // 2), (cx - w // 2, cy)]
    draw.polygon(points, outline=BLACK, fill=WHITE)
    draw.line(points + [points[0]], fill=BLACK, width=LINE, joint="curve")
    box = (cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2)
    text_center(box, text, font)
    return box


def arrow_head(start: tuple[int, int], end: tuple[int, int], size: int = 24) -> None:
    x1, y1 = start
    x2, y2 = end
    if abs(x2 - x1) >= abs(y2 - y1):
        if x2 > x1:
            points = [(x2, y2), (x2 - size, y2 - size // 2), (x2 - size, y2 + size // 2)]
        else:
            points = [(x2, y2), (x2 + size, y2 - size // 2), (x2 + size, y2 + size // 2)]
    else:
        if y2 > y1:
            points = [(x2, y2), (x2 - size // 2, y2 - size), (x2 + size // 2, y2 - size)]
        else:
            points = [(x2, y2), (x2 - size // 2, y2 + size), (x2 + size // 2, y2 + size)]
    draw.polygon(points, fill=BLACK)


def arrow(points: list[tuple[int, int]]) -> None:
    draw.line(points, fill=BLACK, width=LINE, joint="curve")
    arrow_head(points[-2], points[-1])


def line(points: list[tuple[int, int]]) -> None:
    draw.line(points, fill=BLACK, width=LINE, joint="curve")


def branch_label(x: int, y: int, text: str) -> None:
    draw.text((x, y), text, fill=BLACK, font=font_branch)


# 主流程
rect((1570, 70, 2526, 230), "读取 2.1 LithoPilot")
arrow([(2048, 230), (2048, 310)])

diamond(2048, 430, 1500, 240, "Switch='Y' 且当前时间\n在 Trigger Time Slot?")
rect((3400, 350, 3970, 510), "不加卡控")
arrow([(2798, 430), (3400, 430)])
branch_label(3305, 370, "否")
arrow([(2048, 550), (2048, 650)])
branch_label(2080, 570, "是")

diamond(2048, 770, 1450, 240, "adhocplanname 含\n'UnScheduleSorter'?")
rect((160, 965, 1450, 1165), "卡控同 FOUP、非 AdhocSorter 的\nOther Lot", font_small)
rect((2646, 965, 3936, 1165), "卡控 Pilot 与同 FOUP、\n非 AdhocSorter 的 Other Lot", font_small)
arrow([(1323, 770), (805, 770), (805, 965)])
branch_label(1220, 700, "是")
arrow([(2773, 770), (3291, 770), (3291, 965)])
branch_label(2795, 700, "否")

line([(805, 1165), (805, 1215), (2048, 1215)])
line([(3291, 1165), (3291, 1215), (2048, 1215)])
rect((1505, 1270, 2591, 1430), "添加 WaitPilotChangeFOUP", font_small)
arrow([(2048, 1215), (2048, 1270)])

rect((1605, 1500, 2491, 1650), "按对象判断 Remove", font_small)
arrow([(2048, 1430), (2048, 1500)])

# 下半部分：所有判断分支均从菱形左右侧向外引出
diamond(2048, 1790, 1200, 220, "对象是 LithoPilot?")
branch_label(1390, 1710, "是")
branch_label(2620, 1710, "否")

diamond(760, 2060, 760, 210, "RemainQ<4H\n或触发 Qu_0?", font_small)
arrow([(1448, 1790), (760, 1790), (760, 1955)])

diamond(2910, 2000, 980, 210, "Other Lot 在 Litho?", font_small)
arrow([(2648, 1790), (2910, 1790), (2910, 1895)])

# Pilot 分支：结果节点置于菱形外侧，连线不向内折返
rect((40, 1975, 330, 2145), "Remove\n卡控", font_small)
rect((1190, 1975, 1510, 2145), "保持\n卡控", font_small)
arrow([(380, 2060), (330, 2060)])
arrow([(1140, 2060), (1190, 2060)])
branch_label(335, 1985, "是")
branch_label(1100, 1985, "否")

# Other Lot 位于 Litho：是则在右侧保持；否则向下继续判断 Barco
rect((3510, 1915, 4050, 2085), "保持卡控", font_small)
arrow([(3400, 2000), (3510, 2000)])
branch_label(3430, 1925, "是")
diamond(2910, 2310, 980, 210, "Other Lot 在 Barco?", font_small)
arrow([(2910, 2105), (2910, 2205)])
branch_label(2945, 2115, "否")

# Barco/其他站点继续向菱形左右外侧展开
diamond(1900, 2620, 720, 200, "RemainQ<4H\n或触发 Qu_0?", font_small)
arrow([(2420, 2310), (1900, 2310), (1900, 2520)])
branch_label(2300, 2325, "是")

diamond(3500, 2620, 560, 200, "触发 Qu_0?", font_small)
arrow([(3400, 2310), (3500, 2310), (3500, 2520)])
branch_label(3425, 2325, "否")

rect((1040, 2535, 1500, 2705), "Remove卡控", font_small)
rect((2300, 2535, 2720, 2705), "保持卡控", font_small)
arrow([(1540, 2620), (1500, 2620)])
arrow([(2260, 2620), (2300, 2620)])
branch_label(1480, 2540, "是")
branch_label(2220, 2540, "否")

rect((2780, 2535, 3160, 2705), "Remove卡控", font_small)
rect((3820, 2535, 4070, 2705), "保持\n卡控", font_small)
arrow([(3220, 2620), (3160, 2620)])
arrow([(3780, 2620), (3820, 2620)])
branch_label(3140, 2540, "是")
branch_label(3730, 2540, "否")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
image.save(OUTPUT, format="PNG", optimize=True, dpi=(300, 300))
print(OUTPUT)
