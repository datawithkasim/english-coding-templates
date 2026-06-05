# ⭐ WD003 Week 4 — English Worksheet

**Topic:** Hero + About — Polish · **Course:** Portfolio Site · **Time:** about 45 minutes

This week you make your **Hero** and **About** sections look great. The Hero is the **first impression** — big text, lots of space, centered. The About section sits a photo next to your introduction, side by side. And you make both work on a **phone** with a media query.

> Two new tools this week: **Flexbox** (`display: flex`) to line things up, and a **media query** (`@media (max-width: 600px)`) to change the layout on small screens.

---

## 1 · Predict 🔮

Read each block of CSS. Before you imagine the page, write what you think will happen.

```css
#hero {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

**`100vh` means "100% of the screen height." How big is the Hero, and where does its content sit?**

<div class="write-space"></div>

```css
#about {
  display: flex;
  gap: 32px;
  align-items: center;
}
```

**The About section has a photo and a paragraph inside it. With `display: flex`, do they sit side by side or stacked? What does `gap` do?**

<div class="write-space"></div>

```css
@media (max-width: 600px) {
  #about { flex-direction: column; }
}
```

**On a wide laptop the About content is side by side. What happens when the screen gets narrower than 600px?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of CSS below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The Hero content is supposed to be centered in the middle of the screen, but everything is stuck in the top-left corner.

```css
#hero {
  height: 100vh;
  display: flex;
}
```

**Hint:** flex can center, but only when you tell it to — on both axes.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The About photo and paragraph are supposed to sit side by side, but they are stacked on top of each other on the laptop.

```css
#about {
  display: flex;
  flex-direction: column;
  gap: 32px;
}
```

**Hint:** one of these lines forces a stack. The default flex direction is a row.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — On a phone, the side-by-side About layout is supposed to stack into a column so it fits. Right now the media query never triggers because the condition is backwards.

```css
@media (min-width: 600px) {
  #about { flex-direction: column; }
}
```

**Hint:** you want this to apply on *small* screens, not big ones.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Hero + About 📸

Open your site and finish these two sections.

1. Make the Hero **full screen height** and center your name and one-line tagline inside it.
2. Give the Hero a background using one of your color variables.
3. In the About section, place your **photo next to your introduction** with Flexbox.
4. Add a media query so that on a narrow screen, the About content **stacks** and the Hero text shrinks a little.

When you finish, open your site on a **laptop and on a phone** (or resize the browser window narrow). Send **photos or a video** of both layouts, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My Hero section says …
>
> I centered the Hero content by …
>
> In the About section, Flexbox lined up …
>
> On a phone, my layout changes by …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show both layouts. Talk through it like you are teaching someone who has never used Flexbox. Try to use these words: **Hero**, **Flexbox**, **center**, **media query**, **mobile**.

> 1. Show your Hero filling the whole screen.
> 2. Show your About section side by side on a wide screen.
> 3. Make the window narrow (or open it on a phone) and show the layout change.
> 4. Read your media query out loud and say what makes it trigger.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
