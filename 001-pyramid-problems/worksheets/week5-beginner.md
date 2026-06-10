# 🔺 M001 Week 5 — English Worksheet (Beginner)

**Topic:** First Pyramid · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 30 minutes

A pyramid is square layers stacked up. Each layer is **smaller** than the one below it.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
set size to 5
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**The layers go 5, then …, then … Circle one:** 5 · 4 · 3 → 5 · 3 · 1

**Where is the biggest layer — bottom or top?**

<div class="write-space short"></div>

```
set size to 5
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**How many layers does this pyramid have? Circle one:** 2 · 3 · 5

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — Each new layer must sit **on top** of the one below.

```
# clean
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

```
# buggy
while size > 0:
    [build layer]
    set size to size - 2
```

**What is wrong? Where do all the layers land?**

<div class="write-space short"></div>

**Pair B** — Each layer should be **2 smaller** than the one below.

```
# clean
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

```
# buggy
while size > 0:
    [build layer]
    move up by 1
    set size to size - 1
```

**What is wrong? Does the buggy pyramid still work, or does it look different?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The pyramid should shrink and stop when the size reaches 0. One line is missing. Fill it in using the word bank.

```
set size to 5
while size > 0:
    [build layer]
    move up by 1
    ____________
```

**Word bank:** `set size to size - 2` · `set size to size + 2` · `move forward`

**Write the missing line:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build a pyramid **starting at size 5** (so the layers go 5 → 3 → 1). When you finish, come back here.

Send a photo or video of your pyramid, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The bottom layer is … blocks long.
>
> Each new layer gets smaller by …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and walk the camera around your pyramid. Talk like you are teaching a friend. Try to use these words: **pyramid**, **layer**, **size**, **shrink**.

> 1. Walk around the pyramid and show all 4 sides.
> 2. Say the sizes of the layers from bottom to top.
> 3. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
