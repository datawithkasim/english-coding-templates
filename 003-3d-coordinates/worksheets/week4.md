# 🧊 M003 Week 4 — English Worksheet

**Topic:** The Ground Plane (x, z) · **Course:** 3D Coordinates · **Time:** about 45 minutes

For three weeks you drew standing up on a **wall** with (x, y). This week you look **down** at the **floor**, where the two numbers are **(x, z)**: x is how far **across**, z is how far **forward**. A nested loop fills a whole floor — x runs across each row, z steps forward to the next row.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

```
place gold block at (3, 0)
place gold block at (3, 5)
```

**On the floor these are (x, z). The two blocks share the same x. Are they close together or far apart? Which number changed, and what does it mean?**

<div class="write-space"></div>

```
set z to 0
repeat 5 times:
    place stone block at (2, z)
    add 1 to z
```

**Which way does this line run — across or forward? How long is it? Which number stays the same?**

<div class="write-space"></div>

```
set z to 0
repeat 3 times:
    set x to 0
    repeat 4 times:
        place stone block at (x, z)
        add 1 to x
    add 1 to z
```

**The inner loop runs x across, the outer loop steps z forward. What shape covers the floor — a line or a rectangle? How wide and how deep?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The path should run **forward** at x = 2, from (2, 0) to (2, 4). x should stay 2. Right now it runs across instead.

```
set n to 0
repeat 5 times:
    place stone block at (n, 2)
    add 1 to n
```

**Hint:** look at which slot n is in — the x slot (across) or the z slot (forward).

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should fill a floor **5 across and 3 forward**. Right now each row lands on top of the last one, so you get a thin line instead of a rectangle.

```
set z to 0
repeat 3 times:
    set x to 0
    repeat 5 times:
        place stone block at (x, z)
        add 1 to x
```

**Hint:** after each row, the floor needs to step forward to the next z.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The floor block should land at **(4, 6)** — 4 across, 6 forward. Right now it lands somewhere else.

```
place gold block at (6, 4)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Fill a **floor pad** with a nested loop, then lay a **path** across it that runs forward (z grows) or across (x grows). When you finish, come back here.

Send a photo or video of your floor, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My floor pad is … across and … forward.
>
> The inner loop grew the number … and the outer loop grew the number …
>
> My path runs … because it grows the number …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you look down at your floor. Talk through it like you are teaching someone who only knew the wall before. Try to use these words: **floor**, **x**, **z**, **forward**, **across**.

> 1. Show the block at (0, 0) where the floor begins.
> 2. Show your code and say which loop runs **across** and which steps **forward**.
> 3. Walk along your path and say which number is growing as you move.
> 4. Say in your own words why the floor uses **x and z**, not x and y.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
