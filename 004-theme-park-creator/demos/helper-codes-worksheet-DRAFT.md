# 🎢 005 — Helper Codes: Coaster Supports — English Worksheet

**Topic:** Roller Coaster Supports — Helper Codes · **Course:** Theme Park Creator · **Level:** Base · **Time:** about 45 minutes

<!-- DRAFT — pairs with demos/helper-codes.html. Before shipping: (1) swap [[VIDEO LINK]] for the real YouTube link, (2) confirm the world name in §5, (3) run scripts/build-worksheets.py, (4) split into -beginner / -intermediate / -advanced tiers if needed, (5) add a row to the course README. Delete this note before build. -->

▶ **Watch the lesson video first:** [[VIDEO LINK — pending]]

Your park needs a **roller coaster**. A coaster stands on a whole **row of support pillars** — and every pillar is the **same job**. So you write that job **once**, name it, then **call** it for every support.

A **helper code** is a job you name once and reuse. These are the tools this week:

```python
def pillar(x, height):
    blocks.fill(IRON_BLOCK, pos(x, 0, 0),
        pos(x, height, 0), FillOperation.REPLACE)

for x in range(2, 21, 3):
    pillar(x, 3)
```

> `def pillar(...)` **names** a job. Writing it builds **nothing** yet.
> `pillar(2, 3)` **calls** it — now it runs and a pillar appears.
> The words in the brackets are **parameters** — the parts you get to change.
> `for x in range(2, 21, 3):` runs the line under it again and again.
> `IRON_BLOCK` = the support. `pos(x, 0, 0)` = bottom. `pos(x, height, 0)` = top.

**The job is written once. Turning it into a helper you can reuse is your job.**

---

## 1 · What a Helper Is 🧩

A helper is not a special kind of code. It is a normal function — the word describes its **job**: a small job you name **once**, then **reuse**.

| | Without a helper | With a helper |
|---|---|---|
| One pillar | one `fill` | `pillar(2, 3)` |
| Ten pillars | ten `fill`s, copy-pasted | one loop calling `pillar` |
| Change all heights | edit every line | change one number |

> ⚠️ Writing `def pillar(...)` does **not** build anything. It only **teaches** the computer the job. A pillar appears when you **call** it.

**In your own words: what is the difference between _writing_ a helper and _calling_ a helper?**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each one. Write what you think happens.

```python
def pillar(x, height):
    blocks.fill(IRON_BLOCK, pos(x, 0, 0),
        pos(x, height, 0), FillOperation.REPLACE)
```

**This is the whole program. How many pillars appear when you run it? Why?**

<div class="write-space"></div>

```python
pillar(2, 3)
pillar(5, 3)
pillar(8, 3)
```

**One helper, three calls. What is the same about the three pillars, and what is different?**

<div class="write-space"></div>

```python
h = 2
for x in range(2, 21, 3):
    pillar(x, h)
    h += 1
```

**What shape does the row of pillars make, and why?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

**Bug A** — This should build a row of pillars, but nothing appears in the world.

```python
def pillar(x, height):
    blocks.fill(IRON_BLOCK, pos(x, 0, 0),
        pos(x, height, 0), FillOperation.REPLACE)
```

**Why does nothing build? What one line is missing?**

<div class="write-space"></div>

**Write the missing line:**

<div class="write-space short"></div>

**Bug B** — Every pillar comes out the **same** height, even though the height should change.

```python
h = 2
for x in range(2, 21, 3):
    pillar(x, 2)
    h += 1
```

**Where is the mistake, and what should that call say instead?**

<div class="write-space"></div>

---

## 4 · Build the Coaster Supports 🏗️

In this week's world, write **one** helper and use it to raise a coaster.

**Work through these in order — do not skip to step 4.**

**Step 1.** Write the helper `pillar(x, height)`. It builds one column of `IRON_BLOCK` from the ground up.

**Step 2.** Test it once. Call `pillar(2, 3)` with numbers you can see. Fix it now if it looks wrong.

**Step 3.** Loop it. Use `for x in range(2, 21, 3):` to call `pillar` along the row.

**Step 4.** Make it climb. Add a height that goes up by 1 each time, so the track rises.

**Write your helper and your loop:**

<div class="write-space tall" style="min-height: 360px"></div>

**Your helper is written once. Count how many times it runs when the loop finishes. Explain your number.**

<div class="write-space"></div>

---

## 5 · Extension — Open a Second Ride 🎡

You already have one helper. A helper's whole point is that you can **reuse** it — anywhere, any number of times.

**Part A — Reuse.** Build a **second coaster** in another corner of the park. Do **not** write a new pillar function. Call your **same** `pillar` helper with new `x` numbers.

**Part B — Compose.** Write a **second** helper `topper(x, height)` that places one **SEA_LANTERN** on top of a pillar (so the ride lights up at night). Call `topper` inside the same loop as `pillar`, so every support gets a light.

```python
def topper(x, height):
    blocks.place(SEA_LANTERN, pos(x, height + 1, 0))
```

> A helper can **call another helper**. When your loop calls `pillar` **and** `topper`, one line of the loop now does two jobs — and you still only wrote each job once.

**Write your second ride, and your `topper` helper:**

<div class="write-space tall" style="min-height: 300px"></div>

**How many times does `topper` run for a 7-pillar coaster? How did you get your answer?**

<div class="write-space"></div>

---

## 6 · Show Your Work 📸🎥

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera at the coaster. Name the parts.

**3 · Your helper.** Point at `pillar` and say how many times it ran.

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

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 200px"></div>
