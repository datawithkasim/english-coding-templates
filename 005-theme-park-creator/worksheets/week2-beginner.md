# 🎢 005 Week 2 — English Worksheet (Beginner)

**Topic:** One Function, Many Booths — Arguments & Parameters · **Course:** Theme Park Creator · **Level:** Beginner · **Time:** about 30 minutes

This week you build a small park **booth** with a **function**. You give the function some **parameters** — words and numbers it uses inside — so the same function can build a wood booth, a stone booth, a big one, or a small one, just by changing what you **call** it with.

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

A **parameter** is an empty box with a name. An **argument** is what you drop into that box.
Same boxes, different stuff → **same function, different booths**.

```text
   WHEN YOU MAKE IT — the names in ( ) are PARAMETERS (empty boxes):

       def build_booth( wall , size ):

   WHEN YOU CALL IT — the values in ( ) are ARGUMENTS (real stuff):

       build_booth( OAK_PLANKS , 4 )

   They line up by position, left to right:

       1st box   wall  ⟵  1st value   OAK_PLANKS
       2nd box   size  ⟵  2nd value   4
```

**In your own words: what is a parameter? What is an argument?**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read the code. Before you imagine the booth, write your answer.

```python
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)

build_booth(STONE_BRICKS, 4)
```

**What material is the booth made of, and how wide is it?**

<div class="write-space short"></div>

```python
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 0, size), FillOperation.HOLLOW)
```

**There is no call after the definition. Does a booth get built? Circle one:** yes · no

---

## 3 · Find the Difference 🐛

Each pair shows clean code first, then a broken version. Circle what's different and write one short sentence about the bug.

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

**What is wrong? Why does the buggy code build nothing?**

<div class="write-space short"></div>

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

**What is wrong? Why is every booth stone, even when you send in `OAK_PLANKS`?**

<div class="write-space short"></div>

---

## 4 · Fill the Gap ✏️

This function should build a booth the size of the number you send in. One word is missing — the **parameter** the function forgot to use. Fill it in from the word bank.

```python
def build_booth(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(____, 0, ____), FillOperation.HOLLOW)

build_booth(OAK_PLANKS, 6)
```

**Word bank:** `size` · `wall` · `HOLLOW`

**Write the missing word:**

<div class="write-space short"></div>

---

## 5 · Tell Me What You Built 📸

Now switch to your homework world. Write one `build_booth` function with a `wall` parameter and a `size` parameter, then call it two times with different materials or sizes. When you finish, come back here.

Send a photo or video of your booths, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My function's two parameters were …
>
> When I called it with a different material, …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your code builds the booth. Talk like you are teaching a friend. Try to use these words: **function**, **parameter**, **argument**, **call**.

> 1. Show your function and run your code.
> 2. Show two booths built with different values.
> 3. Say in your own words what a **parameter** is and what an **argument** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
