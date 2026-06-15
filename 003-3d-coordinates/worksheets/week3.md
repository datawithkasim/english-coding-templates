# 🧊 M003 Week 3 — English Worksheet

**Topic:** Pixel Art on the Wall (x, y) · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week you draw **pictures with blocks** on the wall. A picture is made of **rows**, and a row is made of colors in order. A **nested loop** — a loop inside a loop — draws the picture row by row: the inner loop grows **x** across, the outer loop grows **y** up.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

```
set y to 0
repeat 2 times:
    set x to 0
    repeat 3 times:
        place red block at (x, y)
        add 1 to x
    add 1 to y
```

**How many red blocks are in each row? How many rows? How many blocks in total?**

<div class="write-space"></div>

```
set x to 0
repeat 2 times:
    place red block at (x, 0)
    add 1 to x
place blue block at (x, 0)
```

**This draws one row. Say the colors in order — what does the bottom row look like?**

<div class="write-space"></div>

```
set y to 0
repeat 3 times:
    place red block at (0, y)
    place yellow block at (1, y)
    place red block at (2, y)
    add 1 to y
```

**Every row is red, yellow, red. What does the whole picture look like? Which color makes a stripe straight up the middle?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should draw **3 rows** of blue blocks, each row one step higher. Right now every row lands in the **same place**.

```
set y to 0
repeat 3 times:
    set x to 0
    repeat 4 times:
        place blue block at (x, y)
        add 1 to x
```

**Hint:** after each row, the picture needs to step up to the next y.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The bottom row should look like **red, red, blue** — red at (0, 0) and (1, 0), blue at (2, 0). Right now the colors come out in the wrong order.

```
place blue block at (0, 0)
place red block at (1, 0)
place red block at (2, 0)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The picture should be **5 blocks wide** and 3 rows tall. Right now it comes out squashed and thin.

```
set y to 0
repeat 3 times:
    set x to 0
    repeat 2 times:
        place green block at (x, y)
        add 1 to x
    add 1 to y
```

**Hint:** the inner loop controls how wide each row is.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Draw a **pixel art picture** on the wall — a heart, a face, or the first letter of your name — using rows of colored blocks. When you finish, come back here.

Send a photo or video of your picture, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I planned my picture by …
>
> My picture is … rows tall and … blocks wide.
>
> The colors in the bottom row are …
>
> I used a nested loop when …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your pixel art on the wall. Talk through it like you are teaching someone who has never seen it. Try to use these words: **row**, **nested loop**, **inner**, **outer**, **pattern**.

> 1. Show your finished picture from the front.
> 2. Point at the bottom row and say the colors in order.
> 3. Show your code and say what the **inner** loop does (across) and what the **outer** loop does (up).
> 4. Say in your own words why the picture is drawn row by row.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
