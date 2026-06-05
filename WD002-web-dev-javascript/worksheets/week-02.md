# ⚡ WD002 Week 2 — English Worksheet

**Topic:** Variables and the DOM — Changing the Page Live · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week you reach into the page and change it with code. A **variable** (`let`) stores a piece of information. `document.querySelector()` grabs an element by its `id`, and `.textContent` swaps the words inside it. Put them together and a click can rewrite the screen.

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<h1 id="title">Hello</h1>

<script>
  let element = document.querySelector("#title");
  element.textContent = "Goodbye";
</script>
```

**What word ends up on the screen — `Hello` or `Goodbye`? Why?**

<div class="write-space"></div>

```html
<script>
  let name = "Minjun";
  let greeting = "Hi, " + name + "!";
  console.log(greeting);
</script>
```

**What full sentence does the console show? What is the `+` doing here?**

<div class="write-space"></div>

```html
<h1 id="title">Start</h1>
<button onclick="change()">Go</button>

<script>
  function change() {
    let element = document.querySelector("#title");
    element.textContent = "Changed!";
  }
</script>
```

**Before the button is clicked, what does the title say? After one click?**

<div class="write-space"></div>

```html
<script>
  let count = 5;
  count = count + 1;
  console.log(count);
</script>
```

**A variable can be changed after it is made. What number prints?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should change the heading text to `Welcome`. Right now nothing changes on the page.

```html
<h1 id="title">Hello</h1>

<script>
  let element = document.querySelector("title");
  element.textContent = "Welcome";
</script>
```

**Hint:** to select something by its `id`, the selector needs a special symbol in front.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should show `Hi, Sora!` on the page. Right now it shows the words `Hi, name!` exactly.

```html
<h1 id="out"></h1>

<script>
  let name = "Sora";
  document.querySelector("#out").textContent = "Hi, name!";
</script>
```

**Hint:** the variable is stuck inside the quotes, so it is treated as plain text. Pull it out and join it with `+`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Clicking should change the heading. Right now you get an error because the element cannot be found.

```html
<h1 id="message">Hi</h1>
<button onclick="update()">Update</button>

<script>
  function update() {
    let element = document.querySelector("#mesage");
    element.textContent = "Updated!";
  }
</script>
```

**Hint:** compare the `id` in the HTML with the one in the selector, letter by letter.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Build a page where clicking **one** button changes **3 or more things** on the screen at once.

1. Put a few elements on the page, each with its own `id` (a heading, a subtitle, a paragraph…).
2. Store a value in a variable with `let`.
3. In a function, use `querySelector` and `.textContent` to change each element.
4. Use your variable in at least one of the changes (join it with `+`).

**Stretch:** try putting a *different* value in the variable and watch how every change updates. What does that tell you about variables?

When you finish, come back here. Send a **photo or video** of the page before and after the click, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I gave each element an `id` so …
>
> I stored ___ in a variable called …
>
> When the button is clicked, my function changes …
>
> I used the variable when I …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your page runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **variable**, **DOM**, **querySelector**, **textContent**, **id**.

> 1. Show the page before clicking.
> 2. Click the button and show everything change at once.
> 3. Read one line out loud and say which element it grabs.
> 4. Show where your variable is used.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
