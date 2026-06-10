# 🎮 M004 Week 1 — English Worksheet

**Topic:** Functions with Parameters & Returns · **Course:** Functions & Games · **Time:** about 45 minutes

This week you give a function a **parameter** — a number it uses inside. Call the same function with different numbers and it builds different things. A function can also **give back** an answer.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(3)
```

**The function uses `height` inside the repeat. How many blocks tall is this tower?**

<div class="write-space"></div>

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(2)
build_tower(5)
```

**The same function is called twice with different numbers. What gets built? Are the two towers the same?**

<div class="write-space"></div>

```
define count_steps(distance):
    give back distance + 2

steps = count_steps(4)
say steps
```

**This function gives an answer back instead of building. What number does the agent say?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The code should build a tower 4 blocks tall. But when you run it, **nothing happens at all**.

```
define build_tower(height):
    repeat height times:
        place block
        move up
```

**Hint:** defining a function only **teaches** it. Something is missing after the definition.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The function should build a tower as tall as the number you give it. But `build_tower(7)` and `build_tower(2)` both build the **same** tower.

```
define build_tower(height):
    repeat 3 times:
        place block
        move up

build_tower(7)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The function needs a number to know how tall to build. But the call forgot to give it one, so the code breaks.

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower()
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a tower village: write **one** function with a `height` parameter, then call it at least **three** times with different numbers. When you finish, come back here.

Send a photo or video of your towers, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> My function's parameter was …
>
> When I called it with a different number, …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your code builds the towers. Talk through it like you are teaching someone who has never seen it. Try to use these words: **function**, **parameter**, **call**, **give back**, **repeat**.

> 1. Show your function definition and read the line with the **parameter** out loud.
> 2. Run a call with a small number, then a call with a big number, and show the difference.
> 3. Point at one tower and say which **call** built it.
> 4. Say in your own words what a **parameter** is.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
