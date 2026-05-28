# 💎 M001 Week 8 — English Worksheet

**Topic:** Diamond Structure (Final Project) · **Course:** Pyramid Problems · **Time:** about 60 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build your diamond using **one `max_size` variable**. Try `max_size = 9` first, then try a different value (e.g. 5 or 11) and see how it changes. When you finish, come back here.

Send a photo or video of your diamond, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I built the bottom half by …
>
> Then I built the top half by …
>
> The widest layer is … blocks long.
>
> The total height is … blocks.
>
> When I changed `max_size`, what happened was …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your diamond. Talk through it like you are teaching someone who has never seen it. Try to use these words: **diamond**, **bottom half**, **top half**, **widest**, **max_size**.

> 1. Walk around the diamond and show all 4 sides.
> 2. Read the bottom-half loop and the top-half loop out loud and say what each one does.
> 3. Show one bug you hit and how you fixed it.
> 4. Say what you learned across the 8 weeks of this course.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk. This is the **last week** of Pyramid Problems — well done!
