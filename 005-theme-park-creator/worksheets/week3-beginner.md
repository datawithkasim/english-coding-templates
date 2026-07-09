# 🎢 005 Week 3 — English Worksheet (Beginner)

**Topic:** Amenities — Functions Calling Functions · **Course:** Theme Park Creator · **Level:** Beginner · **Time:** about 30 minutes

Your park has stalls. Now it needs **amenities** — a **bathroom**, a **janitor room**.

Both are rooms. So you write **one** room function, and your amenity functions **call** it.

These are the blocks you use this week:

```python
blocks.fill(QUARTZ_BLOCK, pos(0, 0, 0), pos(4, 3, 4), FillOperation.HOLLOW)
blocks.place(CAULDRON, pos(1, 1, 1))
```

> `blocks.fill(...)` fills a box between two corners.
> `FillOperation.HOLLOW` builds only the **walls** and leaves the middle empty.
> `blocks.place(block, pos(x, y, z))` puts **one** block in **one** spot.
> `CAULDRON` = the toilet. `BARREL` = the janitor's supplies.

---

## 1 · Meet Helper Functions 🧰

A **helper function** does one job. Other functions **call** it instead of writing that job again.

```text
   build_bathroom(5)
        │
        ├─▶ build_room(QUARTZ_BLOCK, 5)   ← the helper builds the walls
        │
        └─▶ place CAULDRON                ← the bathroom adds its own thing
```

```python
def build_room(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)

def build_bathroom(size):
    build_room(QUARTZ_BLOCK, size)
    blocks.place(CAULDRON, pos(1, 1, 1))

build_bathroom(5)
```

**Which function builds the walls? Circle one:** `build_room` · `build_bathroom` · `blocks.place`

**Which function places the cauldron? Circle one:** `build_room` · `build_bathroom` · `blocks.fill`

---

## 2 · Predict 🔮

Read the code. Circle your answer.

```python
def build_room(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)

def build_bathroom(size):
    build_room(QUARTZ_BLOCK, size)
    blocks.place(CAULDRON, pos(1, 1, 1))

build_bathroom(5)
```

**`build_bathroom(5)` sends `5` to the helper. How wide is the room? Circle one:** 5 · 3 · 1

**What are the walls made of? Circle one:** `QUARTZ_BLOCK` · `CAULDRON` · `BARREL`

```python
def build_janitor_room(size):
    build_room(OAK_PLANKS, size)
    blocks.place(BARREL, pos(1, 1, 1))

build_janitor_room(4)
```

**The same helper builds this room too. What are these walls made of? Circle one:** `OAK_PLANKS` · `QUARTZ_BLOCK` · `BARREL`

---

## 3 · Find the Difference 🐛

Clean code first, then a broken version. Circle the answer.

**Pair A** — The bathroom should have walls **and** a cauldron.

```python
# clean
def build_bathroom(size):
    build_room(QUARTZ_BLOCK, size)
    blocks.place(CAULDRON, pos(1, 1, 1))
```

```python
# buggy
def build_bathroom(size):
    blocks.place(CAULDRON, pos(1, 1, 1))
```

**What is wrong? Circle one:** it never calls `build_room` · it never places the cauldron · nothing

**Pair B** — The helper wants the material first, then the size.

```python
# clean
def build_bathroom(size):
    build_room(QUARTZ_BLOCK, size)
```

```python
# buggy
def build_bathroom(size):
    build_room(size, QUARTZ_BLOCK)
```

**What is wrong? Circle one:** the two arguments are swapped · the size is missing · the material is missing

---

## 4 · Fill the Gap ✏️

The janitor room should have wooden walls, then a barrel. One line is missing.

```python
def build_room(wall, size):
    blocks.fill(wall, pos(0, 0, 0), pos(size, 3, size), FillOperation.HOLLOW)

def build_janitor_room(size):
    ____________________
    blocks.place(BARREL, pos(1, 1, 1))

build_janitor_room(4)
```

**Which line is missing? Circle one:** `build_room(OAK_PLANKS, size)` · `build_janitor_room(4)` · `blocks.place(BARREL, pos(1, 1, 1))`

---

## 5 · Show Your Work 📸🎥

Switch to your homework world. Write a `build_room` helper, then a `build_bathroom` function that **calls** it and places a `CAULDRON`. Call `build_bathroom` once.

Record **one video** (a phone is fine). Show two things:

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

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
