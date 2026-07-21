# 🎢 005 Week 4 — Helper Functions 2 (Extension · Advanced)

**Topic:** Petting Zoo — Helper Functions · **Course:** Theme Park Creator · **Level:** Advanced · **Time:** about 55 minutes

Your week 4 code. A **boss** that calls three **helpers**, every block offset from `x, z`.

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

## 1 · Trace the Call Chain 🪆

When a function calls another, it **pauses** and waits. The called function runs to the end, then hands control **back to whoever called it**. Follow the arrows.

```text
   YOU TYPE:  petting_zoo(5, 5)
        |
        |  line 1 --> post(5, 5)          [boss pauses]
        |                 |-- 2 fills: solid fence, then carve AIR
        |            <-- back to petting_zoo
        |
        |  line 2 --> tree(5, 5)          [boss pauses]
        |                 |-- 3 saplings
        |            <-- back to petting_zoo
        |
        |  line 3 --> animals(5, 5)       [boss pauses]
        |                 |-- for i in range(7): spawn CHICKEN
        v            <-- back to petting_zoo, done
```

**a) While `post` is running, is `petting_zoo` finished, or paused and waiting? Explain.**

<div class="write-space short"></div>

**b) Count every function *run* for one `petting_zoo(5, 5)` — count the boss, each helper, and each `mobs.spawn` inside the loop.**

<div class="write-space short"></div>

---

## 2 · Make the Size a Parameter 📐

Right now the fence size is hardcoded (`+15`, `+14`). Turn it into a **parameter** so one helper can build any size.

```python
def post(x, z, size):
    blocks.fill(OAK_FENCE, pos(x, 0, z), pos(x+____, 0, z+____), FillOperation.REPLACE)
    blocks.fill(AIR, pos(x+1, 0, z+1), pos(x+____, 0, z+____), FillOperation.REPLACE)
```

**a) Fill the four blanks in terms of `size`.**

<div class="write-space short"></div>

**b) What does `post(5, 5, 25)` build compared to `post(5, 5, 15)`? Give the far corner of each.**

<div class="write-space short"></div>

---

## 3 · Fix and Generalise `animals` 🐔

The chickens pile up (the loop never uses `i`), and the count 7 is hardcoded. Fix **both**: spread them out *and* take the number as a parameter.

```python
def animals(x, z, n):
    for i in range(n):
        mobs.spawn(CHICKEN, pos(____, 0, ____))
```

**Fill the two blanks so `n` chickens spawn in a spread-out line.**

<div class="write-space short"></div>

---

## 4 · A Row of Zoos 🎡

Because the boss takes `x, z`, you can loop the **boss itself**:

```python
for i in range(3):
    petting_zoo(5 + i*20, 5)
```

**a) Write the starting `x` of each of the three zoos.**

<div class="write-space short"></div>

**b) Each fence is 15 wide. The step is 20. Why does 20 work but `i*10` would break the zoos? Show the numbers.**

<div class="write-space"></div>

> 💡 This is the whole reward of helper functions: one boss, written once, becomes a **row of zoos** from a 2-line loop. Nothing is copy-pasted.

---

## 5 · Design and Build 🏗️

In your homework world, upgrade the zoo:

- `post` takes a `size` parameter.
- `animals` takes a `count` parameter and spreads them out.
- Add **two** new helpers of your own (e.g. `pond`, `gate`), called by the boss.
- Build a **row of 3 zoos** with a loop, and make at least one a different size.

**Write your full code — all helpers, the boss, and the loop that builds the row:**

<div class="write-space tall" style="min-height: 420px"></div>

**Trace one chicken from the very top down to its `mobs.spawn`. Name every function it passes through, and the `x, z` (and `count`) at each level.**

<div class="write-space tall" style="min-height: 160px"></div>

---

## 6 · Show Your Work 🎥

Record **one video**, one take, on your phone. Show in order:

**1 · Your code.** Scroll through it. Point at the boss, every helper, and your parameters.

**2 · Your row of zoos.** Walk the camera down the row. Name each part.

Then say these out loud, filling the blanks:

> A helper function is ______, and my boss function is ______.
>
> I turned ______ into a parameter, which let me ______.
>
> I built a whole row of zoos by ______.
>
> The hardest idea this week was ______ because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
