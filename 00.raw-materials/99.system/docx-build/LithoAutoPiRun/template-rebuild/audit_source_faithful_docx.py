from __future__ import annotations

import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}
W = f"{{{W_NS}}}"


def attr(node: etree._Element | None, name: str) -> str:
    return "" if node is None else node.get(f"{W}{name}", "")


def main() -> None:
    docx_path = Path(sys.argv[1])
    with zipfile.ZipFile(docx_path) as package:
        document = etree.fromstring(package.read("word/document.xml"))
        media = [name for name in package.namelist() if name.startswith("word/media/")]

    visible_runs = []
    table_runs = []
    bad_colors = []
    run_shading = []

    for run in document.xpath("//w:r", namespaces=NS):
        text = "".join(run.xpath(".//w:t/text()", namespaces=NS))
        if not text.strip():
            continue
        visible_runs.append(run)
        if run.xpath("ancestor::w:tbl", namespaces=NS):
            table_runs.append(run)

        color = run.find("./w:rPr/w:color", namespaces=NS)
        color_value = attr(color, "val").upper()
        if color_value not in {"", "000000", "AUTO"}:
            bad_colors.append({"text": text, "color": color_value})

        shading = run.find("./w:rPr/w:shd", namespaces=NS)
        if shading is not None:
            run_shading.append({"text": text, "fill": attr(shading, "fill")})

    font_sets = Counter()
    invalid_body_fonts = []
    for run in table_runs:
        text = "".join(run.xpath(".//w:t/text()", namespaces=NS))
        rfonts = run.find("./w:rPr/w:rFonts", namespaces=NS)
        size = run.find("./w:rPr/w:sz", namespaces=NS)
        signature = (
            attr(rfonts, "ascii"),
            attr(rfonts, "hAnsi"),
            attr(rfonts, "eastAsia"),
            attr(size, "val"),
        )
        font_sets[signature] += 1
        if signature != ("Times New Roman", "Times New Roman", "SimSun", "21"):
            invalid_body_fonts.append({"text": text, "font": signature})

    result = {
        "file": str(docx_path),
        "visible_text_runs": len(visible_runs),
        "body_table_text_runs": len(table_runs),
        "bad_visible_colors": bad_colors,
        "character_shading": run_shading,
        "body_font_sets": [
            {"ascii": key[0], "hAnsi": key[1], "eastAsia": key[2], "size_half_points": key[3], "runs": count}
            for key, count in font_sets.items()
        ],
        "invalid_body_font_runs": invalid_body_fonts,
        "embedded_media": media,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
