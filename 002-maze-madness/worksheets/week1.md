# 🌀 M002 Week 1 — While Loop

**Topic:** Repeat Until a Wall · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

A while loop checks, then runs the body, then checks again. It stops when the check is false.

---

## 1 · Trace the Loop 🔮

```python
while not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

**The wall is 5 steps ahead. How many moves? When does the loop end?**

<div class="write-space"></div>

---

## 2 · Read the API 📖

| Call | What it does |
|------|--------------|
| `agent.detect(BLOCK, FORWARD)` | true if a wall is ahead |
| `agent.move(FORWARD, 1)` | step forward once |
| `agent.turn(RIGHT_TURN)` | turn right |

**Why check `not agent.detect(...)` and not `agent.detect(...)`?**

<div class="write-space short"></div>

---

## 3 · Spot the Bugs 🐛

**Bug A** — should move until the wall.

```python
while agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

**Fix it:**

<div class="write-space short"></div>

**Bug B** — should stop right at the wall, not crash.

```python
while not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 1)
```

**Fix it. Say why it crashed:**

<div class="write-space"></div>

---

## 4 · Write a Chat Command ✏️

Make `go` move the agent forward until a wall.

> Use `player.on_chat`, `while`, `agent.detect`, `agent.move`.

<div class="write-space"></div>

---

## 5 · Loop, Turn, Loop ✏️

Move to the wall, turn right, then move to the next wall.

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Finish the Maze 📸

Open your homework world. Use a while loop to drive the agent down the straight maze to the wall.

Send a photo OR video of the agent at the wall. Then write 4-6 sentences.

> First, I read the maze and saw …
>
> My loop checked …
>
> The agent stopped because …
>
> The hard part was …
>
> A while loop beats many `move` lines because …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 7 · Narrate Your Walkthrough 🎥

Record on a phone while the agent runs. Teach it like the viewer is new. Use: **while**, **loop**, **detect**, **wall**, **forward**.

> 1. Show the start. Run your code.
> 2. Read your loop. Say what makes it stop.
> 3. Show one bug and your fix.
> 4. Say why a loop beats many `move` lines.

**Plan your words:**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
