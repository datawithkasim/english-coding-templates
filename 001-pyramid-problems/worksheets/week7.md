# 🔷 M001 Week 7 — English Worksheet

**Topic:** Pyramid Variations · **Course:** Pyramid Problems · **Time:** about 45 minutes

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
set size to 7
repeat size times:
    repeat size times:
        if row is 0 OR row is size-1 OR col is 0 OR col is size-1:
            place block down
        move forward
    [turn and walk back to start of next row]
```

**Which blocks get placed — all of them, or just some? Where?**

<div class="write-space"></div>

```
set size to 9
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 4
```

**How is this pyramid different from a normal one? How many layers?**

<div class="write-space"></div>

```
set size to 7
while size > 0:
    [build one HOLLOW size × size layer]
    move up by 1
    set size to size - 2
```

**Is this pyramid filled or hollow? Could a person walk inside it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block below is broken. Read what it should do, rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to build a **hollow layer** — only place a block when it is on the edge of the square (not in the middle).

```
repeat size times:
    repeat size times:
        place block down
        move forward
    [turn and walk back to start of next row]
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The agent is supposed to build a **stepped pyramid** where each layer is 4 blocks shorter than the one below.

```
set size to 9
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 1
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The agent is supposed to build a pyramid with a **gap of 2 blocks** between each layer (the layers float).

```
set size to 7
while size > 0:
    [build one size × size square layer]
    move up by 1
    set size to size - 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Build **one pyramid variation** — hollow, stepped, two-block pattern, or your own idea. Give your variation a **name** and a **one-sentence description**. When you finish, come back here.

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
