# 🧩 M002 Extension 2 — Piston & Logic Maze

**Topic:** Two Pistons + AND Conditions · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

The agent follows a **redstone trail** through a long maze. At some junctions it checks **two things at once** — an **AND** condition. Twice, a **lever powers a piston** that opens the way. Your job: get the agent through the **whole maze**.

You drive it with chat words: `l` turn left, `r` turn right, `run` start the solver, `rl` teleport back to you.

---

## 1 · Read the Chat Commands 🎛️

Each block binds a **chat word** to an action.

```
def on_chat():
    agent.turn(RIGHT_TURN)
player.on_chat("r", on_chat)
```

**You type `r`. What does the agent do?**

<div class="write-space short"></div>

```
def on_chat():
    agent.teleport_to_player()
player.on_chat("rl", on_chat)
```

**You type `rl`. Where does the agent go? When does that help in a long maze?**

<div class="write-space"></div>

---

## 2 · AND at a Junction 🔀

**AND** is true only when **both** parts are true.

```
if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, AHEAD):
    agent.turn(LEFT_TURN)
```

**Fill the table. Write turn or no turn.**

| Redstone LEFT? | Redstone AHEAD? | What happens? |
|---|---|---|
| yes | no | |
| no | yes | |
| yes | yes | |

**In your own words: what must be true for the agent to turn left?**

<div class="write-space short"></div>

---

## 3 · Trace the Solver 🔍

This loop runs when you type `run`.

```
while True:
    agent.move(FORWARD, 1)
    if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, AHEAD):
        agent.turn(LEFT_TURN)
    elif agent.detect(BLOCK, AHEAD):
        agent.interact(AHEAD)
        agent.move(FORWARD, 1)
```

**The last `elif` is a piston gate. A block is ahead. What does `agent.interact(AHEAD)` do?**

<div class="write-space"></div>

**Why can the agent move forward right after it interacts?**

<div class="write-space short"></div>

---

## 4 · Fix the Bug 🐛

**The agent should turn left only when redstone is left AND ahead. This turns on either one.**

```
if agent.detect(REDSTONE, LEFT) or agent.detect(REDSTONE, AHEAD):
    agent.turn(LEFT_TURN)
```

**Hint:** "left and ahead" — both at once.

**Write the fixed line:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Finish the Whole Maze 📸

Open the **M002 EXT 2** world. Type `run`. Watch where it gets stuck, fix it, run again — until it reaches the goal past both pistons.

Send a photo or video of the agent at the goal. Use these starters — 3 or 4 sentences.

> The maze had two pistons, so the agent had to …
>
> At a junction the AND check made the agent …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film on a phone while the agent solves the maze. Talk like you are teaching a friend. Try to use: **redstone**, **trail**, **AND**, **piston**, **lever**, **loop**.

> 1. Show the maze and the redstone trail.
> 2. Type `run` and show the agent following it.
> 3. Read one AND check out loud and say what it decides.
> 4. Show the agent flipping a lever to open a piston.
> 5. Show it reaching the goal.

**Write what you will say. Plan it here first.**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
