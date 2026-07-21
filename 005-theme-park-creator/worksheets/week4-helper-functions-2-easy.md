# 🎢 005 Week 4 — Helper Functions 2 (Extension · Easy)

**Topic:** Petting Zoo — Helper Functions · **Course:** Theme Park Creator · **Level:** Easy · **Time:** about 45 minutes

This is the code you are learning this week. It builds a whole **petting zoo**: a fence, some trees, and animals inside.

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

> 💡 **The big idea:** `petting_zoo` is the **boss**. It does no building itself — it just **calls** three **helper functions**, and each helper does **one** job. Write each job once, and the boss puts them together.

---

## 1 · Who Does What? 🧩

Read the code above. Fill the table.

| Function | Its one job (in your words) | Boss or helper? |
|---|---|---|
| `post` |  |  |
| `tree` |  |  |
| `animals` |  |  |
| `petting_zoo` |  |  |

> 💡 A **helper** is just a function that **another** function calls. There is no special keyword — the word describes its **job**, not its code.

---

## 2 · The Hollow Fence 🧱

Look at `post`. It runs **two** fills. A big solid square, then it carves the middle back to `AIR`.

```text
   fill 1 — solid fence           fill 2 — carve middle to AIR
      ## ## ## ## ## ##               ## ## ## ## ## ##
      ## ## ## ## ## ##               ## .  .  .  .  ##
      ## ## ## ## ## ##      -->      ## .  .  .  .  ##
      ## ## ## ## ## ##               ## .  .  .  .  ##
      ## ## ## ## ## ##               ## ## ## ## ## ##
   (x, z) to (x+15, z+15)         (x+1, z+1) to (x+14, z+14)
```

**What is left after both fills? How thick is the fence wall, and why is fill 2 moved in by exactly 1?**

<div class="write-space"></div>

---

## 3 · Predict — Everything Comes From x and z 🔮

Every block is placed **relative** to `x` and `z` (like `x+3`, `z+11`). Right now the boss is called with `petting_zoo(5, 5)`.

**a)** The trees are at `x+3`. With `petting_zoo(5, 5)`, what is the real `x` value of the trees?

<div class="write-space short"></div>

**b)** You change the last line to `petting_zoo(30, 5)`. What moves — the fence, the trees, the animals, or all of them? **Why?**

<div class="write-space"></div>

> 💡 This is the whole point of parameters: the boss hands `x, z` down to **every** helper, so the **whole zoo** moves together with one number.

---

## 4 · Spot the Bug 🐛

Look closely at `animals`. It loops 7 times, but all 7 chickens land in the **same spot**.

```python
def animals(x, z):
    for i in range(7):
        mobs.spawn(CHICKEN, pos(x+6, 0, z+3))
```

**a) Why do all 7 chickens spawn on top of each other?** (Hint: look at where `i` is used… or not used.)

<div class="write-space short"></div>

**b) Rewrite the `mobs.spawn` line so each chicken is 2 blocks further along than the last.** Use `i` in the position.

<div class="write-space short"></div>

---

## 5 · Extend the Zoo 💧

Add **one new helper** that digs a little pond, then let the boss call it. Fill the blank.

```python
def pond(x, z):
    blocks.fill(WATER, pos(x+8, 0, z+9), pos(x+11, 0, z+12), FillOperation.REPLACE)

def petting_zoo(x, z):
    post(x, z)
    tree(x, z)
    animals(x, z)
    ____(x, z)          # <-- call your new pond helper
```

> 💡 See how easy it grows? One new helper + one new line in the boss. The boss stays short and readable no matter how big the zoo gets.

**In your homework world: add the pond, then change one more thing of your own** (a different animal, more trees, a bigger fence). Write what you added and what happened:

<div class="write-space tall"></div>

---

## 6 · Show Your Work 🎥

Record **one video**, one take, on your phone. Show in order:

**1 · Your code.** Scroll through it. Point at the boss and the four helpers.

**2 · Your zoo.** Point the camera. Name the fence, the trees, the animals.

Then say these out loud, filling the blanks:

> Today I built ______.
>
> The boss function is ______, and it calls ______, ______, and ______.
>
> A helper function is ______.
>
> My favourite part was ______ because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
