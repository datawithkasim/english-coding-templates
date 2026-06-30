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

This checks for a wall and turns. Fill the two blanks.

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

## 5 · Finish the Maze 📸

Open your homework world. Use `if` / `else` to turn at walls. Get the agent out.

Take a photo or video at the maze end.

**Phone video plan — say each line out loud:**

> The wall was on my …
>
> I used `agent.turn(…)` to …
>
> My agent got stuck when …
>
> I fixed it by …

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
