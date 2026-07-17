# 🎨 M003 Extension — English Worksheet (Advanced)

**Topic:** Design Your Own Pixel Art (x, y) · **Course:** 3D Coordinates · **Level:** Advanced (Extension, after Week 3) · **Time:** about 45 minutes

Every other week the picture was given to you. This week **you** draw it — then **you** read your own drawing back onto the wall.

**Build your canvas.** Run this to make a blank **15 × 15** wall, then put a **red block at your feet** as your **home spot**:

<div style="display:flex; gap:14px; align-items:flex-start; margin:10px 0; page-break-inside:avoid; break-inside:avoid"><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🧩 Blocks</p><img src="../assets/week3-canvas-blocks.png" alt="MakeCode blocks: on chat command run, fill with white concrete from ~1 ~1 ~0 to ~15 ~15 ~0, replace" style="width:100%; max-width:240px; border-radius:8px; display:block"></div><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🐍 Python</p><pre style="margin:0; white-space:pre; font-size:12px">def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(1, 1, 0),
        pos(15, 15, 0),
        FillOperation.REPLACE)
player.on_chat("run", on_run)</pre></div></div>

> 🔴 **Stand on the red block every time you run.** If you move, the picture moves too.

---

## 1 · Predict 🔮

Read each set of steps. Write what you will see **and the reason**.

```
place blue block at (3, 9)
place blue block at (4, 9)
place blue block at (5, 9)
```

**Three blocks share y = 9. Row or column? Which number stays the same, and why?**

<div class="write-space"></div>

```
place blue block at (7, 2)
place blue block at (7, 3)
place blue block at (7, 4)
place blue block at (7, 5)
```

**These four share x = 7. Row or column? Which number changes, and why?**

<div class="write-space"></div>

```
place green block at (5, 6)
place green block at (6, 6)
place green block at (5, 7)
place green block at (6, 7)
```

**These four change both numbers. What shape do they make, and why?**

<div class="write-space"></div>

```
place green block at (6, 6)
place blue block at (6, 6)
```

**Two blocks aim for the same (x, y). What ends up on the wall, and why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each one is broken. Fix it, then explain why the original was wrong and why your fix works.

**Bug A** — The flower's two leaves should sit at (2, 4) and (4, 4). Both land in the **same spot**.

```
place green block at (2, 4)
place green block at (2, 4)
```

**Write the fixed line:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should be a column going **up** at x = 8, from y = 5 to y = 7.

```
place black block at (8, 5)
place black block at (9, 5)
place black block at (10, 5)
```

**Write the fixed lines:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should be a 2 × 2 square with its bottom-left corner at (4, 4).

```
place blue block at (4, 4)
place blue block at (5, 4)
place blue block at (4, 4)
place blue block at (5, 4)
```

**Write the fixed lines:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Stand on your **home spot** (the red block).

**Your five rules.**

| # | Your design must… |
|---|---|
| 1 | fit inside the **15 × 15** wall |
| 2 | use **3 or more** different block colours |
| 3 | use **25 or more** blocks |
| 4 | be **recognisable** — someone else can name it without being told |
| 5 | be **drawn on the grid below before you place a single block** |

**Draw your design.** Colour the squares. x goes **across**, y goes **up**.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">✏️ Your design</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">1</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">3</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">5</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">6</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">7</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">8</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">9</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">10</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">11</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">12</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">13</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">14</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">15</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">15</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">14</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">13</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">12</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">11</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">10</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">9</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">8</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">7</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">6</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">5</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">4</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">3</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">2</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">1</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #d9d9d9"></td></tr></table></div>

**Write the plan.** List the (x, y) of every block in your **biggest** colour, in the order you will place them.

<div class="write-space tall" style="min-height: 200px"></div>

**Then build it.** Read each coloured square's (x, y) and place that block on your wall.

**Check your work.** Hold your grid next to your wall. Write down every block you had to move, and what was wrong with your first (x, y).

<div class="write-space"></div>

**Someone else names it.** Show your build to a person who has not seen your grid. What did they say it was? If they got it wrong, what would you change?

<div class="write-space"></div>

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your grid.** Hold this paper up to the camera.

**2 · Your build.** Hold your paper next to the wall so both are in the shot.

**3 · Your five rules.** Check each one out loud against your build.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 220px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
