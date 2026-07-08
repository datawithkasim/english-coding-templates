# 🎮 M004 Week 5 — English Worksheet (Beginner)

**Topic:** Your Function Library — Reusable Building Blocks · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week you collect your best functions into a **library** — reusable building blocks like `build_wall` and `build_tower`.

---

## 1 · Predict 🔮

```
function build_wall(length):
    repeat length times:
        place stone block
        move forward 1

build_wall(3)
```

**Does this build a wall 3 blocks long? Circle one:** yes · no

**Why? Circle one:** `build_wall(3)` is called · there is no call

```
function build_tower(height):
    repeat height times:
        place stone block
        move up 1
```

**No call line at the bottom. Does the tower get built? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

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

**What is wrong? Circle one:** two functions share a name · two different names

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

**What is wrong? Circle one:** uses `3` not `height` · uses `height` not `3`

---

## 3 · Fill the Gap ✏️

One word is missing.

```
function build_tower(height):
    repeat ____ times:
        place stone block
        move up 1
```

**Fill the gap. Circle one:** `height` · `tower` · `block`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Build something using your own functions.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Say these out loud, filling in the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
