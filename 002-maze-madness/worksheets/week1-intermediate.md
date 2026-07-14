# 🌀 M002 Week 1 — While Loop

**Topic:** Repeat Until a Wall · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

A while loop checks first, then moves. It stops at a wall.

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

## 5 · Show Your Work 📸🎥

Open your homework world. Use a while loop to move the agent down the straight maze to the wall.

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
