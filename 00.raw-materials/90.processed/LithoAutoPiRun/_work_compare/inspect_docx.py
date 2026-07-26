from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "a": A, "r": R}


def paragraph_text(paragraph: etree._Element) -> str:
    parts: list[str] = []
    for node in paragraph.xpath(".//w:t | .//w:tab | .//w:br", namespaces=NS):
        if node.tag == f"{{{W}}}t":
            parts.append(node.text or "")
        elif node.tag == f"{{{W}}}tab":
            parts.append("\t")
        else:
            parts.append("\n")
    return "".join(parts)


def inspect_docx(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        document_xml = archive.read("word/document.xml")
        rels_xml = archive.read("word/_rels/document.xml.rels")
        rel_root = etree.fromstring(rels_xml)
        rel_map = {
            rel.get("Id"): rel.get("Target")
            for rel in rel_root
            if rel.get("Id") and rel.get("Target")
        }

    root = etree.fromstring(document_xml)
    paragraphs = []
    for index, paragraph in enumerate(root.xpath(".//w:body//w:p", namespaces=NS)):
        text = paragraph_text(paragraph)
        image_ids = paragraph.xpath(".//a:blip/@r:embed", namespaces=NS)
        image_targets = [rel_map.get(image_id, image_id) for image_id in image_ids]
        style = paragraph.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
        paragraphs.append(
            {
                "index": index,
                "text": text,
                "style": style[0] if style else "",
                "images": image_targets,
            }
        )

    return {"path": str(path), "paragraphs": paragraphs}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    args = parser.parse_args()

    result = inspect_docx(args.docx)
    if args.json_path:
        args.json_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    for paragraph in result["paragraphs"]:
        suffix = f" [IMAGE: {', '.join(paragraph['images'])}]" if paragraph["images"] else ""
        print(f"{paragraph['index']:04d}\t{paragraph['style']}\t{paragraph['text']}{suffix}")


if __name__ == "__main__":
    main()
