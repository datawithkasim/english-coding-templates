# 🎮 M004 Week 2 — English Worksheet

**Topic:** Chat Commands · **Course:** Functions & Games · **Time:** about 45 minutes

This week you type a word in chat and your code runs. A **chat command** can take a number — `tower 5` builds a 5-block tower.

---

## 1 · Predict 🔮

Before you imagine the agent doing it, write what you think will happen.

```
on chat command "bridge":
    repeat 6 times:
        place block
        move forward
```

**You type `bridge` in chat. What does the agent do? What if you type nothing?**

<div class="write-space"></div>

```
on chat command "tower" with number n:
    repeat n times:
        place block
        move up
```

**You type `tower 4` in chat. How tall is the tower? What about `tower 8`?**

<div class="write-space"></div>

```
define build_tower(height):
    repeat height times:
        place block
        move up

on chat command "tower" with number n:
    build_tower(n)
```

**The chat command passes `n` into the function. You type `tower 3` — what happens, step by step?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — Typing `bridge` in chat should build a bridge. But when you type `bridge`, **nothing runs**.

```
on chat command "brige":
    repeat 6 times:
        place block
        move forward
```

**Hint:** read the command name very slowly, letter by letter.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — `tower 7` should build a tower 7 blocks tall. The command receives the number, but the tower is always 3 tall.

```
define build_tower(height):
    repeat height times:
        place block
        move up

on chat command "tower" with number n:
    build_tower(3)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — One command should build a bridge and another should build a tower. Right now they have the **same name**, so typing `build` is confusing — only one of them can win.

```
on chat command "build":
    repeat 6 times:
        place block
        move forward

on chat command "build":
    repeat 4 times:
        place block
        move up
```

**Hint:** give each command its own name.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Make at least **two** chat commands: one simple command, and one command with a number that passes the number into a function. When you finish, come back here.

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
