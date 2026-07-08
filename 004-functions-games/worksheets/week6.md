# 🎮 M004 Week 6 — English Worksheet

**Topic:** A Space that Reacts — Event → Check → Action · **Course:** Functions & Games · **Time:** about 45 minutes

This week your world **reacts to the player**. The pattern: an **event** happens → the code **checks** something → an **action** runs.

---

## 1 · Predict 🔮

Before you imagine the player doing it, write what you think will happen.

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

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

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

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Build a space that reacts to the player — use the event → check → action pattern at least once. When you finish, come back here.

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
