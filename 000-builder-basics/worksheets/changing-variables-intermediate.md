# 📈 Builder Basics · Changing a Variable — English Worksheet (Intermediate)

**Topic:** Changing a Variable While You Build · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 38 minutes

---

## 1 · Predict 🔮

A variable can **change while the code runs**. `height = height + 1` means: take what `height` holds, add 1, put it back.

```
height = 1
repeat 4 times:
    place block down
    move up by height
    move forward
    height = height + 1
```

**Does each step climb the same amount, or more each time?**

<div class="write-space"></div>

**Fill the table. Start at 1 and add 1 after every step.**

| Step | `height` before the step |
|:----:|:------------------------:|
| 1    | 1                        |
| 2    |                          |
| 3    |                          |
| 4    |                          |

---

## 2 · Find the Bug 🐛

Each code block is broken. Write one or two sentences on what is wrong.

**Bug A** — Each step should climb higher than the one before.

```
height = 1
repeat 4 times:
    place block down
    move up by height
    move forward
```

**What shape do you get instead, and what line is missing?**

<div class="write-space"></div>

**Bug B** — The first step should climb 1, then 2, then 3.

```
height = 1
repeat 3 times:
    height = 1
    place block down
    move up by height
    move forward
    height = height + 1
```

**Hint:** look at the line inside the loop that sets `height` back to 1.

**What is wrong?**

<div class="write-space"></div>

---

## 3 · Fix the Code ✏️

The first step should climb **1**, then 2, then 3, then 4. Right now the first step climbs 2.

```
height = 1
repeat 4 times:
    height = height + 1
    place block down
    move up by height
    move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why does the order of those two lines matter? Write one sentence.**

<div class="write-space short"></div>

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Build a **staircase** where each step climbs higher than the one before, using a variable that changes inside the loop. Then change **one number** — the start value or the amount you add — and run it again.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does. Point at the line that changes your variable.

**2 · Your build.** Point the camera. Show both staircases.

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
