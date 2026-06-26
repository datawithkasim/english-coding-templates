# 🎨 M000 Week 0 — English Worksheet

**Topic:** Pixel Art — Counting Squares · **Course:** Builder Basics · **Type:** Warm-Up (before Week 1) · **Time:** about 40 minutes

Every block in Minecraft has three numbers: **X** (left ↔ right), **Y** (up ↕ down), and **Z** (depth, in ↔ out). Pixel art sits on a flat wall, so **Z stays the same** the whole time — you only change **X** and **Y**.

> 🌱 This is a quick warm-up to do **before Week 1**. It teaches you to count squares so your builds line up perfectly.

---

## 1 · Read the Wall 🔍

Open the **Pixel Art** world. In front of you is a flat wall with red pixel art on it.

Think of the wall like graph paper:

- **X** counts the columns, left to right →
- **Y** counts the rows, bottom to top ↑
- **Z** is how deep the wall is. It is the **same** for every red square, so we can ignore it here.

Every red shape you build needs two corners: a **START** and an **END**. The rest of this worksheet is one skill — **how to count to those two corners.**

**Look at the wall and find the smallest red mark — a single square. Do you think its START and its END are the same spot, or two different spots?**

<div class="write-space"></div>

---

## 2 · Find START and END — Step by Step 🧭

Here is the recipe. Use it for **every** straight line or square.

> **① Count X across** (left → right): 0, 1, 2, 3 … Find the column where the red **begins** and where it **ends**.
> **② Count Y up** (bottom → top): 0, 1, 2, 3 … Find the row where the red **begins** and where it **ends**.
> **③ START = (left X, bottom Y).   END = (right X, top Y).**
> **④ Same-number check:** 1 square **wide** → START X = END X. 1 square **tall** → START Y = END Y.

In the grids below: **🟩 START · 🟥 END · 🟧 in between · 🟪 START and END are the same square.**

### Case 1 — A single square

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **3** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **2** | ⬜ | ⬜ | ⬜ | 🟪 | ⬜ |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

- **① Count X:** 0, 1, 2, **3** → red begins at X 3 and ends at X 3.
- **② Count Y:** 0, 1, **2** → red begins at Y 2 and ends at Y 2.
- **③ START = (3, 2).   END = (3, 2).**
- **④** 1 wide **and** 1 tall → START and END are the **same square**. 🟪

**Blocks**

```
fill  [ 🟥 red wool ]
  from   world   X 3   Y 2   Z 0
  to     world   X 3   Y 2   Z 0
```

**Python**

```python
blocks.fill(RED_WOOL, world(3, 2, 0), world(3, 2, 0), FillOperation.Replace)
```

> 💡 For a single block you can also use `blocks.place(RED_WOOL, world(3, 2, 0))` — place needs only **one** spot, because there is nothing to count.

### Case 2 — A line lying down (1 tall)

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **3** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **2** | ⬜ | 🟩 | 🟧 | 🟥 | ⬜ |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

- **① Count X:** red fills columns **1, 2, 3** → begins at X 1, ends at X 3.
- **② Count Y:** red is only in row **2** → begins at Y 2, ends at Y 2.
- **③ START = (1, 2).   END = (3, 2).**
- **④** 1 tall → **START Y = END Y = 2** (same Y!).

**Python**

```python
blocks.fill(RED_WOOL, world(1, 2, 0), world(3, 2, 0), FillOperation.Replace)
```

### Case 3 — A line standing up (1 wide)

| Y \ X | 0 | 1 | 2 |
|---|---|---|---|
| **3** | ⬜ | 🟥 | ⬜ |
| **2** | ⬜ | 🟧 | ⬜ |
| **1** | ⬜ | 🟩 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ |

- **① Count X:** red is only in column **1** → begins at X 1, ends at X 1.
- **② Count Y:** red fills rows **1, 2, 3** → begins at Y 1, ends at Y 3.
- **③ START = (1, 1).   END = (1, 3).**
- **④** 1 wide → **START X = END X = 1** (same X!).

**Python**

```python
blocks.fill(RED_WOOL, world(1, 1, 0), world(1, 3, 0), FillOperation.Replace)
```

> 🔑 **The big idea:** when a shape is **1 square thick**, one number does **not** change — START and END share it. That is correct, not a mistake.

---

## 3 · Your Turn: Find START and END ✏️

Use the recipe (count X across, count Y up). For each shape, write START, END, and circle the number that is the **same**.

### Shape A

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | ⬜ | 🟪 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ |

**START = ( ___ , ___ )    END = ( ___ , ___ )    Same number:  X  ·  Y  ·  both**

<div class="write-space short"></div>

### Shape B

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **3** | 🟩 | 🟧 | 🟥 | ⬜ |
| **2** | ⬜ | ⬜ | ⬜ | ⬜ |

**START = ( ___ , ___ )    END = ( ___ , ___ )    Same number:  X  ·  Y  ·  both**

<div class="write-space short"></div>

### Shape C

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | 🟥 |
| **1** | ⬜ | ⬜ | ⬜ | 🟧 |
| **0** | ⬜ | ⬜ | ⬜ | 🟩 |

**START = ( ___ , ___ )    END = ( ___ , ___ )    Same number:  X  ·  Y  ·  both**

<div class="write-space short"></div>

---

## 4 · Count the Length 🔢

Counting squares has a trap. From **X = 2** to **X = 5** is **not** 5 squares — it is **2, 3, 4, 5 = 4 squares**. You count the START square too.

> **Length = (END − START) + 1.**
> So to make a line **N** long starting at X, the END is **X + (N − 1)** — not X + N.

**You want a line lying down that is 3 squares long, starting at X = 1 (Y stays 2). What is the END X?**

<div class="write-space short"></div>

**Now write the fill for it — blocks or python, your choice:**

<div class="write-space short"></div>

**You want a line standing up, 5 squares tall, starting at Y = 0 (X stays 6). What is the END Y?**

<div class="write-space short"></div>

---

## 5 · Spot the Bug 🐛

Each command was meant to do one thing, but it is wrong. Rewrite it so it works, then explain why the original was wrong.

**Bug A** — Meant to color **one** square at X 4, Y 4.

```python
blocks.fill(RED_WOOL, world(4, 4, 0), world(5, 5, 0), FillOperation.Replace)
```

**Hint:** count how many squares `(4,4)` to `(5,5)` really covers.

**Write the fixed command:**

<div class="write-space short"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space short"></div>

**Bug B** — Meant to make a line lying down **3** squares long starting at X 0 (Y stays 1).

```python
blocks.fill(RED_WOOL, world(0, 1, 0), world(3, 1, 0), FillOperation.Replace)
```

**Write the fixed command:**

<div class="write-space short"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space short"></div>

**Bug C** — Meant to make a line **standing up**, 4 tall at X 2, starting Y 0.

```python
blocks.fill(RED_WOOL, world(2, 0, 0), world(5, 0, 0), FillOperation.Replace)
```

**Hint:** for a standing line, which number should change — X or Y?

**Write the fixed command:**

<div class="write-space short"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space short"></div>

---

## 6 · Build It 📸

Now switch to your homework world. Recreate the red wall. Start with the single squares (START = END), then the lines lying down, then the lines standing up. Do as much of the wall as you like.

Send a photo or video of your wall, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My first square had START at X … , Y … and END at the same spot because …
>
> To find START and END I counted …
>
> To make a line … long, I counted …
>
> The hardest part was …
>
> To fix it, I …
>
> Next time I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 7 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you build one square and one line. Talk through it like you are teaching someone who has never seen it. Try to use these words: **X**, **Y**, **START**, **END**, **same**, **fill**.

> 1. Show the empty wall and point out X (across) and Y (up).
> 2. Color one square. Count to its START and END out loud and say why they are the same.
> 3. Make a line. Count to its START and END out loud.
> 4. Show one counting mistake and how you fixed it.

**Write what you will say in your video.** Plan it below before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
