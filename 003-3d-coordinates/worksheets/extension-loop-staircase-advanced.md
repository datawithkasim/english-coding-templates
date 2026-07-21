# 🌀 M003 Extension — The Loop Pattern (Advanced)

**Topic:** One loop, three counters (x, y, z) · **Course:** 3D Coordinates · **Level:** Extension (Advanced, after Week 6) · **Time:** about 45 minutes

Until now you placed and filled blocks by choosing **every** coordinate **by hand**. This time **one loop** builds all **7** obsidian walls for you. The loop keeps three counters — **x**, **y**, **z** — and nudges each one by a fixed **step** every pass. That is an **algorithm**: a short list of steps a computer repeats. Load the world, type `SPIRAL` in the chat, and watch 7 walls grow into a pattern.

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

> 🔁 **Big idea:** the fill line **never changes** — it is the same seven times. The walls come out **different** only because **x, y, z change** between passes. Same code, new numbers.

One corner of every wall is **pinned at (14, 0)**. The other corner is **(x, y, z)** — and that is the counter that moves. Each pass the new wall is **2 wider** (x), **1 taller** (y), and **2 deeper** (z) than the last.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move the whole pattern.
>
> 🎨 Every wall is **obsidian**.

**Trace** (or **dry-run**) means: be the computer. Walk the code line by line and write down what each variable holds — **before** you ever run it.

---

## 1 · Predict 🔮

**Trace the loop.** For each iteration write the **START** values (what x, y, z hold when the pass begins — these are the numbers the `fill` line uses) and the **END** values (what they hold after the three update lines run).

Iteration 0's START is given. **The END of one row is the START of the next row** — that is your check.

<table style="border-collapse:collapse;margin:6px 0"><tr><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">Iteration</th><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">START x</th><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">START y</th><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">START z</th><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">END x</th><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">END y</th><th style="padding:5px 4px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6">END z</th></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">0</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">14</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">0</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">2</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">1</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">2</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">3</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">4</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">5</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="width:64px;height:34px;padding:0 6px;text-align:center;font-size:13px;font-weight:700;background:#faf7ff;color:#1a1a2e;border:1px solid #cfcfd6">6</td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="width:46px;height:34px;padding:0 4px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr></table>

**The `fill` line runs *before* x, y, z change. So which x, y, z does iteration 0's wall actually use?**

<div class="write-space short"></div>

**`range(7)` — how many walls does the loop build, and what are the first and last values of `step`?**

<div class="write-space short"></div>

**Which counter makes each wall *taller*? Which makes it *deeper*? Which makes it *wider*? Say why for each.**

<div class="write-space"></div>

**The wall grows every single pass, yet the `fill` line is never edited. Explain how that is possible.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each loop below is broken. Trace it in your head, fix it, then explain **why** the original was wrong and **why** your fix works.

**Bug A — a counter that never steps.** The `z = z + 2` line was deleted. The loop still runs 7 times, but z stays **2** the whole time.

```python
x = 14
y = 0
z = 2
for step in range(7):
    fill OBSIDIAN from (14, 0, z) to (x, y, z)
    x = x - 2
    y = y + 1
```

**All 7 walls land at z = 2, on top of each other. What do you see in the world instead of a pattern, and why? Write the missing line and where it goes.**

<div class="write-space"></div>

**Bug B — right steps, wrong order.** The three update lines were moved **above** the `fill` line instead of below it.

```python
x = 14
y = 0
z = 2
for step in range(7):
    x = x - 2
    y = y + 1
    z = z + 2
    fill OBSIDIAN from (14, 0, z) to (x, y, z)
```

**Iteration 0 now fills using x = 12, y = 1, z = 4 — the tiny 1×1 starter step never appears, and the whole pattern shifts. Explain why "update *then* use" and "use *then* update" give different builds.**

<div class="write-space"></div>

**Bug C** *(the tricky one)* — **wrong step size.** It runs with no error, but the 7 separate steps merged into one solid slope with no gaps. A friend changed one line to `z = z + 1`.

```python
    z = z + 1
```

**The walls are each 1 block thick. Explain why `z = z + 2` leaves a gap between steps but `z = z + 1` makes them touch. Write the fix.**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Load the world. Stand on your home spot. Type `SPIRAL` in the chat and watch the loop build all 7 walls. Walk around the pattern — see the tiny 1-block step out front and the tall 7-high wall at the back.

<div style="page-break-inside:avoid;break-inside:avoid;margin:16px 0"><p style="font-weight:700;margin:0 0 6px">🧱 The finished pattern — side view (y &uarr; up, z &rarr; deeper)</p><table style="border-collapse:collapse;margin:4px 0"><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">2</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">4</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">6</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">8</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">10</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">12</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">14</th></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">7</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">6</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">5</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">4</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">3</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">2</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr><tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">1</th><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#241934;border:1px solid #0000002a"></td></tr></table></div>

**Look closely.** Reading left to right, the steps climb **1, 2, 3, 4, 5, 6, 7** blocks high — one taller each pass, because `y = y + 1` runs every loop. (Width, the x step, is not drawn here — each step is also wider than the last.)

**Modify challenge.** Change **one** thing and **predict the new pattern before you run it.** For example: change `range(7)` to `range(10)`, or make the step `y = y + 2` (steeper), or swap `OBSIDIAN` for another block. Write what will move, then build it and check.

<div class="write-space"></div>

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what the loop does and what each counter changes.

**2 · Your build.** Point the camera at the pattern. Name the smallest and biggest step.

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

Send this worksheet + your **one** video to teacher on KakaoTalk.
