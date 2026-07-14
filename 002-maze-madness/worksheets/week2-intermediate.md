# 🧭 M002 Week 2 — Turning (Intermediate)

**Topic:** Turn at Walls · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

The rule: wall ahead, turn. No wall, move forward.

---

## 1 · Trace It 🔮

```
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**Say what the agent does over and over.**

<div class="write-space short"></div>

---

## 2 · Fill the Code ✏️

Checks a wall, then turns. Fill the two blanks.

```
if agent.detect(BLOCK, ________):
    agent.turn(RIGHT_TURN)
else:
    agent.move(________, 1)
```

**Word bank:** `FORWARD` · `RIGHT_TURN` · `LEFT`

<div class="write-space short"></div>

---

## 3 · Spot the Bug 🐛

Turn and move should be in different branches.

```
# buggy
if agent.detect(BLOCK, FORWARD):
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
```

**What is wrong?**

<div class="write-space"></div>

---

## 4 · Write It ✍️

Wall ahead? Turn left. No wall? Move forward 1.

Write 2 lines.

<div class="write-space"></div>

---

## 5 · Show Your Work 📸🎥

Open your homework world. Use `if` / `else` to turn at walls. Get the agent out.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
