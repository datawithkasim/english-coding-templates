# 🕷️ M003 Extension — Build the Spider (Advanced)

**Topic:** 3D Spider (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced (Extension, after Week 6) · **Time:** about 45 minutes

Build a **red spider** in 3D — a fat body, eight legs spread out, two eyes on the front. Every block needs **three** numbers **(x, y, z)**: x **across**, y **up**, z **deeper** (forward).

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your spider.
>
> 🎨 Red parts = **red concrete**. Eyes = **black wool**.

---

## 1 · Predict 🔮

Read each set. Write your prediction **and the reason**.

```
place red block at (1, 1, 2)
place red block at (1, 1, 3)
place red block at (1, 1, 4)
```

**Does this leg go across, up, or deeper? Why?**

<div class="write-space"></div>

```
place red block at (1, 1, 2)
place red block at (5, 1, 2)
```

**These are two legs on opposite sides. What changed, and why does that move them apart? Why?**

<div class="write-space"></div>

```
place red block at (1, 1, 2)
place red block at (2, 1, 2)
place red block at (3, 1, 2)
```

**One leg bends across toward the body. Which number counts the bend? Why?**

<div class="write-space"></div>

```
place red block at (2, 3, 3)
place black block at (2, 3, 3)
```

**Same (x, y, z). Red, black, or both? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Fix each one. Then say why it was wrong.

**Bug A** — This eye should sit **up high on the front**, at (2, 3, 3). It has only two numbers, so it drops flat on the floor.

```
place black block at (2, 3)
```

**Fixed code:**

<div class="write-space"></div>

**Why wrong? Why does your fix work? (2–3 sentences)**

<div class="write-space"></div>

**Bug B** — This right-side leg should be **across on the right**: (5, 1, 3). The last two numbers are swapped.

```
place red block at (5, 3, 1)
```

**Fixed code:**

<div class="write-space"></div>

**Why wrong? Why does your fix work? (2–3 sentences)**

<div class="write-space"></div>

**Bug C** *(the tricky one)* — The code runs with no error, but this eye landed **inside** the body instead of on the front face. The front of the body is at z = 3, but the eye was placed at z = 4 — one block too deep.

```
place red block at (2, 3, 3)
place black block at (2, 3, 4)
```

**Fix it so the eye is on the front face, and explain what "one block too deep" means. (2–3 sentences)**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Walk around the 🕷️ spider in the world. Then plan and build a **full spider** on your home spot, then add one change of your own.

**Plan your coordinates first.** The body is a small block; four legs reach out on each side; the eyes sit on the front.

> **Red body:** fill from (2, 2, 3) to (4, 3, 4).
>
> **Left legs** (share x = 1, step deeper): (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 5).
>
> **Right legs** (share x = 5, step deeper): (5, 1, 2), (5, 1, 3), (5, 1, 4), (5, 1, 5).
>
> **Two black eyes on the front** (z = 3): (2, 3, 3) and (4, 3, 3).

**Then a MODIFY challenge:** change one thing your own way — longer legs that bend across (add blocks at x = 2 and x = 4), a bigger body, a different colour, or fangs under the eyes.

> 💡 Tip: legs reach **across** (x) to the sides and spread **deeper** (z) front to back. The eyes only show on the **front** (smallest z).

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera at the spider. Name the parts.

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your **one** video to teacher on KakaoTalk.
