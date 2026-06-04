# 🔺 M001 Week 5 — English Worksheet

**Topic:** First Pyramid · **Course:** Pyramid Problems · **Time:** about 45 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
set size to 9
repeat size times:
    repeat size times:
        place block down
        move forward
    [turn and walk back to start of next row]
```

**This builds the **bottom** layer of the pyramid. How long is each side?**

<div class="write-space"></div>

```
set size to 9
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**Why does the pyramid shrink by 2 each layer instead of 1?**

<div class="write-space"></div>

```
set size to 9
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**How many layers does the pyramid have? List the sizes from bottom to top.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to build a pyramid where each layer is **2 blocks smaller** than the one below.

```
set size to 9
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 1
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Each new layer must sit **on top** of the one below.

```
set size to 9
while size > 0:
    [build one size × size square layer]
    set size to size - 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The agent is supposed to **stop** building once the layer is gone (size 0 or smaller).

```
set size to 9
while size > -10:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a pyramid **starting at size 7** (so the layers go 7 → 5 → 3 → 1). Then try once more with a **different material** — sandstone, gold, or your choice. When you finish, come back here.

Send a photo or video of your pyramid, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> The bottom layer is … blocks long.
>
> Each new layer gets smaller by … because …
>
> The pyramid has … layers in total.
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your pyramid. Talk through it like you are teaching someone who has never seen it. Try to use these words: **pyramid**, **layer**, **size**, **shrink**, **stack**.

> 1. Walk around the pyramid and show all 4 sides.
> 2. Read your `while` loop out loud and say what each part does.
> 3. Show one bug you hit and how you fixed it.
> 4. Say how many layers your pyramid has and how the size changes each time.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
