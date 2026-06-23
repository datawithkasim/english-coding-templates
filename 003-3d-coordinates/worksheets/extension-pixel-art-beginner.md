# 🧊 M003 Extension — English Worksheet (Beginner)

**Topic:** Pixel-Art Mobs (x, y) · **Course:** 3D Coordinates · **Level:** Extension (Beginner, after Week 3) · **Time:** about 30 minutes

This is a **bonus picture challenge** between Week 3 and Week 4. You copy a mob onto your wall using **(x, y)**. x is how far **across**, y is how far **up**. Read the picture and place each block at its (x, y).

**First, build your canvas.** Run this to make a blank **15 × 15** wall, then put a **red block at your feet** as your **home spot**:

<div style="display:flex; gap:14px; align-items:flex-start; margin:10px 0; page-break-inside:avoid; break-inside:avoid"><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🧩 Blocks</p><img src="../assets/week3-canvas-blocks.png" alt="MakeCode blocks: on chat command run, fill with white concrete from ~1 ~1 ~0 to ~15 ~15 ~0, replace" style="width:100%; max-width:240px; border-radius:8px; display:block"></div><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🐍 Python</p><pre style="margin:0; white-space:pre; font-size:12px">def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(1, 1, 0),
        pos(15, 15, 0),
        FillOperation.REPLACE)
player.on_chat("run", on_run)</pre></div></div>

> 🔴 **Stand on the red block every time you run.** If you move, the picture moves too and the blocks land in the wrong place. Same spot every time = a clean picture.

---

## 1 · Predict 🔮

Read the steps. Before you imagine it happening, circle or write your answer.

```
place pink block at (4, 13)
place pink block at (5, 13)
place pink block at (6, 13)
```

**Do these blocks make a line going across? Circle one:** across · up

**Which number stays the same — x or y?**

<div class="write-space short"></div>

```
place black block at (8, 7)
place black block at (8, 8)
```

**These share x = 8 and y grows. Do they go across or up? Circle one:** across · up

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows the **correct** line first, then a **broken** one. Circle what's different and write one short sentence about the bug.

**Pair A** — The axolotl's two eyes should be at **different** spots: (6, 10) and (11, 10).

```
# correct
place black block at (6, 10)
place black block at (11, 10)
```

```
# broken
place black block at (6, 10)
place black block at (6, 10)
```

**What is wrong? Where do both blocks land?**

<div class="write-space short"></div>

**Pair B** — The dragon's eye should be at (8, 10).

```
# correct
place purple block at (8, 10)
```

```
# broken
place purple block at (10, 8)
```

**What is wrong? Which two numbers got swapped?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

To move **up** a column, the **second** number (y) has to grow. Fill in the missing numbers so this line goes up at x = 8.

```
place black block at (8, 7)
place black block at (8, __)
place black block at (8, __)
```

**Word bank for the blanks:** `8` · `9`

**Write the two missing numbers:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Stand on your **home spot** (the red block).

**Warm up first.** Copy this small axolotl frill onto your wall. Read each pink square's (x, y) and place a pink block there.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">🌸 Axolotl frill</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ff5fa2;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr></table></div>

**Now build the big 🦜 axolotl from the main worksheet grid.** Read each colored square and place that color at its (x, y).

When your picture is finished, send a photo of it, then explain what you did. Use these sentence starters — write 3 to 5 sentences total.

> First, I built the …
>
> The lowest block in my picture is at (x = …, y = …).
>
> To go across I changed the … number; to go up I changed the … number.
>
> One time a block landed in the wrong place because …

<div class="write-space tall" style="min-height: 300px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a short video on your phone (or a parent's phone) while you show your axolotl on the wall. Try to use these words: **x**, **y**, **across**, **up**, **home spot**.

> 1. Show your home spot (the red block).
> 2. Show your finished axolotl.
> 3. Point at one block and read its coordinate: "this one is at x …, y …".

**Write what you will say in your video.**

<div class="write-space tall" style="min-height: 300px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
