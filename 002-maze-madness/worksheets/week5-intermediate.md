# 🧊 M002 Week 5 — Mini Cube Puzzle

**Topic:** Mini Cube Puzzle · **Course:** Maze Madness · **Level:** Intermediate · **Time:** about 35 minutes

Finish the mini cube. Add a conditional, fill every layer, then break the top and climb out.

---

## 1 · Predict 🔮

Read the steps. Write what happens.

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

The agent should move up one block. Match the plain words to the API.

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

## 5 · Finish the Cube 📸🎥

Open this week's world. Find the **mini cube starter** — part is built.

1. Keep the starter going.
2. Add one conditional that uses `OR`.
3. Fill every layer.
4. Break a hole in the top and climb out.

Send a photo or video of the finished cube and the hole. Then finish:

> To keep building, I …
>
> I used a conditional when …
>
> I made the hole by …

<div class="write-space tall" style="min-height: 240px"></div>

**Phone video plan.** Film the agent building. Use these words: **cube**, **layer**, **conditional**, **OR**, **hole**.

> 1. Show the starter cube.
> 2. Run your code and watch it fill.
> 3. Read your conditional out loud.
> 4. Show the hole and the climb out.

**Write what you will say:**

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
