from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"D:\Obsidian\work\OBSidianCodex")
ASSET_DIR = ROOT / "00.raw-materials" / "99.system" / "docx-build" / "LithoAutoPiRun" / "assets"

CANVAS = (1800, 2100)
INK = "#000000"
PAPER = "#FFFFFF"
STROKE = 4
FLOW_STROKE = 4


def font(size: int, bold: bool = False):
    candidates = [
        Path(r"C:\Windows\Fonts\msyhbd.ttc") if bold else Path(r"C:\Windows\Fonts\msyh.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


FONT = font(31)
SMALL = font(25)
LIST_FONT = font(26)


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    w: int
    h: int
    text: str
    kind: str = "process"
    text_font: ImageFont.FreeTypeFont = FONT
    align: str = "center"

    @property
    def cx(self):
        return self.x + self.w // 2

    @property
    def cy(self):
        return self.y + self.h // 2

    def anchor(self, side: str):
        return {
            "top": (self.cx, self.y),
            "bottom": (self.cx, self.y + self.h),
            "left": (self.x, self.cy),
            "right": (self.x + self.w, self.cy),
        }[side]


def wrap(draw: ImageDraw.ImageDraw, text: str, used_font, max_width: int):
    lines = []
    for raw in text.split("\n"):
        if not raw:
            lines.append("")
            continue
        current = ""
        for char in raw:
            trial = current + char
            if draw.textbbox((0, 0), trial, font=used_font)[2] <= max_width or not current:
                current = trial
            else:
                lines.append(current)
                current = char
        if current:
            lines.append(current)
    return lines


def draw_text(draw: ImageDraw.ImageDraw, node: Node):
    if node.kind == "decision":
        max_width = int(node.w * 0.70)
    else:
        max_width = node.w - 70
    lines = wrap(draw, node.text, node.text_font, max_width)
    spacing = 8
    boxes = [draw.textbbox((0, 0), line or " ", font=node.text_font) for line in lines]
    heights = [box[3] - box[1] for box in boxes]
    total_h = sum(heights) + spacing * max(0, len(lines) - 1)
    y = node.cy - total_h // 2
    for line, box, line_h in zip(lines, boxes, heights):
        line_w = box[2] - box[0]
        if node.align == "left":
            x = node.x + 38
        else:
            x = node.cx - line_w // 2
        draw.text((x, y), line, font=node.text_font, fill=INK)
        y += line_h + spacing


def draw_node(draw: ImageDraw.ImageDraw, node: Node):
    box = (node.x, node.y, node.x + node.w, node.y + node.h)
    if node.kind == "terminator":
        draw.rounded_rectangle(box, radius=node.h // 2, fill=PAPER, outline=INK, width=STROKE)
    elif node.kind == "decision":
        points = [(node.cx, node.y), (node.x + node.w, node.cy),
                  (node.cx, node.y + node.h), (node.x, node.cy)]
        draw.polygon(points, fill=PAPER, outline=INK)
        draw.line(points + [points[0]], fill=INK, width=STROKE, joint="curve")
    else:
        draw.rectangle(box, fill=PAPER, outline=INK, width=STROKE)
    draw_text(draw, node)


def line(draw: ImageDraw.ImageDraw, points, arrow: bool = True):
    for start, end in zip(points, points[1:]):
        if start[0] != end[0] and start[1] != end[1]:
            raise ValueError(f"Connector must be orthogonal: {start} -> {end}")
    draw.line(points, fill=INK, width=FLOW_STROKE, joint="curve")
    if not arrow:
        return
    start, end = points[-2], points[-1]
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length, wing = 18, 9
    back_x = end[0] - math.cos(angle) * length
    back_y = end[1] - math.sin(angle) * length
    left = (back_x + math.cos(angle + math.pi / 2) * wing,
            back_y + math.sin(angle + math.pi / 2) * wing)
    right = (back_x + math.cos(angle - math.pi / 2) * wing,
             back_y + math.sin(angle - math.pi / 2) * wing)
    draw.polygon([end, left, right], fill=INK)


def edge_label(draw: ImageDraw.ImageDraw, xy, text: str):
    box = draw.textbbox((0, 0), text, font=SMALL)
    w, h = box[2] - box[0], box[3] - box[1]
    x, y = xy
    draw.rectangle((x - 7, y - 4, x + w + 7, y + h + 5), fill=PAPER)
    draw.text((x, y), text, font=SMALL, fill=INK)


def page():
    img = Image.new("RGB", CANVAS, PAPER)
    return img, ImageDraw.Draw(img)


def save(img: Image.Image, name: str):
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    img.save(ASSET_DIR / name, format="PNG", dpi=(300, 300), optimize=True)


def chart_rtd():
    img, d = page()
    n = {
        "a": Node(500, 40, 700, 90, "从 FAB6、FAB8 获取候选 Lot", "terminator"),
        "b": Node(430, 170, 840, 110, "获取 Lot、Carrier、Capability、RemainQ 等基础信息"),
        "c": Node(500, 330, 700, 140, "基础筛选条件全部满足？", "decision"),
        "d": Node(430, 520, 840, 110, "向后 Fetch 20 个站点，形成 PiRunLoop"),
        "e": Node(500, 680, 700, 140, "存在有效 CD、Litho 和 Reticle？", "decision"),
        "f": Node(500, 870, 700, 150, "同 FOUP 已有 Pilot、FutureHold\n或 RC？", "decision"),
        "g": Node(430, 1070, 840, 110, "获取并筛选可作业 Litho 机台"),
        "h": Node(500, 1230, 700, 140, "存在 Pi_split_flag='Y'\n的有效机台？", "decision"),
        "i": Node(430, 1420, 840, 110, "检查 R2R Context，并剔除多路径 Lot"),
        "j": Node(430, 1580, 840, 110, "计算 Lot 与 Context 排序指标"),
        "k": Node(500, 1740, 700, 100, "循环选择每个 Context 的最优 Pilot", "terminator"),
        "x": Node(1410, 910, 320, 110, "剔除该 Lot", "terminator"),
    }
    for node in n.values():
        draw_node(d, node)

    for a, b in [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"),
                 ("e", "f"), ("f", "g"), ("g", "h"), ("h", "i"),
                 ("i", "j"), ("j", "k")]:
        line(d, [n[a].anchor("bottom"), n[b].anchor("top")])
    edge_label(d, (920, 482), "是")
    edge_label(d, (920, 832), "是")
    edge_label(d, (920, 1030), "否")
    edge_label(d, (920, 1380), "是")

    bus_x = 1360
    for key, label in [("c", "否"), ("e", "否"), ("f", "是"), ("h", "否")]:
        start = n[key].anchor("right")
        line(d, [start, (bus_x, start[1])], arrow=False)
        edge_label(d, (1218, start[1] - 35), label)
    line(d, [(bus_x, n["c"].cy), (bus_x, n["h"].cy)], arrow=False)
    line(d, [(bus_x, n["x"].cy), n["x"].anchor("left")])
    save(img, "01-rtd-selection.png")


def chart_split():
    img, d = page()
    n = {
        "a": Node(520, 35, 760, 95, "取得已选 Lot + Context", "terminator"),
        "b": Node(400, 175, 1000, 235,
                  "整批条件（OR）\n1. BulletLot=1 或 KeyLot=1\n2. CurCapability=LithoCapability 且 FuLL(RemainQ)\n3. RequiredChuckCount=0\n4. SplitCntMatched=0\n5. componentqty<=6",
                  text_font=LIST_FONT, align="left"),
        "c": Node(520, 455, 760, 140, "以上任一条件满足？", "decision"),
        "x1": Node(80, 470, 360, 110, "IsNeedSplit=F\n整批设置为 Pilot", "terminator", SMALL),
        "d": Node(520, 650, 760, 105, "IsNeedSplit=T，读取 pi_splitcnt"),
        "e": Node(520, 805, 760, 140, "pi_splitcnt 是否为空，\n或 <=0，或 >25？", "decision"),
        "f": Node(1390, 820, 330, 110, "使用默认值 4", text_font=SMALL),
        "g": Node(520, 1000, 760, 140, "选片数是否大于\n当前可用 Wafer 数？", "decision"),
        "x2": Node(80, 1015, 360, 110, "改为整批 Pilot", "terminator", SMALL),
        "h": Node(520, 1195, 760, 105, "按 Wafer ID、Chuck／Slot 建立分组"),
        "i": Node(520, 1350, 760, 105, "计算 GroupRank 和 WaferRank"),
        "j": Node(520, 1505, 760, 110, "按 WaferRank ASC、GroupRank ASC 选片"),
        "k": Node(520, 1670, 760, 115, "生成 pi_splitwafer，并确定 Merge 站点", "terminator"),
    }
    for node in n.values():
        draw_node(d, node)

    line(d, [n["a"].anchor("bottom"), n["b"].anchor("top")])
    line(d, [n["b"].anchor("bottom"), n["c"].anchor("top")])
    line(d, [n["c"].anchor("left"), n["x1"].anchor("right")])
    edge_label(d, (452, 495), "是")
    line(d, [n["c"].anchor("bottom"), n["d"].anchor("top")])
    edge_label(d, (920, 605), "否")
    line(d, [n["d"].anchor("bottom"), n["e"].anchor("top")])
    line(d, [n["e"].anchor("right"), (1350, n["e"].cy), (1350, n["f"].cy), n["f"].anchor("left")])
    edge_label(d, (1295, n["e"].cy - 35), "是")
    line(d, [n["f"].anchor("bottom"), (n["f"].cx, 975), (900, 975), n["g"].anchor("top")])
    line(d, [n["e"].anchor("bottom"), n["g"].anchor("top")])
    edge_label(d, (920, 955), "否，使用配置值")
    line(d, [n["g"].anchor("left"), n["x2"].anchor("right")])
    edge_label(d, (452, 1040), "是")
    line(d, [n["g"].anchor("bottom"), n["h"].anchor("top")])
    edge_label(d, (920, 1150), "否")
    for a, b in [("h", "i"), ("i", "j"), ("j", "k")]:
        line(d, [n[a].anchor("bottom"), n[b].anchor("top")])
    save(img, "02-pilot-split.png")


def chart_wait():
    img, d = page()
    n = {
        "a": Node(520, 35, 760, 95, "获取需要 Transfer FOUP 的 Litho Pilot", "terminator"),
        "b": Node(520, 180, 760, 140, "WatchDog 已开启且位于\n触发时间范围？", "decision"),
        "x": Node(1400, 195, 320, 110, "不新增卡控", "terminator", SMALL),
        "c": Node(520, 370, 760, 140, "Pilot 位于 UnscheduledSorter？", "decision"),
        "d": Node(70, 585, 660, 120, "同 FOUP 中不在 Sorter 的 Other Lot\n增加 WaitPilotChangeFOUP", text_font=SMALL),
        "e": Node(1070, 585, 660, 120, "同 FOUP 中同样不在 Sorter 的 Other Lot\n增加 WaitPilotChangeFOUP", text_font=SMALL),
        "f": Node(520, 790, 760, 145, "Pilot 的 RemainQ<4 h\n或触发 Qu_0？", "decision"),
        "x2": Node(1400, 807, 320, 110, "解除相关卡控", "terminator", SMALL),
        "g": Node(520, 1000, 760, 145, "Other Lot 当前站点类型？", "decision"),
        "h": Node(50, 1240, 360, 110, "Litho：保持卡控", "terminator", SMALL),
        "i": Node(520, 1215, 520, 160, "BARCO：RemainQ<4 h\n或触发 Qu_0？", "decision", SMALL),
        "j": Node(1180, 1215, 520, 160, "其他站点：触发 Qu_0？", "decision", SMALL),
        "i1": Node(580, 1530, 400, 110, "解除卡控", "terminator", SMALL),
        "i2": Node(70, 1530, 360, 110, "保持卡控", "terminator", SMALL),
        "j1": Node(1120, 1530, 400, 110, "解除卡控", "terminator", SMALL),
        "j2": Node(1600, 1530, 200, 110, "保持卡控", "terminator", SMALL),
    }
    for node in n.values():
        draw_node(d, node)

    line(d, [n["a"].anchor("bottom"), n["b"].anchor("top")])
    line(d, [n["b"].anchor("right"), n["x"].anchor("left")])
    edge_label(d, (1290, 225), "否")
    line(d, [n["b"].anchor("bottom"), n["c"].anchor("top")])
    edge_label(d, (920, 330), "是")
    line(d, [n["c"].anchor("left"), (400, n["c"].cy), (400, 560), n["d"].anchor("top")])
    edge_label(d, (430, 432), "是")
    line(d, [n["c"].anchor("right"), (1400, n["c"].cy), (1400, 560), n["e"].anchor("top")])
    edge_label(d, (1295, 432), "否")
    line(d, [n["d"].anchor("bottom"), (n["d"].cx, 750), (900, 750)], arrow=False)
    line(d, [n["e"].anchor("bottom"), (n["e"].cx, 750), (900, 750)], arrow=False)
    line(d, [(900, 750), n["f"].anchor("top")])
    line(d, [n["f"].anchor("right"), n["x2"].anchor("left")])
    edge_label(d, (1290, 835), "是")
    line(d, [n["f"].anchor("bottom"), n["g"].anchor("top")])
    edge_label(d, (920, 950), "否")
    line(d, [n["g"].anchor("left"), (230, n["g"].cy), n["h"].anchor("top")])
    edge_label(d, (430, 1050), "Litho")
    line(d, [n["g"].anchor("bottom"), (900, 1180), (780, 1180), n["i"].anchor("top")])
    edge_label(d, (790, 1150), "BARCO")
    line(d, [n["g"].anchor("right"), (1440, n["g"].cy), n["j"].anchor("top")])
    edge_label(d, (1360, 1050), "其他")
    line(d, [n["i"].anchor("bottom"), n["i1"].anchor("top")])
    edge_label(d, (800, 1400), "是")
    line(d, [n["i"].anchor("left"), (460, n["i"].cy), (460, 1470), (250, 1470), n["i2"].anchor("top")])
    edge_label(d, (465, 1320), "否")
    line(d, [n["j"].anchor("bottom"), (1440, 1480), (1320, 1480), n["j1"].anchor("top")])
    edge_label(d, (1460, 1400), "是")
    line(d, [n["j"].anchor("right"), n["j2"].anchor("top")])
    edge_label(d, (1710, 1320), "否")
    save(img, "03-wait-pilot-control.png")


def chart_ama():
    img, d = page()
    n = {
        "a": Node(520, 35, 760, 95, "AMA 读取 Central_GetLithoR2RAutoPirunInfo", "terminator", SMALL),
        "b": Node(520, 180, 760, 140, "IsNeedSplit=T？", "decision"),
        "x1": Node(70, 195, 360, 110, "整批 Lot 传给 R2R", "terminator", SMALL),
        "c": Node(430, 370, 940, 285,
                  "物理分批前六项复核\n1. Lot 属于当前工厂（FAB6／FAB8）\n2. extrastatus='WaitForJobPrep'\n3. runcardid 为空\n4. Capability 为 LithoCapability／L-BARCO-L／L-BARCO-S\n5. CarrierKind='FOUP'\n6. Report 选中 Wafer 仍属于该 Lot",
                  text_font=LIST_FONT, align="left"),
        "d": Node(520, 705, 760, 140, "六项复核全部通过？", "decision"),
        "x2": Node(50, 710, 390, 130, "停止处理并记录原因\n等待下一轮重新计算", "terminator", SMALL),
        "e": Node(520, 900, 760, 105, "获取并预占空 FOUP"),
        "f": Node(520, 1055, 760, 140, "是否成功取得空 FOUP？", "decision"),
        "x3": Node(50, 1070, 390, 110, "整批 Lot 传给 R2R", "terminator", SMALL),
        "g": Node(520, 1250, 760, 105, "调用 MES 物理分批接口"),
        "h": Node(520, 1405, 760, 140, "接口调用成功？", "decision"),
        "x4": Node(70, 1620, 440, 125, "释放预占 FOUP\n整批 Lot 传给 R2R", "terminator", SMALL),
        "x5": Node(1120, 1610, 610, 145,
                   "生成子批并设置为 Pilot\n按现有顺序传给 R2R、执行 Transfer FOUP",
                   "terminator", SMALL),
    }
    for node in n.values():
        draw_node(d, node)

    line(d, [n["a"].anchor("bottom"), n["b"].anchor("top")])
    line(d, [n["b"].anchor("left"), n["x1"].anchor("right")])
    edge_label(d, (445, 225), "否")
    line(d, [n["b"].anchor("bottom"), n["c"].anchor("top")])
    edge_label(d, (920, 330), "是")
    line(d, [n["c"].anchor("bottom"), n["d"].anchor("top")])
    line(d, [n["d"].anchor("left"), n["x2"].anchor("right")])
    edge_label(d, (450, 750), "否")
    line(d, [n["d"].anchor("bottom"), n["e"].anchor("top")])
    edge_label(d, (920, 855), "是")
    line(d, [n["e"].anchor("bottom"), n["f"].anchor("top")])
    line(d, [n["f"].anchor("left"), n["x3"].anchor("right")])
    edge_label(d, (450, 1095), "否")
    line(d, [n["f"].anchor("bottom"), n["g"].anchor("top")])
    edge_label(d, (920, 1205), "是")
    line(d, [n["g"].anchor("bottom"), n["h"].anchor("top")])
    line(d, [n["h"].anchor("left"), (290, n["h"].cy), n["x4"].anchor("top")])
    edge_label(d, (450, 1450), "否")
    line(d, [n["h"].anchor("right"), (1425, n["h"].cy), n["x5"].anchor("top")])
    edge_label(d, (1295, 1450), "是")
    save(img, "04-ama-split.png")


def make_flowcharts():
    chart_rtd()
    chart_split()
    chart_wait()
    chart_ama()


if __name__ == "__main__":
    make_flowcharts()
