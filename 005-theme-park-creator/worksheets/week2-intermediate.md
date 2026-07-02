# 🎢 005 Week 2 — English Worksheet (Intermediate)

**Topic:** One Function, Many Booths — Arguments & Parameters · **Course:** Theme Park Creator · **Time:** about 45 minutes

This week you build a park **booth** with a **function**. You give it **parameters** — the materials and the size it should use — so the **same** function can build a wood booth, a stone booth, a big one or a small one, just by changing the **arguments** you **call** it with.

These are the blocks you use this week:

```python
blocks.fill(OAK_PLANKS, pos(0, 0, 0), pos(4, 0, 4), FillOperation.HOLLOW)
blocks.fill(STONE, pos(0, 0, 0), pos(4, 0, 4), FillOperation.REPLACE)
blocks.fill(AIR, pos(2, 0, 0), pos(2, 1, 0), FillOperation.REPLACE)
```

> `blocks.fill(material, corner1, corner2, ...)` fills a box between two corners.
> `pos(x, y, z)` is a spot: `x` = left/right, `y` = up, `z` = forward/back.
> `FillOperation.HOLLOW` = only the outer **walls**. `FillOperation.REPLACE` = the **whole solid** box.
> `AIR` = empty space. Fill a slot with `AIR` to **carve a doorway** out of a wall.

---

## 1 · Meet Arguments and Parameters 🎁

A **parameter** is an empty box with a name — you make it when you *define* the function.
An **argument** is the real value you drop into that box — you send it when you *call* the function.
They line up **by position**, left to right.

```text
   MAKE IT  →  the names in ( ) are PARAMETERS (empty named boxes):

       def build_booth( wall , floor , size ):

   CALL IT  →  the values in ( ) are ARGUMENTS (real values sent in):

       build_booth( OAK_PLANKS , STONE , 5 )

   Position matches — 1st→1st, 2nd→2nd, 3rd→3rd:

       wall   ⟵  OAK_PLANKS     (1st box gets the 1st value)
       floor  ⟵  STONE          (2nd box gets the 2nd value)
       size   ⟵  5              (3rd box gets the 3rd value)
```

**Why does one function with parameters let you build many different booths?**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each function. Before you imagine the booth, write what you think happens.

```python
def build_booth(wall, floor, size):
    blocks.fill(floor, pos(0, 0, 0), pos(size, 0, size), FillOperation.REPLACE)
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)

build_booth(OAK_PLANKS, STONE, 5)
```

**What material is the floor? What material are the walls? How wide is the booth?**

<div class="write-space"></div>

```python
def build_booth(wall, floor, size):
    blocks.fill(floor, pos(0, 0, 0), pos(size, 0, size), FillOperation.REPLACE)
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)

build_booth(GLASS, STONE, 3)
build_booth(BRICKS, OAK_PLANKS, 8)
```

**The same function is called twice with different arguments. Are the two booths the same? Which one is bigger?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block was meant to do something but is broken. Read what it is **supposed** to do, rewrite it so it works, then explain why the original was wrong.

**Bug A** — This should build one booth. But when you run it, **nothing happens at all**.

```python
def build_booth(wall, floor, size):
    blocks.fill(floor, pos(0, 0, 0), pos(size, 0, size), FillOperation.REPLACE)
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)
```

**Hint:** writing `def` only **teaches** the function. Something is missing after it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The booth should be as wide as the number you send in. But `build_booth(OAK_PLANKS, STONE, 9)` and `build_booth(OAK_PLANKS, STONE, 2)` build the **same size** every time.

```python
def build_booth(wall, floor, size):
    blocks.fill(floor, pos(0, 0, 0), pos(4, 0, 4), FillOperation.REPLACE)
    blocks.fill(wall, pos(0, 0, 0), pos(4, 3, 4), FillOperation.HOLLOW)

build_booth(OAK_PLANKS, STONE, 9)
```

**Hint:** look at the numbers inside. The function never uses `size`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should build a **stone floor** with **glass walls**. But it comes out with glass on the floor and stone walls — the wrong way around.

```python
def build_booth(wall, floor, size):
    blocks.fill(floor, pos(0, 0, 0), pos(size, 0, size), FillOperation.REPLACE)
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)

build_booth(STONE, GLASS, 5)
```

**Hint:** the arguments line up with the parameters **by position**. Which value landed in which box?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Build the Booth 🏪

Now the real challenge. In your homework world, write **one** function called `build_booth` that builds a booth a visitor can walk into. Your function must have these **three parameters**:

```python
def build_booth(wall, floor, size):
```

Your booth must include:

- a **floor** made from the `floor` material, `size` wide
- **walls** made from the `wall` material (use `FillOperation.HOLLOW` so the middle stays empty)
- a **doorway** carved out of one wall with `AIR` so a visitor can walk in

Then **call your function twice** with different materials and sizes, for example:

```python
build_booth(OAK_PLANKS, STONE, 5)
build_booth(BRICKS, OAK_PLANKS, 8)
```

**Write your finished `build_booth` function and the two lines that call it:**

<div class="write-space tall" style="min-height: 360px"></div>

---

## 5 · Tell Me What You Built 📸

When your two booths stand side by side, send a photo or video and explain what you did. Use these sentence starters — write 4 to 6 sentences.

> My three parameters were …
>
> The argument that changed the booth the most was …
>
> To carve the doorway I …
>
> The same function built two different booths because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) of your code and your booths. Talk it through like you are teaching someone who has never seen it. Try to use these words: **function**, **parameter**, **argument**, **call**, **position**.

> 1. Show your `build_booth` function and read the line with the three **parameters** out loud.
> 2. Point at one parameter and say what it controls.
> 3. Run a **call** and show the booth appear, then run another with different **arguments**.
> 4. Say in your own words how parameters and arguments line up by **position**.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
