# 🎢 005 Week 3 — English Worksheet (Advanced)

**Topic:** Amenities — Functions Calling Functions · **Course:** Theme Park Creator · **Time:** about 50 minutes

Your park has a market row. Now it needs **amenities** — a **bathroom**, a **janitor room**.

Both are rooms, so **one** `build_room` helper builds both. Each amenity function calls the helper, then adds its own fitting. Then one more function calls **both amenities** — a chain three levels deep.

These are the blocks you use this week:

```python
blocks.fill(QUARTZ_BLOCK, pos(x1, 0, z1), pos(x2, 3, z2), FillOperation.HOLLOW)
blocks.fill(AIR, pos(x1 + 1, 1, z1), pos(x1 + 1, 2, z1), FillOperation.REPLACE)
blocks.place(CAULDRON, pos(x1 + 1, 1, z1 + 1))
```

> `blocks.fill(material, corner1, corner2, ...)` fills a box between two corners.
> `FillOperation.HOLLOW` = outer **shell** only — the middle is **cleared to air**.
> `FillOperation.REPLACE` = the **whole solid** box.
> `blocks.place(block, pos(x, y, z))` puts **one** block in **one** spot.
> `CAULDRON` = the toilet. `BARREL` = the janitor's supplies.

---

## 1 · Meet the Call Chain 🧰

A **helper function** does one job. Functions above it **call** it. Functions above *those* call **them**.

```text
   build_amenities(2)
        │
        ├─▶ build_bathroom(2, 8, 0, 6)
        │        ├─▶ build_room(QUARTZ_BLOCK, STONE, 2, 8, 0, 6)
        │        └─▶ place CAULDRON
        │
        └─▶ build_janitor_room(10, 14, 0, 4)
                 ├─▶ build_room(OAK_PLANKS, STONE, 10, 14, 0, 4)
                 └─▶ place BARREL
```

One `build_room` runs twice — different materials, different corners. The helper takes **four corners**, so the caller decides where each room sits and how big it is.

```python
def build_room(wall, floor, x1, x2, z1, z2):
    blocks.fill(wall, pos(x1, 0, z1), pos(x2, 3, z2), FillOperation.HOLLOW)
    blocks.fill(floor, pos(x1, 0, z1), pos(x2, 0, z2), FillOperation.REPLACE)
    blocks.fill(AIR, pos(x1 + 1, 1, z1), pos(x1 + 1, 2, z1), FillOperation.REPLACE)
```

**One helper is called by two functions, which are called by a third. What would you have to change if the doorway needed to be two blocks wide?**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each function. Write what you think happens.

```python
def build_bathroom(x1, x2, z1, z2):
    build_room(QUARTZ_BLOCK, STONE, x1, x2, z1, z2)
    blocks.place(CAULDRON, pos(x1 + 1, 1, z1 + 1))

def build_janitor_room(x1, x2, z1, z2):
    build_room(OAK_PLANKS, STONE, x1, x2, z1, z2)
    blocks.place(BARREL, pos(x1 + 1, 1, z1 + 1))

build_bathroom(2, 8, 0, 6)
```

**Which lines run, and in what order? Which materials reach `build_room`, and which never do?**

<div class="write-space"></div>

```python
def build_amenities(x):
    build_bathroom(x, x + 6, 0, 6)
    build_janitor_room(x + 8, x + 12, 0, 4)

build_amenities(2)
build_amenities(20)
```

**`build_amenities` is called twice. How many rooms are built, and how many times does `build_room` run?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block is broken. Read what it should do, rewrite it so it works, then explain why the original was wrong.

**Bug A** — This should build a bathroom **next to** a janitor room. Instead only **one** room is there — wooden, with a barrel. The cauldron is gone.

```python
def build_amenities(x):
    build_bathroom(x, x + 6, 0, 6)
    build_janitor_room(x, x + 6, 0, 6)

build_amenities(2)
```

**Hint:** look at the corners each amenity is given.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The bathroom should hold a cauldron. The room builds fine, but the **cauldron never survives**.

```python
def build_bathroom(x1, x2, z1, z2):
    blocks.place(CAULDRON, pos(x1 + 1, 1, z1 + 1))
    build_room(QUARTZ_BLOCK, STONE, x1, x2, z1, z2)

build_bathroom(2, 8, 0, 6)
```

**Hint:** `FillOperation.HOLLOW` clears the middle of the room to air. The cauldron is in the middle.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The janitor room should be a wide, shallow box. It comes out the **wrong shape**, and the barrel is not inside it.

```python
def build_janitor_room(x1, x2, z1, z2):
    build_room(OAK_PLANKS, STONE, x1, z1, x2, z2)
    blocks.place(BARREL, pos(x1 + 1, 1, z1 + 1))

build_janitor_room(10, 14, 0, 4)
```

**Hint:** the helper's parameters are `(wall, floor, x1, x2, z1, z2)`. Which value landed in `x2`?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Build the Amenity Block 🚻

In your homework world, write **one** helper and **three** functions that call down into it:

```python
def build_room(wall, floor, x1, x2, z1, z2):
def build_bathroom(x1, x2, z1, z2):
def build_janitor_room(x1, x2, z1, z2):
def build_amenities(x):
```

`build_room` must build:

- **walls** from the `wall` material with `FillOperation.HOLLOW`
- a **floor** from the `floor` material
- a **doorway** carved with `AIR` so a visitor can walk in

`build_bathroom` calls `build_room`, then places a `CAULDRON` inside.
`build_janitor_room` calls `build_room` with different materials, then places a `BARREL` inside.
`build_amenities(x)` calls both, giving each its own corners so they stand side by side.

Only `build_room` may contain `blocks.fill`. Where the rooms sit must come from the corner parameters — no fixed corner numbers inside the helper.

Then build two amenity blocks in different corners of your park:

```python
build_amenities(2)
build_amenities(20)
```

**Write your helper, your amenity functions, and the lines that call them:**

<div class="write-space tall" style="min-height: 460px"></div>

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
