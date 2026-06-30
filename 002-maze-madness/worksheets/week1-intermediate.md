# 🌀 M002 Week 1 — While Loop

**Topic:** Repeat Until a Wall · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

A while loop repeats. It checks first, then moves. It stops at a wall.

---

## 1 · Trace It 🔮

```
while no wall ahead:
    move forward
```

**The wall is 4 steps away. How many times does the agent move?**

<div class="write-space short"></div>

---

## 2 · Real Code 🤖

This is the real check.

```
while not agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

`agent.detect(BLOCK, FORWARD)` is true when a wall is ahead.

**Fill the blanks:**

```
while not agent.detect(BLOCK, ____):
    agent.____(FORWARD, 1)
```

<div class="write-space short"></div>

---

## 3 · Fix the Bug 🐛

The agent should move until the wall. This is backwards.

```
while agent.detect(BLOCK, FORWARD):
    agent.move(FORWARD, 1)
```

**Write the fix:**

<div class="write-space"></div>

---

## 4 · Write It ✏️

Make the agent move forward until a wall, then turn right.

> Use `while`, `agent.detect`, `agent.move`, `agent.turn`.

<div class="write-space"></div>

---

## 5 · Finish the Maze 📸

Open your homework world. Use a while loop. Move the agent down the straight maze to the wall.

Send a photo OR video of the agent at the wall. Then write 2-3 sentences.

> My loop checked …
>
> The agent stopped because …
>
> A while loop helps because …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Video Plan 🎥

Record on a phone while the agent runs. Use: **while**, **loop**, **detect**, **wall**.

> 1. Run your code.
> 2. Read your loop. Say what stops it.
> 3. Say why a loop beats many `move` lines.

**Plan your words:**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
