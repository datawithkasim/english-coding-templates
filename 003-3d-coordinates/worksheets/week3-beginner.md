# 🧊 M003 Week 3 — English Worksheet (Beginner)

**Topic:** Pixel Art on the Wall (x, y) · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 30 minutes

This week you copy a picture made of blocks onto your wall. Every block sits at **(x, y)**. x is **across**, y is **up**.

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

Read the steps. Circle your answer.

```
place red block at (6, 1)
place red block at (7, 1)
place red block at (8, 1)
```

**Across or up? Circle one:** across · up

**Which number changes? Circle one:** x · y

```
place green block at (8, 13)
place green block at (8, 14)
```

**Across or up? Circle one:** across · up

**Which number changes? Circle one:** x · y

---

## 2 · Spot the Bug 🐛

This should make a row going **across**: (6, 1), (7, 1), (8, 1). But all three blocks land in the **same spot**.

```
place yellow block at (6, 1)
place yellow block at (6, 1)
place yellow block at (6, 1)
```

**Hint:** to go across, the **x** must grow. Fill in the blanks.

```
place yellow block at (6, 1)
place yellow block at (__, 1)
place yellow block at (__, 1)
```

**Which two numbers are missing? Circle one:** 7 and 8 · 6 and 6

**Why was it broken? Circle one:** all three had the same x · the color was wrong

---

## 3 · Show Your Work 📸🎥

Stand on your **home spot** (the red block).

**Warm up first.** Copy this small green cross. Read each green square's (x, y) and place a green block there.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">🟩 Green cross</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr></table></div>

**Now try a big one.** Pick the 🍍 pineapple or the 🍎 apple from the main worksheet grid and copy it the same way. Read each colored square and place that color at its (x, y).

Record **one video** (a phone is fine). Show two things:

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

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
