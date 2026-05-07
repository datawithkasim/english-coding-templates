# 📝 Content Production Checklist

Per-lesson task list. Check off slowly as content gets produced. Start at top, go down.

---

## 🛠️ One-time prep (do once before W1)

- [ ] Test `.mcworld` export from Minecraft Education (File → Export World)
- [ ] Test `.mkcd` export from MakeCode (Code Builder → ⋯ → Save / Download)
- [ ] Set up screen recording (OBS / Win+G / iPad Screen Record — pick one)
- [ ] Create YouTube playlist: `MS001 / MBS001 — Pyramid Problems`
- [ ] Create YouTube playlist: `MS002 / MBS002 — Maze Madness`
- [ ] Confirm git workflow: `cd english-coding-templates && git pull && (drop files) && git add . && git commit -m "..." && git push`

---

# 🔺 001 — Pyramid Problems

## Week 1 — Meeting the Agent / 에이전트와 첫 인사

- [ ] Build world: flat ground, agent at spawn, chest with stone/dirt/wood
- [ ] Export `.mcworld` → drop into `001-pyramid-problems/worlds/week-1.mcworld`
- [ ] Write/test Python code (5-block path)
- [ ] Save `.py` → `001-pyramid-problems/python/week-1.py`
- [ ] Build/test Block code (matching logic)
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-1.mkcd`
- [ ] `git add . && git commit -m "001 W1 files" && git push`
- [ ] Record demo video (~3 min): agent moves 5 blocks, places different block types
- [ ] Edit + upload to YouTube
- [ ] Add to "Pyramid Problems" playlist
- [ ] Paste video link into Notion W1 page → 🎬 데모 영상 slot

## Week 2 — Loops / 반복문

- [ ] Build world: open flat area, agent at corner
- [ ] Export `.mcworld` → `001-pyramid-problems/worlds/week-2.mcworld`
- [ ] Write/test Python code (10-block wall + L-shape)
- [ ] Save `.py` → `001-pyramid-problems/python/week-2.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-2.mkcd`
- [ ] git push
- [ ] Record video (~3 min): for-loop wall + U-shape
- [ ] Upload + add to playlist
- [ ] Link in Notion W2 page

## Week 3 — Variables / 변수

- [ ] Build world: open flat area (can reuse W2 world)
- [ ] Export `.mcworld` → `001-pyramid-problems/worlds/week-3.mcworld`
- [ ] Write/test Python code (`size` variable wall)
- [ ] Save `.py` → `001-pyramid-problems/python/week-3.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-3.mkcd`
- [ ] git push
- [ ] Record video (~3 min): swap `size = 5` → `12` → re-run
- [ ] Upload + add to playlist
- [ ] Link in Notion W3 page

## Week 4 — Nested Loops / 중첩 반복문

- [ ] Build world: bigger flat area (~10×10 minimum)
- [ ] Export `.mcworld` → `001-pyramid-problems/worlds/week-4.mcworld`
- [ ] Write/test Python code (5×5 floor)
- [ ] Save `.py` → `001-pyramid-problems/python/week-4.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-4.mkcd`
- [ ] git push
- [ ] Record video (~4 min): 5×5 floor → 7×7 by changing size
- [ ] Upload + add to playlist
- [ ] Link in Notion W4 page

## Week 5 — First Pyramid / 첫 피라미드

- [ ] Build world: large flat area ~12×12 with vertical clearance
- [ ] Export `.mcworld` → `001-pyramid-problems/worlds/week-5.mcworld`
- [ ] Write/test Python code (5-layer pyramid, size 9→7→5→3→1)
- [ ] Save `.py` → `001-pyramid-problems/python/week-5.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-5.mkcd`
- [ ] git push
- [ ] Record video (~4 min): 5-layer pyramid build, narrate `move("up")` placement
- [ ] Upload + add to playlist
- [ ] Link in Notion W5 page

## Week 6 — Inverted Pyramid / 거꾸로 피라미드

- [ ] World: reuse W5 world (`.mcworld` shared) → just copy to `worlds/week-6.mcworld`
- [ ] Write/test Python code (size 1→9 inverted)
- [ ] Save `.py` → `001-pyramid-problems/python/week-6.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-6.mkcd`
- [ ] git push
- [ ] Record video (~3 min): show inverted build, compare with W5
- [ ] Upload + add to playlist
- [ ] Link in Notion W6 page

## Week 7 — Variations / 피라미드 광기

- [ ] World: reuse W5 world (`.mcworld` shared) → copy to `worlds/week-7.mcworld`
- [ ] Write/test Python code (hollow pyramid edges)
- [ ] Save `.py` → `001-pyramid-problems/python/week-7.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-7.mkcd`
- [ ] git push
- [ ] Record video (~4 min): hollow + stepped variants, narrate `if` edge logic
- [ ] Upload + add to playlist
- [ ] Link in Notion W7 page

## Week 8 — **Final: Diamond** / 최종: 다이아몬드

- [ ] Build world: largest flat area, 15×15 base + ~17 blocks vertical clearance
- [ ] Export `.mcworld` → `001-pyramid-problems/worlds/week-8.mcworld`
- [ ] Write/test Python code (full diamond, `max_size = 9`)
- [ ] Save `.py` → `001-pyramid-problems/python/week-8.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `001-pyramid-problems/blocks/week-8.mkcd`
- [ ] git push
- [ ] Record video (~5 min): full diamond build, change `max_size` to 7 + re-run, present
- [ ] Upload + add to playlist
- [ ] Link in Notion W8 page

## 001 wrap-up

- [ ] Copy YouTube playlist URL → Notion `📦 주차별 숙제` parent page header (top of weekly hub)
- [ ] Verify all 8 download links work in Notion (click each from a fresh browser)
- [ ] Update repo `001-pyramid-problems/README.md` table — replace TBD with ✅ for each format

---

# 🌀 002 — Maze Madness

## Week 1 — While Loops / While 루프

- [ ] Build world: straight tunnel, wall at end, agent at start
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-1.mcworld`
- [ ] Write/test Python (`while not agent.detect("forward")`)
- [ ] Save `.py` → `002-maze-madness/python/week-1.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-1.mkcd`
- [ ] git push
- [ ] Record video (~3 min): agent walks until wall
- [ ] Upload + add to playlist
- [ ] Link in Notion W1 page

## Week 2 — Turning at Walls / 방향 전환

- [ ] Build world: L-shaped or U-shaped maze
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-2.mcworld`
- [ ] Write/test Python (if/else turn at wall)
- [ ] Save `.py` → `002-maze-madness/python/week-2.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-2.mkcd`
- [ ] git push
- [ ] Record video (~3 min): agent navigates corners
- [ ] Upload + add to playlist
- [ ] Link in Notion W2 page

## Week 3 — AND / OR / 조건

- [ ] Build world: maze with 2–3 forks
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-3.mcworld`
- [ ] Write/test Python (combined AND/OR conditions)
- [ ] Save `.py` → `002-maze-madness/python/week-3.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-3.mkcd`
- [ ] git push
- [ ] Record video (~4 min): fork navigation
- [ ] Upload + add to playlist
- [ ] Link in Notion W3 page

## Week 4 — Mini Cube Maze Practice / 미니 큐브 미로 연습

- [ ] **Migrate existing world**: `cube_maze_001.mcworld` already on legacy 002 PYTHON hub → re-upload to `002-maze-madness/worlds/week-4.mcworld`
- [ ] Write/test Python (priority navigation in 3D cube)
- [ ] Save `.py` → `002-maze-madness/python/week-4.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-4.mkcd`
- [ ] git push
- [ ] Watch existing video `youtu.be/4pOwe7mKoxA` → decide: keep OR re-record for new plan
- [ ] If keep: confirm link still in Notion W4 page (already there)
- [ ] If re-record: upload new + replace link in Notion W4 page

## Week 5 — Redstone Basics / 레드스톤 기초

- [ ] Build world: maze with **redstone-powered doors** blocking some passages (kept closed by default — no levers placed yet)
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-5.mcworld`
- [ ] Write/test Python (treat doors as walls, route around)
- [ ] Save `.py` → `002-maze-madness/python/week-5.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-5.mkcd`
- [ ] git push
- [ ] Record video (~5 min): redstone circuit demo first (lever→door wired), then maze traversal avoiding doors
- [ ] Upload + add to playlist
- [ ] Link in Notion W5 page

## Week 6 — Lever Interaction / 레버 조작

- [ ] Build world: lever + redstone-connected door + corridor beyond
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-6.mcworld`
- [ ] Write/test Python (`agent.interact()` flips lever, agent passes through)
- [ ] Save `.py` → `002-maze-madness/python/week-6.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-6.mkcd`
- [ ] git push
- [ ] Record video (~4 min): walk to lever → interact → door opens → walk through
- [ ] Upload + add to playlist
- [ ] Link in Notion W6 page

## Week 7 — Multi-Lever Combine / 다중 레버 종합

- [ ] Build world: 2–3 levers, sequence-dependent (wrong order = dead end)
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-7.mcworld`
- [ ] Write/test Python (function `move_until_wall()` + sequenced interacts)
- [ ] Save `.py` → `002-maze-madness/python/week-7.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-7.mkcd`
- [ ] git push
- [ ] Record video (~5 min): solve multi-lever maze using a function
- [ ] Upload + add to playlist
- [ ] Link in Notion W7 page

## Week 8 — **Final: 15×15×15 Redstone Cube Maze** / 최종

- [ ] Build world: full 15×15×15 cube · multi-level · ≥1 redstone door · ≥1 lever · clear start/finish
- [ ] Export `.mcworld` → `002-maze-madness/worlds/week-8.mcworld`
- [ ] Write/test Python (autonomous solver: priority + lever flipping)
- [ ] Save `.py` → `002-maze-madness/python/week-8.py`
- [ ] Build/test Block code
- [ ] Save `.mkcd` → `002-maze-madness/blocks/week-8.mkcd`
- [ ] git push
- [ ] Record video (~6 min): design walkthrough → run solver → present
- [ ] Upload + add to playlist
- [ ] Link in Notion W8 page

## 002 wrap-up

- [ ] Copy YouTube playlist URL → Notion `📦 주차별 숙제` parent page header
- [ ] Verify all 8 download links work in Notion
- [ ] Update repo `002-maze-madness/README.md` table — replace TBD with ✅
- [ ] Migrate legacy W2 files (`m001_world_1_2.mcworld` + `minecraft-M001-W12.mkcd` from old 🧱 BLOCK page) — these are 001 W2 files, drop into `001-pyramid-problems/` if not already done

---

## ✅ Done state (final)

- [ ] 16 videos uploaded to YouTube + organized into 2 playlists
- [ ] 16 worlds, 16 Python files, 16 block files in repo
- [ ] All Notion weekly hubs show working download links
- [ ] Both YouTube playlist links pinned in Notion
- [ ] Old stub guide pages cleaned up via Notion UI (orphans noted in TASKS.md)
