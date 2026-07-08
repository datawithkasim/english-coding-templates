# ⚙️ M002 Week 7 — Pistons

**Topic:** Pistons and Mazes · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

A **sticky piston** pulls a block back to open a path, but only while a lever keeps the signal ON. Flip the lever to power it, then cross the gap.

---

## 1 · Predict 🔮

Write what happens.

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

Read the goal, write the fix, then explain it.

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

**Bug C** — A sticky piston holds the bridge **only while the lever is ON**. The second `interact` turns it OFF and the bridge vanishes, so cross first.

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

## 5 · Show Your Work 📸🎥

Open your homework world. Run your code so the agent crosses the piston gap and reaches the goal.

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
