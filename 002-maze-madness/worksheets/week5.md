# 🧊 M002 Week 5 — Mini Cube Puzzle

**Topic:** Mini Cube Puzzle · **Course:** Maze Madness · **Level:** Advanced · **Time:** about 55 minutes

Finish the mini cube. Keep the starter going: add **2 more conditionals** with **one `OR`**, fill the cube, then break a hole in the **top** and climb out.

---

## 1 · Predict 🔮

Write what happens.

```python
for i in range(5):
    agent.place(BLOCK)
    agent.move(FORWARD, 1)
```

**What shape is left behind? How long is it?**

<div class="write-space"></div>

```python
if on_edge or on_top_layer:
    agent.place(BLOCK)
else:
    pass  # leave empty
```

**Only one condition must be true. Which spots get a block? Which stay empty?**

<div class="write-space"></div>

---

## 2 · Trace 👣

```python
for layer in range(3):
    fill_layer()
    agent.move(UP, 1)
if agent.detect(BLOCK, UP):
    # break above, then climb
    agent.move(UP, 1)
```

**How many layers fill? Where does the agent end up? Is there still a block above it?**

<div class="write-space"></div>

---

## 3 · Spot + Fix the Bugs 🐛

**Bug A** — The agent should place blocks across the layer, **then** move up. It moves up too early.

```python
agent.place(BLOCK)
agent.move(UP, 1)
agent.place(BLOCK)
agent.place(BLOCK)
```

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Place a block when on the **bottom layer** `OR` on an **outer wall**. It only checks the bottom.

```python
if on_bottom_layer:
    agent.place(BLOCK)
```

**Hint:** add the wall check with `or`.

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — To climb out, break the block above **first**, then move up. It moves up into solid block and gets stuck.

```python
agent.move(UP, 1)
agent.destroy(UP)
```

**Hint:** make the hole, then move into it.

**Fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Write Code ✍️

Write a loop that fills **one layer**: place a block, move forward, repeat 4 times.

<div class="write-space"></div>

Write a conditional that uses `or`: if the agent is on a **corner** `OR` on the **top**, place a block.

<div class="write-space"></div>

---

## 5 · Show Your Work 📸🎥

Open this week's world. Find the **mini cube starter** — part is built.

1. Keep the starter running.
2. Add **2 more conditionals** that decide where blocks go.
3. Make **one** use `or` (e.g. corner `OR` top → place glass).
4. Break a hole in the **top** and climb out.

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
