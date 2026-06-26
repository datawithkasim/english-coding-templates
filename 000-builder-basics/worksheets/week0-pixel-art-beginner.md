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

Every red shape has a **START** and an **END**. This worksheet shows you how to count to them.

**Find the smallest red mark on the wall. Circle one — is it 1 square or 2 squares?**   1   ·   2

<div class="write-space short"></div>

---

## 2 · Find START and END 🧭

Two steps find any square's spot:

> **Step ① — Count across (→) for X.**  0, 1, 2, 3 …
> **Step ② — Count up (↑) for Y.**  0, 1, 2, 3 …

The red square below is **🟪**.

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | ⬜ | 🟪 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ |

- **Count across:** 0, 1, **2** → X = 2.
- **Count up:** 0, **1** → Y = 1.
- **START = (2, 1).   END = (2, 1).**
- It is **one** square, so START and END are the **same**. 🟪

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

**This square is 1 wide and 1 tall. Circle one — are START and END the same or different?**   same   ·   different

<div class="write-space short"></div>

---

## 3 · Find START and END of a Line 🧭

A line lying down has a **START** on the left and an **END** on the right.

In the grid: **🟩 START · 🟥 END · 🟧 in between.**

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | 🟩 | 🟧 | 🟥 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

- **Count across:** red begins at X **1** and ends at X **3**.
- **Count up:** red is in row **1** only → Y = **1** for both.
- **START = (1, 1).   END = (3, 1).**
- It is **1 tall**, so the **Y is the same** (1) for START and END.

**Fill the blanks:  START = ( ___ , ___ )    END = ( ___ , ___ )**

<div class="write-space short"></div>

**Circle the number that is the SAME for START and END:**   X   ·   Y

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

You want a line lying down, **3** squares long. It starts at **X = 1** and sits on **Y = 2**. One number is missing.

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **2** | ⬜ | 🟩 | 🟧 | 🟥 | ⬜ |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

```python
blocks.fill(RED_WOOL, world(1, 2, 0), world(__, 2, 0), FillOperation.Replace)
```

**Word bank:**  `2`  ·  `3`  ·  `4`

**Write the missing END number (count across to the 🟥):**

<div class="write-space short"></div>

---

## 6 · Tell Me What You Built 📸

Now switch to your homework world. Color **one single square**, then make **one short line**. When you finish, come back here.

Send a photo or video, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My square had START at X … , Y …
>
> For one square, my START and END were …
>
> Then I made a line. Its START was … and its END was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 7 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and show your wall. Talk like you are teaching a friend. Try to use these words: **X**, **Y**, **START**, **END**, **same**.

> 1. Show the square you colored.
> 2. Count to its START and END out loud and say why they are the same.
> 3. Show your line and count to its START and END.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
