# 👾 M003 Week 7 — English Worksheet (Advanced)

**Topic:** Recreate 2 Mob Heads (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced · **Time:** about 45 minutes

Two blocky **mob heads** — a **creeper** and a **skeleton** — stand in your world, each a cube with a face on the **front**. Build the **front face first** (z the same, read x across and y up), then **add depth** at z = 2 and z = 3.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your head.

---

## 1 · Predict 🔮

Read each set. Write what you will see **and the reason**.

```
fill green block from (0, 4, 1) to (4, 8, 1)
fill green block from (0, 4, 2) to (4, 8, 3)
```

**The first line is the front face; the second adds depth. How wide (x), how tall (y), and how deep (z) is the finished cube? Why is it 3 deep?**

<div class="write-space"></div>

```
fill green block from (0, 4, 1) to (4, 8, 3)
fill white block from (7, 4, 1) to (11, 8, 3)
```

**Read the x ranges: 0–4 and 7–11. Do the heads overlap? How big is the gap, and why does the gap stop a crash?**

<div class="write-space"></div>

```
place black block at (1, 7, 1)
place black block at (1, 7, 2)
```

**Both eyes share x = 1, but one is z = 1 and one is z = 2. Are they both on the front face? Where is the second one, and why can't you see it from the front?**

<div class="write-space"></div>

```
fill white block from (7, 4, 1) to (11, 8, 1)
fill white block from (7, 4, 1) to (11, 8, 3)
```

**Both lines start at the same corner. The second line covers the first. What is the final shape, and did the first line do anything in the end? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Fix each one. Then say why it was wrong.

**Bug A** — The creeper head should be **3 blocks deep**. Right now it is only the flat front face — paper thin.

```
fill green block from (0, 4, 1) to (4, 8, 1)
```

**Hint:** add the same face again at z = 2 and z = 3.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences)**

<div class="write-space"></div>

**Bug B** — The two eyes should sit **side by side on the front face** (z stays 1, x changes). This code put the second eye one step **deeper**, so it landed on the **side** of the head, not the face.

```
place black block at (1, 7, 1)
place black block at (1, 7, 2)
```

**Hint:** the face only shows on the front. To move across the front, change x and keep z = 1.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences)**

<div class="write-space"></div>

**Bug C** — The code below is correct, but every block in **both** heads came out one step too far **forward** — the whole build landed one z too deep. Your friend never touched the code.

```
(the code matched the heads exactly)
```

**Hint:** the build always starts from where you stand.

**What did your friend forget before pressing run? Why does that move the whole head, not just one block? (2–3 sentences)**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

First, **plan your coordinates**. Write the x range you will give each head so they do not overlap.

> Creeper x range: … to …
>
> Skeleton x range: … to …
>
> Gap between them: … blocks

<div class="write-space short"></div>

Switch to your homework world. Build **both** heads side by side, each on its own x range.

```
# ---- Creeper (x 0–4) ----
# front face
fill green block from (0, 4, 1) to (4, 8, 1)
# depth
fill green block from (0, 4, 2) to (4, 8, 3)
# face (front, z = 1)
place black block at (1, 7, 1)
place black block at (3, 7, 1)
place black block at (2, 6, 1)
place black block at (2, 5, 1)
place black block at (1, 4, 1)
place black block at (3, 4, 1)

# ---- Skeleton (x 7–11) ----
# front face
fill white block from (7, 4, 1) to (11, 8, 1)
# depth
fill white block from (7, 4, 2) to (11, 8, 3)
# face (front, z = 1)
place black block at (8, 7, 1)
place black block at (10, 7, 1)
place black block at (9, 6, 1)
place black block at (8, 5, 1)
place black block at (9, 5, 1)
place black block at (10, 5, 1)
```

The two heads use different x ranges (0–4 and 7–11) with a gap, so they never crash into each other.

**MODIFY challenge:** change one thing that is your own idea — a new colour, an extra part (nose, ears, antenna), or make a head bigger. Build it, then say what you changed.

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
