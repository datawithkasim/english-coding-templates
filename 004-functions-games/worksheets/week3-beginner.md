# 🎮 M004 Week 3 — English Worksheet (Beginner)

**Topic:** Sensing the World · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week your agent **senses** the world before it acts. It can detect a block **ahead** and check what is **below** — like stopping before lava.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
if agent detects block ahead:
    turn left
otherwise:
    move forward
```

**There is a wall right in front of the agent. Does the agent turn left? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
if block below is lava:
    place block below
move forward
```

**The agent is standing over lava. Does it place a safe block before moving? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The lava is **below** the agent, so the check should look below.

```
# clean
if block below is lava:
    place block below
```

```
# buggy
if agent detects block ahead:
    place block below
```

**What is wrong? Where does the buggy agent look?**

<div class="write-space short"></div>

**Pair B** — On safe ground the agent should still **move**. It needs an `otherwise`.

```
# clean
if block below is lava:
    place block below
otherwise:
    move forward
```

```
# buggy
if block below is lava:
    place block below
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should place a safe block when the block under its feet is lava. One word is missing. Fill it in using the word bank.

```
if block ____ is lava:
    place block below
otherwise:
    move forward
```

**Word bank:** `below` · `ahead` · `repeat`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Send your agent across the danger field using at least one `if block below is …` check. When you finish, come back here.

Send a photo or video of the agent crossing safely, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My agent detected …
>
> When the block below was lava, my agent …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent crosses the field. Talk like you are teaching a friend. Try to use these words: **detect**, **below**, **ahead**.

> 1. Show the danger field, then run your code.
> 2. Read your `if block below is …` line out loud.
> 3. Say in your own words why the agent checks **before** it moves.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
