# 🎨 Pixel Art — Count the Boxes (Beginner)

**Builder Basics · Warm-Up · about 20 minutes**

We color red boxes on a wall. First we count. 🟥

> 🌱 Do this before Week 1.

---

## 1 · X and Y 👀

Open the **Pixel Art** world. Look at the wall.

Numbers go two ways:

- **X** = across  →
- **Y** = up  ↑

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ |

Top row = **X**.   Side = **Y**.

---

## 2 · One Red Box 🟥

Find the red box. Count to it.

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | ⬜ |
| **1** | ⬜ | ⬜ | 🟥 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ |

Across →   0, 1, **2**.   **X = 2**

Up ↑   0, **1**.   **Y = 1**

> **START = (2, 1)**
>
> **END = (2, 1)**
>
> One box. START and END are the **same**! ✅

This is the code. Two ways:

**Blocks**

```
fill  🟥
  from   X 2   Y 1   Z 0
  to     X 2   Y 1   Z 0
```

**Python**

```python
blocks.fill(RED_WOOL, world(2, 1, 0), world(2, 1, 0))
```

See? `2 1 0` and `2 1 0`. Same!

**Write the box:**   X = ___   Y = ___

<div class="write-space short"></div>

---

## 3 · A Red Line ▬

A line has two ends.

🟩 = START   ·   🟥 = END

| Y \ X | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **1** | ⬜ | 🟩 | 🟧 | 🟥 | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Across →   START at **X 1**.   END at **X 3**.

Up ↑   Both on **Y 1**.

> **START = (1, 1)**
>
> **END = (3, 1)**
>
> Flat line. The **Y is the same**! (1 and 1)

**Write it:**   START = ( ___ , ___ )   END = ( ___ , ___ )

<div class="write-space short"></div>

---

## 4 · Your Turn ✏️

Count the red box. Write the numbers.

| Y \ X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **2** | ⬜ | ⬜ | ⬜ | 🟥 |
| **1** | ⬜ | ⬜ | ⬜ | ⬜ |
| **0** | ⬜ | ⬜ | ⬜ | ⬜ |

**X = ___    Y = ___**

<div class="write-space short"></div>

**One box. Are START and END the same?**   yes  ·  no

<div class="write-space short"></div>

---

## 5 · Build and Show 📸

Go to your world. Color **one** red box.

Take a photo or a video. Say:

> My box is at X … , Y …
>
> START and END are the same.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send to teacher on KakaoTalk.
