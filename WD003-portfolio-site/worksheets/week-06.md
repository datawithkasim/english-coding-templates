# 🌙 WD003 Week 6 — English Worksheet

**Topic:** JavaScript Dark Mode Toggle · **Course:** Portfolio Site · **Time:** about 45 minutes

This week you add a **dark mode** button with JavaScript. The trick is simple: clicking the button **toggles one class** (`.dark`) on the `<body>`, and your CSS does the rest. As a bonus, you save the choice in `localStorage` so the site remembers it next time.

> `classList.toggle("dark")` flips the class on and off — on if it is missing, off if it is there. `classList.contains("dark")` checks whether it is currently on.

---

## 1 · Predict 🔮

Read each block of code. Before you imagine the page, write what you think will happen.

```js
btn.addEventListener("click", function() {
  document.body.classList.toggle("dark");
});
```

**The body starts with no `.dark` class. The visitor clicks the button once, then a second time. What is on the body after each click?**

<div class="write-space"></div>

```css
body { background-color: white; color: black; }
body.dark { background-color: #1a1a1a; color: #f0f0f0; }
```

**When `.dark` is added to the body, which colors win — the first rule or the second? What does the page look like?**

<div class="write-space"></div>

```js
if (document.body.classList.contains("dark")) {
  btn.textContent = "Light Mode";
} else {
  btn.textContent = "Dark Mode";
}
```

**The site is currently in dark mode. What does the button say? What should it say so the label makes sense?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Clicking the button is supposed to flip dark mode on and off. Right now clicking it does nothing at all.

```js
let btn = document.querySelector("#darkBtn");
btn.classList.toggle("dark");
```

**Hint:** the toggle should happen *when the button is clicked*, and it should change the **body**, not the button.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Dark mode is supposed to *switch back and forth* each click. Right now it only ever turns dark on, and never off.

```js
btn.addEventListener("click", function() {
  document.body.classList.add("dark");
});
```

**Hint:** `add` only ever adds. There is a method that flips instead.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When dark mode is on, the button is supposed to say "Light Mode" so the visitor knows what clicking it will do. Right now the labels are swapped.

```js
if (document.body.classList.contains("dark")) {
  btn.textContent = "Dark Mode";
} else {
  btn.textContent = "Light Mode";
}
```

**Hint:** the label should describe what the button *switches to*, not what it is now.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Dark Mode 📸

Open your site and add a working dark mode toggle.

1. Add a **button** with an id (for example `id="darkBtn"`).
2. In CSS, write a `body.dark` rule with a dark background and light text. Don't forget your project cards.
3. In JavaScript, **toggle** the `.dark` class on the body when the button is clicked.
4. Update the button's text so it says "Dark Mode" or "Light Mode" depending on the current state.
5. **Bonus:** save the choice in `localStorage` so a refresh keeps the same mode.

When you finish, send **photos or a video** of both light and dark mode, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My dark mode button toggles …
>
> When `.dark` is on the body, the page …
>
> I made the button text change by …
>
> The hardest part was …
>
> To fix it, I …
>
> (If you tried the bonus) localStorage helped me by …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you toggle dark mode. Talk through it like you are teaching someone who has never written JavaScript. Try to use these words: **toggle**, **class**, **click**, **dark mode**, **button**.

> 1. Show your site in light mode, then click the button to go dark.
> 2. Read your `toggle` line out loud and say what it changes.
> 3. Show the button's text changing between the two modes.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
