# ✉️ WD003 Week 7 — English Worksheet

**Topic:** Contact Form + Smooth Scroll · **Course:** Portfolio Site · **Time:** about 45 minutes

This week you add a **contact form** and **smooth scrolling**. The form has a name field and a message field. When the visitor clicks Send, JavaScript stops the page from reloading, hides the form, and shows a thank-you message. And one line of CSS makes your nav links glide instead of jumping.

> `event.preventDefault()` stops the form's default behavior (reloading the page) so *your* code can run instead. `scroll-behavior: smooth` on `html` makes `#` links glide.

---

## 1 · Predict 🔮

Read each block of code. Before you imagine the page, write what you think will happen.

```css
html { scroll-behavior: smooth; }
```

**A visitor clicks a nav link that points to `#contact`. How is the scroll different now compared to before this line?**

<div class="write-space"></div>

```js
form.addEventListener("submit", function(event) {
  event.preventDefault();
  form.style.display = "none";
  thanks.style.display = "block";
});
```

**The visitor fills in the form and clicks Send. List, in order, what happens on the page.**

<div class="write-space"></div>

```html
<input type="text" id="contactName" placeholder="Name" required>
```

**The visitor leaves this field empty and clicks Send. What does `required` do?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — When the form is submitted, the page is supposed to stay put and show a thank-you message. Right now the whole page reloads and nothing seems to happen.

```js
form.addEventListener("submit", function(event) {
  form.style.display = "none";
  thanks.style.display = "block";
});
```

**Hint:** the form's default action is reloading. One line stops it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The thank-you message is supposed to be hidden until the form is sent, then appear. Right now it shows from the very start.

```html
<p id="thanks">Thanks, your message has been sent!</p>
```

**Hint:** it needs to start hidden, and your JavaScript will reveal it later.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Smooth scrolling is supposed to apply to the whole page when nav links are clicked. Right now it is set on the wrong thing, so nothing glides.

```css
button { scroll-behavior: smooth; }
```

**Hint:** smooth scrolling belongs on the page itself, not on a button.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Contact Form 📸

Open your site and finish the Contact section.

1. Build a `<form>` with a **name** `<input>`, a **message** `<textarea>`, and a Send `<button>`.
2. Add a thank-you `<p>` that **starts hidden**.
3. In JavaScript, handle the form's `submit`: call `event.preventDefault()`, hide the form, and show the thank-you message.
4. Add `scroll-behavior: smooth` to `html` and click your nav links to feel the difference.

When you finish, send **photos or a video** of the form before and after you submit it, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My contact form has fields for …
>
> When I click Send, `event.preventDefault()` stops …
>
> After submitting, the form …
>
> Smooth scroll made my nav links …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you use your form and nav. Talk through it like you are teaching someone who has never made a form. Try to use these words: **form**, **submit**, **prevent default**, **smooth scroll**, **message**.

> 1. Show your contact form and fill it in.
> 2. Click Send and show the form being replaced by the thank-you message.
> 3. Read your `preventDefault` line out loud and say why it matters.
> 4. Click a nav link and show the smooth scroll.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
