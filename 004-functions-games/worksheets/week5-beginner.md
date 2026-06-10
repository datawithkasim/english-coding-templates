# 🎮 M004 Week 5 — English Worksheet (Beginner)

**Topic:** Your Function Library — Reusable Building Blocks · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week you collect your best functions into a **library** — reusable building blocks like `build_wall` and `build_tower`. Big builds become easy when small functions do the work.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the build happening, circle or write your answer.

```
function build_wall(length):
    repeat length times:
        place stone block
        move forward 1

build_wall(3)
```

**Does this build a wall 3 blocks long? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
function build_tower(height):
    repeat height times:
        place stone block
        move up 1
```

**There is no call line at the bottom. Does the tower get built? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The library should have **two different** functions with two different names.

```
# clean
function build_wall(length):
    place stone blocks

function build_glass_wall(length):
    place glass blocks
```

```
# buggy
function build_wall(length):
    place stone blocks

function build_wall(length):
    place glass blocks
```

**What is wrong? Why does the computer get confused?**

<div class="write-space short"></div>

**Pair B** — The tower should be **as tall as the number you give it**.

```
# clean
function build_tower(height):
    repeat height times:
        place stone block
        move up 1
```

```
# buggy
function build_tower(height):
    repeat 3 times:
        place stone block
        move up 1
```

**What is wrong? What happens when you call `build_tower(10)`?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The tower should be as tall as the number you give it. One word is missing. Fill it in using the word bank.

```
function build_tower(height):
    repeat ____ times:
        place stone block
        move up 1
```

**Word bank:** `height` · `tower` · `block`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build something using your own functions. When you finish, come back here.

Send a photo or video of your build, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I made a function called …
>
> I reused it when …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your code builds. Talk like you are teaching a friend. Try to use these words: **function**, **call**, **reuse**.

> 1. Show your functions before you run anything.
> 2. Read one function name out loud and say what it builds.
> 3. Say in your own words why reusing a function is better than copying code.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
