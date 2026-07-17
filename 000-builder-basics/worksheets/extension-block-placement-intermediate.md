# 🧱 Builder Basics — Block Placement Practice (Extension · Intermediate)

**Topic:** Move, Turn, Climb With Place On Move · **Course:** Builder Basics · **Type:** Extension Activity · **Level:** Intermediate · **Time:** about 38 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you can move the agent around, before you start placing blocks by hand.

In Week 1 the agent **walked**. Here it walks and **draws** at the same time. You flip one switch — **place on move** — at the very top, and you never touch it again. After that, every step drops a block.

Your commands: `move forward`, `turn left`, `turn right`, `move up`.

> 🧱 One step = one block. A turn is not a step.

---

## 1 · Predict 🔮

The switch is ON at the top and stays ON.

```
place on move ON
set block to stone
move forward by 3
turn right
move forward by 2
```

**How many blocks land in total? Show your adding.**

<div class="write-space short"></div>

**Draw the shape those blocks make. Mark where the agent started with an S.**

<div class="write-space blank tall"></div>

---

## 2 · A Turn Is Not a Step 🧭

- `move forward by 2` — the agent **travels** two blocks. Two steps, so two blocks drop.
- `turn right` — the agent **spins** on the spot. It goes nowhere. No step, so **no block**.

**The switch is ON. The agent runs `turn left`. How many blocks does it place? Circle one:** 0 · 1 · 2

**Why? Explain in one sentence.**

<div class="write-space"></div>

**Both of these programs place 4 blocks. Explain what is different about the two trails.**

```
Program A            Program B
move forward by 2    move forward by 2
move forward by 2    turn right
                     move forward by 2
```

<div class="write-space"></div>

---

## 3 · Count the Blocks 🔢

Follow this program one line at a time. Fill in the table. Turns get a row too.

```
place on move ON
set block to stone
move forward by 4
turn right
move forward by 3
turn right
move forward by 4
```

| Command | Blocks this line | Total so far |
|:-------:|:----------------:|:------------:|
| move forward by 4 |          |              |
| turn right        |          |              |
| move forward by 3 |          |              |
| turn right        |          |              |
| move forward by 4 |          |              |

**Two lines placed zero blocks. Which ones, and why?**

<div class="write-space"></div>

---

## 4 · Going Up 🪜

`move up` is a step too, so it drops blocks as well. Up steps stack blocks instead of laying them flat. Mix `move forward` and `move up` and you get **stairs**:

```
place on move ON
set block to stone
move forward by 1
move up by 1
move forward by 1
move up by 1
move forward by 1
```

**How many blocks does this staircase use?**

<div class="write-space short"></div>

**Draw this staircase from the side. Mark the start with an S.**

<div class="write-space blank tall"></div>

---

## 5 · Spot the Bug 🐛

**Bug A** — This should draw a line 5 blocks long.

```
set block to stone
move forward by 5
```

**What is missing from the program? What is on the ground when it finishes?**

<div class="write-space"></div>

**Bug B** — This should draw a corner: 3 blocks, turn, 3 more blocks.

```
place on move ON
set block to stone
move forward by 3
turn right
turn right
move forward by 3
```

**The agent placed 6 blocks, but there is no corner. Explain what those two turns did.**

<div class="write-space"></div>

---

## 6 · Design Your Own Path 🏗️

Plan a trail before you build it. Use `move forward`, `turn left`, `turn right` and `move up`. The switch goes ON once and stays ON.

**Choose your block and your path. Fill in the blanks:**

> My block is …
>
> move forward by … (… blocks)
>
> … (… blocks)
>
> … (… blocks)

<div class="write-space tall"></div>

**How many blocks does your path place in total?**

<div class="write-space short"></div>

**Draw the shape your path will make. Mark the start with an S and the end with an E.**

<div class="write-space blank tall"></div>

---

## 7 · Show Your Work 📸🎥

Open your world and build the path you designed in Section 6. Flip **place on move** ON once at the top, then never touch it again. If the shape comes out wrong, change your numbers and run it again.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
