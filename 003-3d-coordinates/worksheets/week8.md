# 🧊 M003 Week 8 — English Worksheet

**Topic:** Final — My Own Museum · **Course:** 3D Coordinates · **Time:** about 60 minutes

This is your big final project — no new commands, every idea from this course in one build. Your museum is a **room** visitors walk into, with **flat pictures** on the walls (2D, x and y) and **solid sculptures** on pedestals (3D, x, y, z). Plan it like an architect: coordinates first, then build.

---

## 1 · Predict 🔮

Read each plan. Write what you think you will see.

```
# 2D art: a picture on the back wall — z stays 0, blocks climb with x and y
set x to 0
repeat 5 times:
    place red block at (x, 1, 0)
    add 1 to x
```

**Every block stays at z = 0; only x changes. Is this flat like a painting, or solid like a statue? From which direction do you look to see the whole picture?**

<div class="write-space"></div>

```
# 3D art: a sculpture on a pedestal — all three numbers used
fill stone from (4, 0, 4) to (5, 1, 5)
place gold block at (4, 2, 4)
place gold block at (5, 2, 5)
```

**This uses x, y, and z. Is it flat or solid? Can a visitor walk all the way around it? Where do the gold blocks sit — on top of the pedestal or beside it?**

<div class="write-space"></div>

```
gallery floor: fill stone from (0, 0, 0) to (10, 0, 10)
pedestal A:    fill stone from (2, 0, 2) to (3, 1, 3)
pedestal B:    fill stone from (7, 0, 7) to (8, 1, 8)
```

**Read the (x, z) footprints. Are the two pedestals far apart? Looking down from above, sketch in words where each one sits on the floor.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block below is broken. Read what it should do, fix it, then explain why the original was wrong and your fix works.

**Bug A** — The gallery should be a **hollow room** with a doorway. Right now it is a solid block of stone with no inside.

```
fill stone from (0, 0, 0) to (10, 4, 10)
fill air from (5, 2, 0) to (6, 3, 0)
```

**Hint:** before you can cut a doorway, the inside has to be hollowed out with air.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — These two sculptures should stand on **two different pedestals**. Right now both pedestals share the same (x, z) footprint, so they pile up in one spot.

```
fill stone from (2, 0, 2) to (3, 1, 3)
place gold block at (2, 2, 2)
fill stone from (2, 0, 2) to (3, 1, 3)
place blue block at (2, 2, 2)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This wall picture should be **flat 2D art** that stands up the back wall — z stays 0 while the picture climbs with x and y. Right now the second row steps **forward** onto the floor instead of **up** the wall.

```
set x to 0
repeat 4 times:
    place red block at (x, 1, 0)
    add 1 to x
set x to 0
repeat 4 times:
    place red block at (x, 1, 1)
    add 1 to x
```

**Hint:** to climb the wall, the row above should raise **y**, not raise z.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Blueprint Your Museum 🗺️

Plan **before** you build. Looking down from above, write the coordinates of every piece.

Gallery room: from ( … , … , … ) to ( … , … , … ) · doorway at ( … , … , … )

<div class="write-space"></div>

Wall picture 1 — shows … · stands on the wall where … stays 0

<div class="write-space short"></div>

Wall picture 2 — shows … · stands on the wall where … stays 0

<div class="write-space short"></div>

Pedestal 1: from ( … , … , … ) to ( … , … , … ) · sculpture on top at ( … , … , … )

<div class="write-space short"></div>

Pedestal 2: from ( … , … , … ) to ( … , … , … ) · sculpture on top at ( … , … , … )

<div class="write-space short"></div>

---

## 4 · Show Your Work 📸🎥

Now switch to your homework world and build your museum from your blueprint. Check your build against this list:

> ☐ A **gallery room** with a floor, walls, and a **doorway** to walk through.
>
> ☐ At least **two different flat pictures** on the walls — **2D art**, where only x and y change.
>
> ☐ At least **two sculptures**, each on its **own pedestal** — **3D art**, using x, y, and z.
>
> ☐ The two pedestals **do not overlap**, and each sculpture **rests on top** of its pedestal.
>
> ☐ The museum matches the coordinates on your blueprint.

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
