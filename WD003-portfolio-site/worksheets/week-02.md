# 🏗️ WD003 Week 2 — English Worksheet

**Topic:** Page Structure — HTML Sections · **Course:** Portfolio Site · **Time:** about 45 minutes

This week you turn last week's paper plan into **real HTML**. You use meaningful tags — `<nav>`, `<section>`, `<footer>` — and give each section an `id` so the nav menu can jump to it. No colors yet. This week is all about **structure**.

> Remember: `id="about"` on a section, and `href="#about"` on a nav link, work as a pair. The `#` link finds the matching `id` and jumps there.

---

## 1 · Predict 🔮

Read each block of HTML. Before you imagine the page, write what you think will happen.

```html
<nav>
  <a href="#projects">Projects</a>
</nav>

<section id="projects">
  <h2>Projects</h2>
</section>
```

**A visitor clicks the "Projects" link. What happens, and why?**

<div class="write-space"></div>

```html
<section id="about">
  <h2>About</h2>
</section>

<section id="contact">
  <h2>Contact</h2>
</section>
```

**There are two sections here. How does the browser know where one ends and the next begins?**

<div class="write-space"></div>

```html
<nav>
  <a href="#hero">Home</a>
  <a href="#contact">Contact</a>
</nav>

<section id="hero"><h1>Minjun</h1></section>
<section id="about"><h2>About</h2></section>
```

**The nav has a "Contact" link, but there is no `id="contact"` anywhere on the page. What happens when you click it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of HTML below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The nav link is supposed to jump to the About section, but clicking it does nothing.

```html
<nav>
  <a href="about">About</a>
</nav>

<section id="about">
  <h2>About</h2>
</section>
```

**Hint:** an `id` link needs one small symbol in front.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Each section is supposed to have a *different* `id` so the nav can tell them apart. Right now two sections share the same one.

```html
<section id="section">
  <h2>About</h2>
</section>

<section id="section">
  <h2>Projects</h2>
</section>
```

**Hint:** an `id` is a name. Two things should not share the same name.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This page is supposed to have a navigation bar, but the link is floating loose with no `<nav>` around it, and the section never closes.

```html
<a href="#hero">Home</a>

<section id="hero">
  <h1>My Name</h1>
```

**Hint:** wrap the link, and close the tag you opened.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Sections 📸

Open your editor and build the **five sections** from your Week 1 plan as real HTML. No design yet — placeholder text is fine.

1. Add a `<nav>` with four links: Home, About, Projects, Contact.
2. Add five blocks: a Hero `<section>`, an About `<section>`, a Projects `<section>`, a Contact `<section>`, and a `<footer>`.
3. Give each section a matching `id` so the nav links jump to them.
4. Put a placeholder heading in each section so you can see where you are.

When you finish, click each nav link and watch the page jump. Send a **photo or video** of your result (the page, or your code), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I looked at my Week 1 plan and …
>
> I gave each section an `id` so that …
>
> When I clicked a nav link, the page …
>
> One link did not work at first because …
>
> To fix it, I …
>
> Next week I want to start on …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you click through your page. Talk through it like you are teaching someone who has never seen HTML. Try to use these words: **section**, **nav**, **id**, **link**, **footer**.

> 1. Show your page from top to bottom.
> 2. Click a nav link and show the page jumping to that section.
> 3. Read one section's `id` and the matching `href` out loud, and say how they pair up.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
