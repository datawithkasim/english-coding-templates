# 🧩 M002 Extension 4 — Complete the Maze

**Topic:** Add Two AND Conditions · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

The agent follows a redstone trail with **four rules**, but the solver is **not finished**. At two junctions two signals fire at once and it stops — add two **AND** rules, then drive it to the goal.

Chat: `l` turn left, `r` turn right, `run` start solver, `rl` bring agent back.

---

## 1 · The Four Rules 🎛️

Each rule checks **one** signal and does **one** action.

```
if agent.detect(REDSTONE, LEFT):
    agent.turn(RIGHT_TURN)
elif agent.detect(REDSTONE, RIGHT):
    agent.turn(LEFT_TURN)
elif agent.detect(REDSTONE, DOWN):
    agent.move(UP, 1)
elif agent.detect(REDSTONE, UP):
    agent.move(DOWN, 1)
```

**Fill the table from the code. You will reuse these actions.**

| Signal | Action |
|---|---|
| redstone **left** | |
| redstone **right** | |
| redstone **below** (down) | |
| redstone **above** (up) | |

---

## 2 · Find the Two Stuck Junctions 🔍

Open the **M002 Complete the Maze** world and type `run`. Watch where the agent stops, then look around it.

**Tick the signals on at each stuck junction.**

| | left | right | below | above |
|---|---|---|---|---|
| **Junction 1** | | | | |
| **Junction 2** | | | | |

**Only the first matching `elif` fires. Why does that leave the second signal unused?**

<div class="write-space"></div>

---

## 3 · AND means BOTH 🧠

An **AND** is true **only when both** halves are true.

```
if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, DOWN):
    ...
```

**Example: left on but NOT below. Is the whole condition true?**

<div class="write-space short"></div>

**Look at Junction 1 in your table. Write the AND condition that is true only there.**

<div class="write-space short"></div>

---

## 4 · Add the Two New Rules 🛠️

Add **two `elif` branches**, one per stuck junction, using the signals **you** found. Each branch does the action for **each** signal.

**Junction 1 — fill the blanks:**

```
elif agent.detect(REDSTONE, ______) and agent.detect(REDSTONE, ______):
    agent.________(__________)
    agent.________(__________)
```

<div class="write-space"></div>

**Junction 2 — write the whole branch yourself:**

<div class="write-space"></div>

**Put both new rules _before_ the four single-signal rules. Why?**

<div class="write-space short"></div>

---

## 5 · Spot the Bug 🐛

This branch should fire **only when both** signals are on. It fires when **either** one is on, so it triggers at wrong spots.

```
elif agent.detect(REDSTONE, LEFT) or agent.detect(REDSTONE, DOWN):
    agent.turn(RIGHT_TURN)
    agent.move(UP, 1)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

---

## 6 · Show Your Work 📸🎥

Type `run`. Goal: start to the **very end**, past both stuck junctions — fix your rules and run again until it reaches the goal.

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
