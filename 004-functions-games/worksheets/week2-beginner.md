# 🎮 M004 Week 2 — English Worksheet (Beginner)

**Topic:** Chat Commands · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week you type a word in chat and your code runs. A **chat command** can take a number with it — `tower 5` builds a 5-block tower.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
on chat command "bridge":
    repeat 6 times:
        place block
        move forward
```

**You type `bridge` in chat. Does the agent build the bridge? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
on chat command "tower" with number n:
    repeat n times:
        place block
        move up
```

**You type `tower 4`. Is the tower 4 blocks tall? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — Typing `bridge` should run the code. The command **name** must match what you type.

```
# clean
on chat command "bridge":
    repeat 6 times:
        place block
        move forward
```

```
# buggy
on chat command "brige":
    repeat 6 times:
        place block
        move forward
```

**What is wrong? Why does nothing run when you type `bridge`?**

<div class="write-space short"></div>

**Pair B** — The number from chat should go **into** the function.

```
# clean
on chat command "tower" with number n:
    build_tower(n)
```

```
# buggy
on chat command "tower" with number n:
    build_tower(3)
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

Typing `tower 5` should build a 5-block tower. One word is missing. Fill it in using the word bank.

```
on chat command "tower" with number n:
    repeat ____ times:
        place block
        move up
```

**Word bank:** `n` · `tower` · `chat`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Make one chat command with a number that builds something. When you finish, come back here.

Send a photo or video of your command running, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> When I typed my command in chat, …
>
> My command's number was used for …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you type your command and the code runs. Talk like you are teaching a friend. Try to use these words: **chat command**, **number**, **run**.

> 1. Show the chat box and type your command.
> 2. Show what the code builds.
> 3. Say in your own words what a **chat command** does.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
