# 🎮 M004 Week 8 — English Worksheet

**Topic:** Final — Your Minigame / Dungeon · **Course:** Functions & Games · **Time:** about 45 minutes

This is your **final week** — no new ideas. You combine everything you already know: your function library, chat commands, sensing, and events. Together they make a playable **minigame or dungeon**.

---

## 1 · Predict 🔮

Below is the plan for a small minigame. Read each part, then write what you think happens step by step.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

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

Send a photo or video of someone playing your game, then explain what you built. Use these sentence starters — write 4 to 6 sentences total.

> My game starts when …
>
> The player has to …
>
> I reused functions from week … when …
>
> One tricky moment was when …
>
> During playtesting, I found …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you play your minigame from start to finish. Talk through it like you are teaching someone who has never seen it. Try to use these words: **goal**, **trap**, **reward**, **event**, **function**.

> 1. Type your start command and show what gets built.
> 2. Walk through each room and say what happens there.
> 3. Show the trap firing, then show reaching the goal.
> 4. Say which parts came from your function library and which events make the game react.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
