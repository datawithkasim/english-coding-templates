# 💎 M001 Week 8 — English Worksheet

**Topic:** Diamond Structure (Final Project) · **Course:** Pyramid Problems · **Time:** about 60 minutes

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
set max_size to 9

# Bottom half
set size to 1
while size <= max_size:
    [build one size × size square layer]
    move up by 1
    set size to size + 2
```

**What shape is the bottom half? List the sizes from bottom to top.**

<div class="write-space"></div>

```
set max_size to 9

# Top half
set size to max_size - 2
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**What shape is the top half? List the sizes from bottom to top.**

<div class="write-space"></div>

```
set max_size to 9

# Bottom half (1 → 9)
[grow from 1 up to 9]
# Top half (7 → 1)
[shrink from 7 down to 1]
```

**Put together, what does the agent build? Why does the top half start at 7 (not 9)?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block below is broken. Read what it should do, rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to build a diamond: bottom half grows 1 → 9, top half shrinks 7 → 1. The two halves should meet at the widest layer.

```
set max_size to 9

set size to 1
while size <= max_size:
    [build layer]
    move up by 1
    set size to size + 2

set size to max_size
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**Hint:** the top half repeats the widest layer. Fix it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent is supposed to use **one variable** (`max_size`) to control the entire diamond size.

```
# Bottom half
set size to 1
while size <= 9:
    [build layer]
    move up by 1
    set size to size + 2

# Top half
set size to 7
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**Hint:** there are two hard-coded numbers (9, 7). Rewrite so changing `max_size` changes both.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The diamond's two halves should be **vertically stacked** (top half sits on the widest layer of the bottom half).

```
set max_size to 9

set size to 1
while size <= max_size:
    [build layer]
    set size to size + 2

set size to max_size - 2
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**Hint:** the bottom half never moves up. Fix it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Build your diamond using **one `max_size` variable**. Try `max_size = 9` first, then try a different value (e.g. 5 or 11) and see how it changes. When you finish, come back here.

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
