# 🧊 M003 Week 2 — English Worksheet

**Topic:** Lines and Grids · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week you place a **line of blocks with a loop**. One number stays the same, the other grows by 1 each time. With lines you can also make a **square outline**.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

```
set z to 0
repeat 5 times:
    place stone block at (2, z)
    add 1 to z
```

**Where does the line start? Where does it end? Which number stays the same?**

<div class="write-space"></div>

```
set x to 0
repeat 4 times:
    place gold block at (x, 3)
    add 1 to x
```

**Which way does this line grow — along x or along z? How long is it?**

<div class="write-space"></div>

```
set z to 0
repeat 3 times:
    place stone block at (0, z)
    place stone block at (4, z)
    add 1 to z
```

**Each turn of the loop places two blocks. What do the blocks make — one line or two lines? How far apart are they?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The line should grow along **z**, from (2, 0) to (2, 4). x should stay at 2. Right now the line grows the wrong way.

```
set n to 0
repeat 5 times:
    place stone block at (n, 2)
    add 1 to n
```

**Hint:** look at which slot n is in — the x slot or the z slot.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The line should be **6 blocks long**, from (0, 0) to (0, 5). Right now it comes out one block short.

```
set z to 0
repeat 5 times:
    place gold block at (0, z)
    add 1 to z
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should make a line of 4 stone blocks starting at (3, 0). Right now all the blocks land in the **same spot**.

```
set z to 0
repeat 4 times:
    place stone block at (3, z)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a **square outline** — like a fence for a garden — using loops to place the lines. When you finish, come back here.

Send a photo or video of your square, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My loop repeated … times because …
>
> The number that stayed the same was …
>
> The number that grew was …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your square in the world. Talk through it like you are teaching someone who has never seen it. Try to use these words: **loop**, **line**, **repeat**, **coordinate**, **grow**.

> 1. Show your square outline, then show the code that built it.
> 2. Read one loop out loud and say which number grows.
> 3. Point at the start and the end of one line and say their coordinates.
> 4. Say in your own words why a loop is better than placing every block by hand.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
