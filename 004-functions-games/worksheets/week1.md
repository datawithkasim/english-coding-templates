# 🎮 M004 Week 1 — English Worksheet

**Topic:** Functions with Parameters & Returns · **Course:** Functions & Games · **Time:** about 45 minutes

This week you give a function a **parameter** — a number it uses inside, so calling it with different numbers builds different things. A function can also **give back** an answer.

---

## 1 · Predict 🔮

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

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

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

## 3 · Show Your Work 📸🎥

Switch to your homework world. Build a tower village: write **one** function with a `height` parameter, then call it **three** times with different numbers.

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
