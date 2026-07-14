# 🎮 M004 Week 7 — English Worksheet (Beginner)

**Topic:** Auto-Building Spaces — Loops + Functions + Chat Commands · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week one chat command builds a **whole space by itself**. A loop repeats a room piece, and the **number** you type decides how big it grows.

---

## 1 · Predict 🔮

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 6
```

**You type `dungeon 3`. Does it build 3 rooms? Circle one:** yes · no

**Why? Circle one:** repeat runs `rooms`, which is 3 · repeat runs 1 time

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 6
```

**You type `dungeon 1`. Does it build 3 rooms? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

**Pair A** — The rooms should sit in a row, not on top of each other.

```
# clean
repeat rooms times:
    build_room()
    move forward 6
```

```
# buggy
repeat rooms times:
    build_room()
```

**What is wrong? Circle one:** no move, rooms stack in one spot · rooms spread out

**Pair B** — The number you type should decide how many rooms get built.

```
# clean
repeat rooms times:
    build_room()
    move forward 6
```

```
# buggy
repeat 1 times:
    build_room()
    move forward 6
```

**What is wrong? Circle one:** uses `1` not `rooms` · uses `rooms` not `1`

---

## 3 · Fill the Gap ✏️

One word is missing.

```
on chat command "dungeon" with number rooms:
    repeat ____ times:
        build_room()
        move forward 6
```

**Fill the gap. Circle one:** `rooms` · `dungeon` · `forward`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Make a chat command with a number that auto-builds a space.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
