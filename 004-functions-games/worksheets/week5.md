# 🎮 M004 Week 5 — English Worksheet

**Topic:** Your Function Library — Reusable Building Blocks · **Course:** Functions & Games · **Time:** about 45 minutes

This week you collect your best functions into a **library** — a set of reusable building blocks like `build_wall`, `build_tower`, and `clear_area`. Big builds become easy when small functions do the work.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the build happening, write what you think will happen.

```
function build_wall(length):
    repeat length times:
        place stone block
        move forward 1

build_wall(5)
build_wall(3)
```

**The function is called twice with different numbers. How many stone blocks get placed in total? Which call builds the longer wall?**

<div class="write-space"></div>

```
function build_tower(height):
    repeat height times:
        place stone block
        move up 1

function build_house():
    build_wall(4)
    build_tower(3)

build_house()
```

**`build_house` calls two helper functions. What gets built, and in what order?**

<div class="write-space"></div>

```
function clear_area(size):
    repeat size times:
        repeat size times:
            replace block with air
            move forward 1
        move right 1

clear_area(4)
build_wall(4)
```

**What happens first — clearing or building? Why does the order of these two calls matter?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The library should have **two different** functions: a stone wall and a glass wall. Right now both functions have the **same name**, so the computer gets confused about which one to use.

```
function build_wall(length):
    repeat length times:
        place stone block
        move forward 1

function build_wall(length):
    repeat length times:
        place glass block
        move forward 1

build_wall(4)
```

**Hint:** every function in your library needs its own clear name.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — `build_house` is supposed to build four walls **and a door**. The door function exists, but the house never gets a door.

```
function build_door():
    replace block with air
    replace block above with air

function build_house():
    build_wall(4)
    build_wall(4)
    build_wall(4)
    build_wall(4)

build_house()
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `build_tower(height)` should build a tower **as tall as the number you give it**. But `build_tower(10)` keeps making a tiny tower.

```
function build_tower(height):
    repeat 3 times:
        place stone block
        move up 1

build_tower(10)
```

**Hint:** the parameter `height` is never used inside the function.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build something using your own function library — at least one function should call another function. When you finish, come back here.

Send a photo or video of your build, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made a function called …
>
> I reused it when …
>
> One function called another function when …
>
> I chose the name … because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your code builds. Talk through it like you are teaching someone who has never seen it. Try to use these words: **function**, **parameter**, **call**, **reuse**, **name**.

> 1. Show your function library before you run anything.
> 2. Read each function name out loud and say what it builds.
> 3. Show one place where a function **calls another function**.
> 4. Say in your own words why reusing functions is better than copying code.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
