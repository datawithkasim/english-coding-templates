# 🧊 M003 Week 6 — English Worksheet

**Topic:** Building Solid Shapes with the Builder · **Course:** 3D Coordinates · **Time:** about 45 minutes

This week you use the **builder** — an invisible helper that moves through the world. The pattern is always the same: move the builder to the start, **place a mark**, move along **x**, **y**, or **z**, then **trace** or **fill** between the mark and where the builder is now.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine it happening, write what you think you will see.

```
move builder to (0, 0, 0)
place mark
move builder along x by 5
fill from mark with stone
```

**The builder marks, then moves along x only. What shape appears — a line, a wall, or a box?**

<div class="write-space"></div>

```
move builder to (0, 0, 0)
place mark
move builder along x by 5
move builder along y by 3
fill from mark with stone
```

**Now the builder also moves up along y. What shape does `fill` make this time? How tall is it?**

<div class="write-space"></div>

```
move builder to (0, 0, 0)
place mark
move builder along x by 5
move builder along z by 5
move builder along y by 3
fill from mark with stone
```

**The builder moves along all three axes — x, z, and y. What shape do you get now? Is it flat or solid?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should build a stone line from **(0, 0, 0)** to **(5, 0, 0)**. Right now only one block appears.

```
move builder to (0, 0, 0)
move builder along x by 5
place mark
fill from mark with stone
```

**Hint:** the mark must go down **before** the builder moves, not after.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should trace a wall that **starts at the corner (0, 0, 0)**. Right now the wall appears wherever the builder happened to be standing.

```
place mark
move builder along x by 6
trace wall with stone
move builder to (0, 0, 0)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should fill a stone wall 5 long and 3 tall. Right now `fill from mark` has nothing to work with.

```
move builder to (0, 0, 0)
move builder along x by 4
move builder along y by 2
fill from mark with stone
```

**Hint:** read every line — is there a `place mark` anywhere?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Use the builder to make a **solid shape**: move to a start corner, place a mark, move along at least **two axes**, then fill. When you finish, come back here.

Send a photo or video of your shape, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I moved the builder to …
>
> I placed the mark before … because …
>
> The builder moved along … and then along …
>
> The shape I got was …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your shape in the world. Talk through it like you are teaching someone who has never seen the builder. Try to use these words: **builder**, **mark**, **trace**, **fill**, **axis**.

> 1. Show the empty spot, then run your code so the shape appears.
> 2. Point at the start corner and say where the mark went down.
> 3. Say which axes the builder moved along — x, y, or z — and in what order.
> 4. Say in your own words why the mark must come **before** the builder moves.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
