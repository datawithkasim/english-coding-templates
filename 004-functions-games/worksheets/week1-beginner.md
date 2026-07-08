# 🎮 M004 Week 1 — English Worksheet (Beginner)

**Topic:** Functions with Parameters & Returns · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week you give a function a **parameter** — a number it uses inside.

---

## 1 · Predict 🔮

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(3)
```

**Is the tower 3 blocks tall? Circle one:** yes · no

**Why? Circle one:** repeat runs 3 times · repeat runs 1 time

```
define build_tower(height):
    repeat height times:
        place block
        move up
```

**No call after the definition. Does anything build? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

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

**What is wrong? Circle one:** no call line · wrong block

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

**What is wrong? Circle one:** uses `3` not `height` · missing call

---

## 3 · Fill the Gap ✏️

One word is missing.

```
define build_tower(height):
    repeat height times:
        place block
        move up

build_tower(____)
```

**Fill the gap. Circle one:** `5` · `repeat` · `define`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Write one tower function with a `height` parameter and call it two times with different numbers.

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
