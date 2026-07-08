# 🗿 M003 Week 5 — English Worksheet (Advanced)

**Topic:** Recreate the Statues (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced · **Time:** about 45 minutes

A statue is many **stacked fill boxes**: legs, a torso, arms, a head. One **`fill`** makes a solid box between **two corners** (x, y, z) — x **across**, y **up**, z **forward**, feet on the **ground (y = 0)**.

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your head.

---

## 1 · Predict 🔮

Read each box. Write what you will see, **where it sits**, **and the reason**.

```
fill GRAY from (3, 0, 4) to (3, 2, 4)
fill GRAY from (5, 0, 4) to (5, 2, 4)
```

**Two thin boxes, x = 3 and x = 5, both y = 0–2. What part is this, why two of them, and why y = 0?**

<div class="write-space"></div>

```
fill GRAY from (2, 3, 4) to (2, 5, 4)
fill GRAY from (6, 3, 4) to (6, 5, 4)
```

**These start at y = 3 and sit at x = 2 and x = 6 — outside the legs. What part is this, and why is the x outside?**

<div class="write-space"></div>

```
fill WHITE from (3, 7, 4) to (5, 8, 4)
```

**This is the highest box (y = 7–8). What part is it, and how do you know from the y?**

<div class="write-space"></div>

```
fill GRAY from (3, 3, 4) to (5, 6, 4)
fill WHITE from (3, 7, 4) to (5, 8, 4)
```

**Two boxes together. The torso ends at y = 6 but the head starts at y = 7. What sits between them, and what does that gap mean?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block is broken. Read what it should do, write the fixed code, then explain.

**Bug A** — The torso should sit **on top** of the legs. The legs go y = 0–2, so the torso should start at y = 3. Right now it starts at **y = 0**, so nothing rises.

```
fill GRAY from (3, 0, 4) to (5, 6, 4)
```

**Hint:** the **2nd number (y)** is height. Where should the torso's bottom y be?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences.)**

<div class="write-space"></div>

**Bug B** — This should be the **right arm**, hanging on the **side** of the torso at x = 6. The torso fills x = 3–5, so x = 4 is **inside** it — the arm disappears into the body.

```
fill GRAY from (4, 3, 4) to (4, 5, 4)
```

**Hint:** to be on the outside, the arm's **1st number (x)** must be past the torso's x = 3–5.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences.)**

<div class="write-space"></div>

**Bug C** *(the tricky one)* — Your friend's whole statue is **floating** — a gap of air under the feet. The legs are built at **y = 1–3** instead of touching the ground. The feet must sit on the floor.

```
fill GRAY from (3, 1, 4) to (3, 3, 4)
fill GRAY from (5, 1, 4) to (5, 3, 4)
```

**Hint:** the ground is **y = 0**. What is the lowest y a foot should have?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work? (2–3 sentences.)**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Walk around a statue in your world. Then plan and build a **full golem** on your home spot — **6 fill boxes**: two legs, a torso, two arms, and a head.

> 🧱 Recipe (every corner is **(x, y, z)**, feet on the ground y = 0):
> - left leg: gray from (3, 0, 4) to (3, 2, 4)
> - right leg: gray from (5, 0, 4) to (5, 2, 4)
> - torso: gray from (3, 3, 4) to (5, 6, 4)
> - left arm: gray from (2, 3, 4) to (2, 5, 4)
> - right arm: gray from (6, 3, 4) to (6, 5, 4)
> - head: white from (3, 7, 4) to (5, 8, 4)

Before you build, **plan the heights** in the space below: which y does each part start and stop at?

> ✨ **Modify challenge:** after it works, change one thing of your own — a new colour, a different pose, or an extra part (a hat, a tail, longer arms). Write what you changed.

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
