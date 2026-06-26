# Worksheet → PDF generation guide (for future AI / contributors)

This is the single source of truth for **how worksheet PDFs are made** in this repo.
Read it before authoring a worksheet or touching `build-worksheets.py`. If you change
the rules, update this file too.

---

## 1. The pipeline

```
<course>/worksheets/<name>.md          ← you write this (Markdown)
        │  python scripts/build-worksheets.py
        ▼
<course>/worksheets/_html/<name>.html  ← generated, brand-styled, A4 (do not hand-edit)
        │  Microsoft Edge --headless --print-to-pdf
        ▼
<course>/worksheets/<name>.pdf         ← the file we ship to parents/students
        +
<course>/worksheets/<name>.doc         ← Word-editable companion (same build, no extra tools)
```

- **Source of truth is the `.md` file.** Never edit the `_html/*.html`, `*.pdf`, or `*.doc`
  by hand — they are overwritten on every build.
- **The `.doc`** is an Office-flavoured HTML file Word opens natively (no pandoc/LibreOffice
  needed). It reuses the exact same Markdown→HTML as the PDF; ruled write-on boxes become
  blank type-on lines so students can fill it in on a computer. Coordinate grids (Markdown
  tables) render as bordered graph paper in both the PDF and the `.doc`.
- One command rebuilds **every** `*/worksheets/*.md` in the repo:
  ```bash
  pip install -r requirements.txt     # first time only (markdown package)
  python scripts/build-worksheets.py
  ```
- Requires **Microsoft Edge** installed (the PDF renderer). The script finds `msedge`
  on PATH, else the default `Program Files` install path.
- Output is **deterministic**: rebuilding unchanged `.md` produces byte-identical PDFs.
  So if `git status` shows no PDF change after a build, nothing actually changed.

---

## 2. What makes a PDF "clean" (the rules already enforced)

You do **not** need to add page-break CSS yourself. `build-worksheets.py` guarantees all
of this automatically — your job is only to follow the Markdown conventions in §3 so the
machinery has something to grab onto.

| Guarantee | How it's enforced |
|---|---|
| **Every `##` section heading starts on a new page** | CSS `h2 { page-break-before: always }` (first H2 is exempt so page 1 isn't blank) |
| **A question never splits from its answer box** | Build wraps each prompt + its `write-space` in a `.qa` div with `page-break-inside: avoid` |
| **Code blocks never split across pages** | CSS `pre { page-break-inside: avoid }` |
| **No orphan `<hr>` on a blank page before a heading** | Build strips any `---` immediately before an `##` (the heading already starts a page) |
| **Numbered "answer lines" render as fixed ruled lines** | A bare ```` ``` ```` block of `1.` `2.` … is converted to a `.answer-lines` box |

Consequence to expect: because each section gets its own page, short sections leave
white space at the bottom of a page. **That is intended** ("each heading on a new page"),
not a bug.

---

## 3. Markdown conventions an author MUST follow

Start from `scripts/templates/week-template.md` (general) or `vocab-template.md` (vocab).
The build only behaves well if you stick to these shapes:

- **Title** — one `#` line at the top: `# 🔴 RS002 Week 1 — English Worksheet`.
  The build reads it as the `<title>`.
- **Sections** — each is an `## N · Title 🙂` heading. **Each one gets its own page.**
  Keep sections coherent; don't split one task across two headings expecting them together.
- **Write-on space** — insert a blank answer area with:
  ```html
  <div class="write-space"></div>            <!-- standard ~4 lines -->
  <div class="write-space short"></div>      <!-- smaller -->
  <div class="write-space tall" style="min-height: 340px"></div>   <!-- big, for paragraphs -->
  ```
  Put the **question/prompt directly above** the `write-space` (a `**bold paragraph**`, a
  `>` blockquote of sentence starters, or an `###`/`####` sub-heading). The build glues that
  one preceding block to the box. Don't put two paragraphs of gap between prompt and box, or
  only the nearest one is glued.
- **Code** — fenced blocks ```` ```python ````. They render dark, monospace, and never split.
- **Sentence starters / callouts** — use `>` blockquotes (rendered as a tangerine card).
- **Ruled answer lines** (e.g. for "write 5 sentences") — a fenced block of `1.` `2.` …
  becomes a fixed ruled box. Otherwise prefer `write-space`.
- **Section dividers** — `---` between sections is fine; the build removes the redundant one
  that lands right before a heading.

### Content rules (house style — see also the team's memory/CLAUDE notes)
- Student-facing worksheet copy stays **English** (this is an ESL coding school; the worksheet
  itself is the English-practice surface). Parent-facing READMEs stay Korean.
- **Under-prescribe**: no "at least N", no "Optional:" buckets, no redundant rules.
- Submission is **online via KakaoTalk only** — never "bring to class". Photo **or** video.
- No `input()` dependency in expected output examples (the grader/runtime has no stdin).

---

## 4. Adding a new worksheet

1. Copy a template: `cp scripts/templates/week-template.md <course>/worksheets/week-NN.md`.
2. Fill it in following §3. Delete the `<!-- authoring notes -->` block before shipping.
3. Build: `python scripts/build-worksheets.py` (or scope to one course — see §5).
4. Eyeball the PDF (see §6). Commit the `.md`, the generated `_html/*.html`, the `.pdf`, and the `.doc`.
5. Add the row to the course `README.md` table so parents can download it.

---

## 5. Rebuilding ONE course only

`build-worksheets.py` builds the whole repo. To regenerate a single course without touching
others (useful when other courses have uncommitted edits), run the functions against a scoped
glob:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("bw", "scripts/build-worksheets.py")
bw = importlib.util.module_from_spec(spec); spec.loader.exec_module(bw)
for md in sorted((bw.ROOT / "RS002-pokedex" / "worksheets").glob("*.md")):
    html_dir = md.parent / "_html"; html_dir.mkdir(exist_ok=True)
    html_path = html_dir / (md.stem + ".html"); pdf_path = md.parent / (md.stem + ".pdf")
    t = md.read_text(encoding="utf-8")
    html_path.write_text(bw.wrap_html(bw.title_from_md(t, md.stem), bw.md_to_html(t)), "utf-8")
    bw.render_pdf(html_path, pdf_path)
```

---

## 6. Verifying a PDF looks right

Use **PyMuPDF** (`fitz`), not poppler. Quick check that headings land on fresh pages and
nothing is interrupted:

```python
import fitz
d = fitz.open("RS002-pokedex/worksheets/week-01.pdf")
for i, p in enumerate(d):
    lines = [l for l in p.get_text().splitlines() if l.strip()]
    print(f"p{i+1}: {lines[0][:60] if lines else '(empty)'}")
    d[i].get_pixmap(dpi=90).save(f"/tmp/p{i+1}.png")   # eyeball the image
```
Each `## N · …` section should appear as the first line of a page, and no `write-space`
box should sit on a different page from its question.
(On Windows set `PYTHONIOENCODING=utf-8` so the emoji/Korean print doesn't crash.)

---

## 7. Gotchas

- **PDF "changed" but byte-size identical** → it didn't really change; the renderer is
  deterministic. Safe to discard or commit, no visible difference.
- **Edge not found** → install Microsoft Edge or put `msedge` on PATH. There is no fallback
  renderer.
- **Worksheet world scripts** (`_gen_*.py`, `_builder_*.py`) under each course's `worlds/` are
  teacher-only and gitignored — unrelated to this PDF pipeline.
- **Don't `git add -A`** in this repo — other courses often have in-progress uncommitted edits.
  Stage only the worksheet/doc files you actually changed.
