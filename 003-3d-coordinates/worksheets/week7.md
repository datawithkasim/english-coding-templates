# 🧊 M003 Week 7 — English Worksheet

**Topic:** Voxel Statue — Building Layer by Layer · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week you build a statue **one layer at a time**. Each layer is a small pixel-art grid, and the layers stack **upward along y**: layer 1 at height 0, layer 2 at height 1, and so on. In the plans below, `#` means stone and `.` means air.

---

## 1 · Predict 🔮

Read each plan and set of steps. Before you imagine it happening, write what you think you will see.

```
layer 1:   # # #      layer 2:   . # .
           # # #                 . # .
           # # #                 . # .

build layer 1 at height 0
build layer 2 at height 1
```

**Layer 1 is a full 3×3 square. Layer 2 is only the middle row. What does the statue look like from the side — wide at the bottom or wide at the top?**

<div class="write-space"></div>

```
build layer 2 at height 0
build layer 1 at height 1
```

**Same two layers, but the order is swapped. What does the statue look like now? Does it look like it could fall over?**

<div class="write-space"></div>

```
set h to 0
repeat 4 times:
    build layer 2 at height h
    add 1 to h
```

**Layer 2 (the thin middle strip) is built 4 times, each time one block higher. What shape do you get?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The statue plan says: **feet** layer at the bottom, **body** layer in the middle, **head** layer on top. Right now the statue is upside down.

```
build head layer at height 0
build body layer at height 1
build feet layer at height 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Every layer should start at the **same corner**, x = 0 and z = 0, so the statue stands straight. Right now the statue leans to one side.

```
build layer 1 at (0, 0, 0)
build layer 2 at (1, 1, 0)
build layer 3 at (0, 2, 0)
```

**Hint:** compare the **x** number on each line. Only the **y** number should change.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The plan has exactly **three** layers: 1, 2, 3. Right now the statue is too tall and has the wrong middle.

```
build layer 1 at height 0
build layer 2 at height 1
build layer 2 at height 2
build layer 3 at height 3
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Draw a **layer plan** for a small statue — at least 3 layers, each one a small grid — then build it layer by layer, going up one height at a time. When you finish, come back here.

Send a photo or video of your statue, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I planned my layers by …
>
> My statue has … layers, and layer 1 is …
>
> Each layer went one higher because …
>
> I kept every layer at the same corner so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your statue in the world. Talk through it like you are teaching someone who has never built layer by layer. Try to use these words: **layer**, **height**, **stack**, **plan**, **grid**.

> 1. Show your layer plan on paper, then show the finished statue.
> 2. Point at the bottom layer and say its height, then point at the top layer and say its height.
> 3. Show how two layers are different shapes but sit on the same corner.
> 4. Say in your own words why the **order** of the layers matters.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
