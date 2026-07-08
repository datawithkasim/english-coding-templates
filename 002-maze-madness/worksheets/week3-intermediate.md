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

Turn left only when both walls are there.

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

## 5 · Show Your Work 📸🎥

Solve the maze with one `AND`.

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
