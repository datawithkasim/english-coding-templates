# 🪣 M000 Week 6 — English Worksheet (Intermediate)

**Topic:** Building a Well · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 38 minutes

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
repeat 3 times:
    destroy block down
    move down by 1
```

**What does the agent do, and how deep is the hole?**

<div class="write-space"></div>

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

**What shape does the agent leave on the ground? How many blocks total?**

<div class="write-space"></div>

---

## 2 · Find the Bug 🐛

The goal is written first. Circle the line that breaks it, then explain in one sentence.

**Bug A** — Goal: dig **3 blocks straight down** to make the well hole. After each `destroy`, the agent must step down into the hole.

```
repeat 3 times:
    destroy block down
```

**Which line is missing, and why does that break the dig?**

<div class="write-space short"></div>

**Bug B** — Goal: build the square wall **first**, then dig the hole. Think about where the agent ends up after it digs.

```
repeat 3 times:
    destroy block down
    move down by 1
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

**What is in the wrong order, and what problem does that cause?**

<div class="write-space short"></div>

---

## 3 · Fix the Code ✏️

The agent should build the **4 sides** of a 3×3 square wall around the well. It builds only **one side** — the outer loop is missing.

```
repeat 3 times:
    place block down
    move forward
    turn right
```

> Hint: a square has 4 sides. You need to repeat "3 blocks, then turn" four times.

**Write the fixed code:**

<div class="write-space"></div>

**Why does your fix make a full square?**

<div class="write-space short"></div>

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Build a **well** — a 3×3 square wall on top, and a hole **3 or 4 blocks deep** inside it.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
