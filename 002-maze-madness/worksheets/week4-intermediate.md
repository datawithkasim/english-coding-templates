# 🔀 M002 Week 4 — AND / OR

**Topic:** AND and OR Conditions · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

Last week you used `AND` (both true). This week you add `OR` (one is enough) and mix them.

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

## 5 · Finish + Show 📸

Go to your homework world. Solve the maze using **one AND** and **one OR**. Come back here.

Send a photo or video of the agent at the end. Write 3 or 4 lines.

> I used **AND** when …
>
> I used **OR** when …
>
> One tricky part was …
>
> I fixed it by …

<div class="write-space tall" style="min-height: 240px"></div>

**Video plan.** Film the maze on your phone. Plan your words first, then record.

> 1. Run your code from the start.
> 2. Read your `and` line and your `or` line out loud. Say what makes each run.
> 3. Say how **AND** is different from **OR**.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
