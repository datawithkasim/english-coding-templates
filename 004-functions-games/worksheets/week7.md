# 🎮 M004 Week 7 — English Worksheet

**Topic:** Auto-Building Spaces — Loops + Functions + Chat Commands · **Course:** Functions & Games · **Time:** about 45 minutes

This week one chat command builds a **whole space by itself**. A loop repeats a room piece, a function builds each piece, and the **number argument** decides how big the space grows.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the build happening, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Make a chat command with a number argument that auto-builds a space — a loop should repeat a room piece. When you finish, come back here.

Send a photo or video of your space being built, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My chat command is called …
>
> The number argument decides …
>
> The loop repeats …
>
> Between each piece, the builder …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while your command builds the space. Talk through it like you are teaching someone who has never seen it. Try to use these words: **chat command**, **argument**, **loop**, **repeat**, **function**.

> 1. Show the empty space, then type your command with a **small** number.
> 2. Say what the number argument changed.
> 3. Run the command again with a **bigger** number and show the difference.
> 4. Say in your own words how the loop and the function work together.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
