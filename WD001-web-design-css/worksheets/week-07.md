# ✨ WD001 Week 7 — English Worksheet

**Topic:** Hover Effects and Animations · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you make your page **feel alive**. `:hover` adds a style that only shows when the mouse is on top of something. `transition` makes the change smooth instead of sudden, and `transform: scale()` grows an element a little. Together they make buttons and cards that react when you point at them.

---

## 1 · Predict 🔮

Read each bit of CSS. Before you imagine the browser drawing it, write what you think will happen.

```html
<style>
  .btn {
    background-color: red;
  }
  .btn:hover {
    background-color: blue;
  }
</style>
```

**What colour is the button normally? What colour when the mouse is on it?**

<div class="write-space"></div>

```html
<style>
  .card:hover {
    transform: scale(1.2);
  }
</style>
```

**`scale(1.2)` on hover. Does the card get bigger or smaller when you point at it?**

<div class="write-space"></div>

```html
<style>
  .btn {
    background-color: red;
    transition: background-color 1s;
  }
  .btn:hover {
    background-color: blue;
  }
</style>
```

**With `transition: background-color 1s`, does the colour change instantly or fade slowly?**

<div class="write-space"></div>

```html
<style>
  .card:hover {
    transform: scale(0.8);
  }
</style>
```

**`scale(0.8)` is less than 1. What do you think happens to the card on hover?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of CSS below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The button is supposed to change colour when you point at it, but it never changes.

```html
<style>
  .btn hover {
    background-color: green;
  }
</style>
```

**Hint:** `:hover` attaches to the selector in a special way.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The card is supposed to grow **smoothly** on hover, but it snaps to the bigger size instantly.

```html
<style>
  .card:hover {
    transform: scale(1.1);
  }
</style>
```

**Hint:** which property makes a change happen smoothly over time, and where should it go?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The button is supposed to get slightly bigger on hover, but instead it disappears or breaks.

```html
<style>
  .btn:hover {
    transform: scale;
  }
</style>
```

**Hint:** `scale` needs a number to know how much to grow.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build 3 Hover Cards 📸

In Replit, build **3 cards with hover effects**, and make each card react **differently**. For example: one changes colour, one grows a little, one gets a shadow. Use `transition` so the change is smooth.

You can start from this button and use the same idea on your cards:

```html
<button class="btn">Click Me</button>

<style>
  .btn {
    background-color: #d4380d;
    color: #ffffff;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-size: 18px;
    cursor: pointer;
    transition: transform 0.2s, background-color 0.2s;
  }
  .btn:hover {
    background-color: #b32d09;
    transform: scale(1.05);
  }
</style>
```

Try your transition at `0.1s`, `0.5s`, and `1s`, and keep the speed that feels most natural to you.

When you finish, send a **video** (hover effects are easier to see in a video) or a picture of your code, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My three hover effects are …
>
> I made the change smooth by using …
>
> I tried the transition at ___ and kept …
>
> `transform: scale()` did …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you hover over your cards. Talk through it like you are teaching someone who has never made a hover effect. Try to use these words: **hover**, **transition**, **scale**, **smooth**, **effect**.

> 1. Show all three cards, then hover over each one.
> 2. Read one `:hover` rule out loud and say what it changes.
> 3. Point out which card changes colour, which grows, and which gets a shadow.
> 4. Show one thing you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
