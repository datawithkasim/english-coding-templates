# 📦 WD001 Week 3 — English Worksheet

**Topic:** The Box Model — Padding, Margin, Border · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you learn that **every element is a box**. Around the content there is `padding` (space **inside** the box), then a `border` (the line **around** it), then `margin` (space **outside**, pushing other boxes away). You will also use `border-radius` to round the corners.

---

## 1 · Predict 🔮

Read each bit of CSS. Before you imagine the browser drawing it, write what you think will happen.

```html
<style>
  .card {
    border: 2px solid red;
    padding: 30px;
  }
</style>
```

**Lots of padding. Is the text close to the border or far from it?**

<div class="write-space"></div>

```html
<style>
  .card {
    border: 2px solid black;
    margin: 40px;
  }
</style>
```

**Lots of margin. Does the space go **inside** the box or **outside** it, pushing other things away?**

<div class="write-space"></div>

```html
<style>
  .card {
    border-radius: 50px;
    width: 100px;
    height: 100px;
  }
</style>
```

**A 100×100 box with a 50px corner radius. What shape do you think it becomes?**

<div class="write-space"></div>

```html
<style>
  .card {
    padding: 0px;
    border: 1px solid blue;
  }
</style>
```

**No padding at all. Where does the text sit compared to the border line?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of CSS below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The card is supposed to have a visible line around it. There is no line.

```html
<style>
  .card {
    border: solid blue;
  }
</style>
```

**Hint:** a border needs a **thickness** too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The text inside the card is supposed to have breathing room, but it is squished right up against the border.

```html
<style>
  .card {
    border: 2px solid green;
    margin: 20px;
  }
</style>
```

**Hint:** which property adds space **inside** the box?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The card is supposed to have softly rounded corners, but the corners are still sharp.

```html
<style>
  .card {
    border: 2px solid #d4380d;
    radius: 12px;
  }
</style>
```

**Hint:** check the property name.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build 3 Cards 📸

In Replit, build **3 cards** about you — for example: favourite food, favourite movie, favourite school subject. Each card has a heading and a short line of text. Make each card a little **different** in colour or border so they don't all look the same.

You can start one card like this and change it to your own:

```html
<div class="card">
  <h2>My Favorite Game</h2>
  <p>Minecraft is the best!</p>
</div>

<style>
  .card {
    background-color: #ffffff;
    border: 2px solid #d4380d;
    border-radius: 12px;
    padding: 20px;
    margin: 16px;
    width: 300px;
  }
</style>
```

When you finish, send a **photo or video** of your cards (or a picture of your code), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My three cards are about …
>
> I made them look different by …
>
> I used padding to …
>
> I used border-radius to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your cards. Talk through it like you are teaching someone who has never seen the box model. Try to use these words: **box**, **padding**, **margin**, **border**, **rounded**.

> 1. Show your three cards in the browser.
> 2. Point to one card and show where the padding is and where the margin is.
> 3. Say what `border-radius` did to the corners.
> 4. Show one thing you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
