"""End-to-end CJK mapping, independent rendering, and link preservation check.

Run: python -m unittest discover -s tests -v
Requires the same tools as scripts/check-pdf.py plus XeLaTeX.
"""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import fitz
from pypdf import PdfReader, PdfWriter


CHECKER = Path(__file__).resolve().parents[1] / "scripts" / "check-pdf.py"
TOOLS = ("xelatex", "kpsewhich", "pdffonts", "pdftotext", "pdftoppm")


@unittest.skipUnless(all(shutil.which(tool) for tool in TOOLS), "XeLaTeX and Poppler are required")
class PdfCompatibilityTest(unittest.TestCase):
    def test_cjk_mapping_rendering_and_links(self):
        with tempfile.TemporaryDirectory(prefix="paper-report-test-") as temporary:
            root = Path(temporary) / "中文 空格路径"
            root.mkdir()
            tex = root / "sample.tex"
            tex.write_text(r"""\documentclass[UTF8,fontset=fandol]{ctexart}
\usepackage{amsmath,hyperref}
\begin{document}
\pdfbookmark[0]{中文目录}{contents}
重复测量的中文说明。\hyperlink{next}{跳转到结果}
\[\underbrace{\cdots}_{\text{数学装饰字形}}\]
\newpage
\hypertarget{next}{}\textbf{结果解释}：误差方差降低。
\end{document}
""", encoding="utf-8")
            for _ in range(2):  # Hyperref reads its outline file on the next pass.
                build = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                                       cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace")
                self.assertEqual(build.returncode, 0, build.stdout[-3000:] + build.stderr)
            pdf = tex.with_suffix(".pdf")

            def check(path, name, repair=False):
                output = root / name
                command = [sys.executable, str(CHECKER), str(path), "--output-dir", str(output)]
                if repair:
                    command.append("--embed-cjk-maps")
                process = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
                audit = json.loads((output / "audit.json").read_text(encoding="utf-8"))
                return process, audit, output

            process, audit, output = check(pdf, "initial", repair=True)
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
            self.assertEqual(len(audit["pages"]), 2)
            for engine in ("poppler", "mupdf"):
                self.assertEqual(len(list((output / engine).glob("page-*.png"))), 2)
                text = (output / f"{engine}-text.txt").read_text(encoding="utf-8")
                self.assertIn("重复测量", text)
                self.assertIn("结果解释", text)
            with fitz.open(pdf) as document:
                self.assertEqual(document[0].get_links()[0]["page"], 1)
                self.assertEqual(document.get_toc()[0][1], "中文目录")

            reader = PdfReader(pdf)
            removed = 0
            for page in reader.pages:
                for reference in page["/Resources"]["/Font"].values():
                    font = reference.get_object()
                    if "Fandol" in str(font.get("/BaseFont")) and "/ToUnicode" in font:
                        del font["/ToUnicode"]
                        removed += 1
            self.assertGreater(removed, 0)
            damaged = root / "missing-map.pdf"
            writer = PdfWriter()
            writer.clone_document_from_reader(reader)
            writer.write(damaged)
            process, audit, _ = check(damaged, "detected")
            self.assertNotEqual(process.returncode, 0)
            self.assertTrue(any("ToUnicode" in issue for issue in audit["issues"]))
            process, audit, _ = check(damaged, "repaired", repair=True)
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
            self.assertGreater(audit["embedded_cjk_maps"], 0)
            self.assertTrue(audit["visual_review_required"])


if __name__ == "__main__":
    unittest.main()
