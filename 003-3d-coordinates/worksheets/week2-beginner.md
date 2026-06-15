# 🧊 M003 Week 2 — English Worksheet (Beginner)

**Topic:** Lines & Rectangles on the Wall (x, y) · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 30 minutes

This week you use a **loop** to draw a whole **line** of blocks on the wall instead of placing them one at a time. Grow **x** to go across. Grow **y** to go up.

---

## 1 · Predict 🔮

Read the steps. Before you imagine it happening, circle or write your answer.

```
set x to 0
repeat 4 times:
    place stone block at (x, 0)
    add 1 to x
```

**x grows and y stays 0. Does this draw a line going across, or a line going up? Circle one:** across · up

**Why?**

<div class="write-space short"></div>

```
set y to 0
repeat 4 times:
    place stone block at (0, y)
    add 1 to y
```

**This time y grows and x stays 0. Across or up? Circle one:** across · up

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The line should go **across** the bottom of the wall.

```
# clean
set x to 0
repeat 4 times:
    place block at (x, 0)
    add 1 to x
```

```
# buggy
set x to 0
repeat 4 times:
    place block at (0, x)
    add 1 to x
```

**What is wrong? Which way does the buggy line go?**

<div class="write-space short"></div>

**Pair B** — The line should be **4 blocks long**.

```
# clean
set x to 0
repeat 4 times:
    place block at (x, 0)
    add 1 to x
```

```
# buggy
set x to 0
repeat 2 times:
    place block at (x, 0)
    add 1 to x
```

**What is wrong? How long is the buggy line?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

You want a line going **straight up** the left edge of the wall. x must stay **0** while y grows. One number is missing. Fill it in using the word bank.

```
set y to 0
repeat 4 times:
    place block at (____, y)
    add 1 to y
```

**Word bank:** `0` · `y` · `4`

**Write the missing number:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Use a loop to draw **one line going across** and another loop for **one line going up**, so they meet at the corner (0, 0) and make an **L** shape. When you finish, come back here.

Send a photo or video of your L, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My across line grew the number …
>
> My up line grew the number …
>
> The two lines meet at …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you show your L on the wall. Talk like you are teaching a friend. Try to use these words: **loop**, **line**, **across**, **up**.

> 1. Run the loop that draws the across line.
> 2. Run the loop that draws the up line.
> 3. Say which number (x or y) grew in each loop.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
