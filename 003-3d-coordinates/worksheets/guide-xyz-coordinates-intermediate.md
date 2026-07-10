# 🧭 M003 Guide — Counting (x, y, z) · Intermediate

**Topic:** Before 3D · **Course:** 3D Coordinates · **Level:** Intermediate · **Time:** about 25 minutes

Pixel art used **two** numbers. A 3D build needs **three**. They always come in the same order:

<div style="display:flex; gap:8px; flex-wrap:wrap; margin:6px 0 2px"><div style="flex:1; min-width:120px; background:#fff3ea; border:1px solid #ffd9c2; border-radius:8px; padding:8px 12px"><b style="color:#e0681c">1st = X</b><br>right → left<br><span style="color:#8a8a8a">starts at 0</span></div><div style="flex:1; min-width:120px; background:#f0ecff; border:1px solid #d9cdff; border-radius:8px; padding:8px 12px"><b style="color:#6b4ee6">2nd = Y</b><br>down → up<br><span style="color:#8a8a8a">starts at 0</span></div><div style="flex:1; min-width:120px; background:#e8f7ef; border:1px solid #c4ead6; border-radius:8px; padding:8px 12px"><b style="color:#1a8f5a">3rd = Z</b><br>back → forward<br><span style="color:#8a8a8a">starts at 0</span></div></div>

All three rulers meet on **one block** — your home spot. That block is **(0, 0, 0)**, and every count starts there.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your build.

---

## 1 · Build Your Grid 🎨

Make a striped ruler for each axis, so you can **see** the numbers.

<img src="../assets/guide-grid.png" alt="A white grid floor with yellow lines. A striped line runs sideways, a striped line runs forward, and a striped pillar rises from the corner where they meet" style="width:100%; max-width:420px; border-radius:8px; display:block; margin:10px 0">

The floor starts at the corner **(0, -1, 0)** — one below your feet — and reaches 15 blocks left and 15 blocks forward. Fill in the missing corners.

```python
def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(0, -1, 0),
        pos(__, -1, __),
        FillOperation.REPLACE)
    # yellow line 5 to the left
    blocks.fill(YELLOW_CONCRETE,
        pos(5, -1, 0),
        pos(5, -1, 15),
        FillOperation.REPLACE)
    # yellow line 5 forward
    blocks.fill(YELLOW_CONCRETE,
        pos(0, -1, __),
        pos(15, -1, __),
        FillOperation.REPLACE)
player.on_chat("grid", on_run)
```

**Why is the floor at y = -1 and not y = 0?**

<div class="write-space short"></div>

Now place the three rulers by hand — **yellow, black, yellow, black** all the way. All three start on the corner block:

- **X ruler** — one block at a time, **to your left**.
- **Z ruler** — one block at a time, **forward**.
- **Y ruler** — a pillar straight **up**.

---

## 2 · Predict 🔮

Read each set of blocks. Circle the direction, then say which number changed.

<img src="../assets/guide-axis-x.png" alt="Striped yellow and black line running sideways across the grid floor, going to the player's left" style="width:100%; max-width:340px; border-radius:8px; display:block; margin:10px 0">

```
place red block at (1, 0, 0)
place red block at (2, 0, 0)
place red block at (3, 0, 0)
```

**Circle one:** left · up · forward

**Which number changed? Circle one:** x · y · z

```
place red block at (0, 0, 1)
place red block at (0, 0, 2)
place red block at (0, 0, 3)
```

**Circle one:** left · up · forward

**Which number changed? Circle one:** x · y · z

```
place red block at (7, 1, 2)
place red block at (7, 2, 2)
```

**Circle one:** left · up · forward

**Where is the corner block? Write its coordinate:** ( ____ , ____ , ____ )

---

## 3 · Spot the Bug 🐛

Each one is broken. Write the fixed code, then explain.

**Bug A** — This should be a pillar 3 blocks **up** the y ruler. Right now the same block is placed three times, because the **2nd number** never changes.

```
place red block at (0, 1, 0)
place red block at (0, 1, 0)
place red block at (0, 1, 0)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (1–2 sentences.)**

<div class="write-space short"></div>

**Bug B** — Your friend says the corner block is **(1, 1, 1)**, so they start counting there. Their whole build sits one step left, one block up, and one step forward from where it should be.

```
place red block at (1, 1, 1)   # they think this is the corner
```

**Write the corner's real coordinate:**

<div class="write-space short"></div>

**Which number is floating their build off the ground? Circle one:** x · y · z

---

## 4 · Put Them Together 🧭

Read **(5, 2, 3)** in three steps:

| Step | Number | Ruler | Do this |
|---|---|---|---|
| 1 | x = 5 | right → left | go 5 to your left |
| 2 | y = 2 | down → up | go 2 up (the ground is 0) |
| 3 | z = 3 | back → forward | go 3 forward |

**Which coordinate is on the ground? Circle one:** (2, 1, 2) · (2, 0, 2)

**A block sits 4 to your left and 6 forward, on the ground. Write it:** ( ____ , ____ , ____ )

---

## 5 · Show Your Work 📸🎥

**Warm-up:** stand on your home spot and place one block at **(3, 0, 3)**. Check it against your rulers.

Open the world. Part of the shape is **already built** for you:

<img src="../assets/guide-partial-build.png" alt="A half-built shape made of gold ore blocks, standing on the white grid beside the striped ruler" style="width:100%; max-width:330px; border-radius:8px; display:block; margin:10px 0">

The rest of the blocks are **missing**. Here they are, spread apart so you can see each one:

<img src="../assets/guide-missing-blocks.png" alt="The missing blocks laid out apart on the white grid — red blocks and one long yellow block" style="width:100%; max-width:300px; border-radius:8px; display:block; margin:10px 0">

**Finish the shape.** Read each missing block off the model and count from the corner — x, then y, then z.

**Write the coordinates you counted, then the code you ran.**

<div class="write-space tall"></div>

> 🧱 The corner block is **(0, 0, 0)**. Use the same blocks you see in the world.

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
