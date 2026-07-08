# 🔻 M001 Week 6 — English Worksheet (Beginner)

**Topic:** Inverted Pyramid · **Course:** Pyramid Problems · **Level:** Beginner · **Time:** about 30 minutes

An **inverted** pyramid is upside down: the **smallest** layer is at the bottom and the **biggest** is at the top.

---

## 1 · Predict 🔮

Read the steps. Circle your answer.

```
set size to 1
while size <= 5:
    [build one size × size square layer]
    move up by 1
    set size to size + 2
```

**Each new layer gets … Circle one:** bigger · smaller

**Where is the widest layer? Circle one:** bottom · top

```
set size to 1
while size <= 5:
    [build one size × size square layer]
    move up by 1
    set size to size + 2
```

**The sizes go 1, then …, then … Circle one:** 1 · 3 · 5 → 1 · 2 · 3

---

## 2 · Find the Difference 🐛

Clean steps first, then a buggy version. Circle the bug.

**Pair A** — The pyramid should be **inverted**: it starts small and grows.

```
# clean
set size to 1
while size <= 5:
    [build layer]
    move up by 1
    set size to size + 2
```

```
# buggy
set size to 5
while size > 0:
    [build layer]
    move up by 1
    set size to size - 2
```

**What is wrong? Circle one:** it builds a normal pyramid (wide bottom) · it builds an inverted pyramid · it builds a flat floor

**Pair B** — Each layer must sit **on top** of the one below.

```
# clean
while size <= 5:
    [build layer]
    move up by 1
    set size to size + 2
```

```
# buggy
while size <= 5:
    [build layer]
    set size to size + 2
```

**What is wrong? Circle one:** it never moves up · it moves up too far · it turns the wrong way

---

## 3 · Fill the Gap ✏️

The inverted pyramid should **grow** by 2 each layer. Fill the missing line.

```
set size to 1
while size <= 5:
    [build layer]
    move up by 1
    ____________
```

**Missing line? Circle one:** set size to size + 2 · set size to size - 2 · turn right

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Build an inverted pyramid that grows from **size 1 up to size 5**, then check the shape from the side.

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
