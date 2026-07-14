# 🧊 M002 Week 5 — Mini Cube Puzzle

**Topic:** Mini Cube Puzzle · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

Finish the mini cube. Add a conditional, fill every layer, then break the top and climb out.

---

## 1 · Predict 🔮

Write what happens.

```
repeat 5 times:
    place block
    move forward
```

**What shape is left? How long?**

<div class="write-space"></div>

```
if on the edge OR on the top layer:
    place block
otherwise:
    leave empty
```

**Only one part must be true. Which spots get a block?**

<div class="write-space"></div>

---

## 2 · Plain to Code 🔁

Match the plain words to the API.

```
move up one block
```

**Word bank:** `agent.move(UP, 1)` · `agent.move(FORWARD, 1)` · `agent.turn(LEFT_TURN)`

**Write the line:**

<div class="write-space short"></div>

---

## 3 · Trace 👣

```
agent.place(BLOCK)
agent.move(FORWARD, 1)
agent.place(BLOCK)
agent.move(UP, 1)
```

**How many blocks placed? Where does the agent end — on the floor or one up?**

<div class="write-space"></div>

---

## 4 · Spot the Bug 🐛

**Bug A** — The agent should fill the layer, **then** move up. It moves up too soon.

```
agent.place(BLOCK)
agent.move(UP, 1)
agent.place(BLOCK)
```

**Fix it:**

<div class="write-space"></div>

**Bug B** — To climb out, make the hole **first**, then move up. Fix the order.

```
agent.move(UP, 1)
agent.detect(BLOCK, UP)
```

**Hint:** break the block above first.

**Fix it:**

<div class="write-space"></div>

---

## 5 · Show Your Work 📸🎥

Open this week's world. Find the **mini cube starter** — part is built.

1. Keep the starter going.
2. Add one conditional that uses `OR`.
3. Fill every layer.
4. Break a hole in the top and climb out.

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
