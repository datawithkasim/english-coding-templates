# ⚡ WD002 Week 3 — English Worksheet

**Topic:** Events — Reacting to the User · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week your page **listens**. An *event* is something the user does — a click, a hover, a key press. `addEventListener("click", ...)` runs a function when that event happens. You will build a score counter that goes up, down, and resets.

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<button id="btn">Tap</button>

<script>
  document.querySelector("#btn").addEventListener("click", function() {
    console.log("tapped");
  });
</script>
```

**What prints when you click the button **three** times?**

<div class="write-space"></div>

```html
<span id="score">0</span>
<button id="up">+1</button>

<script>
  let score = 0;
  document.querySelector("#up").addEventListener("click", function() {
    score = score + 1;
    document.querySelector("#score").textContent = score;
  });
</script>
```

**You click `+1` four times. What number is on the screen?**

<div class="write-space"></div>

```html
<button id="reset">Reset</button>

<script>
  let score = 10;
  document.querySelector("#reset").addEventListener("click", function() {
    score = 0;
    document.querySelector("#score").textContent = score;
  });
</script>
```

**The score starts at 10. After clicking reset, what is it?**

<div class="write-space"></div>

```html
<button id="down">-1</button>

<script>
  let score = 2;
  document.querySelector("#down").addEventListener("click", function() {
    score = score - 1;
    document.querySelector("#score").textContent = score;
  });
</script>
```

**You click `-1` five times starting from 2. What number shows? Is anything strange about it?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — Clicking the button should add 1 to the score on screen. Right now the number on screen never changes, even though the click happens.

```html
<span id="score">0</span>
<button id="up">+1</button>

<script>
  let score = 0;
  document.querySelector("#up").addEventListener("click", function() {
    score = score + 1;
  });
</script>
```

**Hint:** the variable goes up, but nobody updates the screen. One line is missing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should listen for a **click**. Right now clicking the button does nothing.

```html
<button id="go">Go</button>

<script>
  document.querySelector("#go").addEventListener("clik", function() {
    console.log("go!");
  });
</script>
```

**Hint:** the event name is misspelled, so the browser is listening for an event that never happens.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The score should never drop below 0. Right now clicking `-1` past zero gives negative numbers.

```html
<button id="down">-1</button>

<script>
  let score = 0;
  document.querySelector("#down").addEventListener("click", function() {
    score = score - 1;
    document.querySelector("#score").textContent = score;
  });
</script>
```

**Hint:** before subtracting, check whether the score is already 0. Use an `if`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Build a score counter with **three** buttons: `+1`, `-1`, and `reset`.

1. Show the score somewhere on the page.
2. Use `addEventListener` to connect each button to its own job.
3. `+1` adds, `-1` subtracts, `reset` sets the score back to 0.
4. Make sure the score **never goes below 0** (use an `if`).

**Stretch:** add a `+5` button, or change the page color when the score reaches a certain number.

When you finish, come back here. Send a **photo or video** of all three buttons working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made buttons for …
>
> I used `addEventListener` to …
>
> To stop the score going below 0, I …
>
> The reset button works by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your counter runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **event**, **listener**, **click**, **score**, **reset**.

> 1. Show the counter at 0.
> 2. Click `+1` a few times, then `-1`, then `reset`.
> 3. Read one listener out loud and say which button it belongs to.
> 4. Show what happens when you try to go below 0.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
