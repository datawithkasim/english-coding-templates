# 🔻 M001 Week 6 — English Worksheet

**Topic:** Inverted Pyramid · **Course:** Pyramid Problems · **Time:** about 45 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
set size to 1
while size <= 9:
    [build one size × size square layer]
    move up by 1
    set size to size + 2
```

**Each layer gets bigger or smaller? Where is the widest layer — bottom or top?**

<div class="write-space"></div>

```
set size to 1
while size <= 9:
    [build one size × size square layer]
    move up by 1
    set size to size + 2
```

**List the sizes from bottom to top. How many layers in total?**

<div class="write-space"></div>

```
set size to 1
while size <= 5:
    [build one size × size square layer]
    move up by 1
    set size to size + 2
```

**How is this different from the code above? How does it look?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to build an **inverted pyramid**: the smallest layer at the bottom, the biggest at the top.

```
set size to 9
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent is supposed to grow the pyramid from 1 up to 9. Each layer must be **2 blocks longer** than the one below.

```
set size to 1
while size <= 9:
    [build one size × size square layer]
    move up by 1
    set size to size + 1
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Each new layer should sit **on top** of the one below.

```
set size to 1
while size <= 9:
    [build one size × size square layer]
    set size to size + 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build an inverted pyramid that grows from **size 1 up to size 9**. Look from the side and check the shape is right. When you finish, come back here.

Send a photo or video of your pyramid, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> The top layer is … blocks long.
>
> Each new layer grows by … because …
>
> The pyramid has … layers in total.
>
> The hardest part was …
>
> Compared to last week's normal pyramid, this one is different because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your inverted pyramid. Talk through it like you are teaching someone who has never seen it. Try to use these words: **inverted**, **layer**, **size**, **grow**, **stack**.

> 1. Walk around the pyramid and show that the top is the widest part.
> 2. Read your `while` loop out loud and say how the size changes each time.
> 3. Show one bug you hit and how you fixed it.
> 4. Compare this pyramid to last week's normal pyramid.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
