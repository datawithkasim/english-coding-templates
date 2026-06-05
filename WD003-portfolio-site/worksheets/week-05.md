# 🖼️ WD003 Week 5 — English Worksheet

**Topic:** Projects Gallery — Show What You Made · **Course:** Portfolio Site · **Time:** about 45 minutes

This week you build your **Projects gallery**. Each project becomes a **card** with an image, a title, and a short description. You line the cards up with **CSS Grid**, and add a small **lift-up animation** when you hover over a card.

> Grid lays items out in rows and columns. With `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`, the browser fits as many cards across as it can, then wraps the rest to the next row.

---

## 1 · Predict 🔮

Read each block of code. Before you imagine the page, write what you think will happen.

```css
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
```

**There are 4 cards inside `.project-grid`, and the screen is wide enough for 3 across. How do the cards arrange themselves?**

<div class="write-space"></div>

```css
.project-card {
  transition: transform 0.2s;
}
.project-card:hover {
  transform: translateY(-4px);
}
```

**What happens when the visitor's mouse moves over a card? What does `transition` add to it?**

<div class="write-space"></div>

```html
<div class="project-card">
  <img src="quiz.png" alt="Quiz">
  <h3>Quiz App</h3>
  <p>A quiz built in JavaScript</p>
</div>
```

**Describe what a visitor sees inside this one card, top to bottom.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The cards are supposed to lay out in a grid, side by side. Right now they are stacked in one tall column.

```css
.project-grid {
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
```

**Hint:** one line is missing that turns this element into a grid in the first place.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The hover lift is supposed to be smooth, but right now the card *snaps* up instantly with no animation.

```css
.project-card:hover {
  transform: translateY(-4px);
}
```

**Hint:** the smoothness comes from a property on the card itself, not the hover.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Each card is supposed to show an image, a title, and a description. This card is missing its `alt` text and its description, and the image has no source.

```html
<div class="project-card">
  <img>
  <h3>My Game</h3>
</div>
```

**Hint:** an `<img>` needs a `src` and an `alt`. Add the missing description too.

**Write the fixed code:**

<div class="write-space"></div>

**Why does an image need `alt` text? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Projects Gallery 📸

Open your site and fill in the Projects section.

1. Build **three or more** project cards. Use projects you have made before (a Minecraft build, a quiz app, a game) — or anything you are proud of.
2. Each card needs an **image**, a **title** (`<h3>`), and a one-line **description**.
3. Lay the cards out with **CSS Grid** so they sit side by side and wrap on narrow screens.
4. Add a **hover lift** so each card rises a little when you point at it.

If you do not have real screenshots, an emoji or a placeholder image is fine. When you finish, send a **photo or video** of your gallery (try hovering a card on camera!), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The projects I put in my gallery are …
>
> I used CSS Grid to …
>
> When I hover over a card, it …
>
> The hardest part was …
>
> To fix it, I …
>
> If I had more time, I would add …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your gallery. Talk through it like you are teaching someone who has never used Grid. Try to use these words: **card**, **grid**, **column**, **hover**, **animation**.

> 1. Show your gallery with all the cards lined up.
> 2. Hover over a card and show it lift up.
> 3. Make the window narrow and show the cards re-arrange.
> 4. Read one of your card's HTML out loud and name its parts.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
