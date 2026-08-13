# 🐒 Extra — set or change? Two Ways to Give a Variable a Number

**Topic:** `set` vs `change` · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 35 minutes

A variable is a number with a name. `set` gives it a brand new number. `change` adds to the number it already holds.

---

## 1 · Predict 🔮

Read the code. The agent moves the number of blocks that `monkey` holds.

```
set monkey to 2
move forward by monkey
change monkey by 3
move forward by monkey
set monkey to 1
move forward by monkey
```

**Fill the table. Write what `monkey` holds before each move.**

| Move | `monkey` before this move |
|:----:|:-------------------------:|
| 1    | 2                         |
| 2    |                           |
| 3    |                           |

**How many blocks does the agent move in total?**

<div class="write-space short"></div>

---

## 2 · Which Block Do You Need? ✏️

**`monkey` holds 5. You run `change monkey by 5`. Now `monkey` holds… Circle one:** 5 · 10 · 25

**`monkey` holds 5. You run `set monkey to 5`. Now `monkey` holds… Circle one:** 5 · 10 · 0

**You want the number to start at 6. Circle one:** `set monkey to 6` · `change monkey by 6`

**`monkey` holds 6 and you want 6 more. Circle one:** `set monkey to 6` · `change monkey by 6`

**Finish the rule in your own words.**

> `set` means ______.
>
> `change` means ______.

<div class="write-space short"></div>

---

## 3 · Find the Bug 🐛

**Bug A** — This should build three walls: 4 blocks long, then 8, then 12. It builds 4, then 12, then 12.

```
set monkey to 4
move forward by monkey
set monkey to 12
move forward by monkey
set monkey to 12
move forward by monkey
```

**Hint:** what number does the second wall need?

**Write the fixed code. Use `change` instead.**

<div class="write-space"></div>

**Bug B** — The first wall should be 4 blocks long. It comes out 8.

```
set monkey to 4
repeat 3 times
    change monkey by 4
    move forward by monkey
```

**Which two lines swap places? Write the fixed code.**

<div class="write-space"></div>

**Why does the order of those two lines matter? One sentence.**

<div class="write-space short"></div>

---

## 4 · Count the Corner 📐

The agent starts on **A1** facing right. It places 5 blocks along row **A**. Then it turns right and finishes the L.

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **A** | ■ | ■ | ■ | ■ | ■ |
| **B** | | | | | ■ |
| **C** | | | | | ■ |

**Count the ■ blocks in the picture. How many in total? Circle one:** 7 · 8 · 10

**After the turn, how many more blocks does the agent still place? Circle one:** 2 · 3 · 5

**The corner block is A5. Why is it not placed twice? One sentence.**

<div class="write-space short"></div>

**Write the code for this L. Use `monkey` for the long arm.**

<div class="write-space"></div>

---

## 5 · Show Your Work 📸🎥

Switch to your homework world. Build **three walls in a row**: the first 4 blocks long, the second 8, the third 12. Use one variable and `change` it — no `set` inside the loop. Then change **one number** (the start value or the change amount) and run it again.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does. Point at your `change` block and say the new number it makes.

**2 · Your build.** Point the camera. Show both versions.

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
