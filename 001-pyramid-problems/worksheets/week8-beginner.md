# 💎 M001 Week 8 — English Worksheet (Beginner)

**Topic:** Diamond Structure (Final Project) · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 45 minutes

A diamond is two pyramids: the **bottom half grows** (1 → 3 → 5) and the **top half shrinks** (3 → 1).

---

## 1 · Predict 🔮

Read the steps. Circle your answer.

```
# Bottom half
set size to 1
while size <= 5:
    [build layer]
    move up by 1
    set size to size + 2
```

**The bottom half grows or shrinks? Circle one:** grows · shrinks

**Layer sizes in order? Circle one:** 1 · 3 · 5 → 5 · 3 · 1

```
# Top half
set size to 3
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**The top half grows or shrinks? Circle one:** grows · shrinks

**Why start at 3, not 5? Circle one:** the size-5 layer is already built · 5 is too big to build · the agent cannot count to 5

---

## 2 · Find the Difference 🐛

Clean steps first, then a buggy version. Circle the bug.

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

**What is wrong? Which layer is built twice? Circle one:** the size-5 layer · the size-3 layer · the size-1 layer

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

**What is wrong? Circle one:** it never moves up · it moves up too far · it turns right

---

## 3 · Fill the Gap ✏️

Here is the diamond skeleton. Fill the missing number.

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

**Missing number? Circle one:** 3 · 5 · 1

---

## 4 · Show Your Work 📸🎥

Now build your **final project**: a diamond with a bottom half that grows **1 → 3 → 5** and a top half that shrinks **3 → 1**. When you finish, come back here.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
