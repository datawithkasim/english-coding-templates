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

Move forward only when the path ahead is clear AND the path on the left is clear.

<div class="write-space"></div>

---

## 5 · Show Your Work 📸🎥

Solve your homework maze using one or more `AND` conditions.

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
