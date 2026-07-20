# ☃️ M003 Extension — Build the Snow Golem (Advanced)

**Topic:** 3D Snow Golem (x, y, z) · **Course:** 3D Coordinates · **Level:** Advanced (Extension, after Week 6) · **Time:** about 45 minutes

Build a **standing snow golem** in 3D — a snow body, a carved-pumpkin head, coal buttons down the front, and two stick arms — then make it your own. Every block needs **three** numbers **(x, y, z)**: x **across**, y **up**, z **deeper** (forward).

> 🔴 Stand on your **home spot** (red block) every run. Move your feet, move your golem.
>
> 🎨 Snow = **snow block**. Head = **carved pumpkin**. Buttons + eyes = **coal block**. Arms = a **brown block** (oak log).

---

## 1 · Predict 🔮

Read each set. Write your prediction **and the reason**.

```
place snow block at (3, 1, 1)
place snow block at (3, 2, 1)
place snow block at (3, 3, 1)
```

**Does this snow tower go across, up, or deeper? Which number changes, and why?**

<div class="write-space"></div>

```
place snow block at (3, 3, 1)
place snow block at (3, 3, 2)
place snow block at (3, 3, 3)
```

**Across, up, or deeper? Which number changes, and why?**

<div class="write-space"></div>

```
place snow block at (2, 1, 1)
place snow block at (4, 1, 1)
place snow block at (2, 5, 1)
place snow block at (4, 5, 1)
```

**Where do these four blocks sit, and what shape do the corners mark? Why?**

<div class="write-space"></div>

```
place snow block at (3, 4, 1)
place coal block at (3, 4, 1)
```

**Same (x, y, z). Snow, coal, or both? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Fix each one. Then say why it was wrong.

**Bug A** — A coal button belongs **on the front** of the body at (3, 4, 1). It has only **two** numbers, so it lands flat on the ground.

```
place coal block at (3, 4)
```

**Fixed code:**

<div class="write-space"></div>

**Why wrong? Why does your fix work? (2–3 sentences)**

<div class="write-space"></div>

**Bug B** — An eye should be **up high on the front** of the head at (4, 7, 1). The last two numbers are swapped.

```
place coal block at (4, 1, 7)
```

**Fixed code:**

<div class="write-space"></div>

**Why wrong? Why does your fix work? (2–3 sentences)**

<div class="write-space"></div>

**Bug C** *(the tricky one)* — The code runs with no error, but the coal button ended up on the **side** of the body instead of the front. The snow body is built at z = 1, but this button was placed at z = 2 — one block too deep.

```
place snow block at (3, 4, 1)
place coal block at (3, 4, 2)
```

**Fix it so the button is on the front face, and explain what "one block too deep" means. (2–3 sentences)**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Walk around the ☃️ snow golem in the world. Then plan and build a **full snow golem** on your home spot, then add one change of your own.

**Plan your coordinates first.** The body is a tall tower; the head sits on top; the eyes and buttons show on the front; the arms poke out the sides.

> **Snow body** (z = 1): fill snow blocks from (2, 1, 1) to (4, 5, 1).
>
> **Pumpkin head** (up, bigger y): fill carved pumpkin from (2, 6, 1) to (4, 7, 1).
>
> **Coal eyes** (front): (2, 7, 1) and (4, 7, 1).
>
> **Coal buttons** (front, down the middle): (3, 4, 1) and (3, 2, 1).
>
> **Arms** (out the sides): a brown block at (1, 4, 1) and (5, 4, 1).
>
> **Add depth:** build the snow body and pumpkin head again at z = 2 and z = 3. At z = 2 and z = 3, place plain snow and pumpkin where the eyes and buttons were — the face and buttons show on the **front only**.

**Then a MODIFY challenge:** change one thing your own way — a new colour, a taller body, a longer arm, a scarf, or more buttons.

> 💡 Tip: the eyes and buttons only show on the **front** (z = 1). The sides and back are plain snow.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera at the golem. Name the parts.

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
