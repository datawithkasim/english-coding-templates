# 🔴 M002 Week 6 — Redstone & Levers

**Topic:** Redstone Levers · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

This week the maze has a **lever**. The agent flips the lever with `interact` to open a closed redstone door, then walks through to the goal.

---

## 1 · Predict 🔮

Read the steps. Write what the agent does.

```
move forward
interact ahead
move forward
```

**The agent flips the lever. What happens to the door?**

<div class="write-space short"></div>

```
interact ahead
move forward
move forward
```

**There is no lever in front. What happens?**

<div class="write-space short"></div>

---

## 2 · Plain to API 🔁

Match the plain words to the real code line.

| Plain words | Code |
| --- | --- |
| flip the lever in front | `agent.move(FORWARD, 1)` |
| step forward one block | `agent.interact(...)` |
| is there redstone ahead? | `agent.detect(REDSTONE, FORWARD)` |

**Write each pair:**

<div class="write-space short"></div>

---

## 3 · Trace the Code 🔍

```python
while not agent.detect(REDSTONE, FORWARD):
    agent.move(FORWARD, 1)
agent.interact(...)
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
```

**What does the agent do? Write it in plain English.**

<div class="write-space"></div>

---

## 4 · Fix the Bug 🐛

The agent should walk **up to** the lever, then flip it **once**. This flips on every step.

```python
while not agent.detect(REDSTONE, FORWARD):
    agent.move(FORWARD, 1)
    agent.interact(...)
```

**Write the fixed code:**

<div class="write-space"></div>

**One line: why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Finish the Maze 📸

Open your homework world. Write code that:

1. moves the agent to the lever,
2. flips it with `interact`,
3. walks through the open door to the goal.

Send a photo or video of the agent at the end. Then write 3 sentences.

> I used `interact` to …
>
> Once the door opened, the agent …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

**Phone video plan.** Film the agent running the maze. Say these words: **lever**, **interact**, **door**, **open**.

> 1. Show the closed door and the lever.
> 2. Run your code. Show the agent flip the lever.
> 3. Say which line opens the door.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
