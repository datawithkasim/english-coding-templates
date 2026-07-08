# 🎢 005 Week 2 — English Worksheet (Beginner)

**Topic:** One Function, Many Booths — Arguments & Parameters · **Course:** Theme Park Creator · **Level:** Beginner · **Time:** about 30 minutes

This week you build a park **booth** with a **function**. You give it **parameters** — words and numbers — and change them to build wood or stone booths, big or small.

These are the blocks you use this week:

```python
blocks.fill(OAK_PLANKS, pos(0, 0, 0), pos(4, 0, 4), FillOperation.HOLLOW)
```

> `blocks.fill(...)` fills a box between two corners.
> The first word is the **material** (like `OAK_PLANKS` or `STONE_BRICKS`).
> `pos(x, y, z)` is a spot: `x` = left/right, `y` = up, `z` = forward/back.
> `FillOperation.HOLLOW` builds only the **walls** and leaves the middle empty.

---

## 1 · Meet Arguments and Parameters 🎁

A **parameter** is an empty named box. An **argument** is what you drop in — same boxes with different stuff make different booths.

```text
   WHEN YOU MAKE IT — the names in ( ) are PARAMETERS (empty boxes):

       def build_booth( wall , size ):

   WHEN YOU CALL IT — the values in ( ) are ARGUMENTS (real stuff):

       build_booth( OAK_PLANKS , 4 )

   They line up by position, left to right:

       1st box   wall  ⟵  1st value   OAK_PLANKS
       2nd box   size  ⟵  2nd value   4
```

**Which one is the empty named box? Circle one:** parameter · argument

---

## 2 · Predict 🔮

Read the code. Circle your answer.

```python
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)

build_booth(STONE_BRICKS, 4)
```

**What is the booth, and how wide? Circle one:** STONE_BRICKS, 4 · OAK_PLANKS, 4 · STONE_BRICKS, 0

```python
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)
```

**There is no call after the definition. Does a booth get built? Circle one:** yes · no

---

## 3 · Find the Difference 🐛

Clean code first, then a broken version. Circle the answer.

**Pair A** — The function should be **called** so a booth appears.

```python
# clean
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)

build_booth(OAK_PLANKS, 4)
```

```python
# buggy
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)
```

**What is wrong? Circle one:** no call after `def` · wrong material · wrong size

**Pair B** — The booth should be made of whatever material you send in.

```python
# clean
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)
```

```python
# buggy
def build_booth(wall, size):
    blocks.fill(STONE_BRICKS, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)
```

**What is wrong? Circle one:** it uses `STONE_BRICKS`, not `wall` · it uses `wall`, not `STONE_BRICKS` · nothing

---

## 4 · Fill the Gap ✏️

This booth should be the size you send in. One word is missing — the **parameter** it forgot to use.

```python
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(____, 0, ____), FillOperation.HOLLOW)

build_booth(OAK_PLANKS, 6)
```

**Which word is missing? Circle one:** `size` · `wall` · `HOLLOW`

---

## 5 · Show Your Work 📸🎥

Switch to your homework world. Write one `build_booth` function with a `wall` parameter and a `size` parameter, then call it two times with different materials or sizes.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Say these out loud, filling in the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
