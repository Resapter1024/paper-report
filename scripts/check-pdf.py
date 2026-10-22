#!/usr/bin/env python3
"""Audit fonts/text and render every PDF page with Poppler and MuPDF.

Requires pypdf, PyMuPDF, and Poppler's pdffonts, pdftotext, and pdftoppm on PATH.
--embed-cjk-maps additionally requires kpsewhich from a TeX distribution and
updates a generated PDF with standard Adobe CMaps. Visual review is still required.
"""

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

import fitz
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject


def run(*command):
    return subprocess.run(
        command, check=True, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    ).stdout


def resource_fonts(resources, seen):
    resources = resources.get_object()
    if id(resources) in seen:
        return
    seen.add(id(resources))
    fonts = resources["/Font"] if "/Font" in resources else {}
    for font in fonts.values():
        yield font.get_object()
    forms = resources["/XObject"] if "/XObject" in resources else {}
    for form in forms.values():
        form = form.get_object()
        if "/Resources" in form:
            yield from resource_fonts(form["/Resources"], seen)


def embed_cjk_maps(pdf):
    reader = PdfReader(pdf)
    if reader.is_encrypted:
        raise ValueError("Use an unencrypted generated PDF for CMap embedding.")
    count = 0
    seen = set()
    for page in reader.pages:
        for font in resource_fonts(page["/Resources"], seen):
            if "/ToUnicode" in font or font.get("/Encoding") not in ("/Identity-H", "/Identity-V"):
                continue
            descendants = font.get("/DescendantFonts", [])
            if not descendants:
                continue
            descendant = descendants[0].get_object()
            if "/CIDSystemInfo" not in descendant:
                continue
            info = descendant["/CIDSystemInfo"]
            ordering = str(info.get("/Ordering", ""))
            if str(info.get("/Registry")) != "Adobe" or ordering not in ("GB1", "CNS1", "Japan1", "Korea1"):
                continue
            cmap_name = f"Adobe-{ordering}-UCS2"
            cmap_path = run("kpsewhich", "--format=cmap", cmap_name).strip()
            if not cmap_path or not Path(cmap_path).is_file():
                raise ValueError(f"Missing TeX CMap resource: {cmap_name}")
            stream = DecodedStreamObject()
            stream.set_data(Path(cmap_path).read_bytes())
            font[NameObject("/ToUnicode")] = stream.flate_encode()
            count += 1
    if count:
        writer = PdfWriter()
        writer.clone_document_from_reader(reader)
        # Replace only after a complete write; retain pages, links, and bookmarks.
        with tempfile.TemporaryDirectory(dir=pdf.parent) as temporary:
            replacement = Path(temporary) / "mapped.pdf"
            writer.write(replacement)
            os.replace(replacement, pdf)
    return count


def cjk_characters(text):
    return Counter(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323af]", text))


def check(pdf, output, embed=False):
    output.mkdir(parents=True, exist_ok=True)
    for engine in ("poppler", "mupdf"):
        (output / engine).mkdir(exist_ok=True)
    embedded_maps = embed_cjk_maps(pdf) if embed else 0
    fonts = run("pdffonts", str(pdf))
    (output / "fonts.txt").write_text(fonts, encoding="utf-8")
    issues = []
    fonts_without_tounicode = []
    font_rows = 0
    for line in fonts.splitlines()[2:]:
        match = re.search(r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", line)
        if not match:
            if line.strip():
                raise ValueError(f"Cannot interpret pdffonts output: {line}")
            continue
        font_rows += 1
        name = line.split()[0]
        if match[1] != "yes":
            issues.append(f"Font is not embedded: {name}")
        if match[3] != "yes":
            fonts_without_tounicode.append(name)
            # XeLaTeX uses composite fonts for Chinese text. Extensible math
            # pieces can be embedded without a textual Unicode counterpart.
            if re.search(r"\sCID\s", line[:match.start()]):
                issues.append(f"Composite text font has no explicit ToUnicode map: {name}")
    if not font_rows:
        issues.append("No text fonts found; an image-only PDF cannot prove searchable Chinese text.")
    poppler_text = run("pdftotext", "-enc", "UTF-8", "-layout", str(pdf), "-")
    (output / "poppler-text.txt").write_text(poppler_text, encoding="utf-8")
    text_pages = poppler_text.split("\f")
    pages = []
    with fitz.open(pdf) as document:
        mupdf_text = []
        for index, page in enumerate(document):
            number = index + 1
            prefix = output / "poppler" / f"page-{number:03}"
            run("pdftoppm", "-f", str(number), "-l", str(number), "-singlefile",
                "-r", "144", "-png", str(pdf), str(prefix))
            image = output / "mupdf" / f"page-{number:03}.png"
            page.get_pixmap(dpi=144, alpha=False).save(image)
            text = page.get_text()
            mupdf_text.append(text)
            other = text_pages[index] if index < len(text_pages) else ""
            if "\ufffd" in text or "\ufffd" in other:
                issues.append(f"Page {number}: replacement characters in extracted text")
            if cjk_characters(text) != cjk_characters(other):
                issues.append(f"Page {number}: Chinese extraction differs between engines")
            pages.append({"page": number, "poppler": str(prefix.with_suffix(".png")),
                          "mupdf": str(image), "chinese_characters": sum(cjk_characters(text).values())})
        (output / "mupdf-text.txt").write_text("\f".join(mupdf_text), encoding="utf-8")
    result = {"pdf": str(pdf), "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
              "embedded_cjk_maps": embedded_maps, "fonts_checked": font_rows,
              "fonts_without_tounicode": fonts_without_tounicode,
              "pages": pages, "issues": issues, "automated_checks_passed": not issues,
              "visual_review_required": True}
    (output / "audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--embed-cjk-maps", action="store_true",
                        help="Embed missing standard CJK maps in this generated PDF before checking.")
    args = parser.parse_args()
    try:
        result = check(args.pdf.resolve(strict=True), args.output_dir.resolve(), args.embed_cjk_maps)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", "") or str(error)
        parser.exit(1, f"PDF check failed: {detail}\n")
    print(json.dumps({"pages_rendered_per_engine": len(result["pages"]),
                      "embedded_cjk_maps": result["embedded_cjk_maps"], "issues": result["issues"],
                      "visual_review_required": True}, ensure_ascii=False))
    return 0 if result["automated_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
