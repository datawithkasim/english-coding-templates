# 🌀 M003 Extension — The Loop Pattern (Beginner)

**Topic:** One loop, three counters (x, y, z) · **Course:** 3D Coordinates · **Level:** Extension (Beginner, after Week 6) · **Time:** about 30 minutes

Until now you placed blocks by choosing **every** coordinate **by hand**. This time **one loop** builds all **7** obsidian walls for you. The loop keeps three counters — **x**, **y**, **z** — and changes each one a little every pass. That is an **algorithm**: a short list of steps a computer repeats. Load the world, type `SPIRAL` in the chat, and watch 7 walls grow into a pattern.

```python
x = 14
y = 0
z = 2
for step in range(7):
    fill OBSIDIAN from (14, 0, z) to (x, y, z)
    x = x - 2
    y = y + 1
    z = z + 2
```

> 🔁 **Big idea:** the loop does the same three changes every pass — x goes **down 2**, y goes **up 1**, z goes **up 2**. So each new wall is a little **wider**, **taller**, and **deeper** than the last.

> 🔴 Stand on your **home spot** (red block) every run.
>
> 🎨 Every wall is **obsidian**.

---

## 1 · Predict 🔮

Read the code. Circle one.

**`for step in range(7)` — how many walls does the loop build? Circle one:** 3 · 7 · 10

**Each pass runs `y = y + 1`. Does that make the next wall...? Circle one:** taller · wider · deeper

**Each pass runs `z = z + 2`. Does that make the next wall...? Circle one:** taller · wider · deeper

**The loop starts with z = 2. After one pass, `z = z + 2` runs. What is z now? Circle one:** 3 · 4 · 6

---

## 2 · Spot the Bug 🐛

The `z = z + 2` line was deleted. Now z stays **2** every pass, so all 7 walls land in the **same spot**, on top of each other — you see one wall, not a pattern.

```python
for step in range(7):
    fill OBSIDIAN from (14, 0, z) to (x, y, z)
    x = x - 2
    y = y + 1
```

**What is missing? Circle one:** the z step · the loop

**Should each wall sit at a new z or the same z? Circle one:** a new z · the same z

---

## 3 · Show Your Work 📸🎥

Load the world. Stand on your home spot. Type `SPIRAL` in the chat and watch the loop build all 7 walls. Walk around the pattern.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">🧱 The finished pattern — side view (y &uarr; up, z &rarr; deeper)</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">6</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">8</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">10</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">12</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">14</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">7</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">6</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">5</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">4</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">3</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">2</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">1</th><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr></table></div>

**Reading left to right, the steps get taller: 1, 2, 3, 4, 5, 6, 7.**

**How many steps are there? Circle one:** 5 · 7 · 9

**Which step is the tallest? Circle one:** the first (front) · the last (back)

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera at the pattern. Name the smallest and biggest step.

Say these out loud, filling in the blanks:

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

---

### Submit ✅

Send this worksheet + your **one** video to teacher on KakaoTalk.
