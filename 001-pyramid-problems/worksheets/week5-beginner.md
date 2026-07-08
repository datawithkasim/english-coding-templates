# 🔺 M001 Week 5 — English Worksheet (Beginner)

**Topic:** First Pyramid · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 30 minutes

The agent walks around a **square** and drops blocks as it walks. Stack squares that get **smaller** and you get a pyramid.

---

## 1 · Predict 🔮

Read the steps. Circle your answer.

```
set f to 4
place on move ON
repeat 4 times:
    move forward by f
    turn left
```

**What shape does the agent draw? Circle one:** line · square · circle

**How many sides does it draw? Circle one:** 1 · 3 · 4

```
set f to 5
repeat 3 times:
    [draw one square]
    move up by 1
    change f by -2
```

**The sides go 5, then …, then … Circle one:** 5 · 3 · 1 → 5 · 4 · 3

**Which square is biggest? Circle one:** bottom · top

---

## 2 · Find the Difference 🐛

Clean steps first, then a buggy version. Circle the bug.

**Pair A** — Should draw a closed **square**.

```
# clean
place on move ON
repeat 4 times:
    move forward by f
    turn left
```

```
# buggy
place on move ON
repeat 4 times:
    move forward by f
```

**What is wrong? Circle one:** it draws a straight line · it draws a square · it draws a circle

**Pair B** — Each new layer should be **2 smaller** than the one below.

```
# clean
[draw one square]
move up by 1
change f by -2
```

```
# buggy
[draw one square]
move up by 1
change f by 2
```

**What is wrong? The buggy tower gets… Circle one:** bigger going up · smaller going up

---

## 3 · Fill the Gap ✏️

Each square must sit one block **higher** than the last. Fill the missing line.

```
set f to 5
repeat 3 times:
    [draw one square]
    ____________
    change f by -2
```

**Missing line? Circle one:** move up by 1 · move down by 1 · turn left

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Run `pyra` to build a pyramid — if it gets stuck, `1` turns left, `r` turns right, `r1` brings it back.

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
