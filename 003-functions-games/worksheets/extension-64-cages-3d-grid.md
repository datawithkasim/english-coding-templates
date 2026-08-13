# 🦙 Functions Extension · 64 Cages — English Worksheet

**Topic:** One function, three loops · **Course:** Functions & Games · **Level:** Extension (after helper functions) · **Time:** about 45 minutes

Last time one function built one cage. This time the same function builds **64**, stacked in a **4 × 4 × 4** tower. Every cage holds an animal and stands on grass.

Your cage from last lesson:

```python
def make_cage(x: number, y: number, z: number, animal: number):
    blocks.fill(OAK_FENCE,
        pos(x, y, z),
        pos(x + 4, y + 3, z + 4), FillOperation.HOLLOW)
    blocks.fill(GRASS,
        pos(x, y, z),
        pos(x + 4, y, z + 4), FillOperation.REPLACE)
    mobs.spawn(animal, pos(x + 2, y + 1, z + 2))
```

One cage is **5 wide, 4 tall, 5 deep**.

---

## 1 · Predict 🔮

Read each one. Write the number **and the reason**.

```python
for col in range(4):
    make_cage(col * 6, 0, 0, LLAMA)
```

**How many cages? Which way do they run?**

<div class="write-space"></div>

```python
for row in range(4):
    for col in range(4):
        make_cage(col * 6, 0, row * 6, LLAMA)
```

**How many cages now? What shape do they make?**

<div class="write-space"></div>

```python
for level in range(4):
    for row in range(4):
        for col in range(4):
            make_cage(col * 6, level * 5, row * 6, LLAMA)
```

**How many cages? Which loop lifts them off the ground?**

<div class="write-space"></div>

**A cage is 4 tall. The levels are 5 apart. What would happen if you changed `level * 5` to `level * 3`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each one runs. Each one is wrong. Fix it, then say why.

**Bug A** — This should build 64 cages. You count 16.

```python
for row in range(4):
    for col in range(4):
        make_cage(col * 6, 0, row * 6, LLAMA)
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space"></div>

**Bug B** — Every animal disappears the moment the cage appears.

```python
def make_cage(x: number, y: number, z: number, animal: number):
    mobs.spawn(animal, pos(x + 2, y + 1, z + 2))
    blocks.fill(OAK_FENCE,
        pos(x, y, z),
        pos(x + 4, y + 3, z + 4), FillOperation.HOLLOW)
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space"></div>

**Bug C** — All 64 cages land in one flat layer, cutting through each other.

```python
for level in range(4):
    for row in range(4):
        for col in range(4):
            make_cage(col * 6, 0, row * 6, LLAMA)
```

**Write the fix:**

<div class="write-space"></div>

**Why was it wrong?**

<div class="write-space"></div>

---

## 3 · Read the Grid 🧊

Each loop owns one direction.

<div style="page-break-inside:avoid;break-inside:avoid;margin:14px 0" markdown="1">

| loop | it changes | direction |
|---|---|---|
| `col` | x | across |
| `level` | y | up |
| `row` | z | away from you |

</div>

Fill in the missing numbers for `make_cage(col * 6, level * 5, row * 6, LLAMA)`:

<div style="page-break-inside:avoid;break-inside:avoid;margin:14px 0" markdown="1">

| col | level | row | x | y | z |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | | | |
| 0 | 2 | 0 | | | |
| 1 | 1 | 1 | | | |
| 3 | 3 | 3 | | | |

</div>

**The last row is the far top corner. How far is that cage from where you stand?**

<div class="write-space"></div>

---

## 4 · Build It 🧱

Stand somewhere with open space above you and behind you. The tower needs about **20 blocks** in each direction.

Fill the blanks and run it:

```python
def make_cage(x: number, y: number, z: number, animal: number):
    blocks.fill(OAK_FENCE,
        pos(x, y, z),
        pos(x + 4, y + 3, z + 4), FillOperation.HOLLOW)
    blocks.fill(GRASS,
        pos(______, ______, ______),
        pos(x + 4, ______, z + 4), FillOperation.REPLACE)
    mobs.spawn(______, pos(x + 2, y + 1, z + 2))

for level in range(______):
    for row in range(______):
        for col in range(______):
            make_cage(col * 6, level * ______, row * 6, ______)
```

**Your tower must have:**

<div style="page-break-inside:avoid;break-inside:avoid;margin:14px 0" markdown="1">

| # | Check |
|---|---|
| 1 | 64 cages, 4 across, 4 up, 4 deep |
| 2 | an animal alive inside every cage |
| 3 | grass on the floor of every cage |
| 4 | no cage cutting through another cage |

</div>

Once the 64 stand up, keep going. Different animals on each level, or a gate you can walk through.

---

## 5 · Show Your Work 📸🎥

Run your code and walk around the finished tower.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

1. Your code on screen, and explain what each of the three loops does.
2. The tower in the world, and count a row of cages out loud.

**Fill the blanks:**

<div class="write-space tall" style="min-height: 340px"></div>

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

### Submit

Send your video on KakaoTalk.
