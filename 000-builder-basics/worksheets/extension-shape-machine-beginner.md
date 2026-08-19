# 🐒 Builder Basics · Shape Machine — English Worksheet (Beginner)

**Topic:** Loops + Variables Make Shapes · **Course:** Builder Basics · **Level:** Beginner · **Time:** about 25 minutes

A **variable** is a name that holds a number. `monkey` can hold 5. The agent walks `monkey` blocks.

Change the number, and the same code builds a different shape.

---

## 1 · One Square 🟦

The agent walks forward, turns left, four times. It drops a block everywhere it walks.

```
set monkey to 5
place on move ON
repeat 4 times:
    move forward by monkey
    turn left
```

**What shape does the agent draw? Circle one:** line · square · circle

**How long is each side? Circle one:** 4 · 5 · 20

**Now the first line says `set monkey to 3`. How long is each side? Circle one:** 3 · 4 · 5

**How many lines did you have to edit to change the size? Circle one:** 1 · 2 · 4

---

## 2 · set or change? 🔁

`set` gives the variable a **brand new** number. `change` **adds** to the number it already holds.

**`monkey` holds 5. You run `change monkey by -1`. Now `monkey` holds… Circle one:** 4 · 5 · 6

**`monkey` holds 5. You run `set monkey to 3`. Now `monkey` holds… Circle one:** 3 · 5 · 8

**You want to start the number at 5, one time, at the top. Circle one:** `set monkey to 5` · `change monkey by 5`

**You are inside a loop and each square must get 1 smaller. Circle one:** `set monkey to 1` · `change monkey by -1`

**Finish the teacher's rule. Loop → Circle one:** `set` · `change`

**No loop → Circle one:** `set` · `change`

---

## 3 · Stack Them Up 🔺

Each square sits on top of the last one, and each one is 1 smaller.

```
set monkey to 5
place on move ON
repeat 3 times:
    repeat 4 times:
        move forward by monkey
        turn left
    move up by 1
    change monkey by -1
```

**The sides go 5, then …, then … Circle one:** 5 · 4 · 3 → 5 · 3 · 1 → 5 · 5 · 5

**Which square is the biggest? Circle one:** bottom · top

**How many squares does the agent draw? Circle one:** 3 · 4 · 5

---

## 4 · Find the Bug 🐛

Clean code first, then a buggy one. Circle the bug.

**Pair A** — Every layer should get **smaller**.

```
# clean
    move up by 1
    change monkey by -1
```

```
# buggy
    move up by 1
    change monkey by 1
```

**The buggy tower gets… Circle one:** smaller going up · bigger going up

**Pair B** — Every layer should sit **higher** than the one under it.

```
# clean
    repeat 4 times:
        move forward by monkey
        turn left
    move up by 1
```

```
# buggy
    repeat 4 times:
        move forward by monkey
        turn left
```

**What is wrong? Circle one:** all the squares are in the same place · the squares are too small

---

## 5 · Show Your Work 📸🎥

Switch to your homework world. Do these three steps in order. **Start with 5. Do not use a number bigger than 5** — a big number takes a very long time.

**Step 1 — one square.** Type this code. Put your own number in the blank, then run it.

```
set monkey to ____
place on move ON
repeat 4 times:
    move forward by monkey
    turn left
```

**Step 2 — a smaller square.** Change **only** the first line to a smaller number. Run it again, next to the first one.

**Step 3 — stack them.** Type this code. One line is missing — it is the line from Section 3 that makes the next square smaller.

```
set monkey to 5
place on move ON
repeat 3 times:
    repeat 4 times:
        move forward by monkey
        turn left
    move up by 1
    ____________
```

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Point at your `set` block. Point at your `change` block.

**2 · Your build.** Point the camera. Show the two squares, then the stack.

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
