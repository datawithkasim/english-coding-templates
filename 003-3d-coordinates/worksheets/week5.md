# 🧊 M003 Week 5 — English Worksheet

**Topic:** Into 3D (x, y, z) · **Course:** 3D Coordinates · **Time:** about 45 minutes

You know the wall (x, y) and the floor (x, z). This week you put them together and use **all three numbers at once**: **(x, y, z)** — x across, **y up (height)**, z forward. With three numbers you can place a block **anywhere** in space, and build **up**.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

```
set y to 0
repeat 5 times:
    place stone block at (3, y, 3)
    add 1 to y
```

**Which way does this build — across the ground or up into the sky? How tall is it? Which two numbers stay the same?**

<div class="write-space"></div>

```
place gold block at (2, 6, 2)
```

**y is 6 and there are no blocks below it. Where does the gold block sit — on the ground or in the air?**

<div class="write-space"></div>

```
place red block at (0, 0, 0)
place red block at (0, 4, 0)
```

**Both blocks share the same x and z. What is different about them? If you stand next to the first block and look up, what do you see?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should build a **tower going up** at x = 3, z = 3. Right now it makes a flat line on the ground instead.

```
set n to 0
repeat 4 times:
    place stone block at (3, 0, n)
    add 1 to n
```

**Hint:** which slot is n in? The height slot is the **middle** one.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should build a tower **up from the ground** at (2, 0, 2). Right now it builds **down into the ground**.

```
set y to 0
repeat 4 times:
    place stone block at (2, y, 2)
    take 1 from y
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should make a line of stone blocks sitting **on the ground**, where y = 0. Right now the whole line **floats in the air**.

```
set x to 0
repeat 4 times:
    place stone block at (x, 3, 0)
    add 1 to x
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a **tower** that goes up using a loop, then place a **floating gold block** in the air above it, like a beacon. When you finish, come back here.

Send a photo or video of your tower, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My tower is … blocks tall because my loop …
>
> The number that grew was **y**, which means …
>
> My floating gold block is at ( … , … , … ).
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your tower in the world. Talk through it like you are teaching someone who has only seen flat pictures before. Try to use these words: **x**, **y**, **z**, **height**, **coordinate**.

> 1. Show your tower from the bottom to the top.
> 2. Show your code and say which number grows in the loop.
> 3. Point at the floating gold block and say its full coordinate — all three numbers in order.
> 4. Say in your own words what each of **x**, **y**, and **z** means.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
