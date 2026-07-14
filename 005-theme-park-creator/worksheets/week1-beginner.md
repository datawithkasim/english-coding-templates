# 🎢 005 Week 1 — English Worksheet (Beginner)

**Topic:** One Function, Many Coasters — Parameters · **Course:** Theme Park Creator · **Level:** Beginner · **Time:** about 30 minutes

This week you build a roller coaster with a **function**. You give it **parameters** — numbers it uses inside — and change them to build a long or short coaster.

These are the blocks you use this week:

```python
rollerCoasterBuilder.add_straight_line(10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 10)
```

> A direction is `UP` or `DOWN`. The number after it is how many blocks the ramp goes.

---

## 1 · Predict 🔮

Read the code. Circle your answer.

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)

build_hill(6)
```

**The straight line will be 6 blocks long. Circle one:** yes · no

**Why 6? Circle one:** we called `build_hill(6)` · we called `build_hill(10)`

```python
def build_hill(line_len):
    rollerCoasterBuilder.add_straight_line(line_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, line_len)
```

**There is no call after the definition. Does anything get built? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

Clean code first, then a broken version. Circle the answer.

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

**What is wrong? Circle one:** no call after `def` · wrong number · wrong color

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

**What is wrong? Circle one:** it uses `10`, not `line_len` · it uses `line_len`, not `10` · nothing

---

## 3 · Fill the Gap ✏️

This coaster goes **up** then **down** so the cart lands safely. One word is missing.

```python
def up_and_down(ramp_len):
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, ramp_len)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.____, ramp_len)

up_and_down(10)
```

**Which word is missing? Circle one:** `DOWN` · `UP` · `LEFT`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Write one `build_hill` function with a `line_len` parameter and a ramp up, then call it two times with different numbers.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
