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

The big idea for this whole worksheet:

> 🟥 To color **one** square, your **start** and your **end** are the **same** square.
> A 1-wide, 1-tall block goes **from (X, Y) to the same (X, Y)**.

**Look at the wall and find the smallest red mark — a single square. In your own words, why are its start and its end the same?**

<div class="write-space"></div>

---

## 2 · One Square: Start = End 🟥

Here is a grid. **X** runs across the top, **Y** runs up the side. One square is red.

| Y \ X | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **3** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **2** | ⬜ | ⬜ | ⬜ | 🟥 | ⬜ | ⬜ |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

The red square is at **X = 3, Y = 2**. Here is the same command two ways — in **blocks** and in **python**:

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

Look closely: the **from** and the **to** are **exactly the same** — `(3, 2, 0)` and `(3, 2, 0)`. One square in, one square colored.

> 💡 For a single block you can also use `blocks.place(RED_WOOL, world(3, 2, 0))` — place needs only **one** spot, because there is nothing to count.

**A single block has the same start and end. So why does `fill` make you write the numbers twice instead of once?**

<div class="write-space"></div>

---

## 3 · Predict 🔮

Read each command. Before you picture it, write how many squares turn red and where.

```python
blocks.fill(RED_WOOL, world(2, 1, 0), world(2, 1, 0), FillOperation.Replace)
```

**How many squares turn red? Where?**

<div class="write-space short"></div>

```python
blocks.fill(RED_WOOL, world(2, 1, 0), world(5, 1, 0), FillOperation.Replace)
```

**Y stays 1. X goes 2 → 5. How many squares turn red? List every X number it covers.**

<div class="write-space short"></div>

```python
blocks.fill(RED_WOOL, world(4, 0, 0), world(4, 3, 0), FillOperation.Replace)
```

**X stays 4. Y goes 0 → 3. Is this line flat or standing up? How tall is it?**

<div class="write-space short"></div>

---

## 4 · Count the Length 🔢

Counting squares has a trap. From **X = 2** to **X = 5** is **not** 5 squares — it is **2, 3, 4, 5 = 4 squares**. You count the start square too.

> **Length = (end − start) + 1.**
> So to make a line **N** long starting at X, the end is **X + (N − 1)** — not X + N.

**You want a flat red line that is 3 squares long, starting at X = 1 (Y stays 2). What is the end X?**

<div class="write-space short"></div>

**Now write the fill for it — blocks or python, your choice:**

<div class="write-space short"></div>

**You want a line standing up, 5 squares tall, starting at Y = 0 (X stays 6). What is the end Y?**

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

**Bug B** — Meant to make a flat line **3** squares long starting at X 0 (Y stays 1).

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

Now switch to your homework world. Recreate the red wall. Start with the single squares (start = end), then the flat lines, then the standing lines. Do as much of the wall as you like.

Send a photo or video of your wall, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The first square I colored was at X … , Y …
>
> For one square, my start and end were the same because …
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

Take a video on your phone (or a parent's phone) while you build one square and one line. Talk through it like you are teaching someone who has never seen it. Try to use these words: **X**, **Y**, **start**, **end**, **same**, **fill**.

> 1. Show the empty wall and point out X (across) and Y (up).
> 2. Color one square and say why the start and the end are the same.
> 3. Make a line and count the squares out loud.
> 4. Show one counting mistake and how you fixed it.

**Write what you will say in your video.** Plan it below before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
