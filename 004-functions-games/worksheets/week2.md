# 🎮 M004 Week 2 — English Worksheet

**Topic:** Chat Commands · **Course:** Functions & Games · **Time:** about 45 minutes

This week you type a word in chat and your code runs. A **chat command** can even take a number with it — so `tower 5` builds a 5-block tower using your function from last week.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Make at least **two** chat commands: one simple command, and one command with a number that passes the number into a function. When you finish, come back here.

Send a photo or video of your commands running, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> When I typed my command in chat, …
>
> My command with a number was …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you type your commands and the code runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **chat command**, **number**, **pass**, **function**, **call**.

> 1. Show the chat box, type your first command, and show what happens.
> 2. Type your number command with a **small** number, then a **big** number, and show the difference.
> 3. Point at the line where the number gets **passed** into the function.
> 4. Say in your own words what a **chat command** does.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
