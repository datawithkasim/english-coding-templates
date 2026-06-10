# 🎮 M004 Week 6 — English Worksheet

**Topic:** A Space that Reacts — Event → Check → Action · **Course:** Functions & Games · **Time:** about 45 minutes

This week your world **reacts to the player**. The pattern is always the same: an **event** happens (the player walks somewhere) → the code **checks** something (what block is there?) → an **action** runs (a door opens, a message appears, a trap triggers).

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the player doing it, write what you think will happen.

```
on player walks on gold block:
    say "Welcome to my world!"
```

**When does the message appear? What happens when the player walks on grass instead?**

<div class="write-space"></div>

```
on player walks on stone bricks:
    if block ahead is iron door:
        open the door
    otherwise:
        say "No door here."
```

**The player walks on stone bricks right in front of the iron door. What happens? What happens on stone bricks far away from the door?**

<div class="write-space"></div>

```
function spring_trap():
    replace block below with air
    say "You fell in my trap!"

on player walks on red carpet:
    spring_trap()
```

**What happens when the player steps on red carpet? Why is the trap written as a function?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The door should open **only after** the code checks that there really is an iron door ahead. Right now the check and the action are **swapped**.

```
on player walks on stone bricks:
    open the door
    if block ahead is iron door:
        say "Door found!"
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The trap is supposed to fire when the player steps on **red carpet**. But in the world, the red carpet does nothing and the blue carpet — the safe path — keeps eating players.

```
on player walks on blue carpet:
    spring_trap()
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The secret message should appear **only** when the player stands on a gold block. Right now the message appears everywhere, on every single step.

```
on player walks:
    say "You found the secret room!"
```

**Hint:** the event fires on every step — the **check** is missing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build a space that reacts to the player — use the event → check → action pattern at least once. When you finish, come back here.

Send a photo or video of your space reacting, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My space reacts when the player …
>
> The event is … and the check is …
>
> The action that runs is …
>
> One tricky moment was when …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk through your reacting space. Talk through it like you are teaching someone who has never seen it. Try to use these words: **event**, **check**, **action**, **sensing**, **react**.

> 1. Show your space before anything happens, then start walking.
> 2. Walk into the spot that triggers the reaction and say which **event** fired.
> 3. Show one spot where **nothing** happens because the check is not true there.
> 4. Say in your own words what event → check → action means.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
