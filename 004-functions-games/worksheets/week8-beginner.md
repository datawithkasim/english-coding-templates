# 🎮 M004 Week 8 — English Worksheet (Beginner)

**Topic:** Final — Your Minigame / Dungeon · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This is your **final week** — no new ideas. You combine what you already know — functions, chat commands, sensing, and events — into a playable **minigame or dungeon**.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the game running, circle or write your answer.

```
on chat command "start":
    teleport player to room 1
    say "Find the gold block!"
```

**A friend types `start`. Does the game begin? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
on player walks on gold block:
    say "You win!"
    give player 1 diamond
```

**The player walks on grass. Do they win? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The trap should fire **only on red carpet**, not at spawn.

```
# clean
on player walks on red carpet:
    spring_trap()
```

```
# buggy
on player walks:
    spring_trap()
```

**What is wrong? What happens the moment the game starts?**

<div class="write-space short"></div>

**Pair B** — The gold block is the **goal**, the red carpet is the **trap**.

```
# clean
on player walks on gold block:
    say "You win!"
```

```
# buggy
on player walks on red carpet:
    say "You win!"
```

**What is wrong? Where does the buggy game say "You win!"?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The player should win on the gold block. One word is missing. Fill it in using the word bank.

```
on player walks on ____ block:
    say "You win!"
    give player 1 diamond
```

**Word bank:** `gold` · `trap` · `start`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world and build your own minigame or dungeon. Plan first: pick a goal, one trap, and one reward. Then build and try it like a player.

Send a photo or video of someone playing your game, then explain what you built. Use these sentence starters — write 2 or 3 sentences.

> My game's goal is …
>
> My trap is … and my reward is …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you play your minigame from start to finish. Talk like you are teaching a friend. Try to use these words: **goal**, **trap**, **reward**.

> 1. Type your start command and show what happens.
> 2. Show the trap, then show reaching the goal.
> 3. Say in your own words how your game works.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
