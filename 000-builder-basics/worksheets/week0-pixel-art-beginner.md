# 🎨 M000 Week 0 — English Worksheet (Beginner)

**Topic:** Pixel Art — Counting Squares · **Course:** Builder Basics · **Level:** Beginner · **Time:** about 30 minutes

A block in Minecraft has three numbers: **X** (left ↔ right), **Y** (up ↕ down), and **Z** (depth). On a flat wall, **Z stays the same** — you only change **X** and **Y**.

> 🌱 This is a warm-up to do **before Week 1**. It helps you count squares.

---

## 1 · Read the Wall 🔍

Open the **Pixel Art** world. A flat wall has red pixel art on it.

- **X** = the columns, left to right →
- **Y** = the rows, bottom to top ↑
- **Z** = the depth. It stays the **same**, so we ignore it here.

The big idea:

> 🟥 To color **one** square, the **start** and the **end** are the **same** square.

**Find the smallest red mark on the wall. Circle one — is it 1 square or 2 squares?**   1   ·   2

<div class="write-space short"></div>

---

## 2 · One Square: Start = End 🟥

**X** runs across the top. **Y** runs up the side. One square is red.

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | ⬜ | 🟥 | ⬜ | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

The red square is at **X = 2, Y = 1**. Here is the command two ways:

**Blocks**

```
fill  [ 🟥 red wool ]
  from   world   X 2   Y 1   Z 0
  to     world   X 2   Y 1   Z 0
```

**Python**

```python
blocks.fill(RED_WOOL, world(2, 1, 0), world(2, 1, 0), FillOperation.Replace)
```

The **from** and the **to** are the **same**.

**In the python line, the from is `(2, 1, 0)`. What is the to?**

<div class="write-space short"></div>

---

## 3 · Count the Squares 🔢

This line is flat. It sits on **Y = 1** and goes from **X = 1** to **X = 3**.

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | 🟥 | 🟥 | 🟥 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

**Count the red squares. Circle one:**   2   ·   3   ·   4

<div class="write-space short"></div>

**The line covers X = 1, then which numbers? Fill the gaps:**   1 ,  ___ ,  ___

<div class="write-space short"></div>

---

## 4 · Find the Difference 🐛

Both lines look almost the same. One colors **one** square. One colors **four**.

```python
# Line A
blocks.fill(RED_WOOL, world(2, 2, 0), world(2, 2, 0), FillOperation.Replace)
```

```python
# Line B
blocks.fill(RED_WOOL, world(2, 2, 0), world(3, 3, 0), FillOperation.Replace)
```

**Which line colors only ONE square — A or B? Why?**

<div class="write-space short"></div>

---

## 5 · Fill the Gap ✏️

You want a flat line **3** squares long. It starts at **X = 1** and sits on **Y = 2**. One number is missing.

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **2** | ⬜ | 🟥 | 🟥 | 🟥 | ⬜ |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

```python
blocks.fill(RED_WOOL, world(1, 2, 0), world(__, 2, 0), FillOperation.Replace)
```

**Word bank:**  `2`  ·  `3`  ·  `4`

**Write the missing number (look at the grid and count):**

<div class="write-space short"></div>

---

## 6 · Tell Me What You Built 📸

Now switch to your homework world. Color **one single square**, then make **one short line**. When you finish, come back here.

Send a photo or video, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> First, I colored a square at X … , Y …
>
> For one square, my start and end were …
>
> Then I made a line that was … squares long.

<div class="write-space tall" style="min-height: 240px"></div>

---

## 7 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and show your wall. Talk like you are teaching a friend. Try to use these words: **X**, **Y**, **same**, **fill**.

> 1. Show the square you colored.
> 2. Say why the start and the end are the same.
> 3. Show your line and count the squares out loud.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
