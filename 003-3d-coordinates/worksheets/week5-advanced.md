# 🗿 M003 Week 5 — English Worksheet (Advanced)

**Topic:** Recreate the Statues (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced · **Time:** about 45 minutes

A statue is many **stacked fill boxes**: two legs, a torso, a head, and two arms. One **`fill`** makes a solid box between **two corners**, each written **(x, y, z)** — x **across**, y **up**, z **forward**. To make a real figure you have to plan: where each part **starts** (its bottom y), how **wide** it is (x and z), and that the feet sit on the **ground (y = 0)**.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your head.

---

## 1 · Predict 🔮

Read each box. Write what you will see, and where it sits on the statue.

```
fill GRAY from (3, 0, 4) to (3, 2, 4)
fill GRAY from (5, 0, 4) to (5, 2, 4)
```

**Two thin boxes, x = 3 and x = 5, both y = 0–2. What part of the statue is this, and why two of them?**

<div class="write-space"></div>

```
fill GRAY from (2, 3, 4) to (2, 5, 4)
fill GRAY from (6, 3, 4) to (6, 5, 4)
```

**These start at y = 3 and sit at x = 2 and x = 6 — outside the legs. What part is this?**

<div class="write-space"></div>

```
fill WHITE from (3, 7, 4) to (5, 8, 4)
```

**This is the highest box (y = 7–8). What part of the statue is it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block is broken. Read what it should do, write the fixed code, then explain.

**Bug A** — The torso should sit **on top** of the legs. The legs go y = 0–2, so the torso should start at y = 3. Right now the torso starts at **y = 0**, so it builds over the legs and nothing rises.

```
fill GRAY from (3, 0, 4) to (5, 6, 4)
```

**Hint:** the **2nd number (y)** is height. Where should the torso's bottom y be?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should be the **right arm**, hanging on the **side** of the torso at x = 6. The torso fills x = 3–5, so x = 4 is **inside** it — the arm disappears into the body.

```
fill GRAY from (4, 3, 4) to (4, 5, 4)
```

**Hint:** to be on the outside, the arm's **1st number (x)** must be past the torso's x = 3–5.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** *(the tricky one)* — Your friend says their whole statue is **floating** — there is a gap of air under the feet. The legs are built at **y = 1–3** instead of touching the ground. The bottom of the feet must be on the floor.

```
fill GRAY from (3, 1, 4) to (3, 3, 4)
fill GRAY from (5, 1, 4) to (5, 3, 4)
```

**Hint:** the ground is **y = 0**. What is the lowest y a foot should have?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build the Statue 📸

Walk around a statue in your world. Then plan and build a **full golem** on your home spot — **6 fill boxes**: two legs, a torso, two arms, and a head.

> 🧱 Recipe (every corner is **(x, y, z)**):
> - left leg: gray from (3, 0, 4) to (3, 2, 4)
> - right leg: gray from (5, 0, 4) to (5, 2, 4)
> - torso: gray from (3, 3, 4) to (5, 6, 4)
> - left arm: gray from (2, 3, 4) to (2, 5, 4)
> - right arm: gray from (6, 3, 4) to (6, 5, 4)
> - head: white from (3, 7, 4) to (5, 8, 4)

Before you build, **plan the heights** in the space below: which y does each part start and stop at? Then build, and send a **photo or video**. Finish these — 4 to 6 sentences.

> I planned the heights like this: legs y = … , torso y = … , head y = …
>
> The feet touch the ground because the lowest **y** is …
>
> My arms sit on the outside because their **x** is …
>
> Each part stacks on the one below because its **y** starts at …
>
> One part I had to fix was … because …
>
> If I had more time, I would add …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Film yourself showing your statue. Try to use these words: **fill**, **box**, **x**, **y**, **z**, **stack**, **ground**, **home spot**.

> 1. Show your home spot and stand on it. Say why you stand there every run.
> 2. Walk around your statue — show the front, a side, and the back.
> 3. Point at one part and read its corners: "from x …, y …, z … to x …, y …, z …".
> 4. Say in your own words how you know the head ends up on top and the feet stay on the ground.

**Plan what you will say:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
