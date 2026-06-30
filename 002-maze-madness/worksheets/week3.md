# 🔗 M002 Week 3 — AND Conditions

**Topic:** AND — two things both true · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

`AND` checks two things. The action runs only when **both** are true.

---

## 1 · Predict 🔮

```python
if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, RIGHT):
    agent.turn(LEFT_TURN)
```

Both true. What happens?

<div class="write-space short"></div>

```python
if not agent.detect(BLOCK, FORWARD) and not agent.detect(BLOCK, DOWN):
    agent.move(FORWARD, 1)
```

Path ahead is clear, but a block is below. Does it move? Why?

<div class="write-space"></div>

---

## 2 · Trace 🔍

```python
while True:
    if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, RIGHT):
        agent.turn(LEFT_TURN)
    else:
        agent.move(FORWARD, 1)
```

At a corner (block ahead AND block right), what runs?

<div class="write-space short"></div>

At an open path, what runs?

<div class="write-space short"></div>

---

## 3 · Spot and Fix Bugs 🐛

**Bug A** — Turn left only when block ahead AND block on right.

```python
if agent.detect(BLOCK, FORWARD):
    agent.turn(LEFT_TURN)
```

Fix:

<div class="write-space"></div>

Why wrong?

<div class="write-space short"></div>

**Bug B** — Both checks should be different: front and right.

```python
if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, FORWARD):
    agent.turn(LEFT_TURN)
```

Fix:

<div class="write-space"></div>

Why wrong?

<div class="write-space short"></div>

---

## 4 · Write Code ✍️

Move forward only when the path ahead is clear AND the path on the left is clear. Write it.

<div class="write-space"></div>

---

## 5 · Finish the Maze 📸

Solve your homework maze using one or more `AND` conditions. Send a photo or video of the agent at the end. Then finish these.

> First, I …
>
> I used **AND** when …
>
> Both were true when …
>
> One tricky moment was …
>
> To fix it, I …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Record Your Walkthrough 🎥

Plan your phone video, then record. Try these words: **AND**, **condition**, **both**, **true**, **turn**.

> 1. Show the start. Run your code.
> 2. Read each `if … and …` block out loud. Say what makes it run.
> 3. Show one spot where the agent did nothing because only one check was true.
> 4. Say what **AND** means.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
