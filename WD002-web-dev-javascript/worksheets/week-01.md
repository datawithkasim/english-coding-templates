# ⚡ WD002 Week 1 — English Worksheet

**Topic:** Meeting JavaScript — `console.log` and `alert` · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week you make a page **move** for the first time. HTML is the structure, CSS is the look, and **JavaScript is the motion**. You will use `console.log()` to send a message to the console, `alert()` to pop a message at the user, and a button to run your code when it is clicked.

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<script>
  console.log("Hello console");
  alert("Hello user");
</script>
```

**Two messages appear in two different places. Where does each one show up?**

<div class="write-space"></div>

```html
<button onclick="sayHi()">Click Me</button>

<script>
  function sayHi() {
    alert("Hi there!");
  }
</script>
```

**When does the alert pop up — the moment the page loads, or later? What makes it run?**

<div class="write-space"></div>

```html
<script>
  console.log("one");
  console.log("two");
  console.log("three");
</script>
```

**In what order do the three messages reach the console?**

<div class="write-space"></div>

```html
<button onclick="greet()">Greet</button>

<script>
  function greet() {
    console.log("greeting...");
    alert("Welcome!");
  }
</script>
```

**The button is clicked once. How many things happen, and in what order?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Clicking the button should pop an alert that says `Hello!`. Right now nothing happens when you click.

```html
<button onclick="sayHello()">Click</button>

<script>
  function sayhello() {
    alert("Hello!");
  }
</script>
```

**Hint:** the button calls one name; the function is spelled another way. JavaScript is picky about capital letters.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should show a popup that says `Good job`. Right now the page shows an error.

```html
<script>
  alert(Good job);
</script>
```

**Hint:** text inside `alert()` needs something around it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Clicking should print `clicked` to the console. Right now the button does nothing.

```html
<button>Press</button>

<script>
  function reportClick() {
    console.log("clicked");
  }
</script>
```

**Hint:** the function exists, but nothing ever calls it. How does the button know which function to run?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Open a new HTML project on Replit and add a `<script>` tag. Build a button that pops a greeting **with your own name** in it.

1. Make a button on the page.
2. Write a function that runs when the button is clicked.
3. Inside the function, use `alert()` to say hello using your name.
4. Also send a message to the console with `console.log()` so you can see your code ran.

**Stretch:** add a second button with a *different* message — maybe your favorite food, or a fact about you.

When you finish, come back here. Send a **photo or video** of your page working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I added a button that …
>
> When the button is clicked, my function …
>
> I used `alert()` to …
>
> I used `console.log()` to …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your page runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **button**, **function**, **click**, **alert**, **console**.

> 1. Show your page before clicking anything.
> 2. Click the button and show the alert popping up.
> 3. Read your function out loud and say what makes it run.
> 4. Open the console and show your `console.log` message.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
