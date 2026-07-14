# 🔴 M002 Week 6 — Redstone & Levers

**Topic:** Redstone Levers · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

The maze has a **lever**. Flip it with `interact` to open the redstone door, then walk to the goal.

---

## 1 · Predict 🔮

Write what the agent does.

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

## 5 · Show Your Work 📸🎥

Open your homework world. Write code that:

1. moves the agent to the lever,
2. flips it with `interact`,
3. walks through the open door to the goal.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
