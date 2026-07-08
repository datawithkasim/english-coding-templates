# 🎮 M004 Week 8 — English Worksheet

**Topic:** Final — Your Minigame / Dungeon · **Course:** Functions & Games · **Time:** about 45 minutes

This is your **final week** — no new ideas. You combine everything you know — your function library, chat commands, sensing, events — into a playable **minigame or dungeon**.

---

## 1 · Predict 🔮

Below is a small minigame plan. Write what you think happens, step by step.

```
on chat command "start":
    teleport player to room 1
    say "Find the gold block!"
```

**A friend types `start` in chat. What two things happen, and in what order?**

<div class="write-space"></div>

```
on player walks on red carpet:
    replace block below with air
    say "Trap!"

on player walks on gold block:
    say "You win!"
    give player 1 diamond
```

**The player crosses the red carpet, then reaches the gold block. What happens at each step?**

<div class="write-space"></div>

```
function build_arena():
    build_room()
    move forward 6
    build_room()
    move forward 6
    build_room()

on chat command "start":
    build_arena()
    teleport player to room 1
    say "Reach the gold block. Watch out for red carpet!"
```

**Walk through `start` step by step — what gets built, where does the player land, and what do they see room by room?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — The gold goal block should be in the **last** room, after the trap. Right now players win in room 1 without ever facing the trap.

```
function build_arena():
    build_room()
    place gold block
    move forward 6
    build_room()
    place red carpet
    move forward 6
    build_room()
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The trap should fire **only on red carpet**. Right now it fires on every step — players fall the moment the game starts, right at spawn.

```
on player walks:
    spring_trap()
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The gold block is the **goal** and the red carpet is the **trap**. Right now the two reactions are swapped.

```
on player walks on gold block:
    say "Trap!"
    replace block below with air

on player walks on red carpet:
    say "You win!"
    give player 1 diamond
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world and build your own minigame or dungeon. **Plan first**, then build, then playtest.

**Plan your game:**

> My game's goal is …

<div class="write-space short"></div>

> My 3 rooms / zones are …

<div class="write-space short"></div>

> My trap is … and my reward is …

<div class="write-space short"></div>

> Functions I reuse from my library: …

<div class="write-space short"></div>

**Playtest checklist** — try your game like a player (or ask a family member to play):

> ☐ Can a player start the game with one chat command?
>
> ☐ Does every trigger work — trap, goal, messages?
>
> ☐ Can a player actually reach the goal and finish?

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
