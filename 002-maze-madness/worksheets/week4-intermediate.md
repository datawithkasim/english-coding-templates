# 🔀 M002 Week 4 — AND / OR

**Topic:** AND and OR Conditions · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

New this week: `OR` (one is enough). Mix it with `AND`.

- `AND` → runs **only when both** are true.
- `OR` → runs **when at least one** is true.

In Python: `and`, `or`. Detect a wall with `agent.detect(BLOCK, FORWARD)`.

---

## 1 · Predict 🔮

```
if wall ahead AND wall on right:
    turn left
```

Wall ahead, but the right is open. Does it turn left? Why?

<div class="write-space short"></div>

```
if no wall ahead OR no wall below:
    move forward
```

Ahead is blocked, below is open. Does it move? Why?

<div class="write-space short"></div>

---

## 2 · Trace It 🔎

```
if agent.detect(BLOCK, FORWARD) and agent.detect(BLOCK, RIGHT):
    agent.turn(LEFT_TURN)
elif not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

The agent has a wall in front and an open right. What runs?

<div class="write-space short"></div>

The agent has open front, wall on right. What runs?

<div class="write-space short"></div>

---

## 3 · Fill the Blanks ✏️

Turn left **only** at a corner (wall front AND wall right).

```
if agent.detect(BLOCK, FORWARD) ____ agent.detect(BLOCK, RIGHT):
    agent.turn(LEFT_TURN)
```

Move when **either** front OR below is open.

```
if not agent.detect(BLOCK, FORWARD) ____ not agent.detect(BLOCK, DOWN):
    agent.move(FORWARD, 1)
```

<div class="write-space short"></div>

---

## 4 · Fix the Bug 🐛

The agent should move when **either** path ahead OR below is clear. This makes it wait for both.

```
if not agent.detect(BLOCK, FORWARD) and not agent.detect(BLOCK, DOWN):
    agent.move(FORWARD, 1)
```

Write the fixed line:

<div class="write-space short"></div>

Why was it wrong?

<div class="write-space short"></div>

---

## 5 · Show Your Work 📸🎥

Go to your homework world. Solve the maze using **one AND** and **one OR**. Come back here.

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
