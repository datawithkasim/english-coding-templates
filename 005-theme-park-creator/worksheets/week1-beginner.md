# 🎢 005 Week 1 — English Worksheet (Beginner)

**Topic:** One Function, Many Coasters — Parameters · **Course:** Theme Park Creator · **Level:** Beginner · **Time:** about 30 minutes

This week you build a roller coaster with a **function**. You give it **parameters** — numbers it uses inside — so the same function can build a long coaster or a short one, just by changing the numbers you **call** it with.

These are the blocks you use this week:

```python
rollerCoasterBuilder.add_straight_line(10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 10)
```

> A direction is `UP` or `DOWN`. The number after it is how many blocks the ramp goes.

---

## 1 · Predict 🔮

Read the code. Before you imagine the cart riding it, circle or write your answer.

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)

build_hill(6)
```

**The straight line will be 6 blocks long. Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)
```

**There is no call after the definition. Does anything get built? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean code first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The function should be **called** so the hill gets built.

```python
# clean
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)

build_hill(6)
```

```python
# buggy
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)
```

**What is wrong? Why does the buggy code build nothing?**

<div class="write-space short"></div>

**Pair B** — The function should use the **parameter** `line_len`, not a fixed number.

```python
# clean
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
```

```python
# buggy
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(10)
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

This coaster should go **up** and then come back **down** so the cart lands safely. One word is missing. Fill it in using the word bank.

```python
def up_and_down(ramp_len):
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, ramp_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.____, ramp_len)

up_and_down(10)
```

**Word bank:** `DOWN` · `UP` · `LEFT`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Write one `build_hill` function with a `line_len` parameter and a ramp up, then call it two times with different numbers. When you finish, come back here.

Send a photo or video of your coaster, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My function's parameter was …
>
> When I called it with a bigger number, …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your code builds the coaster. Talk like you are teaching a friend. Try to use these words: **function**, **parameter**, **call**.

> 1. Show your function and run your code.
> 2. Show two coasters built with different numbers.
> 3. Say in your own words what a **parameter** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
