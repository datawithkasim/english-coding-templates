# 🎨 WD003 Week 3 — English Worksheet

**Topic:** Design System — A Consistent Feel · **Course:** Portfolio Site · **Time:** about 45 minutes

This week you give your site a **design system**. You decide your colors, font, and spacing *once* — as **CSS variables** — and reuse them everywhere. When everything pulls from the same set of values, the whole site feels like it belongs together.

> A CSS variable is defined in `:root` with two dashes, like `--primary: #d4380d;`. You use it anywhere with `var(--primary)`. Change it in one place, and it updates everywhere.

---

## 1 · Predict 🔮

Read each block of CSS. Before you imagine the page, write what you think will happen.

```css
:root {
  --primary: #d4380d;
}
h1 { color: var(--primary); }
h2 { color: var(--primary); }
```

**Both headings pull from `--primary`. If you change `--primary` to blue, how many headings change color?**

<div class="write-space"></div>

```css
:root {
  --space-2: 16px;
  --space-4: 32px;
}
section { padding: var(--space-4); }
```

**What does `padding: var(--space-4)` do to the space inside each section? How much space is it?**

<div class="write-space"></div>

```css
:root {
  --text: #333333;
}
body { color: var(--text); }
h1 { color: var(--primary); }
```

**`--primary` was never defined in `:root`. What color will the `h1` be?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of CSS below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The body text is supposed to use the `--text` color variable, but the page shows plain black instead.

```css
:root {
  --text: #333333;
}
body { color: --text; }
```

**Hint:** a variable name on its own is not enough — it needs to be wrapped.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This is supposed to define a primary color variable, but the value is missing its proper form.

```css
:root {
  primary: d4380d;
}
h1 { color: var(--primary); }
```

**Hint:** a CSS variable name starts with two dashes, and a hex color starts with `#`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Every section is supposed to have the same inside spacing using the spacing scale. Right now every section uses a different random number, so the page looks uneven.

```css
.hero    { padding: 30px; }
.about   { padding: 18px; }
.projects{ padding: 25px; }
```

**Hint:** define one spacing variable and use it for all three.

**Write the fixed code:**

<div class="write-space"></div>

**Why does using one spacing variable make the page look more consistent?**

<div class="write-space"></div>

---

## 3 · Build Your Design System 📸

Open your site from last week and give it a design system in a `<style>` block.

1. In `:root`, define **three colors**: `--primary`, `--secondary`, and `--text`. Pick a palette that feels like *you*.
2. Define a **spacing scale**: `--space-1` through `--space-4` (try 8px, 16px, 24px, 32px).
3. Apply your font to the `body` (a Google Font, or a clean default).
4. Use `var(--space-4)` for the padding on every `<section>` so they all match.

When you finish, send a **photo or video** of your site with its new colors and spacing, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The colors I chose for my variables are …
>
> I picked these colors because …
>
> I used `var(--space-4)` to …
>
> Before the design system, my page looked …
>
> After applying it, my page looked …
>
> If I had more time, I would change …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your styled site. Talk through it like you are teaching someone who has never used CSS variables. Try to use these words: **variable**, **color**, **spacing**, **consistent**, **reuse**.

> 1. Show your `:root` block and read out your color variables.
> 2. Change one variable's value live and show the page update everywhere.
> 3. Point to two sections and show their spacing matching.
> 4. Say why defining values once is better than repeating numbers.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
