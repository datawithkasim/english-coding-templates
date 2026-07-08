# 🎮 M004 Week 4 — English Worksheet

**Topic:** Player Events · **Course:** Functions & Games · **Time:** about 45 minutes

This week your code reacts to **you**, the player. An **event** like `on player walk:` runs by itself — no chat command needed.

---

## 1 · Predict 🔮

```
on player walk:
    if block below is gold:
        say "Treasure room!"
```

**The player walks across stone, stone, gold, stone. When does the message appear? How many times?**

<div class="write-space"></div>

```
on player place block:
    say "You built something!"
```

**The player places 3 blocks, then walks around for a while. How many times does the message appear? Does walking trigger it?**

<div class="write-space"></div>

```
define drop_reward():
    place diamond block

on player walk:
    if block below is redstone:
        drop_reward()
```

**The player steps onto a redstone block. What happens, step by step? What happens on normal ground?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below is broken. Rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — A trap message should appear **by itself** whenever the player walks onto gold. But nothing ever happens unless someone types `trap` in chat.

```
on chat command "trap":
    if block below is gold:
        say "Trap!"
```

**Hint:** this should be an **event** that runs on its own, not a chat command.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The player should get **one** welcome reward when they first step onto the redstone start tile. But the reward keeps firing again and again on every step, flooding the world with diamonds.

```
on player walk:
    if block below is redstone:
        place diamond block
```

**Hint:** use a variable like `reward_given` to remember if the reward already happened.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The message should appear when the player **places a block**, to celebrate building. But right now it appears every time the player simply walks.

```
on player walk:
    say "Nice building!"
```

**Hint:** the behavior is right, the **event** is wrong.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Switch to your homework world. Build a mini game zone with **one trap** and **one reward**, each triggered by a player event (`on player walk:` or `on player place block:`).

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
