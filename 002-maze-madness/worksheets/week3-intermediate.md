# 🔗 M002 Week 3 — AND Conditions

**Topic:** AND — two things both true · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

`AND` checks two things. The action runs only when **both** are true.

---

## 1 · Predict 🔮

```
if wall ahead AND wall on right:
    turn left
```

Both true. The agent does what?

<div class="write-space short"></div>

```
if no wall ahead AND no wall below:
    move forward
```

Path ahead is clear, but a wall is below. Does it move? Why?

<div class="write-space short"></div>

---

## 2 · Trace 🔍

```
keep doing forever:
    if wall ahead AND wall on right:
        turn left
    otherwise:
        move forward
```

At a corner (wall ahead AND wall on right), what happens?

<div class="write-space short"></div>

At an open path, what happens?

<div class="write-space short"></div>

---

## 3 · Fill the Code ✏️

Turn left only when both walls are there. Fill the blanks.

```
if agent.detect(BLOCK, FORWARD) ____ agent.detect(BLOCK, RIGHT):
    agent.turn(____)
```

<div class="write-space short"></div>

---

## 4 · Spot the Bug 🐛

Should turn left only at a corner: wall ahead AND wall on right.

```
if agent.detect(BLOCK, FORWARD):
    agent.turn(LEFT_TURN)
```

Write the fix:

<div class="write-space"></div>

Why was it wrong?

<div class="write-space short"></div>

---

## 5 · Show It 📸

Solve the maze with one `AND`. Send a photo or video of the agent at the end. Then finish these.

> I used **AND** when …
>
> Both were true when …
>
> One tricky part was …

<div class="write-space tall" style="min-height: 240px"></div>

**Phone video plan.** Plan what you will say, then record.

> 1. Show the start. Run your code.
> 2. Read your `if … AND …` line out loud.
> 3. Say what **AND** means.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
