# 🧩 M002 Extension 2 — Piston & Logic Maze

**Topic:** Two Pistons + AND Conditions · **Course:** Maze Madness · **Level:** Extension (Intermediate) · **Time:** about 45 minutes

The agent follows a **redstone trail** through a long maze, using **AND** at some junctions. Twice a **lever powers a piston** to open the way — get the agent through the **whole maze**.

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

**What must be true for the agent to turn left?**

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

## 5 · Show Your Work 📸🎥

Open the **M002 EXT 2** world and type `run`. Watch where it sticks, fix it, run again until it reaches the goal past both pistons.

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
