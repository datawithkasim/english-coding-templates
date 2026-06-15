# 🧊 M003 Week 3 — English Worksheet (Beginner)

**Topic:** Pixel Art on the Wall (x, y) · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 30 minutes

This week you draw **pictures with blocks** on the wall. A picture is made of **rows**. A loop inside a loop draws the picture row by row: the inner loop grows **x** across, then the outer loop grows **y** up to the next row.

---

## 1 · Predict 🔮

Read the steps. Before you imagine it happening, circle or write your answer.

```
set y to 0
repeat 2 times:
    set x to 0
    repeat 3 times:
        place red block at (x, y)
        add 1 to x
    add 1 to y
```

**Does this picture have 2 rows, one above the other? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
set y to 0
repeat 2 times:
    set x to 0
    repeat 3 times:
        place red block at (x, y)
        add 1 to x
```

**This time y never grows. Do the two rows land on top of each other? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — After each row, the picture should step **up** to the next y.

```
# clean
set y to 0
repeat 3 times:
    set x to 0
    repeat 4 times:
        place blue block at (x, y)
        add 1 to x
    add 1 to y
```

```
# buggy
set y to 0
repeat 3 times:
    set x to 0
    repeat 4 times:
        place blue block at (x, y)
        add 1 to x
```

**What is wrong? Where do all the rows land?**

<div class="write-space short"></div>

**Pair B** — The bottom row should look like **red, red, blue**.

```
# clean
place red block at (0, 0)
place red block at (1, 0)
place blue block at (2, 0)
```

```
# buggy
place blue block at (0, 0)
place red block at (1, 0)
place red block at (2, 0)
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The inner loop should make each row grow **across**. One word is missing. Fill it in using the word bank.

```
set y to 0
repeat 3 times:
    set x to 0
    repeat 4 times:
        place blue block at (x, y)
        add 1 to ____
    add 1 to y
```

**Word bank:** `x` · `y` · `block`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Draw a small **pixel art picture** on the wall — a heart, a flower, or a letter — using rows of colored blocks. When you finish, come back here.

Send a photo or video of your picture, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My picture is a …
>
> The colors in the bottom row are …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you show your picture on the wall. Talk like you are teaching a friend. Try to use these words: **row**, **loop**, **pattern**, **color**.

> 1. Show your finished picture.
> 2. Point at the bottom row and say the colors in order.
> 3. Say in your own words how the rows stack up to make a picture.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
