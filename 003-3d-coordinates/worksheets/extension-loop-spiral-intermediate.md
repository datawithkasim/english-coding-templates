# 🌀 M003 Extension — The Loop Spiral (Intermediate)

**Topic:** One loop that **turns** (x, y, z) · **Course:** 3D Coordinates · **Level:** Extension (Intermediate, after the Loop Staircase) · **Time:** about 40 minutes

The **staircase** took the **same** step every pass, so it grew in a **straight diagonal**. A **spiral** also **turns** every pass — same loop, but the direction **changes** — so the squares wrap into a tower. Type `SPIRAL` in the chat and watch it **climb** and **turn**.

```python
x = 8
y = 0
z = 8
for step in range(12):
    fill GOLD from (x, y, z) to (x + 2, y, z + 2)
    y = y + 1
    if step % 4 == 0:
        x = x + 4
    elif step % 4 == 1:
        z = z + 4
    elif step % 4 == 2:
        x = x - 4
    else:
        z = z - 4
```

> 🔁 **Big idea:** `step % 4` counts **0, 1, 2, 3, 0, 1, 2, 3 …** — four directions on repeat. That is the **turn**. `y = y + 1` lifts each square higher. **Turn + rise = a spiral.**

<div style="page-break-inside:avoid;break-inside:avoid;margin:14px 0"><table style="border-collapse:collapse;margin:0 auto"><tr><td style="border:none"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">3 &uarr; back<br>z &minus; 4</td><td style="border:none"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">2 &larr; left<br>x &minus; 4</td><td style="padding:5px 6px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6;text-align:center" style="font-size:13px">step % 4</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">0 &rarr; right<br>x + 4</td></tr><tr><td style="border:none"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">1 &darr; forward<br>z + 4</td><td style="border:none"></td></tr></table></div>

---

## 1 · Predict 🔮

Fill the **turn** for each step. `step % 4` repeats **0, 1, 2, 3**. Step 0 is done.

<div style="page-break-inside:avoid;break-inside:avoid;margin:14px 0"><table style="border-collapse:collapse;margin:0 auto"><tr><th style="padding:5px 6px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6;text-align:center">step</th><th style="padding:5px 6px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6;text-align:center">step % 4</th><th style="padding:5px 6px;font-size:12px;background:#faf7ff;color:#6b4ee6;font-weight:700;border:1px solid #cfcfd6;text-align:center">turn (direction)</th></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">0</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">0</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">right (x + 4)</td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">1</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">2</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">3</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">4</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">5</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">6</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr><tr><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6;background:#f3eefe;color:#6b4ee6;font-weight:700">7</td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td><td style="height:34px;padding:0 8px;text-align:center;font-size:14px;border:1px solid #cfcfd6"></td></tr></table></div>

**`range(12)` builds how many squares? Circle one:** 4 · 8 · 12

**Which line makes the spiral go UP? Circle one:** `y = y + 1` · `x = x + 4` · `step % 4`

**Top-down, the 12 squares land on only **4** spots. Why only 4? (1 sentence)**

<div class="write-space short"></div>

---

## 2 · Spot the Bug 🐛

**Bug A — no turn.** A friend deleted the four `if` lines, so the direction never changes.

```python
for step in range(12):
    fill GOLD from (x, y, z) to (x + 2, y, z + 2)
    y = y + 1
    x = x + 4
```

**What do you build instead of a spiral? Circle one:** a straight diagonal · a flat square · nothing

**Bug B — no rise.** The `y = y + 1` line is gone, so y stays **0**.

**What happens to the tower? Circle one:** it stays flat on the floor · it grows taller · it turns upside down

**Write the missing line and say where it goes:**

<div class="write-space short"></div>

---

## 3 · Show Your Work 📸🎥

Load the world. Stand on your home spot. Type `SPIRAL` and watch each square **turn** to a new corner and **climb** one block.

<div style="page-break-inside:avoid;break-inside:avoid;margin:14px 0">
<p style="font-weight:700;margin:0 0 6px">&#128065; Top-down view (looking DOWN): x &rarr; across, z &darr; deeper</p>
<table style="border-collapse:collapse;margin:4px 0">
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px"></th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">8</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">9</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">10</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">11</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">12</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">13</th><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">14</th></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">8</th><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">9</th><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">10</th><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">11</th><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">12</th><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">13</th><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td></tr>
<tr><th style="font-size:10px;color:#999;font-weight:600;text-align:center;padding:0;height:16px;width:30px">14</th><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#ffffff;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td><td style="width:30px;height:30px;padding:0;background:#f2c14e;border:1px solid #0000002a"></td></tr>
</table></div>

**Looking down, the squares sit on 4 corners — the loop turns right, forward, left, back, then repeats, climbing each time.**

**Modify challenge.** Change **one** thing and **predict before you run** — for example `range(12)` → `range(20)` (taller), or the turn step `+ 4` → `+ 6` (wider). Write what will change, then build it.

<div class="write-space short"></div>

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what the loop does and how `step % 4` turns it.

**2 · Your build.** Point the camera at the spiral. Show it climbing and turning.

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
