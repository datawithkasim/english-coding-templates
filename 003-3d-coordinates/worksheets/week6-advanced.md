# 🐉 M003 Week 6 — English Worksheet (Advanced)

**Topic:** Recreate the Ender Dragon (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced · **Time:** about 45 minutes

A big blocky **ender dragon** stands in your world. It is a set of **parts** — a long **body**, a front **head**, two **wings** (along x), and a **tail** (stepping back and down) — each block **(x, y, z)**: x **across**, y **up**, z **forward**.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your head.

---

## 1 · Predict 🔮

Read each snippet. Write your prediction **and the reason**.

```
fill black from (0, 8, 0) to (0, 8, 10)
```

**How long is the body, and which way does it run? Why?**

<div class="write-space"></div>

```
fill black from (1, 8, 5) to (5, 8, 5)
fill black from (-5, 8, 5) to (-1, 8, 5)
```

**Two wings. How wide is each one? Are they the same size on both sides? Why?**

<div class="write-space"></div>

```
place black block at (0, 7, -1)
place black block at (0, 6, -2)
place black block at (0, 5, -3)
```

**This is the tail behind the body. As z gets more negative, what happens to the height? Why does that make it droop?**

<div class="write-space"></div>

```
fill black from (0, 8, 0) to (0, 8, 10)
place black block at (0, 9, 11)
```

**Body, then head. Is the head in front of or behind the body? Is it higher or lower? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

**Bug A** — These should be **two matching wings**, spreading the same distance out on each side from the body at x = 0. Right now the left wing is much shorter than the right.

```
fill black from (1, 8, 5) to (5, 8, 5)
fill black from (-2, 8, 5) to (-1, 8, 5)
```

**Write the fixed code:**

<div class="write-space short"></div>

**Why was it wrong? Why does your fix work? 2–3 sentences.**

<div class="write-space short"></div>

**Bug B** — This should be a **long body** stretched **deep along z**, from (0, 8, 0) to (0, 8, 10). Right now it lies flat across the ground along x instead.

```
fill black from (0, 8, 0) to (10, 8, 0)
```

**Write the fixed code:**

<div class="write-space short"></div>

**Why was it wrong? Why does your fix work? 2–3 sentences.**

<div class="write-space short"></div>

**Bug C** — The **tail** should step **back and down** behind the body: each block goes one deeper and one lower. Right now every tail block sits at the same height, so the tail floats straight out instead of drooping.

```
place black block at (0, 8, -1)
place black block at (0, 8, -2)
place black block at (0, 8, -3)
```

**Hint:** look at the **y** numbers. A tail that droops must lower y each step, not keep it the same.

**Write the fixed code:**

<div class="write-space short"></div>

**Why was it wrong? Why does your fix work? 2–3 sentences.**

<div class="write-space short"></div>

---

## 3 · Show Your Work 📸🎥

Look at the dragon and walk around it. **Plan your corners first**, then copy it part by part on your home spot:

```
fill black from (0, 8, 0) to (0, 8, 10)
place black block at (0, 9, 11)
fill black from (1, 8, 5) to (5, 8, 5)
fill black from (-5, 8, 5) to (-1, 8, 5)
place black block at (0, 7, -1)
place black block at (0, 6, -2)
place black block at (0, 5, -3)
```

That is body, head, right wing, left wing, and a stepped tail. Add two **purple** eye blocks on the head. Keep the wings the same length on both sides.

**MODIFY challenge:** change one thing that is your own idea — a new colour, an extra part, or a bigger dragon. Write down what you changed.

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
