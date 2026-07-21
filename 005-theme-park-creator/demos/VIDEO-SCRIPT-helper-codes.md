# 🎬 Video Script — Helper Codes (Coaster Supports)

**World:** any prior Theme Park week (world doesn't matter)  ·  **Course:** Theme Park Creator (M005)  ·  **Length:** ~3–4 min
**Pairs with:** `demos/helper-codes.html`  ·  **Concept:** helper functions — write a job once, name it, reuse it.

---

### Beat 1 — Hook (0:00)
🎥 **DO:** Stand where a coaster will go. Empty ground.
🗣️ **SAY:** "A roller coaster stands on a row of support pillars. Every pillar is the **same job**. So instead of writing it over and over, I'll write it **once**, give it a name, and reuse it. That's a **helper code**."

### Beat 2 — One pillar the long way (0:25)
🎥 **DO:** Show a single `blocks.fill` that makes one pillar. Run it — one pillar appears.
🗣️ **SAY:** "Here's one pillar — one fill line. Easy. But my coaster needs a **whole row** of them. If I copy-paste this for every pillar, it gets long, and one wrong number breaks a pillar. There's a better way."

### Beat 3 — Write the helper (0:55)
🎥 **DO:** Show `def pillar(x):` with the fill inside. Do **not** run yet.
🗣️ **SAY:** "I write the job **once** and name it: `def pillar`. Watch — I run this and… **nothing** builds. That's important. Writing a helper doesn't build anything. It just **teaches** the computer a new move. It builds when I **call** it."

### Beat 4 — Call it (1:20)
🎥 **DO:** Type `pillar(2)`. Run. One pillar appears.
🗣️ **SAY:** "Now I **call** it: `pillar(2)`. One short line — and the whole pillar appears. I taught it the job once; now I just say its name."

### Beat 5 — Reuse it (1:45)
🎥 **DO:** Add `pillar(5)` and `pillar(8)`. Run. Three pillars.
🗣️ **SAY:** "Same helper, different spot. I change the number in the brackets and get a pillar right there. **Write once, reuse forever.** That's the whole point of a helper."

### Beat 6 — Loop the helper (2:15)
🎥 **DO:** Replace the calls with `for x in range(2, 21, 3): pillar(x)`. Run — a full row.
🗣️ **SAY:** "Even better — a **loop** calls my helper again and again. Two lines… and I get a whole row of supports. Imagine typing all of those by hand!"

### Beat 7 — Add a parameter (2:45)
🎥 **DO:** Change to `def pillar(x, height):` and raise `height` each loop. Run — the row climbs.
🗣️ **SAY:** "One more trick. I put the **changing number** — the height — in the brackets. That's a **parameter**. Now every pillar can be a different height. I raise it as I go… and my track **climbs**. There's my coaster ramp."

### Beat 8 — Close (3:15)
🗣️ **SAY:** "So a helper code is this: teach one job **once**, then reuse it — anywhere, any number of times, any size. Less typing, fewer mistakes, bigger builds. Your worksheet gives you a coaster to build with your own helper. Have fun."

---

**Code beats (for reference — see `helper-codes.html`):**
1. `blocks.fill(...)` one pillar → 2. copy-paste ×3 → 3. `def pillar(x):` → 4. `pillar(2)` → 5. `pillar(2/5/8)` → 6. `for x in range(...): pillar(x)` → 7. `def pillar(x, height):` + rising `height`.
