# ⚙️ M002 Week 7 — Pistons

**Topic:** Pistons and Mazes · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

A piston opens a path when a lever powers it. Flip the lever, then cross the gap while the path is open.

---

## 1 · Predict 🔮

Write what happens.

```
move forward
interact ahead
move forward
```

**The agent reaches a lever and flips it. A piston opens the path. Can the agent cross now?**

<div class="write-space short"></div>

```
if gap ahead:
    interact ahead
otherwise:
    move forward
```

**The agent is on solid ground, no gap. What does it do?**

<div class="write-space short"></div>

---

## 2 · Trace 👣

```
keep doing forever:
    if gap ahead:
        interact ahead
        move forward
    otherwise:
        move forward
```

**Say in plain English what the agent does at a gap, and what it does on solid ground.**

<div class="write-space"></div>

---

## 3 · Fill the Code Blank 🧩

The agent flips the lever only when it sees a gap ahead.

```python
if not agent.detect(BLOCK, FORWARD):
    agent.____(...)
    agent.move(FORWARD, 1)
else:
    agent.move(FORWARD, 1)
```

**Word bank:** `interact` · `turn` · `detect`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Spot One Bug 🐛

The agent should power the piston **first**, then cross the gap it opens. This code crosses first.

```python
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
agent.interact(...)
```

**Write the fixed code (flip the lever before the gap):**

<div class="write-space"></div>

**One sentence: why was it wrong?**

<div class="write-space short"></div>

---

## 5 · Show Your Work 📸🎥

Open your homework world. Walk the agent to the lever, flip it, cross the open path, and reach the goal.

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
