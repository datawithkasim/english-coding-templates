# 🔷 M001 Week 7 — English Worksheet

**Topic:** Pyramid Variations · **Course:** Pyramid Problems · **Time:** about 45 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build **one pyramid variation** — hollow, stepped, two-block pattern, or your own idea. Give your variation a **name** and a **one-sentence description**. When you finish, come back here.

Send a photo or video of your variation, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My variation is called …
>
> The idea is …
>
> I changed the … part of the code to make it different.
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would change …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your variation. Talk through it like you are teaching someone who has never seen it. Try to use these words: **hollow**, **stepped**, **layer**, **variation**, **edge**.

> 1. Walk around your pyramid and show what makes it different.
> 2. Read your loops out loud and say which part you changed.
> 3. Show one bug you hit and how you fixed it.
> 4. Say the name of your variation and what makes it interesting.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
