# 🎮 M004 Week 1 — English Worksheet (Beginner)

**Topic:** Functions with Parameters & Returns · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week you give a function a **parameter** — a number it uses inside. Call it with different numbers and it builds different things.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(3)
```

**Does the tower become 3 blocks tall? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
define build_tower(height):
    repeat height times:
        place block
        move up
```

**There is no call after the definition. Does anything get built? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The function should be **called** so the tower gets built.

```
# clean
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(3)
```

```
# buggy
define build_tower(height):
    repeat height times:
        place block
        move up
```

**What is wrong? Why does the buggy code build nothing?**

<div class="write-space short"></div>

**Pair B** — The function should use the **parameter** `height`, not a fixed number.

```
# clean
define build_tower(height):
    repeat height times:
        place block
        move up
```

```
# buggy
define build_tower(height):
    repeat 3 times:
        place block
        move up
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The call should tell the function how tall to build. One thing is missing. Fill it in using the word bank.

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(____)
```

**Word bank:** `5` · `repeat` · `define`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Write one tower function with a `height` parameter and call it two times with different numbers. When you finish, come back here.

Send a photo or video of your towers, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My function's parameter was …
>
> When I called it with a different number, …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your code builds the towers. Talk like you are teaching a friend. Try to use these words: **function**, **parameter**, **call**.

> 1. Show your function definition, then run your code.
> 2. Show two towers built with different numbers.
> 3. Say in your own words what a **parameter** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
