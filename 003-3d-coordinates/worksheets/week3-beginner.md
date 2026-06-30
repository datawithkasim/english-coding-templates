# 🧊 M003 Week 3 — English Worksheet (Beginner)

**Topic:** Pixel Art on the Wall (x, y) · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 30 minutes

This week you copy a picture made of blocks onto your wall. Every block sits at a spot named by **two numbers — (x, y)**. x is how far **across**. y is how far **up**.

**First, build your canvas.** Run this to make a blank **15 × 15** wall, then put a **red block at your feet** as your **home spot**:

<div style="display:flex; gap:14px; align-items:flex-start; margin:10px 0; page-break-inside:avoid; break-inside:avoid"><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🧩 Blocks</p><img src="../assets/week3-canvas-blocks.png" alt="MakeCode blocks: on chat command run, fill with white concrete from ~1 ~1 ~0 to ~15 ~15 ~0, replace" style="width:100%; max-width:240px; border-radius:8px; display:block"></div><div style="flex:1; min-width:0"><p style="margin:0 0 4px; font-weight:700">🐍 Python</p><pre style="margin:0; white-space:pre; font-size:12px">def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(1, 1, 0),
        pos(15, 15, 0),
        FillOperation.REPLACE)
player.on_chat("run", on_run)</pre></div></div>

> 🔴 **Stand on the red block every time you run.** If you move, the picture moves too. Same spot every time = a clean picture.

---

## 1 · Predict 🔮

Read the steps. Do not run them. Circle one word, then answer.

```
place red block at (6, 1)
place red block at (7, 1)
place red block at (8, 1)
```

**Across or up? Circle one:** across · up

**Which number changes — x or y?**

<div class="write-space short"></div>

```
place green block at (8, 13)
place green block at (8, 14)
```

**Across or up? Circle one:** across · up

**Which number changes — x or y?**

<div class="write-space short"></div>

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

**Write the two missing numbers:**

<div class="write-space short"></div>

**Why was it broken? Write one short sentence.**

<div class="write-space short"></div>

---

## 3 · Build It 📸

Stand on your **home spot** (the red block).

**Warm up first.** Copy this small green cross. Read each green square's (x, y) and place a green block there.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">🟩 Green cross</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">5</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">4</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">3</th><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">2</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:32px">1</th><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#5a8f2b;border:1px solid #0000002a"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td><td style="width:32px;height:32px;padding:0;background:#ffffff;border:1px solid #e6e6e6"></td></tr></table></div>

**Now try a big one.** Pick the 🍍 pineapple or the 🍎 apple from the main worksheet grid and copy it the same way. Read each colored square and place that color at its (x, y).

When you finish, send a photo. Then write 2 sentences with these starters:

> I built the …
>
> The lowest block is at (x = …, y = …).

<div class="write-space tall" style="min-height: 240px"></div>

---

## 4 · Explain It 🎥

Take a video on your phone. Show your picture and talk like you are teaching a friend.

> 1. Show your home spot (the red block).
> 2. Show your finished picture.
> 3. Point at one block and say "this one is at x …, y …".

Try to use these words: **x** · **y** · **across** · **up** · **home spot**.

**Write 2 short sentences to say in your video.**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
