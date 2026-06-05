# ⚡ WD002 Week 4 — English Worksheet

**Topic:** User Input — Talking with Input Boxes · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week the user gets to **type**. An `<input>` box collects text, and `.value` reads whatever is inside it. You will grab that value, save it in a variable, show it on the page — and politely warn the user when the box is empty.

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<input id="nameBox" type="text">
<button id="show">Show</button>

<script>
  document.querySelector("#show").addEventListener("click", function() {
    let name = document.querySelector("#nameBox").value;
    console.log(name);
  });
</script>
```

**The user types `Jiwoo` and clicks Show. What prints to the console?**

<div class="write-space"></div>

```html
<input id="nameBox" type="text">
<h1 id="out"></h1>

<script>
  document.querySelector("#go").addEventListener("click", function() {
    let name = document.querySelector("#nameBox").value;
    document.querySelector("#out").textContent = "Hi, " + name + "!";
  });
</script>
```

**The user types `Ari`. What full sentence ends up on the screen?**

<div class="write-space"></div>

```html
<script>
  let name = document.querySelector("#nameBox").value;
  if (name === "") {
    alert("Please type something");
  }
</script>
```

**The user clicks without typing anything. What happens?**

<div class="write-space"></div>

```html
<input id="ageBox" type="text">

<script>
  let age = document.querySelector("#ageBox").value;
  console.log(age + 1);
</script>
```

**The user types `10`. You might expect `11`. What actually prints, and why? (Hint: `.value` is always text.)**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Clicking should show what the user typed. Right now it always shows the **same** word, no matter what is typed.

```html
<input id="nameBox" type="text">
<h1 id="out"></h1>

<script>
  document.querySelector("#show").addEventListener("click", function() {
    document.querySelector("#out").textContent = "nameBox";
  });
</script>
```

**Hint:** the code shows the text `"nameBox"`, not the box's `.value`. Read the value first.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should warn the user when the box is empty. Right now the warning shows even when they *did* type something.

```html
<script>
  let name = document.querySelector("#nameBox").value;
  if (name = "") {
    alert("Box is empty!");
  }
</script>
```

**Hint:** one equals sign *sets* a value; you want to *compare*. How many equals signs do you need to check if two things are the same?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should add two numbers the user types. Right now typing `3` and `4` gives `34` instead of `7`.

```html
<script>
  let a = document.querySelector("#num1").value;
  let b = document.querySelector("#num2").value;
  console.log(a + b);
</script>
```

**Hint:** `.value` hands you text, so `+` glues the text together. Turn each value into a number first with `Number(...)`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Build a page that asks for a **name** and an **age**, then shows a short introduction.

1. Add two input boxes and a button.
2. When the button is clicked, read both values with `.value`.
3. Show a sentence like `Hi, I'm ___ and I'm ___ years old.` on the page.
4. If **either** box is empty, show a warning instead of the sentence.

**Stretch:** add the age to a number (for example, show "Next year you'll be ___") — remember to turn the value into a `Number` first.

When you finish, come back here. Send a **photo or video** of both a filled-in result and the empty-box warning, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made input boxes for …
>
> I used `.value` to …
>
> To check for an empty box, I …
>
> When both boxes are filled, the page shows …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your page runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **input**, **value**, **empty**, **warning**, **variable**.

> 1. Show the empty boxes, then type into them.
> 2. Click the button and show the introduction appear.
> 3. Clear a box and show the warning.
> 4. Read one line out loud and say where it reads the value.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
