# 🧩 M002 Extension 5 — Redstone AND Solver

**Topic:** Redstone AND Rules + Single Checks · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

Same **Week 3 world**. Find the **hardest maze** — the big one **your teacher will show you a picture of**, packed with redstone. The agent reads **redstone** to move. Some tiles have **two** redstones — those need an **AND**: both must be true.

> **The rules you need**
>
> - RS **left** → turn right · RS **right** → turn left (single)
> - RS **below** → move up 1 (single)
> - **#1** RS left **and** below → up 1, turn right (AND)
> - **#2** RS right **and** below → up 1, turn left (AND)
> - **#4** RS left **and** right → up 5 (AND)

Chat: `l` turn left · `r` turn right · `run` start · `rl` bring the agent back.

---

## 1 · Read the Chat Commands 🎛️

A chat word binds to an action. Type the word, the agent runs the code.

```python
def turn_left():
    agent.turn(LEFT_TURN)
player.on_chat("l", turn_left)
```

**You type `l`. What does the agent do?**

<div class="write-space short"></div>

```python
def go_back():
    agent.teleport_to_player()
player.on_chat("rl", go_back)
```

**You type `rl`. Where does the agent go? When is that handy?**

<div class="write-space"></div>

---

## 2 · Trace the Solver 🔍

This loop runs when you type `run`.

```python
while True:
    if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, RIGHT):
        agent.move(UP, 5)
    elif agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, DOWN):
        agent.move(UP, 1)
        agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
```

**Rule #4 is `RS LEFT and RS RIGHT`. Which line runs there, and how far does the agent climb?**

<div class="write-space short"></div>

**Rule #1 is `RS LEFT and RS DOWN`. Which line runs, and what two things does it do?**

<div class="write-space"></div>

**A tile has redstone on the **left only** — nothing below, nothing on the right. Does either `if` run? Why not?**

<div class="write-space"></div>

---

## 3 · Fill the Blanks ✏️

Rule #2: move up 1 and turn left **only when both are true** — redstone right and redstone below. Fill the blanks.

```python
if agent.detect(REDSTONE, ________) ________ agent.detect(REDSTONE, DOWN):
    agent.move(UP, 1)
    agent.turn(________)
```

**Word bank:** `RIGHT` · `and` · `LEFT_TURN`

<div class="write-space"></div>

---

## 4 · Spot the Bug 🐛

**Bug A** — Rule #1 should fire **only** when redstone is left **and** below. Right now it checks redstone left only, so it fires on a plain left marker with nothing below it.

```python
if agent.detect(REDSTONE, LEFT):
    agent.move(UP, 1)
    agent.turn(RIGHT_TURN)
agent.move(FORWARD, 1)
```

**Hint:** add the second check with `and`.

**Write the fix:**

<div class="write-space"></div>

**One line: why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Finish + Film 📸🎥

Open the Week 3 world, find the hardest maze from the picture, and run your solver until the agent reaches the **diamond block** goal.

Send a photo OR video of the agent at the goal. Write 3 or 4 sentences.

> The agent read two redstones at once when …
>
> I used **AND** because …
>
> Both checks were true when …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

**Phone video plan.** Film the agent solving the maze. Talk like you teach a friend. Try these words: **detect**, **redstone**, **AND**, **both**, **rule**.

> 1. Show the redstone in the maze.
> 2. Type `run` and show the agent following the rules.
> 3. Say one tile where two redstones were both there.

**Write what you will say:**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
