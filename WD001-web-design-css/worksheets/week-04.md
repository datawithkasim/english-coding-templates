# ↔️ WD001 Week 4 — English Worksheet

**Topic:** Flexbox — Lining Things Up Horizontally · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you put boxes **side by side**. One line — `display: flex` — makes the children of a box line up in a row. Then `justify-content` spreads them across, `align-items` lines them up top-to-bottom, and `gap` adds space between them.

---

## 1 · Predict 🔮

Read each bit of CSS. Before you imagine the browser drawing it, write what you think will happen.

```html
<style>
  .row {
    display: flex;
    gap: 20px;
  }
</style>
```

**The `.row` holds three cards. After `display: flex`, are the cards stacked on top of each other or side by side?**

<div class="write-space"></div>

```html
<style>
  .row {
    display: flex;
    justify-content: center;
  }
</style>
```

**Where do the cards sit — on the left, in the middle, or spread out?**

<div class="write-space"></div>

```html
<style>
  .row {
    display: flex;
    justify-content: space-between;
  }
</style>
```

**`space-between` with three cards. Where does the empty space go?**

<div class="write-space"></div>

```html
<style>
  .menu {
    display: flex;
    gap: 24px;
  }
</style>
```

**The `.menu` holds three links: Home, About, Contact. What does the menu look like now?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of CSS below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The three cards are supposed to line up in a row, but they are still stacked on top of each other.

```html
<style>
  .row {
    flex;
    gap: 16px;
  }
</style>
```

**Hint:** `flex` is the **value**. What is the property name?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The cards are in a row but jammed together with no space. There should be a gap.

```html
<style>
  .row {
    display: flex;
    gap 16px;
  }
</style>
```

**Hint:** something is missing between the property and the value.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `justify-content` is on the wrong box. It was written on a single card instead of on the row that holds the cards.

```html
<div class="row">
  <div class="card" style="justify-content: center;">A</div>
  <div class="card">B</div>
  <div class="card">C</div>
</div>
```

**Hint:** `justify-content` belongs on the **flex container** (the `.row`), not on a child.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build a Menu and a Card Row 📸

In Replit, work on the page you have been building. Add two things:

1. a **navigation menu** with links (Home, About, Contact, and at least one more of your own),
2. your **3 cards from last week lined up in a row** using Flexbox.

You can start your menu like this and change the words and colours:

```html
<div class="menu">
  <a href="#">Home</a>
  <a href="#">About</a>
  <a href="#">Contact</a>
</div>

<style>
  .menu {
    display: flex;
    justify-content: center;
    gap: 24px;
    background-color: #1a3a52;
    padding: 16px;
  }
  .menu a {
    color: #ffffff;
    text-decoration: none;
    font-size: 18px;
  }
</style>
```

Try changing `justify-content` to `center`, then `space-between`, and notice the difference.

When you finish, send a **photo or video** of your menu and card row (or a picture of your code), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The links in my menu are …
>
> I used `display: flex` to …
>
> When I tried `space-between`, the cards …
>
> The `gap` did …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your menu and cards. Talk through it like you are teaching someone who has never seen Flexbox. Try to use these words: **flex**, **row**, **justify-content**, **gap**, **align**.

> 1. Show your menu and your row of cards in the browser.
> 2. Read your `display: flex` line out loud and say what it does.
> 3. Change `justify-content` live and say what moves.
> 4. Show one thing you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
