# 🎢 005 Week 3 — English Worksheet (Intermediate)

**Topic:** Amenities — Functions Calling Functions · **Course:** Theme Park Creator · **Time:** about 45 minutes

Your park has stalls. Now it needs **amenities** — a **bathroom**, a **janitor room**.

Both are rooms. So you write **one** `build_room` helper, and both amenity functions **call** it. Each one then adds its own fitting.

These are the blocks you use this week:

```python
blocks.fill(QUARTZ_BLOCK, pos(0, 0, 0), pos(4, 3, 4), FillOperation.HOLLOW)
blocks.fill(AIR, pos(2, 1, 0), pos(2, 2, 0), FillOperation.REPLACE)
blocks.place(CAULDRON, pos(1, 1, 1))
```

> `blocks.fill(material, corner1, corner2, ...)` fills a box between two corners.
> `FillOperation.HOLLOW` = outer **walls** only — the middle is **cleared to air**.
> `FillOperation.REPLACE` = the **whole solid** box.
> `blocks.place(block, pos(x, y, z))` puts **one** block in **one** spot.
> `CAULDRON` = the toilet. `BARREL` = the janitor's supplies.

---

## 1 · Meet Helper Functions 🧰

A **helper function** does one job well. Other functions **call** it instead of writing that job again.

```text
   build_bathroom(0, 5)                build_janitor_room(8, 4)
        │                                    │
        ├─ calls ─▶ build_room(...)  ◀─ calls ─┤     ← ONE helper, TWO callers
        │                                    │
        └─ places CAULDRON                   └─ places BARREL
```

The helper takes an `x` — where the room starts — so two rooms do not land on top of each other.

```python
def build_room(wall, floor, x, size):
    blocks.fill(wall, pos(x, 0, 0), pos(x + size, 3, size), FillOperation.HOLLOW)
    blocks.fill(floor, pos(x, 0, 0), pos(x + size, 0, size), FillOperation.REPLACE)
    blocks.fill(AIR, pos(x + 2, 1, 0), pos(x + 2, 2, 0), FillOperation.REPLACE)
```

**Why is writing `build_room` once better than writing the same three fills inside both amenity functions?**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each function. Write what you think happens.

```python
def build_bathroom(x, size):
    build_room(QUARTZ_BLOCK, STONE, x, size)
    blocks.place(CAULDRON, pos(x + 1, 1, 1))

build_bathroom(0, 5)
```

**What are the walls made of? What is the floor made of? Where does the cauldron sit?**

<div class="write-space"></div>

```python
def build_janitor_room(x, size):
    build_room(OAK_PLANKS, STONE, x, size)
    blocks.place(BARREL, pos(x + 1, 1, 1))

build_bathroom(0, 5)
build_janitor_room(8, 4)
```

**Both rooms use the same helper. What is different about them? Why is the janitor room's `x` an `8` and not a `0`?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block is broken. Read what it should do, rewrite it so it works, then explain why the original was wrong.

**Bug A** — This should build a bathroom: a room, then a cauldron. But only a **lonely cauldron** appears, with no room around it.

```python
def build_bathroom(x, size):
    blocks.place(CAULDRON, pos(x + 1, 1, 1))

build_bathroom(0, 5)
```

**Hint:** the helper exists, but nobody calls it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should give the bathroom **quartz walls** and a **stone floor**. But the walls come out stone and the floor comes out quartz.

```python
def build_bathroom(x, size):
    build_room(STONE, QUARTZ_BLOCK, x, size)
    blocks.place(CAULDRON, pos(x + 1, 1, 1))

build_bathroom(0, 5)
```

**Hint:** the helper's parameters are `(wall, floor, x, size)`. Arguments land in those boxes **by position**.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should build a room with a cauldron inside. The room appears, but the **cauldron is gone**.

```python
def build_bathroom(x, size):
    blocks.place(CAULDRON, pos(x + 1, 1, 1))
    build_room(QUARTZ_BLOCK, STONE, x, size)

build_bathroom(0, 5)
```

**Hint:** `FillOperation.HOLLOW` clears the middle of the room to air. The cauldron is in the middle.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Build the Amenities 🚻

In your homework world, write **one** helper and **two** functions that call it:

```python
def build_room(wall, floor, x, size):
def build_bathroom(x, size):
def build_janitor_room(x, size):
```

`build_room` must build:

- **walls** from the `wall` material with `FillOperation.HOLLOW`
- a **floor** from the `floor` material
- a **doorway** carved with `AIR` so a visitor can walk in

`build_bathroom` must call `build_room`, then place a `CAULDRON` inside.
`build_janitor_room` must call `build_room` with different materials, then place a `BARREL` inside.

Neither amenity function may contain a `blocks.fill` of its own — the walls, floor and doorway all come from the helper.

Then call them both, at different `x` values so they stand side by side:

```python
build_bathroom(0, 5)
build_janitor_room(8, 4)
```

**Write your helper, your two amenity functions, and the two lines that call them:**

<div class="write-space tall" style="min-height: 420px"></div>

---

## 5 · Show Your Work 📸🎥

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
