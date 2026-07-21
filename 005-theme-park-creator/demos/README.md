# 🎢 Helper Codes — teaching demo + worksheet (Theme Park Creator)

Teaching materials for the **helper functions / "helper codes"** concept, themed to a
roller-coaster support build. Pairs with Week 4 (Petting Zoo — Helper Functions) — this
uses a *different* build (coaster pillars) so the concept lands twice, freshly.

## Files

| File | What it is |
|---|---|
| `helper-codes.html` | 8-step, video-ready walkthrough. Left = MakeCode Python (syntax-highlighted, new line highlighted per step); right = the build growing as the helper is called (pillars rise, track climbs). Nav: ← → arrow keys, click dots, Back/Next. Open full-screen, screen-record for the lesson video. |
| `helper-codes-worksheet-DRAFT.md` | Accompanying worksheet (base tier): What-a-helper-is → Predict → Spot-the-Bug → Build → **Extension (open a 2nd ride + a `topper` helper)** → Show-Your-Work narration video. |

## The arc the demo teaches

1 pillar (one `fill`) → the long copy-paste way → **write the job once: `def pillar(x)`** →
**call it** → **reuse it** (different x) → **loop it** → **add a `height` parameter** so the
track climbs → payoff: *teach one job once, reuse it any number of times, any size.*

## To go fully live (pending assets from Kasim)

- [ ] **YouTube link** — record the video from `helper-codes.html`, then paste the URL into the
      worksheet's `[[VIDEO LINK — pending]]` placeholder.
- [ ] **World file** — drop `weekN.mcworld` into `../worlds/`; confirm the world name in worksheet §4.
- [ ] Decide the slot: **Week 5** of Theme Park Creator (recommended — weeks 1–4 are done) or a
      Week 4 companion. Rename the worksheet accordingly.
- [ ] Split into `-beginner` / `-intermediate` / `-advanced` tiers if the week needs them
      (beginner = zero-writing per the worksheet spec).
- [ ] Build PDFs/DOCs: `python scripts/build-worksheets.py`.
- [ ] Add the download row to `005-theme-park-creator/README.md` and the Notion syllabus page.
