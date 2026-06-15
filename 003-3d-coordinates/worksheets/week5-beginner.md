# 🧊 M003 Week 5 — English Worksheet (Beginner)

**Topic:** Into 3D (x, y, z) · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 30 minutes

You know the wall (x, y) and the floor (x, z). This week you use **all three numbers at once**: **(x, y, z)**. x is across, **y is up (height)**, z is forward. Now you can put a block **anywhere** in space.

---

## 1 · Predict 🔮

Read the steps. Before you imagine it happening, circle or write your answer.

```
set y to 0
repeat 5 times:
    place stone block at (3, y, 3)
    add 1 to y
```

**The middle number y grows by 1 each time. Does this build a tower going up? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
place gold block at (2, 6, 2)
```

**y is 6 and there is nothing below it. Is the gold block high in the air? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The tower should go **up**, so the **middle** number (y) must grow.

```
# clean
set y to 0
repeat 4 times:
    place stone block at (3, y, 3)
    add 1 to y
```

```
# buggy
set z to 0
repeat 4 times:
    place stone block at (3, 0, z)
    add 1 to z
```

**What is wrong? Does the buggy one go up, or forward?**

<div class="write-space short"></div>

**Pair B** — The tower should start **on the ground**, where y is 0.

```
# clean
set y to 0
repeat 4 times:
    place stone block at (2, y, 2)
    add 1 to y
```

```
# buggy
set y to 3
repeat 4 times:
    place stone block at (2, y, 2)
    add 1 to y
```

**What is wrong? Where does the buggy tower start?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The tower should grow **up into the sky**. The middle number must grow. One word is missing. Fill it in using the word bank.

```
set y to 0
repeat 5 times:
    place stone block at (3, y, 3)
    add 1 to ____
```

**Word bank:** `y` · `x` · `z`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build a **tower** that goes up using a loop, then put a gold block floating in the air above it. When you finish, come back here.

Send a photo or video of your tower, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My tower is … blocks tall.
>
> The number that grew was **y**, which means …
>
> My floating block is at ( … , … , … ).

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you show your tower in the world. Talk like you are teaching a friend. Try to use these words: **x**, **y**, **z**, **height**, **up**.

> 1. Show your tower from the bottom to the top.
> 2. Read your loop out loud and say which number grows.
> 3. Point at the floating block and say all three of its numbers.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
