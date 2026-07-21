# 🎬 Video Script — The Loop Pattern (x, y, z)

**World:** `intro to algos.mcworld`  ·  **Course:** 3D Coordinates (M003)  ·  **Length:** ~3–4 min
**Chat command:** `SPIRAL`  ·  **Pairs with:** `demos/loop-pattern.html`
**Honest framing:** this is **not** a staircase and **not** a spiral — it's a **pattern** a loop draws by changing three numbers.

---

### Beat 1 — Hook (0:00)
🎥 **DO:** Stand on the home block. Empty ground in front of you.
🗣️ **SAY:** "One line of code is going to build this whole pattern for me — seven walls, each one bigger than the last. And I only write the build line **once**. Let me show you how."

### Beat 2 — The start values (0:20)
🎥 **DO:** Show the code. Point at `x = 14`, `y = 0`, `z = 2`.
🗣️ **SAY:** "Every block in Minecraft has three numbers: **x**, **y**, **z**. x is across, y is up, z is how deep. My pattern starts here — x is 14, y is 0, z is 2. Nothing is built yet. These are just my starting coordinates."

### Beat 3 — The loop runs once (0:45)
🎥 **DO:** Type `SPIRAL` in chat and run. Point at the single block that appears.
🗣️ **SAY:** "The loop runs. First pass, it fills from (14, 0, 2) to (14, 0, 2) — the same spot — so I get **one block**. Then look what happens: x goes **down 2**, y goes **up 1**, z goes **up 2**. The numbers changed."

### Beat 4 — Watch the pattern grow (1:15)
🎥 **DO:** Point along the row of walls, front to back.
🗣️ **SAY:** "Now the same fill line runs again — but with the **new** numbers. So this wall is a bit wider, a bit taller, a bit deeper. And again. And again. Seven times. Each wall is **2 wider, 1 taller, 2 deeper** than the one before it. That growing is the **pattern**."

### Beat 5 — The big idea (2:00)
🎥 **DO:** Scroll to the `fill` line. Point at it.
🗣️ **SAY:** "Here's the trick. I **never** changed this build line — it's exactly the same every pass. The walls come out different **only** because x, y and z change between passes. That's called an **algorithm**: a short list of steps the computer repeats for you."

### Beat 6 — Change one number (2:40) *(optional)*
🎥 **DO:** Change `range(7)` to `range(10)` (or `z = z + 2` to `+ 3`). Run again.
🗣️ **SAY:** "Watch — I'll change just **one** number. `range(7)` becomes `range(10)`. Predict with me… more walls? Let's see. Yes! Three extra walls, no extra work. Change one number, change the whole pattern."

### Beat 7 — Close (3:10)
🗣️ **SAY:** "So: a loop plus three changing numbers makes a pattern as big as you want. Your worksheet asks you to trace x, y and z for each pass — do that, and you'll know exactly what the computer is thinking. See you in class."

---

**On-screen coordinates to point at (for reference):**
| pass | fill from | fill to | wall size |
|---|---|---|---|
| 0 | (14,0,2) | (14,0,2) | 1 block |
| 1 | (14,0,4) | (12,1,4) | 3 wide · 2 tall |
| 2 | (14,0,6) | (10,2,6) | 5 wide · 3 tall |
| 3 | (14,0,8) | (8,3,8) | 7 wide · 4 tall |
| … | … | … | … |
| 6 | (14,0,14) | (2,6,14) | 13 wide · 7 tall |
