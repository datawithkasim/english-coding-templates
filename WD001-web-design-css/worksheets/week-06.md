# 📱 WD001 Week 6 — English Worksheet

**Topic:** Responsive Design — Looking Good on Mobile Too · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you make your page look good on a **phone** as well as a computer. Phones have narrow screens, so a row of cards that looks great on PC can get squished. With a `@media` query you can change the style **only when the screen is small** — for example, stack the cards top-to-bottom and shrink the heading.

---

## 1 · Predict 🔮

Read each bit of CSS. Before you imagine the browser drawing it, write what you think will happen.

```html
<style>
  .cards {
    display: flex;
    flex-direction: row;
  }
</style>
```

**On a wide screen, are the cards side by side or stacked?**

<div class="write-space"></div>

```html
<style>
  @media (max-width: 600px) {
    .cards {
      flex-direction: column;
    }
  }
</style>
```

**This rule only runs when the screen is 600px or smaller. On a phone, do the cards go in a row or a column?**

<div class="write-space"></div>

```html
<style>
  @media (max-width: 600px) {
    h1 {
      font-size: 24px;
    }
  }
</style>
```

**On a wide PC screen, does this rule change the heading? What about on a narrow phone screen?**

<div class="write-space"></div>

```html
<style>
  .box {
    width: 50%;
  }
</style>
```

**A box set to `width: 50%`. If the screen gets narrower, does the box stay the same pixel width or shrink with the screen?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of CSS below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — On phones the cards are supposed to stack into a column, but the media query never runs.

```html
<style>
  media (max-width: 600px) {
    .cards {
      flex-direction: column;
    }
  }
</style>
```

**Hint:** a media query starts with a special symbol.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The cards should switch to a column **only on small screens**, but right now they are always a column, even on a big PC.

```html
<style>
  .cards {
    display: flex;
    flex-direction: column;
  }
</style>
```

**Hint:** the column rule should live **inside** a media query, not in the normal style.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The page is supposed to react to the real phone width, but on a phone everything looks tiny and zoomed out because the viewport tag is wrong.

```html
<head>
  <meta name="viewport">
</head>
```

**Hint:** the viewport tag needs a `content` value that sets the width to the device.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make Your Page Responsive 📸

In Replit, open your page and make it work on a **phone-sized screen**:

1. add the `viewport` meta tag in your `<head>` if it isn't there,
2. use a `@media` query so your cards line up in a row on PC and **stack into a column** on a narrow screen,
3. make your big heading a bit **smaller** on small screens.

You can start from this:

```html
<style>
  .cards {
    display: flex;
    flex-direction: row;
    gap: 16px;
  }

  /* Applies only when the screen is 600px or smaller */
  @media (max-width: 600px) {
    .cards {
      flex-direction: column;
    }
    h1 {
      font-size: 28px;
    }
  }
</style>
```

To preview a phone size, make your browser window narrow, or use Replit's preview and shrink it.

When you finish, send **two screenshots** — one PC-sized and one phone-sized — then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> On a wide screen my cards are …
>
> On a narrow screen my cards …
>
> I made that change with a media query that …
>
> I also changed my heading so that …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you make the browser window narrow and watch your page change. Talk through it like you are teaching someone who has never seen responsive design. Try to use these words: **responsive**, **media query**, **width**, **column**, **mobile**.

> 1. Show your page at a wide PC size first.
> 2. Slowly drag the window narrower until the layout changes.
> 3. Read your `@media` line out loud and say what triggers it.
> 4. Show one thing you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your two screenshots (PC and mobile) to teacher on KakaoTalk.
