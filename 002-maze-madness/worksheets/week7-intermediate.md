# ⚙️ M002 Week 7 — Pistons

**Topic:** Pistons and Mazes · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

A piston pushes or pulls a block when it gets a redstone signal. A lever sends that signal. Flip the lever, the piston opens a path across a gap, and the agent crosses while the path is open.

---

## 1 · Predict 🔮

Read the steps. Write what happens.

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

Now in real Python. The agent flips the lever only when it sees a gap ahead. Fill the blank.

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

## 5 · Build It + Plan Your Video 📸🎥

Open your homework world. The maze has a gap and a piston that opens it. Walk the agent to the lever, flip it, cross while the path is open, and reach the goal.

Send a photo or video of the agent at the end. Then finish these lines.

> I powered the piston by …
>
> Once the path opened, the agent …
>
> The hardest part was …

<div class="write-space"></div>

Take a phone video while the agent runs. Talk like you are teaching a friend. Use these words: **piston**, **redstone**, **signal**, **gap**.

> 1. Show the gap and the piston.
> 2. Run your code and show the agent crossing.
> 3. Say which line opens the path.

**Write what you will say:**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
