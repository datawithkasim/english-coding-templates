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
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

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
    if not Path(EDGE).exists():
        raise RuntimeError(f"Edge not found at {EDGE}")
    url = html_path.resolve().as_uri()
    cmd = [
        EDGE,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path.resolve()}",
        "--no-pdf-header-footer",
        url,
    ]
    subprocess.run(cmd, check=True, capture_output=True)


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
        html_path.write_text(wrap_html(title, md_to_html(md_text)), encoding="utf-8")
        render_pdf(html_path, pdf_path)
        print(f"[{course}] {md.name} -> {pdf_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
