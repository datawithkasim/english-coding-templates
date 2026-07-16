# 🎢 005 Week 4 — English Worksheet (Beginner)

**Topic:** Petting Zoo — Using Helper Functions · **Course:** Theme Park Creator · **Level:** Beginner · **Time:** about 30 minutes

Your park has stalls and amenities. Now it needs a **petting zoo** — a fence around it, cages inside, animals, and a feeding area.

Every cage is the same job: a fence box with an animal inside. So you write that job **once** as a **helper**, then call it for every animal.

These are the blocks you use this week:

```python
corner1 = pos(0, 0, 0)
corner2 = pos(18, 0, 12)
blocks.fill(OAK_FENCE, corner1, corner2, FillOperation.OUTLINE)
mobs.spawn(CHICKEN, pos(3, 1, 3))
```

> `corner1` and `corner2` are the **two corners** of the box you fill.
> `FillOperation.OUTLINE` builds only the **edge** of the box — the fence ring.
> `mobs.spawn(animal, pos(x, y, z))` puts **one** animal in **one** spot.
> `OAK_FENCE` = the fence. `HAY_BLOCK` = the food. `WATER` = the drink.

---

## 1 · How to Use a Helper Function 🧰

A **helper function** does one job. Other functions **call** it instead of writing that job again.

Four steps, every time:

**Step 1 — Find the job that repeats.** Six cages. Same job, six times.

**Step 2 — Write the job once.** Give it a name that says the job: `build_cage`.

**Step 3 — Put the changing parts in the brackets.** The animal changes. The spot changes. Those become **parameters**.

**Step 4 — Call it.** Once per animal, with different arguments.

```text
   build_zoo()
        │
        ├─▶ build_cage(CHICKEN, 2, 2)    ← same helper
        ├─▶ build_cage(COW, 6, 2)        ← same helper
        └─▶ build_cage(PIG, 10, 2)       ← same helper
```

```python
def build_cage(animal, x, z):
    corner1 = pos(x, 0, z)
    corner2 = pos(x + 2, 0, z + 2)
    blocks.fill(OAK_FENCE, corner1, corner2, FillOperation.OUTLINE)
    mobs.spawn(animal, pos(x + 1, 1, z + 1))

build_cage(CHICKEN, 2, 2)
build_cage(COW, 6, 2)
```

**Which line of `build_cage` builds the fence? Circle one:** `blocks.fill` · `mobs.spawn` · `corner1`

**How many times is `build_cage` written? Circle one:** once · twice · six times

**How many cages do those two calls build? Circle one:** 1 · 2 · 6

---

## 2 · Predict 🔮

Read the code. Circle your answer.

```python
def build_cage(animal, x, z):
    corner1 = pos(x, 0, z)
    corner2 = pos(x + 2, 0, z + 2)
    blocks.fill(OAK_FENCE, corner1, corner2, FillOperation.OUTLINE)
    mobs.spawn(animal, pos(x + 1, 1, z + 1))

build_cage(SHEEP, 6, 2)
```

**`6` goes into the box named `x`. What goes into the box named `animal`? Circle one:** `SHEEP` · `6` · `2`

**Which animal appears? Circle one:** `SHEEP` · `COW` · `CHICKEN`

```python
build_cage(PIG, 10, 2)
build_cage(RABBIT, 10, 8)
```

**Both calls send `10`. What is different about the two cages? Circle one:** the animal and the z spot · nothing · the fence

---

## 3 · Find the Difference 🐛

Clean code first, then a broken version. Circle the answer.

**Pair A** — The cage should have a fence **and** an animal.

```python
# clean
def build_cage(animal, x, z):
    corner1 = pos(x, 0, z)
    corner2 = pos(x + 2, 0, z + 2)
    blocks.fill(OAK_FENCE, corner1, corner2, FillOperation.OUTLINE)
    mobs.spawn(animal, pos(x + 1, 1, z + 1))
```

```python
# buggy
def build_cage(animal, x, z):
    corner1 = pos(x, 0, z)
    corner2 = pos(x + 2, 0, z + 2)
    blocks.fill(OAK_FENCE, corner1, corner2, FillOperation.OUTLINE)
```

**What is wrong? Circle one:** it never spawns the animal · it never builds the fence · nothing

**Pair B** — Six animals should stand in six cages.

```python
# clean
build_cage(CHICKEN, 2, 2)
build_cage(COW, 6, 2)
build_cage(PIG, 10, 2)
```

```python
# buggy
build_cage(CHICKEN, 2, 2)
build_cage(COW, 2, 2)
build_cage(PIG, 2, 2)
```

**What is wrong? Circle one:** every animal goes to the same spot · the animals are the same · the helper is missing

---

## 4 · Fill the Gap ✏️

The zoo needs a **feeding area** — hay to eat, water to drink. The water line is missing.

```python
def build_feeding_area(x, z):
    corner1 = pos(x, 0, z)
    corner2 = pos(x + 2, 0, z + 1)
    blocks.fill(HAY_BLOCK, corner1, corner2, FillOperation.REPLACE)
    ____________________

build_feeding_area(14, 4)
```

**Which line is missing? Circle one:** `blocks.place(WATER, pos(x + 4, 0, z))` · `build_feeding_area(14, 4)` · `mobs.spawn(COW, pos(x, 1, z))`

---

## 5 · Show Your Work 📸🎥

Switch to your homework world. Build your petting zoo:

- one big `OAK_FENCE` ring around the whole zoo
- a `build_cage(animal, x, z)` helper — fence box, then `mobs.spawn`
- call it **six** times, with **six different animals**, at six different spots
- a `build_feeding_area(x, z)` with hay and water

Animals you can use: `CHICKEN` · `COW` · `PIG` · `SHEEP` · `RABBIT` · `LLAMA`

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

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
