# 🔀 M002 Week 4 — AND / OR

**Topic:** AND and OR Conditions — Smarter Decisions · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

Last week your agent used `and` (both true). This week you add `or` (at least one true) and combine them in one maze.

- `and` → the action runs **only when both** conditions are true.
- `or` → the action runs **when at least one** condition is true.

Detect walls with `agent.detect(BLOCK, FORWARD)`. It returns `True` when a block is there. Use `not` for an open path.

---

## 1 · Predict 🔮

Read each block. Write what the agent does before you picture it.

```python
if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, RIGHT):
    agent.turn(LEFT_TURN)
```

Wall ahead, open right. Does it turn left? Why?

<div class="write-space"></div>

```python
if not agent.detect(BLOCK, FORWARD) or not agent.detect(BLOCK, DOWN):
    agent.move(FORWARD, 1)
```

Ahead blocked, below open. Does it move? Why?

<div class="write-space"></div>

```python
while True:
    if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, RIGHT):
        agent.turn(LEFT_TURN)
    elif not agent.detect(BLOCK, FORWARD) or not agent.detect(BLOCK, LEFT):
        agent.move(FORWARD, 1)
    else:
        agent.turn(RIGHT_TURN)
```

At a front-and-right corner, what runs? At an open junction, which branch runs?

<div class="write-space"></div>

---

## 2 · Trace the Truth 🔎

Fill the table. Write the branch that runs for each case.

```python
if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, RIGHT):
    agent.turn(LEFT_TURN)
elif not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
else:
    agent.turn(RIGHT_TURN)
```

| Front | Right | What runs? |
|-------|-------|-----------|
| wall | wall | |
| wall | open | |
| open | wall | |

<div class="write-space short"></div>

---

## 3 · Spot and Fix Bugs 🐛

Read what each block **should** do, then rewrite it. Explain the fix.

**Bug A** — Turn left **only** at a dead-end corner (wall ahead AND wall on right). Right now it turns at any wall.

```python
if agent.detect(BLOCK, FORWARD) or agent.detect(BLOCK, RIGHT):
    agent.turn(LEFT_TURN)
```

Fixed code:

<div class="write-space"></div>

Why was it wrong? Why does your fix work?

<div class="write-space"></div>

**Bug B** — Move forward when **either** the path ahead OR the path below is clear.

```python
if not agent.detect(BLOCK, FORWARD) and not agent.detect(BLOCK, DOWN):
    agent.move(FORWARD, 1)
```

Fixed code:

<div class="write-space"></div>

Why was it wrong? Why does your fix work?

<div class="write-space"></div>

**Bug C** — At a fork, turn right if the right is open, otherwise turn left. The order is wrong, so it always turns left first.

```python
if not agent.detect(BLOCK, LEFT):
    agent.turn(LEFT_TURN)
elif not agent.detect(BLOCK, RIGHT):
    agent.turn(RIGHT_TURN)
```

Hint: check the right side first.

Fixed code:

<div class="write-space"></div>

Why was it wrong? Why does your fix work?

<div class="write-space"></div>

---

## 4 · Write the Code ✍️

Write a `while True` loop that:

- turns left when there is a wall ahead **and** a wall on the right,
- else moves forward when the path ahead **or** the path below is open,
- else turns right.

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Finish the Maze 📸

Switch to your homework world. Solve the maze using **both** an `and` condition and an `or` condition. Come back when the agent reaches the end.

Send a photo or video of the agent at the end. Write 4 to 6 sentences.

> First, I …
>
> I used **and** when …
>
> I used **or** when …
>
> One tricky moment was …
>
> To fix it, I …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film the maze on your phone. Teach someone who has never seen it. Use these words: **and**, **or**, **condition**, **both**, **either**.

> 1. Show the start, then run your code.
> 2. Read each `and` block and `or` block out loud. Say what makes it run.
> 3. Show one bug you hit and how you fixed it.
> 4. Say in your own words how **and** is different from **or**.

Plan your words below before you film. You can read from it while recording.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
