# 🧭 M002 Week 2 — Turning (Advanced)

**Topic:** Turn at Walls · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

The rule: wall ahead, turn. No wall, move forward. This week you write the real code.

---

## 1 · Trace It 🔮

```python
while True:
    if agent.detect(BLOCK, FORWARD):
        agent.turn(RIGHT_TURN)
    else:
        agent.move(FORWARD, 1)
```

**Say what the agent does each loop.**

<div class="write-space"></div>

---

## 2 · Read the API 📖

| Code | Means |
|---|---|
| `agent.detect(BLOCK, FORWARD)` | wall in front? |
| `agent.turn(RIGHT_TURN)` | turn right |
| `agent.turn(LEFT_TURN)` | turn left |
| `agent.move(FORWARD, 1)` | go forward 1 |

**Write one line: turn left if a wall is on the LEFT.**

<div class="write-space short"></div>

---

## 3 · Spot the Bug 🐛

```python
# A
if agent.detect(BLOCK, FORWARD):
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
```

**What is wrong in A?**

<div class="write-space short"></div>

```python
# B
if agent.detect(BLOCK, LEFT):
    agent.turn(RIGHT_TURN)
else:
    agent.move(FORWARD, 1)
```

**B should turn at a front wall. What is wrong?**

<div class="write-space short"></div>

---

## 4 · Fix It 🔧

Rewrite B so it turns left when a wall is in front, else moves forward.

<div class="write-space"></div>

---

## 5 · Write Full Code ✍️

Loop forever. Wall ahead? Turn right. No wall? Move forward 1.

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Chat Command 💬

`player.on_chat("go", fn)` runs `fn` when you type `go` in chat.

**Write code so typing `go` starts your maze loop.**

<div class="write-space"></div>

---

## 7 · Finish the Maze 📸

Open your homework world. Get the agent out with your turn code.

Take a photo or video at the maze end.

**Phone narration plan — say each line out loud while you show the run:**

> The maze turns where …
>
> I checked `agent.detect(BLOCK, …)` for …
>
> When a wall was ahead I …
>
> My agent got stuck when …
>
> I fixed it by …

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
