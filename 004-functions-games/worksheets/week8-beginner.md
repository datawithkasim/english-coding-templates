# 🎮 M004 Week 8 — English Worksheet (Beginner)

**Topic:** Final — Your Minigame / Dungeon · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This is your **final week** — no new ideas. You combine what you know — functions, chat commands, sensing, events — into a playable **minigame or dungeon**.

---

## 1 · Predict 🔮

```
on chat command "start":
    teleport player to room 1
    say "Find the gold block!"
```

**A friend types `start`. Does the game begin? Circle one:** yes · no

**Why? Circle one:** the `start` command runs · nothing is typed

```
on player walks on gold block:
    say "You win!"
    give player 1 diamond
```

**The player walks on grass. Do they win? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

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

**What is wrong? Circle one:** trap fires on every step · trap fires only on red carpet

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

**What is wrong? Circle one:** wins on the trap carpet · wins on the gold block

---

## 3 · Fill the Gap ✏️

One word is missing.

```
on player walks on ____ block:
    say "You win!"
    give player 1 diamond
```

**Fill the gap. Circle one:** `gold` · `trap` · `start`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world and build your own minigame or dungeon. Pick a goal, one trap, and one reward, then play it.

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
