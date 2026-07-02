# 🎮 M004 Week 7 — English Worksheet (Beginner)

**Topic:** Auto-Building Spaces — Loops + Functions + Chat Commands · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week one chat command builds a **whole space by itself**. A loop repeats a room piece, and the **number** you type decides how big the space grows.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the build happening, circle or write your answer.

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 6
```

**You type `dungeon 3`. Does it build 3 rooms? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
on chat command "dungeon" with number rooms:
    repeat rooms times:
        build_room()
        move forward 6
```

**Now you type `dungeon 1`. Does it build 3 rooms? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

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

**What is wrong? Where do all the buggy rooms get built?**

<div class="write-space short"></div>

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

**What is wrong? What happens when you type `dungeon 5`?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The number you type should decide how many rooms get built. One word is missing. Fill it in using the word bank.

```
on chat command "dungeon" with number rooms:
    repeat ____ times:
        build_room()
        move forward 6
```

**Word bank:** `rooms` · `dungeon` · `forward`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Make a chat command with a number that auto-builds a space. When you finish, come back here.

Send a photo or video of your space being built, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My chat command is called …
>
> The number decides …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your command builds the space. Talk like you are teaching a friend. Try to use these words: **chat command**, **number**, **repeat**.

> 1. Show the empty space, then type your command.
> 2. Say what the number you typed changed.
> 3. Say in your own words how the loop builds the space.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
