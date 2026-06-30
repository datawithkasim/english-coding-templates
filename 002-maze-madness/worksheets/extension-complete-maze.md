# 🧩 M002 Extension 4 — Complete the Maze

**Topic:** Add Two AND Conditions · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 55 minutes

The agent knows **four rules** to follow a redstone trail through a 3D maze. The solver is **not finished**: at two junctions two signals are on at once, so one signal is not enough and the agent stops. Add **two AND rules** of your own — **you** decide which two signals each junction needs. Then drive the agent to the goal.

Chat: `l` turn left, `r` turn right, `run` start solver, `rl` bring agent back.

---

## 1 · Read the Four Rules 🎛️

Each rule checks **one** signal and does **one** action.

```python
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

**A left signal makes the agent turn _right_; a signal below makes it move _up_. Why might the maze pair a signal on one side with an action to the other?**

<div class="write-space short"></div>

---

## 2 · Find the Two Stuck Junctions 🔍

Most junctions have **one** signal on, so one rule fires. Two junctions have **two** signals on at once — there the four rules are not enough and the agent stops.

Type `run`. Watch where it stops. Walk over and look around the agent.

**Tick the signals on at each stuck junction.**

| | left | right | below | above |
|---|---|---|---|---|
| **Junction 1** | | | | |
| **Junction 2** | | | | |

**Only the first matching `if`/`elif` branch runs on each pass. Why does that leave the second signal unused?**

<div class="write-space short"></div>

---

## 3 · AND means BOTH 🧠

An **AND** is true **only when both** halves are true.

```python
if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, DOWN):
    ...
```

**(Example only — yours may differ.) Left on but NOT below: is the whole condition true? Below on but not left?**

<div class="write-space short"></div>

**Look at Junction 1 in your table. Write the AND condition true only at that spot, then the action for each signal in the order you want them.**

<div class="write-space"></div>

---

## 4 · Add the Two New Rules 🛠️

Open the **M002 Complete the Maze** world. Find the four rules. Add **two `elif` branches**, one per stuck junction, using the signals **you** found.

**Junction 1 — write the whole branch: the AND condition, then the action for each signal.**

```python
elif agent.detect(REDSTONE, ______) and agent.detect(REDSTONE, ______):
    agent.________(__________)
    agent.________(__________)
```

<div class="write-space"></div>

**Junction 2 — write the whole branch from scratch.**

<div class="write-space"></div>

**Both new rules must be checked _before_ the four single-signal rules. Why? What happens at a stuck junction if a plain single-signal rule is checked first?**

<div class="write-space short"></div>

---

## 5 · Spot the Bug 🐛

Each block is broken. Rewrite it, then explain the fix. (Signals here are examples.)

**Bug A** — should fire **only when both** signals are on, but fires when **either** one is, so it triggers at wrong spots.

```python
elif agent.detect(REDSTONE, LEFT) or agent.detect(REDSTONE, DOWN):
    agent.turn(RIGHT_TURN)
    agent.move(UP, 1)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

**Bug B** — a junction needs **two** actions, but this rule does one, so the agent solves half and sticks again.

```python
elif agent.detect(REDSTONE, RIGHT) and agent.detect(REDSTONE, UP):
    agent.turn(LEFT_TURN)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

---

## 6 · Finish the Whole Maze 📸

The goal is start to the **very end** — past both stuck junctions and every plain turn. Type `run`, watch where it stops, fix your two rules, run again until it reaches the goal.

Send a photo or video of the agent at the goal. Then write 4 to 6 sentences with these starters.

> Each of the four rules checked …
>
> The agent got stuck because one signal was not …
>
> The two signals at the first stuck junction were … and …
>
> My AND rule was true only when both were …
>
> I put my two new rules before the old rules because …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 7 · Plan Your Walkthrough Video 🎥

Film on your phone (or a parent's) while the agent solves the whole maze. Teach it like the viewer has never seen it. Try these words: **detect**, **redstone**, **AND**, **both**, **condition**, **turn**, **move up**, **move down**.

> 1. Show the maze and point out the redstone signals.
> 2. Type `run` and show the agent following the trail.
> 3. Read one AND rule and say which two signals must be true.
> 4. Show the agent passing a stuck junction.
> 5. Show it reaching the goal.

**Write what you will say. Plan it here first — read from it while filming.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
