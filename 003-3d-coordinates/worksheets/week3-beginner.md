# 🧊 M003 Week 3 — English Worksheet (Beginner)

**Topic:** Pixel Art on the Wall (x, y) · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 30 minutes

This week you **copy a picture made of blocks** onto your wall. Every block sits at a spot named by **two numbers — (x, y)**. x is how far **across**, y is how far **up**. You read the picture and place each block at its (x, y).

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
place red block at (6, 1)
place red block at (7, 1)
place red block at (8, 1)
```

**Do these blocks make a line going across? Circle one:** across · up

**Which number stays the same — x or y?**

<div class="write-space short"></div>

```
place green block at (8, 13)
place green block at (8, 14)
```

**These share x = 8 and y grows. Do they go across or up? Circle one:** across · up

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows the **correct** line first, then a **broken** one. Circle what's different and write one short sentence about the bug.

**Pair A** — A line should grow **across** at the bottom: (5, 1), (6, 1), (7, 1).

```
# correct
place red block at (5, 1)
place red block at (6, 1)
place red block at (7, 1)
```

```
# broken
place red block at (5, 1)
place red block at (5, 1)
place red block at (5, 1)
```

**What is wrong? Where do all three blocks land?**

<div class="write-space short"></div>

**Pair B** — The stem should grow **up** at x = 8.

```
# correct
place brown block at (8, 13)
place brown block at (8, 14)
```

```
# broken
place brown block at (13, 8)
place brown block at (14, 8)
```

**What is wrong? Which two numbers got swapped?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

To move **across** a row, the **first** number (x) has to grow. Fill in the missing numbers so this line goes across the bottom.

```
place yellow block at (6, 1)
place yellow block at (__, 1)
place yellow block at (__, 1)
```

**Word bank for the blanks:** `7` · `8`

**Write the two missing numbers:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Stand on your **home spot** (the red block).

**Warm up first.** Copy this small green cross onto your wall. Read each green square's (x, y) and place a green block there.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">🟩 Green cross</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr></table></div>

**Now pick one big picture — the 🍍 pineapple or the 🍎 apple from the main worksheet grid — and copy it the same way.** Read each colored square and place that color at its (x, y).


When you finish, send a photo of your picture, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I built the …
>
> The lowest block in my picture is at (x = …, y = …).
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you show your picture on the wall. Talk like you are teaching a friend. Try to use these words: **x**, **y**, **across**, **up**, **home spot**.

> 1. Show your home spot (the red block) and say why you stand on it.
> 2. Show your finished picture.
> 3. Point at one block and read its coordinate: "this one is at x …, y …".

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
