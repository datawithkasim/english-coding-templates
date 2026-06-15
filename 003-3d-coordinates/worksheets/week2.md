# 🧊 M003 Week 2 — English Worksheet

**Topic:** Lines & Rectangles on the Wall (x, y) · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week you use a **loop** to draw a whole **line** of blocks on the wall. Grow **x** to go across, grow **y** to go up. Put four lines together and you get a **rectangle outline** — a picture frame.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The line should grow **up** at x = 2, from (2, 0) to (2, 4). x should stay 2. Right now the line grows the wrong way.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a **rectangle outline** on the wall — like an empty picture frame — using loops for the four edges (bottom, top, left, right). When you finish, come back here.

Send a photo or video of your frame, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My bottom edge grew the number … and stayed at y = …
>
> My left edge grew the number … and stayed at x = …
>
> My frame is … wide and … tall.
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your frame on the wall. Talk through it like you are teaching someone who has never seen a loop. Try to use these words: **loop**, **line**, **edge**, **across**, **up**.

> 1. Show your rectangle frame, then show the code that built it.
> 2. Read one loop out loud and say which number grows and which stays the same.
> 3. Point at the start and the end of one edge and say their coordinates.
> 4. Say in your own words why a loop is better than placing every block by hand.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
