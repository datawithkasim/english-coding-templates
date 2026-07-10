# 🧭 M003 Guide — Counting (x, y, z) · Beginner

**Topic:** Before 3D · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 20 minutes

Pixel art used **two** numbers. A 3D build needs **three**. They always come in the same order:

<div style="display:flex; gap:8px; flex-wrap:wrap; margin:6px 0 2px"><div style="flex:1; min-width:120px; background:#fff3ea; border:1px solid #ffd9c2; border-radius:8px; padding:8px 12px"><b style="color:#e0681c">1st = X</b><br>left → right<br><span style="color:#8a8a8a">starts at 0</span></div><div style="flex:1; min-width:120px; background:#f0ecff; border:1px solid #d9cdff; border-radius:8px; padding:8px 12px"><b style="color:#6b4ee6">2nd = Y</b><br>down → up<br><span style="color:#8a8a8a">starts at 0</span></div><div style="flex:1; min-width:120px; background:#e8f7ef; border:1px solid #c4ead6; border-radius:8px; padding:8px 12px"><b style="color:#1a8f5a">3rd = Z</b><br>back → forward<br><span style="color:#8a8a8a">starts at 0</span></div></div>

**Count x, then y, then z. Always that order.**

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your build.

---

## 1 · Build Your Grid 🎨

Make a striped ruler for each axis, so you can **see** the numbers.

<img src="../assets/guide-grid.png" alt="A white grid floor with yellow lines. A striped line runs sideways, a striped line runs forward, and a striped pillar rises from the corner where they meet" style="width:100%; max-width:420px; border-radius:8px; display:block; margin:10px 0">

Stand on your home spot. Run this to lay the white floor and the yellow lines:

```python
def on_run():
    blocks.fill(WHITE_CONCRETE,
        pos(0, -1, 0),
        pos(15, -1, 15),
        FillOperation.REPLACE)
    blocks.fill(YELLOW_CONCRETE,
        pos(5, -1, 0),
        pos(5, -1, 15),
        FillOperation.REPLACE)
    blocks.fill(YELLOW_CONCRETE,
        pos(10, -1, 0),
        pos(10, -1, 15),
        FillOperation.REPLACE)
    blocks.fill(YELLOW_CONCRETE,
        pos(0, -1, 5),
        pos(15, -1, 5),
        FillOperation.REPLACE)
    blocks.fill(YELLOW_CONCRETE,
        pos(0, -1, 10),
        pos(15, -1, 10),
        FillOperation.REPLACE)
player.on_chat("grid", on_run)
```

Now place the three rulers by hand — **yellow, black, yellow, black** all the way. All three start on the block under your feet:

- **X ruler** — one block at a time, **to your right**.
- **Z ruler** — one block at a time, **forward**.
- **Y ruler** — a pillar straight **up**.

> 🟨⬛ The stripes are there so you can count without guessing.

---

## 2 · Start at the Corner 🔴

The three rulers all meet on **one block**. That block is your home spot.

Its coordinate is **(0, 0, 0)**. Every count starts there.

| From the corner | You get |
|---|---|
| stand still | (0, 0, 0) |
| 1 step **right** | (1, 0, 0) |
| 1 block **up** | (0, 1, 0) |
| 1 step **forward** | (0, 0, 1) |

**x, y and z all start at which number? Circle one:** 0 · 1

**Where is (0, 0, 0)? Circle one:** the corner · one block up

---

## 3 · The Three Rulers 📏

Each ruler starts at the corner and counts **0, 1, 2, 3 …**

<div style="display:flex; gap:10px; flex-wrap:wrap; margin:10px 0"><figure style="flex:1; min-width:150px; margin:0"><img src="../assets/guide-axis-x.png" alt="Striped yellow and black line running sideways across the grid floor, going to the player's right" style="width:100%; border-radius:8px"><figcaption style="font-size:13px; color:#555; text-align:center; margin-top:4px"><b style="color:#e0681c">X</b> — left → right</figcaption></figure><figure style="flex:1; min-width:110px; margin:0"><img src="../assets/guide-axis-y.png" alt="Striped yellow and black pillar going straight up from the corner of the grid floor" style="width:100%; border-radius:8px"><figcaption style="font-size:13px; color:#555; text-align:center; margin-top:4px"><b style="color:#6b4ee6">Y</b> — down → up</figcaption></figure><figure style="flex:1; min-width:140px; margin:0"><img src="../assets/guide-axis-z.png" alt="Striped yellow and black line running forward, away from the player, across the grid floor" style="width:100%; border-radius:8px"><figcaption style="font-size:13px; color:#555; text-align:center; margin-top:4px"><b style="color:#1a8f5a">Z</b> — back → forward</figcaption></figure></div>

```
place red block at (1, 0, 0)   # 1 step right
place red block at (0, 1, 0)   # 1 block up
place red block at (0, 0, 1)   # 1 step forward
```

**Which ruler goes to your right? Circle one:** x · y · z

**A block at y = 3 is …? Circle one:** on the ground · 3 blocks up

**Which ruler goes forward? Circle one:** x · y · z

---

## 4 · Put Them Together 🧭

Read **(5, 2, 3)** in three steps:

| Step | Number | Ruler | Do this |
|---|---|---|---|
| 1 | x = 5 | left → right | go 5 to your right |
| 2 | y = 2 | down → up | go 2 up (the ground is 0) |
| 3 | z = 3 | back → forward | go 3 forward |

**Which coordinate is on the ground? Circle one:** (2, 1, 2) · (2, 0, 2)

**These two blocks are stacked. Which number grew?**

```
place red block at (7, 1, 2)
place red block at (7, 2, 2)
```

**Circle one:** x · y · z

---

## 5 · Show Your Work 📸🎥

**Warm-up:** stand on your home spot and place one block at **(3, 0, 3)**. Check it against your rulers.

Open the world. Part of the shape is **already built** for you:

<img src="../assets/guide-partial-build.png" alt="A half-built shape made of gold ore blocks, standing on the white grid beside the striped ruler" style="width:100%; max-width:330px; border-radius:8px; display:block; margin:10px 0">

The rest of the blocks are **missing**. Here they are, spread apart so you can see each one:

<img src="../assets/guide-missing-blocks.png" alt="The missing blocks laid out apart on the white grid — red blocks and one long yellow block" style="width:100%; max-width:300px; border-radius:8px; display:block; margin:10px 0">

**Finish the shape.** Count x, then y, then z for every block you place.

**Write each block's coordinate here before you place it.**

<div class="write-space tall"></div>

> 🧱 The corner block is **(0, 0, 0)**. Use the same blocks you see in the world.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Count one block out loud — x, then y, then z.

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

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
