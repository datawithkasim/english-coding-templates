# 🧊 M003 Week 2 — English Worksheet

**Topic:** Lines & Rectangles on the Wall (x, y) · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week you use a **loop** to draw a **line** of blocks: grow **x** to go across, grow **y** to go up. Four lines make a **rectangle outline** — a picture frame.

---

## 1 · Predict 🔮

Read each set of steps. Write what you think you will see.

```
set x to 0
repeat 5 times:
    place stone block at (x, 0)
    add 1 to x
```

**Which way does this line grow — across or up? How long is it? Which number stays the same?**

<div class="write-space"></div>

```
set y to 0
repeat 4 times:
    place gold block at (3, y)
    add 1 to y
```

**This time the line is at x = 3 and y grows. Across or up? How tall is it?**

<div class="write-space"></div>

```
set x to 0
repeat 6 times:
    place stone block at (x, 0)
    place stone block at (x, 4)
    add 1 to x
```

**Each turn places two blocks at the same x — one at y = 0, one at y = 4. What do the blocks make — one line or two lines? How far apart, top to bottom?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block below is broken. Read what it should do, fix it, then explain why the original was wrong and your fix works.

**Bug A** — The line should grow **up** at x = 2, from (2, 0) to (2, 4). Right now it grows the wrong way.

```
set n to 0
repeat 5 times:
    place stone block at (n, 2)
    add 1 to n
```

**Hint:** look at which slot n is in — the x slot (across) or the y slot (up).

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The bottom edge of a frame should be **6 blocks long**, from (0, 0) to (5, 0). Right now it comes out one block short.

```
set x to 0
repeat 5 times:
    place gold block at (x, 0)
    add 1 to x
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should make a line of 4 stone blocks growing up from (3, 0). Right now all the blocks land in the **same spot**.

```
set y to 0
repeat 4 times:
    place stone block at (3, y)
```

**Hint:** read every line of the loop — is anything growing y?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Switch to your homework world. Build a **rectangle outline** on the wall — like an empty picture frame — using loops for the four edges (bottom, top, left, right).

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
