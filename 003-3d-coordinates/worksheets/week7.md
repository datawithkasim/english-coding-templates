# 🧊 M003 Week 7 — English Worksheet

**Topic:** Designing the Museum · **Course:** 3D Coordinates · **Time:** about 45 minutes

A museum brings together everything in this course: a **floor** laid out with (x, z), **pictures on the walls** drawn with (x, y), and **sculptures on pedestals** placed with (x, y, z). This week you make a **blueprint** — you decide the coordinates of every piece **before** you build, so nothing overlaps and every sculpture sits on its stand.

---

## 1 · Predict 🔮

Read each plan. Before you imagine it happening, write what you think you will see.

```
floor:    fill stone from (0, 0, 0) to (8, 0, 8)
picture:  (drawn on the back wall, where z = 0, using x and y)
pedestal: fill stone from (2, 0, 2) to (4, 1, 4)
```

**The floor is flat (y stays 0). The picture stands up the back wall. The pedestal is a short box. Looking down from above, do the picture and the pedestal sit in different places? Why won't they crash?**

<div class="write-space"></div>

```
pedestal A: fill stone from (1, 0, 1) to (2, 1, 2)
pedestal B: fill stone from (6, 0, 6) to (7, 1, 7)
```

**Two pedestals. Read their (x, z) footprints. Are they far apart or on top of each other? How do you know from the numbers?**

<div class="write-space"></div>

```
pedestal: fill stone from (2, 0, 2) to (4, 1, 4)
statue:   place gold block at (3, 2, 3)
```

**The pedestal fills up to height 1. The statue is placed at height 2. Does the statue rest on the pedestal, float above it, or sink into it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The statue should rest **on top** of the pedestal. The pedestal fills up to height 1, so the statue belongs at height 2. Right now it floats high in the air.

```
fill stone from (2, 0, 2) to (4, 1, 4)
place gold block at (3, 5, 3)
```

**Hint:** the top of the pedestal is one block above where the stone ends.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — These two pedestals should stand in **different corners** of the floor. Right now they share the same (x, z) footprint and pile up in one spot.

```
fill stone from (1, 0, 1) to (2, 1, 2)
fill stone from (1, 0, 1) to (2, 1, 2)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This picture should **stand up the back wall**, where z stays 0 and the blocks climb with x and y. Right now it is lying flat on the floor.

```
set x to 0
repeat 4 times:
    place red block at (x, 0, 0)
    add 1 to x
set x to 0
repeat 4 times:
    place red block at (x, 0, 1)
    add 1 to x
```

**Hint:** a wall picture grows **up** (y), it does not step **forward** (z). The second row should be one block higher, not one block forward.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Draw a **blueprint** of one museum room **before** you build. Looking down from above, mark the floor, the back wall picture, and at least **two pedestals** — and write the coordinates of each.

Floor: from ( … , … , … ) to ( … , … , … )

<div class="write-space"></div>

Pedestal 1: from ( … , … , … ) to ( … , … , … ) · its statue at ( … , … , … )

<div class="write-space"></div>

Pedestal 2: from ( … , … , … ) to ( … , … , … ) · its statue at ( … , … , … )

<div class="write-space"></div>

Now build your room from the blueprint, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I planned …
>
> I kept my two pedestals from overlapping by …
>
> Each statue sits on its pedestal because its height starts at …
>
> My wall picture stands up because it grows along … not …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk through your museum room. Talk through it like you are giving a tour. Try to use these words: **blueprint**, **floor**, **pedestal**, **sculpture**, **overlap**.

> 1. Show your blueprint on paper, then show the built room.
> 2. Point at two pedestals and say their (x, z) footprints, and why they don't overlap.
> 3. Show a statue resting on its pedestal and say the height it starts at.
> 4. Say in your own words how planning coordinates first made the room work.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
