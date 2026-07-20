# ☃️ M003 Extension — English Worksheet (Advanced)

**Topic:** Pixel-Art Snow Golem (x, y) · **Course:** 3D Coordinates · **Level:** Advanced (Extension, after Week 3) · **Time:** about 45 minutes

A bonus picture challenge: build a whole **snow golem** — snow body, carved-pumpkin head, coal buttons, stick arms — then make it your own. Every block sits at **(x, y)** — x is how far **across**, y is how far **up**.

**Build your canvas.** Run this to make a blank **15 × 15** wall, then put a **red block at your feet** as your **home spot**:

<div style="display:flex; gap:14px; align-items:flex-start; margin:10px 0; page-break-inside:avoid; break-inside:avoid"><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🧩 Blocks</p><img src="../assets/week3-canvas-blocks.png" alt="MakeCode blocks: on chat command run, fill with white concrete from ~1 ~1 ~0 to ~15 ~15 ~0, replace" style="width:100%; max-width:240px; border-radius:8px; display:block"></div><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🐍 Python</p><pre style="margin:0; white-space:pre; font-size:12px">def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(1, 1, 0),
        pos(15, 15, 0),
        FillOperation.REPLACE)
player.on_chat("run", on_run)</pre></div></div>

> 🔴 **Big idea:** (x, y) is counted from your **home spot**, not the world's corner. Stand on the red block *every* time you run, or the whole picture shifts.

---

## 1 · Predict 🔮

Read each set of steps. Write what you will see **and the reason**.

```
place pumpkin block at (6, 15)
place pumpkin block at (7, 15)
place pumpkin block at (8, 15)
```

**Three pumpkin blocks share y = 15. Do they make a line going across or up? Which number stays the same, and why?**

<div class="write-space"></div>

```
place black block at (8, 3)
place black block at (8, 5)
place black block at (8, 7)
place black block at (8, 9)
```

**These four coal buttons share x = 8. Are they a row going across, or a column going up? Which number changes, and why?**

<div class="write-space"></div>

```
place snow block at (5, 4)
place snow block at (6, 4)
place snow block at (5, 5)
place snow block at (6, 5)
```

**These four blocks change both numbers. What shape do they make on the wall, and why?**

<div class="write-space"></div>

```
place snow block at (8, 7)
place black block at (8, 7)
```

**Two blocks aim for the same (x, y). What happens on the wall — snow, black, or both? Explain the reason.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block below is broken. Read what it should do, fix it, then explain why the original was wrong and your fix works.

**Bug A** — This should make the golem's **two eyes**, one at (7, 13) and one at (9, 13). Both land in the **same spot**.

```
place black block at (7, 13)
place black block at (7, 13)
```

**Hint:** the two eyes are at **different** x values — one is further across than the other.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A **coal button** should sit at (8, 7). The two numbers are **swapped**, so it lands in the wrong place.

```
place black block at (7, 8)
```

**Hint:** the **first** number is across (x), the **second** is up (y). Which one should be 8, which should be 7?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A friend stood on the **wrong block** and ran correct code. The golem came out **shifted two blocks too high** — every block landed at a y two bigger than the grid says.

```
(the code matched the grid exactly)
```

**What did your friend forget to do before pressing run? Why does standing on the home spot change where every block lands?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Stand on your **home spot** (the red block). Copy the golem block by block, reading each colored square's (x, y) — **x** across the top, **y** down the side.

**Plan first.** Before you place anything, find the **lowest** block and the **left-most** block of the golem and write their (x, y) here. That tells you where the picture starts.

<div class="write-space short"></div>

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">☃️ Snow Golem (snow · light blue #cfe0ec, pumpkin · #e5772b, face + coal buttons · black, arms · brown #6b4a2b)</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">1</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">3</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">5</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">6</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">7</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">8</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">9</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">10</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">11</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">12</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">13</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">14</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">15</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">15</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">14</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">13</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">12</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">11</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#e5772b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">10</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">9</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#6b4a2b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#6b4a2b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#6b4a2b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#6b4a2b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#6b4a2b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#6b4a2b;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">8</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">7</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">6</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">5</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">4</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">3</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#1a1a1a;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">2</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:28px">1</th><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#cfe0ec;border:1px solid #0000002a"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:28px;height:28px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr></table></div>

**Modify challenge.** After you copy the golem exactly, change **one thing** that is your own idea — swap a colour, add a scarf row, give it a longer arm, or add more buttons. Write the (x, y) of the blocks you changed, then build it.

<div class="write-space short"></div>

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

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

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
