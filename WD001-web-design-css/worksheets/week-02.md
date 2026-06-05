# 🎨 WD001 Week 2 — English Worksheet

**Topic:** First Steps in CSS — Colors and Text · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you give your page **style**. HTML decides **what** is on the page; CSS decides **how it looks**. You write CSS inside a `<style>` tag, choose a tag with a **selector**, and set properties like `color`, `font-size`, and `background-color`.

---

## 1 · Predict 🔮

Read each bit of CSS. Before you imagine the browser drawing it, write what you think will happen.

```html
<style>
  h1 {
    color: blue;
  }
</style>
```

**Every `<h1>` on the page — what colour does the text become?**

<div class="write-space"></div>

```html
<style>
  body {
    background-color: black;
  }
  p {
    color: black;
  }
</style>
```

**The background and the paragraph text are both black. What problem do you predict?**

<div class="write-space"></div>

```html
<style>
  h1 {
    font-size: 60px;
  }
  p {
    font-size: 12px;
  }
</style>
```

**Which text looks bigger on the page, the heading or the paragraph? By a lot or a little?**

<div class="write-space"></div>

```html
<style>
  p {
    color: red;
    color: green;
  }
</style>
```

**Two `color` lines on the same `p`. Which colour wins? Make a guess, then test it.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of CSS below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The heading is supposed to turn orange. Nothing changes.

```html
<style>
  h1
    color: orange;
  }
</style>
```

**Hint:** a curly bracket is missing where the rule starts.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The paragraph text is supposed to be size 20. Nothing changes.

```html
<style>
  p {
    font-size: 20
  }
</style>
```

**Hint:** the value needs a unit, and the line needs to end properly.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The whole page background is supposed to be light yellow, but the colour shows up on the headings instead.

```html
<style>
  h1 {
    background-color: #fff8e7;
  }
</style>
```

**Hint:** which selector means "the whole page"?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Restyle Your Page 📸

Open last week's About Me page in Replit. Add a `<style>` tag and make it yours:

1. pick a **background colour** for the whole page (`body`),
2. give your heading and your paragraph **different colours**,
3. choose a font with `font-family`.

You can start from this and change the values to your own taste:

```html
<style>
  body {
    background-color: #fff8e7;
    font-family: Arial, sans-serif;
  }
  h1 {
    color: #d4380d;
    font-size: 36px;
  }
  p {
    color: #333333;
    font-size: 18px;
  }
</style>
```

Then try your **heading size two different ways** (for example `36px` and `48px`) and keep the one you like better.

When you finish, send a **photo or video** of your page (or a picture of your code), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The colours I chose were …
>
> I made my heading and paragraph different by …
>
> I tried my heading at ___ and at ___ , and I kept …
>
> The font I picked was …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your styled page. Talk through it like you are teaching someone who has never used CSS. Try to use these words: **style**, **selector**, **colour**, **font**, **background**.

> 1. Show your page before and after styling, if you can.
> 2. Read one CSS rule out loud and say which tag it changes.
> 3. Show your two heading sizes and say which one you kept.
> 4. Show one thing you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
