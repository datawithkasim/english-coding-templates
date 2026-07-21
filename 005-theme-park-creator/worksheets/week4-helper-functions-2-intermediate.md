# 🎢 005 Week 4 — Helper Functions 2 (Extension · Intermediate)

**Topic:** Petting Zoo — Helper Functions · **Course:** Theme Park Creator · **Level:** Intermediate · **Time:** about 50 minutes

This is your week 4 code. One **boss** function, three **helpers**, and every block placed **relative** to `x` and `z`.

```python
def post(x, z):
    blocks.fill(OAK_FENCE, pos(x, 0, z), pos(x+15, 0, z+15), FillOperation.REPLACE)
    blocks.fill(AIR, pos(x+1, 0, z+1), pos(x+14, 0, z+14), FillOperation.REPLACE)

def tree(x, z):
    blocks.place(OAK_SAPLING, pos(x+3, 0, z+3))
    blocks.place(OAK_SAPLING, pos(x+3, 0, z+7))
    blocks.place(OAK_SAPLING, pos(x+3, 0, z+11))

def animals(x, z):
    for i in range(7):
        mobs.spawn(CHICKEN, pos(x+6, 0, z+3))

def petting_zoo(x, z):
    post(x, z)
    tree(x, z)
    animals(x, z)

petting_zoo(5, 5)
```

---

## 1 · Run Order 🔢

You type `petting_zoo(5, 5)`. The boss runs its lines **top to bottom**, and each helper finishes **completely** before the next starts.

**a) Number the order these happen: fence built ⬜ · trees placed ⬜ · chickens spawned ⬜.**

<div class="write-space short"></div>

**b) Could a chicken appear before the fence exists? Why / why not?**

<div class="write-space short"></div>

---

## 2 · Work Out the Coordinates 📐

With `petting_zoo(5, 5)`, `x = 5` and `z = 5`. Add the offsets and fill the real numbers.

| Thing | Code | Real x | Real z |
|---|---|---|---|
| Fence far corner | `pos(x+15, 0, z+15)` |  |  |
| First tree | `pos(x+3, 0, z+3)` |  |  |
| Third tree | `pos(x+3, 0, z+11)` |  |  |
| Chicken spawn | `pos(x+6, 0, z+3)` |  |  |

---

## 3 · Predict — Two Zoos 🔮

You add a second line: `petting_zoo(30, 5)`.

**a) What are the two far corners of the second fence?**

<div class="write-space short"></div>

**b) The first fence reaches x = 20. The second starts at x = 30. Do the two zoos touch, overlap, or leave a gap? Show the numbers.**

<div class="write-space"></div>

> 💡 Because every block comes from `x` and `z`, moving a whole zoo is **one number**. That is the power of parameters.

---

## 4 · Spot the Bug 🐛

**Bug A** — All 7 chickens land in the same spot.

```python
def animals(x, z):
    for i in range(7):
        mobs.spawn(CHICKEN, pos(x+6, 0, z+3))
```

**Why? Rewrite the spawn line so each chicken is 1 block further along than the last.**

<div class="write-space short"></div>

**Not a bug, but messy** — `tree` is three copy-paste lines. The saplings sit at `z+3`, `z+7`, `z+11` (step of 4).

**Rewrite `tree` using a `for` loop so the three saplings come from *one* line inside the loop.**

<div class="write-space tall"></div>

---

## 5 · Extend the Zoo 💧

Add a `pond` helper, and call it from the boss. Then add **one more helper of your own** (a gate, a bench, a path) and call that too.

```python
def pond(x, z):
    blocks.fill(WATER, pos(x+8, 0, z+9), pos(x+11, 0, z+12), FillOperation.REPLACE)
```

**Write your new helper and your updated `petting_zoo` boss (with all the calls):**

<div class="write-space tall" style="min-height: 240px"></div>

---

## 6 · Show Your Work 🎥

Record **one video**, one take, on your phone. Show in order:

**1 · Your code.** Scroll through it. Point at the boss and every helper.

**2 · Your zoo.** Point the camera. Name the fence, trees, animals, pond, and your own helper.

Then say these out loud, filling the blanks:

> The boss function is ______. It calls these helpers: ______.
>
> I moved / resized the zoo by changing ______.
>
> The trickiest part was ______ because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
