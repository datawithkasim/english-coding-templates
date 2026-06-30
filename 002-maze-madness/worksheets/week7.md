# ⚙️ M002 Week 7 — Pistons

**Topic:** Pistons and Mazes · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

A piston pushes or pulls a block when it gets a redstone signal. A **sticky piston** can pull a block back, opening a path — but only while the signal is ON. A lever sends that signal. Your agent flips the lever to power the piston, then crosses the gap it opens.

---

## 1 · Predict 🔮

Read each block. Write what happens before you imagine it.

```python
agent.move(FORWARD, 1)
agent.interact(...)
agent.move(FORWARD, 1)
```

**The agent walks to a lever, flips it, and a sticky piston pulls a block back. Can the agent move forward now?**

<div class="write-space"></div>

```python
if not agent.detect(BLOCK, FORWARD):
    agent.interact(...)
else:
    agent.move(FORWARD, 1)
```

**What does the agent do at a gap? What does it do on solid ground?**

<div class="write-space"></div>

---

## 2 · Trace 👣

```python
while True:
    if not agent.detect(BLOCK, FORWARD):
        agent.interact(...)
        agent.move(FORWARD, 1)
    else:
        agent.move(FORWARD, 1)
```

**Describe step by step what the agent does as it moves through the maze.**

<div class="write-space"></div>

---

## 3 · Spot and Fix Bugs 🐛

Each block is broken. Read the goal, write the fix, then explain it.

**Bug A** — Power the piston **first**, then cross the gap it opens.

```python
agent.move(FORWARD, 1)
agent.move(FORWARD, 1)
agent.interact(...)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space short"></div>

**Bug B** — `interact` should run only when there is a **gap** ahead. This flips a lever on every step.

```python
while True:
    agent.interact(...)
    agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space short"></div>

**Bug C** — A sticky piston holds the bridge **only while the lever is ON**. The second `interact` switches it OFF and the bridge vanishes. Cross first.

```python
agent.interact(...)
agent.move(FORWARD, 1)
agent.interact(...)
agent.move(FORWARD, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space short"></div>

---

## 4 · Write Full Code ✍️

Write code that walks the agent to the lever, flips it so the piston opens the path, crosses while the path is open, and reaches the goal. Use a chat trigger to start it.

```python
def cross_gap(name, message):
    pass  # your code here

player.on_chat("go", cross_gap)
```

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Build It 📸

Open your homework world. The maze has a gap (or blocked path) and a piston that opens it when powered. Run your code so the agent reaches the goal.

Send a photo or video of the agent at the end. Then finish these lines — 4 to 6 sentences.

> First, I walked the agent to …
>
> I powered the piston by …
>
> Once the path opened, the agent …
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Plan Your Walkthrough Video 🎥

Take a phone video while the agent runs the maze. Talk through it like you are teaching someone new. Use these words: **piston**, **redstone**, **signal**, **gap**, **bridge**.

> 1. Show the gap and the piston.
> 2. Run your code and show the agent powering the piston and crossing.
> 3. Read your code out loud and say which line opens the path.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say. Plan it here before you record.**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
