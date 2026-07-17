"""
Build print-ready PDFs from every worksheets/*.md file in this repo.

Pipeline:
  worksheets/<name>.md
    -> worksheets/_html/<name>.html   (brand-styled, A4)
    -> worksheets/<name>.pdf          (Edge headless --print-to-pdf)

Run: python scripts/build-worksheets.py
"""
from pathlib import Path
import subprocess
import sys
import shutil
import re

import markdown

ROOT = Path(__file__).resolve().parent.parent


def find_edge() -> str:
    """Locate Microsoft Edge portably; raise with a hint if missing."""
    for name in ("msedge", "microsoft-edge", "msedge.exe"):
        found = shutil.which(name)
        if found:
            return found
    for candidate in (
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ):
        if Path(candidate).exists():
            return candidate
    raise RuntimeError(
        "Microsoft Edge not found. Install Edge, or add msedge to PATH. "
        "(PDF rendering uses Edge's headless --print-to-pdf.)"
    )

CSS = """
@page { size: A4; margin: 18mm 16mm 22mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-family: "Inter", "Segoe UI", system-ui, sans-serif; color: #1a1a2e; }
body { font-size: 15px; line-height: 1.55; }

.cover { border-bottom: 3px solid #ff7849; padding-bottom: 14px; margin-bottom: 20px; }
.brand { font-size: 14px; font-weight: 800; color: #ff7849; letter-spacing: .06em; }
h1 { font-size: 28px; color: #6b4ee6; margin: 8px 0 6px; line-height: 1.25; }
h2 { font-size: 19px; color: #6b4ee6; margin: 22px 0 12px; padding-top: 10px; border-top: 1px solid #eee; page-break-before: always; }
section.first h2, h2:first-of-type { border-top: none; padding-top: 0; page-break-before: avoid; }
h3, h4 { font-size: 15px; margin: 14px 0 8px; color: #1a1a2e; }
p { margin: 8px 0; }
strong { color: #1a1a2e; }
em { color: #555; }

ul, ol { margin: 8px 0 8px 24px; }
li { margin: 3px 0; }

/* Grids (e.g. pixel-art coordinate grids) render as light graph paper. */
table { border-collapse: collapse; margin: 12px 0; }
th, td { border: 1px solid #ddd; padding: 4px 9px; text-align: center; font-size: 14px; }
th { background: #faf7ff; color: #6b4ee6; font-weight: 700; }

pre {
  font-family: "JetBrains Mono", "Consolas", monospace;
  font-size: 13.5px;
  background: #1e1e2e;
  color: #b9f6ca;
  padding: 12px 16px;
  border-radius: 6px;
  margin: 10px 0;
  white-space: pre-wrap;
  word-break: break-word;
  page-break-inside: avoid;
  line-height: 1.5;
}
pre code { background: transparent; padding: 0; color: inherit; }
code {
  font-family: "JetBrains Mono", "Consolas", monospace;
  font-size: 14px;
  background: #fff1e8;
  color: #ff7849;
  padding: 1px 6px;
  border-radius: 4px;
}
blockquote {
  margin: 10px 0;
  padding: 10px 16px;
  background: #fff6ef;
  border-left: 3px solid #ff7849;
  border-radius: 0 6px 6px 0;
  color: #6a3a1c;
}

.write-space {
  background-image: repeating-linear-gradient(
    to bottom,
    #ffffff 0,
    #ffffff 27px,
    #d4d4d4 27px,
    #d4d4d4 28px
  );
  background-color: #ffffff;
  border: 1px solid #e2e2e2;
  border-radius: 6px;
  min-height: 114px;
  margin: 10px 0 20px;
  page-break-inside: avoid;
}
.write-space.short { min-height: 86px; }
.write-space.tall { min-height: 170px; }
/* Drawing box: same frame, no ruled lines — for "draw the shape" prompts. */
.write-space.blank { background-image: none; }

/* Keep a question (and any hint/code above it) glued to its answer box so a
   page break never lands between the prompt and the lines you write on. */
.qa { page-break-inside: avoid; break-inside: avoid; }
.qa > :last-child { margin-bottom: 20px; }

hr { border: none; border-top: 1px dashed #d0d0d0; margin: 20px 0; }

.meta { color: #666; font-size: 13px; margin: 0 0 14px; }
.answer-lines {
  font-family: "JetBrains Mono", "Consolas", monospace;
  font-size: 14px;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 14px 16px;
  background: #fafafa;
  white-space: pre;
  line-height: 2.2;
}

footer {
  position: fixed;
  bottom: 10mm; left: 16mm; right: 16mm;
  text-align: center;
  font-size: 10px;
  color: #aaa;
}
footer b { color: #ff7849; }
"""

# Brand header injected at the top of every worksheet so the cover area
# matches parent-vocab and slides.
HEADER_HTML = """<div class="cover"><div class="brand">📚 ENGLISH CODING · 영어코딩</div></div>"""

FOOTER_HTML = """<footer>영어코딩 · <b>english-coding.co.uk</b></footer>"""


def md_to_html(md_text: str) -> str:
    """Convert markdown to HTML body. Preserves raw <details> blocks."""
    return markdown.markdown(
        md_text,
        extensions=["extra", "fenced_code", "sane_lists"],
    )


def wrap_html(title: str, body_html: str) -> str:
    # Make the plain ``` 1.\n 2.\n``` block render as fixed-width answer lines.
    body_html = re.sub(
        r'<pre><code>([\s\S]*?\n\d+\.[\s\S]*?)</code></pre>',
        r'<div class="answer-lines">\1</div>',
        body_html,
    )
    # Glue each question to its answer box: wrap the single immediately-
    # preceding block (the question paragraph, a sentence-starter blockquote,
    # or a sub-heading) together with the write-space in a .qa block so a page
    # break can never split a prompt from its lines. The tempered `(?!</tag>)`
    # dot keeps each anchor to ONE block so a match can't span many paragraphs.
    anchor = (
        r'<p>(?:(?!</p>)[\s\S])*?</p>\s*'
        r'|<blockquote>(?:(?!</blockquote>)[\s\S])*?</blockquote>\s*'
        r'|<h[34]>(?:(?!</h[34]>)[\s\S])*?</h[34]>\s*'
    )
    body_html = re.sub(
        r'(' + anchor + r')(<div class="write-space[^"]*"[^>]*>\s*</div>)',
        r'<div class="qa">\1\2</div>',
        body_html,
    )
    # An <hr> right before an <h2> is redundant — every <h2> already starts a
    # fresh page — and a lone rule can orphan onto a blank page. Drop it.
    body_html = re.sub(r'<hr\s*/?>\s*(?=<h2)', '', body_html)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{HEADER_HTML}
{body_html}
</body>
</html>
"""


def title_from_md(md_text: str, fallback: str) -> str:
    m = re.search(r'^#\s+(.+)$', md_text, re.M)
    return m.group(1).strip() if m else fallback


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    edge = find_edge()
    url = html_path.resolve().as_uri()
    cmd = [
        edge,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path.resolve()}",
        "--no-pdf-header-footer",
        url,
    ]
    subprocess.run(cmd, check=True, capture_output=True)


# --- Word (.doc) output ------------------------------------------------------
# Word opens HTML saved with a .doc extension natively, so the editable Word
# companion reuses the exact same Markdown -> HTML conversion as the PDF and just
# wraps it in an Office-flavoured shell. No pandoc/LibreOffice needed. This is the
# fill-in-on-a-computer version of the print PDF; ruled write-on boxes become
# blank type-on lines a student can click into.
WORD_CSS = """
@page WordSection1 { size: 595.3pt 841.9pt; margin: 1.6cm 1.6cm 2cm; }
div.WordSection1 { page: WordSection1; }
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 11.5pt; color: #1a1a2e; line-height: 1.5; }
h1 { font-size: 21pt; color: #6b4ee6; margin: 4px 0 6px; }
h2 { font-size: 15pt; color: #6b4ee6; border-top: 1px solid #dddddd; padding-top: 8px; margin: 18px 0 10px; }
h3, h4 { font-size: 11.5pt; margin: 12px 0 6px; }
p { margin: 7px 0; }
.brand { font-size: 10.5pt; font-weight: bold; color: #ff7849; letter-spacing: .06em;
         border-bottom: 2px solid #ff7849; padding-bottom: 6px; margin-bottom: 14px; }
table { border-collapse: collapse; margin: 10px 0; }
th, td { border: 1px solid #c8c8c8; padding: 4px 9px; text-align: center; }
th { background: #f3eefc; color: #6b4ee6; font-weight: bold; }
pre { font-family: Consolas, "Courier New", monospace; font-size: 10.5pt; background: #f4f4f5;
      border: 1px solid #dddddd; padding: 8px 10px; white-space: pre-wrap; }
pre code { background: transparent; color: #1a1a2e; }
code { font-family: Consolas, "Courier New", monospace; background: #fff1e8; color: #d6531f; padding: 0 3px; }
blockquote { border-left: 3px solid #ff7849; background: #fff6ef; padding: 8px 12px;
             color: #6a3a1c; margin: 9px 0; }
ul, ol { margin: 7px 0 7px 26px; }
p.ruled { border-bottom: 1px solid #bdbdbd; margin: 0 0 13px 0; height: 13pt; }
.footer { color: #999999; font-size: 8.5pt; text-align: center; margin-top: 18px;
          border-top: 1px solid #eeeeee; padding-top: 6px; }
.footer b { color: #ff7849; }
"""


def _write_space_to_lines(html: str) -> str:
    """Turn ruled CSS write-space boxes into blank type-on lines for Word.

    A `blank` box is a drawing frame, not writing lines — Word gets an empty
    bordered cell (a table, which Word sizes reliably) instead of ruled lines.
    """
    def repl(m: "re.Match") -> str:
        cls = m.group(1)
        if "blank" in cls:
            h = 90 if "short" in cls else (220 if "tall" in cls else 150)
            return (
                "<table style='border-collapse:collapse; width:100%; "
                "margin:10px 0 20px;'><tr><td style='border:1px solid #cccccc; "
                f"height:{h}px;'>&nbsp;</td></tr></table>"
            )
        n = 3 if "short" in cls else (10 if "tall" in cls else 5)
        return '<p class="ruled">&nbsp;</p>' * n
    return re.sub(r'<div class="write-space([^"]*)"[^>]*>\s*</div>', repl, html)


def wrap_doc(title: str, body_html: str) -> str:
    body_html = _write_space_to_lines(body_html)
    return (
        "<html xmlns:o='urn:schemas-microsoft-com:office:office' "
        "xmlns:w='urn:schemas-microsoft-com:office:word' "
        "xmlns='http://www.w3.org/TR/REC-html40'>\n"
        "<head><meta charset='utf-8'>\n"
        f"<title>{title}</title>\n"
        "<!--[if gte mso 9]><xml><w:WordDocument><w:View>Print</w:View>"
        "<w:Zoom>100</w:Zoom><w:DoNotOptimizeForBrowser/></w:WordDocument></xml><![endif]-->\n"
        f"<style>{WORD_CSS}</style></head>\n"
        "<body><div class=WordSection1>\n"
        '<div class="brand">📚 ENGLISH CODING · 영어코딩</div>\n'
        f"{body_html}\n"
        '<div class="footer">영어코딩 · <b>english-coding.co.uk</b></div>\n'
        "</div></body></html>\n"
    )


def render_doc(title: str, body_html: str, doc_path: Path) -> None:
    doc_path.write_text(wrap_doc(title, body_html), encoding="utf-8")


def main() -> int:
    md_files = sorted(ROOT.glob("*/worksheets/*.md"))
    if not md_files:
        print("No worksheets/*.md files found.", file=sys.stderr)
        return 1
    for md in md_files:
        course = md.parent.parent.name
        html_dir = md.parent / "_html"
        html_dir.mkdir(exist_ok=True)
        html_path = html_dir / (md.stem + ".html")
        pdf_path = md.parent / (md.stem + ".pdf")

        md_text = md.read_text(encoding="utf-8")
        title = title_from_md(md_text, md.stem)
        body_html = md_to_html(md_text)
        html_path.write_text(wrap_html(title, body_html), encoding="utf-8")
        render_pdf(html_path, pdf_path)
        doc_path = md.parent / (md.stem + ".doc")
        render_doc(title, body_html, doc_path)
        print(f"[{course}] {md.name} -> {pdf_path.name} + {doc_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
