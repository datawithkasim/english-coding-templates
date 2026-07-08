# 🎢 005 Week 1 — English Worksheet

**Topic:** One Function, Many Coasters — Parameters · **Course:** Theme Park Creator · **Time:** about 45 minutes

This week you build a roller coaster with a **function**. You give it **parameters** — numbers it uses inside — and change them to build a long coaster, a tall spiral, or a wide one.

These are the blocks you use this week:

```python
rollerCoasterBuilder.add_straight_line(10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, TurnDirection.LEFT, 10, 3)
rollerCoasterBuilder.add_turn(TurnDirection.LEFT)
```

> `add_spiral(...)`'s last two numbers are the **height** then the **width** of the spiral.
> A direction is `UP` or `DOWN`. A turn is `LEFT` or `RIGHT`.

---

## 1 · Predict 🔮

Read each function. Write what you think will happen.

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)

build_hill(8)
```

**The parameter `line_len` is used twice. How long is the straight part, and how tall is the ramp?**

<div class="write-space"></div>

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)

build_hill(4)
build_hill(12)
```

**The same function is called twice with different numbers. Are the two hills the same size? Which one is bigger?**

<div class="write-space"></div>

```python
def build_spiral(spiral_height, spiral_width):
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, TurnDirection.LEFT, spiral_height, spiral_width)

build_spiral(10, 3)
```

**This function has two parameters. Which number sets how *tall* the spiral is, and which sets how *wide*?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block is broken. Read what it should do, rewrite it so it works, then explain why the original was wrong.

**Bug A** — The code should build a hill 8 long. But when you run it, **nothing happens at all**.

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)
```

**Hint:** writing `def` only **teaches** the function. Something is missing after it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The function should build a hill as long as the number you give it. But `build_hill(20)` and `build_hill(3)` build the **same** hill every time.

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(10)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)

build_hill(20)
```

**Hint:** look at the numbers inside. The function never actually uses `line_len`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This coaster should go **up** and then come back **down** so the cart returns to ground level. But it just keeps climbing into the sky and never comes down.

```python
def up_and_down(ramp_len):
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, ramp_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, ramp_len)

up_and_down(10)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build the Loop Coaster 🎢

In your homework world, write **one** function called `loop_coaster` that builds a coaster which **loops all the way back to the starting area**. Your function must have these **four parameters**:

```python
def loop_coaster(line_len, ramp_len, spiral_height, spiral_width):
```

Your coaster must include, in total:

- **2 ramps** — one going **UP**, one coming back **DOWN**
- **2 spirals** — one going **UP**, one coming back **DOWN**
- enough **turns** that the track curves around and ends back where it started

Here are the building blocks. They use **fixed numbers** and point the **same way** — fix that:

```python
rollerCoasterBuilder.add_straight_line(10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, TurnDirection.LEFT, 10, 3)
rollerCoasterBuilder.add_turn(TurnDirection.LEFT)
```

To finish the challenge you must:

1. **Swap the numbers for parameters** — replace `10`, `10`, `10`, `3` with `line_len`, `ramp_len`, `spiral_height`, `spiral_width` so the size is controlled by the call.
2. **Flip the directions on the way back** — change the second ramp and the second spiral from `UP` to `DOWN` so the cart returns to ground level.
3. **Add turns** — keep adding `add_turn(TurnDirection.LEFT)` until the track curves around and meets the start. Add or remove a turn until it closes the loop.

Finally, **call your function once** with numbers you choose, for example:

```python
loop_coaster(8, 10, 10, 3)
```

**Write your finished `loop_coaster` function and the line that calls it:**

<div class="write-space tall" style="min-height: 360px"></div>

---

## 4 · Show Your Work 📸🎥

When your coaster loops back to the start, ride it once in your world.

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
