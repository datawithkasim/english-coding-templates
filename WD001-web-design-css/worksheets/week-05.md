# 🖼️ WD001 Week 5 — English Worksheet

**Topic:** Images and Backgrounds — Visual Impact · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you make a big, bold **hero section** — a large background image with a heading sitting on top of it. You will use `background-image`, `background-size: cover` so the picture fills the space, and a dark overlay so white text stays readable on a busy photo.

---

## 1 · Predict 🔮

Read each bit of CSS. Before you imagine the browser drawing it, write what you think will happen.

```html
<style>
  .hero {
    background-image: url('beach.jpg');
    height: 400px;
  }
</style>
```

**A 400px-tall box with a background photo. Where does the photo appear?**

<div class="write-space"></div>

```html
<style>
  .hero {
    background-image: url('beach.jpg');
    background-size: cover;
  }
</style>
```

**With `background-size: cover`, does the photo stretch to fill the whole box, or sit small in a corner?**

<div class="write-space"></div>

```html
<style>
  .hero {
    color: white;
    background-color: black;
  }
</style>
```

**White text on a black background. Is the text easy or hard to read?**

<div class="write-space"></div>

```html
<style>
  .hero h1 {
    font-size: 48px;
    color: white;
  }
</style>
```

**A 48px heading in white sitting on top of a photo. Do you think it looks small or like a big title?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of CSS below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The hero is supposed to show a background image, but nothing appears.

```html
<style>
  .hero {
    background-image: beach.jpg;
    height: 400px;
  }
</style>
```

**Hint:** a background image filename needs to be wrapped a certain way.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The photo is supposed to fill the whole hero box, but it sits small and tiles/repeats instead.

```html
<style>
  .hero {
    background-image: url('beach.jpg');
    height: 400px;
  }
</style>
```

**Hint:** one line is missing that tells the image to fill the box.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The heading is supposed to sit in the **middle** of the hero, but it is stuck in the top-left corner.

```html
<style>
  .hero {
    background-image: url('beach.jpg');
    background-size: cover;
    height: 400px;
  }
</style>
```

**Hint:** centring needs `display: flex` plus a way to centre across and down.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Hero Section 📸

In Replit, add a **hero section** to the top of your page. Use a photo you like as the background and put a heading and a short line on top of it.

You can start from this and change the photo and the words:

```html
<div class="hero">
  <h1>Hi, I'm ___</h1>
  <p>A short line about me</p>
</div>

<style>
  .hero {
    background-image: url('background.jpg');
    background-size: cover;
    background-position: center;
    height: 400px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #ffffff;
    text-align: center;
  }
  .hero h1 {
    font-size: 48px;
  }
</style>
```

If your text is hard to read on a busy photo, try giving the hero a darker background colour or a semi-transparent overlay so the white text pops.

When you finish, send a **photo or video** of your hero (or a picture of your code), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The photo I chose for my hero is …
>
> `background-size: cover` made the image …
>
> I centred my heading by …
>
> To keep my text readable, I …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your hero section. Talk through it like you are teaching someone who has never made one. Try to use these words: **hero**, **background**, **cover**, **centre**, **readable**.

> 1. Show your hero section at the top of your page.
> 2. Read your `background-size: cover` line out loud and say what it does.
> 3. Show how your heading sits in the middle.
> 4. Show one thing you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
