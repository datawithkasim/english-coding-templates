# 🎮 M004 Week 7 — English Worksheet

**Topic:** Auto-Building Spaces — Loops + Functions + Chat Commands · **Course:** Functions & Games · **Time:** about 45 minutes

This week one chat command builds a **whole space by itself**. A loop repeats a room piece, a function builds each piece, and the **number argument** decides how big it grows.

---

## 1 · Predict 🔮

Before you imagine the build happening, write what you think will happen.

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 6
```

**You type `dungeon 3` in chat. How many rooms get built? What does `move forward 6` do between rooms?**

<div class="write-space"></div>

```
function build_room():
    build_wall(5)
    build_wall(5)
    build_wall(5)
    build_wall(5)

on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 6
```

**`build_room` reuses `build_wall` four times. You type `dungeon 2` — how many walls get built in total?**

<div class="write-space"></div>

```
on chat command "towers" with number count:
    repeat count times:
        build_tower(random number from 3 to 8)
        move forward 4
```

**You type `towers 5`. Are all five towers the same height? Why does the row of towers feel random?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — `dungeon 4` should build four rooms in a row. Right now all four rooms get built **in the same spot**, so it looks like only one room.

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
```

**Hint:** after each room, the builder needs to move before building the next one.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The number you type should decide how many rooms get built. But `dungeon 5` and `dungeon 1` both build just **one** room.

```
on chat command "dungeon" with number rooms:
    repeat 1 times:
        build_room()
        move forward 6
```

**Hint:** the argument `rooms` is never used.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Each room is **6 blocks long**. The rooms should sit side by side, but every new room breaks the back wall of the room before it.

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 5
```

**Hint:** compare the room length with the move distance.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Make a chat command with a number argument that auto-builds a space — a loop should repeat a room piece. When you finish, come back here.

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
