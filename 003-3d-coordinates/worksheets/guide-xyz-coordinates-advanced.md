# 🧭 M003 Guide — Counting (x, y, z) · Advanced

**Topic:** Before 3D · **Course:** 3D Coordinates · **Level:** Advanced · **Time:** about 30 minutes

Pixel art used **two** numbers. A 3D build needs **three**. They always come in the same order:

<div style="display:flex; gap:8px; flex-wrap:wrap; margin:6px 0 2px"><div style="flex:1; min-width:120px; background:#fff3ea; border:1px solid #ffd9c2; border-radius:8px; padding:8px 12px"><b style="color:#e0681c">1st = X</b><br>right → left<br><span style="color:#8a8a8a">starts at 0</span></div><div style="flex:1; min-width:120px; background:#f0ecff; border:1px solid #d9cdff; border-radius:8px; padding:8px 12px"><b style="color:#6b4ee6">2nd = Y</b><br>down → up<br><span style="color:#8a8a8a">starts at 0</span></div><div style="flex:1; min-width:120px; background:#e8f7ef; border:1px solid #c4ead6; border-radius:8px; padding:8px 12px"><b style="color:#1a8f5a">3rd = Z</b><br>back → forward<br><span style="color:#8a8a8a">starts at 0</span></div></div>

The three rulers meet on **one block** — your home spot. That block is **(0, 0, 0)**. Every number is counted **from there**, so a coordinate is really three instructions: how far left, how far up, how far forward.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your build.

---

## 1 · Build Your Grid 🎨

Make a striped ruler for each axis, so you can **see** the numbers.

<img src="../assets/guide-grid.png" alt="A white grid floor with yellow lines. A striped line runs sideways, a striped line runs forward, and a striped pillar rises from the corner where they meet" style="width:100%; max-width:420px; border-radius:8px; display:block; margin:10px 0">

One **`fill`** makes a solid box between **two corners**. The floor is a flat box one block **below** your feet: from **(0, -1, 0)** out to **(15, -1, 15)**.

```python
def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(0, -1, 0),
        pos(15, -1, 15),
        FillOperation.REPLACE)
player.on_chat("grid", on_run)
```

**Write the two `fill` lines that draw a yellow line 5 to the left (x = 5) and a yellow line 5 forward (z = 5), both across the whole floor.**

<div class="write-space"></div>

**The floor sits at y = -1, not y = 0. Explain what y = 0 is, and what would happen if you filled the floor there instead. (2–3 sentences.)**

<div class="write-space"></div>

Now place the three rulers by hand — **yellow, black, yellow, black** all the way. All three start on the corner block: **x** to your left, **z** forward, **y** straight up.

---

## 2 · Predict 🔮

Read each box. Write what you will see, **where it sits**, **and the reason**.

```
fill RED from (0, 0, 0) to (5, 0, 0)
```

**Only the 1st number changes. Which ruler is this line lying on, and which way does it run?**

<div class="write-space"></div>

```
fill RED from (0, 0, 0) to (0, 5, 0)
fill RED from (0, 0, 0) to (0, 0, 5)
```

**Two lines from the same corner. Describe the shape they make together, and name the corner's coordinate.**

<div class="write-space"></div>

```
fill RED from (3, 0, 4) to (3, 0, 4)
```

**Both corners are the same. How many blocks is this, and why?**

<div class="write-space"></div>

```
place red block at (-1, 0, 0)
```

**x counts to your left, so 1 is one step left. This one is negative. Where does the block land?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each one is broken. Read what it should do, write the fixed code, then explain.

**Bug A** — This should lay the white floor **under** your feet. It fills at **y = 0** instead, so the blocks land at feet height and swallow the home spot.

```
fill WHITE_CONCRETE from (0, 0, 0) to (15, 0, 15)
```

**Hint:** the **2nd number (y)** is height, and 0 is standing height. What is one block lower?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences.)**

<div class="write-space"></div>

**Bug B** — Your friend thinks the corner block is **(1, 1, 1)**, so they count every number from there. Their chicken ends up one step left, one block up, and one step forward from where it belongs — and it floats.

```
place red block at (5, 1, 5)   # they wanted the block 4 left, on the ground, 4 forward
```

**Hint:** the corner is where the three rulers **meet**.

**Write the fixed code:**

<div class="write-space"></div>

**Which of the three numbers is the one lifting the build off the ground? Explain how you know. (2–3 sentences.)**

<div class="write-space"></div>

**Bug C** *(the tricky one)* — The beak should sit in **front of** the head, further along the x ruler at x = 8. This code uses **x = -8**, so the beak appears on the wrong side of the player.

```
place yellow block at (-8, 3, 4)
```

**Hint:** which direction does a **negative** x count?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences.)**

<div class="write-space"></div>

---

## 4 · Show Your Work 📸🎥

**Warm-up:** stand on your home spot and place one block at **(3, 0, 3)**. Check it against all three rulers.

**Build the chicken with `fill` boxes** — five of them. Count x, then y, then z for every corner.

<img src="../assets/guide-chicken.png" alt="A red nether brick chicken with a yellow beak standing on the white and yellow grid" style="width:100%; max-width:380px; border-radius:8px; display:block; margin:10px 0">

> 🧱 Recipe (red nether brick, yellow concrete for the beak; feet on the ground y = 0):
>
> - legs: (4, 0, 4) to (4, 0, 5)
> - body: (3, 1, 4) to (6, 2, 5)
> - tail: (2, 3, 4) to (2, 3, 5)
> - head: (6, 3, 4) to (7, 4, 5)
> - beak: yellow from (8, 3, 4) to (8, 3, 5)

Before you build, **plan the heights**: which y does each box start and stop at?

<div class="write-space"></div>

> ✨ **Modify challenge:** after it works, change one thing of your own — a comb, a tail feather, a taller body, a second chicken further along z. Write what you changed.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Count one block out loud — x, then y, then z.

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
