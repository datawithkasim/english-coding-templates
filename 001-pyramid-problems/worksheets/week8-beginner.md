# 💎 M001 Week 8 — English Worksheet (Beginner)

**Topic:** Diamond Structure (Final Project) · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 45 minutes

A diamond is two pyramids: the **bottom half grows** (1 → 3 → 5) and the **top half shrinks** (3 → 1).

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
# Bottom half
set size to 1
while size <= 5:
    [build layer]
    move up by 1
    set size to size + 2
```

**The bottom half grows or shrinks? Circle one:** grows · shrinks

**Write the layer sizes in order:**

<div class="write-space short"></div>

```
# Top half
set size to 3
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**The top half grows or shrinks? Circle one:** grows · shrinks

**Why does it start at 3 and not 5? (Hint: the size-5 layer is already built.)**

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The top half should start at **3**, so the widest layer is not built twice.

```
# clean
set size to 3
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

```
# buggy
set size to 5
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**What is wrong? Which layer appears twice?**

<div class="write-space short"></div>

**Pair B** — The bottom half must **move up** after each layer.

```
# clean
while size <= 5:
    [build layer]
    move up by 1
    set size to size + 2
```

```
# buggy
while size <= 5:
    [build layer]
    set size to size + 2
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

Here is the diamond skeleton. One starting number is missing. Fill it in using the word bank.

```
# Bottom half (grows 1 → 3 → 5)
set size to 1
while size <= 5:
    [build layer]
    move up by 1
    set size to size + 2

# Top half (shrinks 3 → 1)
set size to ____
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**Word bank:** `3` · `5` · `1`

**Write the missing number:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now build your **final project**: a diamond with a bottom half that grows **1 → 3 → 5** and a top half that shrinks **3 → 1**. When you finish, come back here.

Send a photo or video of your diamond, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> First, I built the bottom half by …
>
> The widest layer is … blocks long.
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and walk the camera around your diamond. Talk like you are teaching a friend. Try to use these words: **diamond**, **bottom half**, **top half**, **widest**.

> 1. Walk around the diamond and show all 4 sides.
> 2. Say the layer sizes from bottom to top.
> 3. Say what you learned in this course.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk. This is the **last week** of Pyramid Problems — well done!
