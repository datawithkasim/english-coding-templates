# 👾 M003 Week 7 — English Worksheet (Advanced)

**Topic:** Recreate 2 Mob Heads (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced · **Time:** about 45 minutes

Two blocky **mob heads** stand in your world — a **creeper** and a **skeleton**. Each one is a cube with a face on the **front**. Build the **front face first** (keep z the same, read x across and y up), then **add depth** at z = 2, z = 3. This week you build **both** heads side by side — and keep them from overlapping by giving each its own x range.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your head.

---

## 1 · Predict 🔮

Read each set. Write what you will see.

```
fill green block from (0, 4, 1) to (4, 8, 1)
fill green block from (0, 4, 2) to (4, 8, 3)
```

**The first line is the front face; the second adds depth. How wide (x), how tall (y), and how deep (z) is the finished cube?**

<div class="write-space"></div>

```
fill green block from (0, 4, 1) to (4, 8, 3)
fill white block from (7, 4, 1) to (11, 8, 3)
```

**Read the x ranges: 0–4 and 7–11. Do the heads overlap? How big is the gap between them?**

<div class="write-space"></div>

```
place black block at (1, 7, 1)
place black block at (1, 7, 2)
```

**Both eyes share x = 1. One is at z = 1 (front), one at z = 2 (deeper). Are they both on the front face? Where is the second one?**

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

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The two eyes should sit **side by side on the front face** (z stays 1, x changes). This code put the second eye one step **deeper**, so it landed on the **side** of the head, not the face.

```
place black block at (1, 7, 1)
place black block at (1, 7, 2)
```

**Hint:** the face only shows on the front. To move across the front, change x and keep z = 1.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The code is correct, but both heads came out one step too far **forward** — every block landed one z too deep. Your friend never changed the code.

```
(the code matched the heads)
```

**Hint:** the build always starts from where you stand.

**What did your friend forget before pressing run? Why does it move the whole head?**

<div class="write-space"></div>

---

## 3 · Build Both Heads 📸

Now switch to your homework world. Build **both** heads side by side, each on its own x range so they never overlap.

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

Send a photo. Then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> I built the front face of each head first by …
>
> I added depth by changing the … number to 2 and 3.
>
> My two heads do not overlap because their x ranges are … and …
>
> The faces stay on the front because their z is …
>
> One head went wrong when …
>
> Next time I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Film yourself showing both heads. Try to use these words: **x**, **y**, **z**, **front face**, **depth**, **overlap**, **home spot**.

> 1. Show your home spot. Why stand on it every run?
> 2. Walk around both heads — show a front face and a plain side.
> 3. Say the x range of each head and why they don't overlap.
> 4. Say in your own words how you turned a flat face into a deep cube.

**Plan what you will say:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
