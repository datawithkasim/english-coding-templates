# ⚡ WD002 Week 5 — English Worksheet

**Topic:** Conditionals — Checking Answers · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week your code **decides**. `if / else` runs different code depending on a condition. `===` checks if two things are exactly equal. `&&` (AND) needs *both* sides true; `||` (OR) needs *either* side. You will build a number-guessing game that tells the user "higher" or "lower".

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<script>
  let guess = 7;
  if (guess === 7) {
    console.log("Correct!");
  } else {
    console.log("Wrong");
  }
</script>
```

**Which message prints?**

<div class="write-space"></div>

```html
<script>
  let guess = 4;
  let secret = 10;
  if (guess < secret) {
    console.log("Try bigger");
  } else {
    console.log("Try smaller");
  }
</script>
```

**The guess is smaller than the secret. Which message prints?**

<div class="write-space"></div>

```html
<script>
  let answer = 5;
  let name = "Suho";
  if (answer === 5 && name === "Suho") {
    console.log("Both correct!");
  }
</script>
```

**`&&` needs both sides true. Does the message print? What if the name were different?**

<div class="write-space"></div>

```html
<script>
  let day = "Saturday";
  if (day === "Saturday" || day === "Sunday") {
    console.log("Weekend!");
  }
</script>
```

**`||` needs only one side true. Does the message print? What about `Monday`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should celebrate only when the guess is exactly 7. Right now it celebrates **every** time, even with the wrong number.

```html
<script>
  let guess = 3;
  if (guess = 7) {
    console.log("Correct!");
  }
</script>
```

**Hint:** one equals sign *sets* the variable to 7; you wanted to *compare*. Use `===`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should say `Try bigger` when the guess is too low and `Try smaller` when it is too high. Right now it says `Try smaller` even when the guess is too low.

```html
<script>
  let guess = 2;
  let secret = 8;
  if (guess > secret) {
    console.log("Try bigger");
  } else {
    console.log("Try smaller");
  }
</script>
```

**Hint:** look closely at the `>` sign — it is pointing the wrong way for "too low".

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A special prize should appear only when the answer is right **and** the player typed their name. Right now the prize shows when *either* one is true.

```html
<script>
  let answer = 5;
  let name = "";
  if (answer === 5 || name === "Mina") {
    console.log("Prize unlocked!");
  }
</script>
```

**Hint:** "and" is not the same as "or". Which operator means both must be true?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Build a number-guessing game with a secret number between **1 and 100**.

1. Store a secret number in a variable.
2. Let the user type a guess and click a button.
3. Tell them `Correct!`, `Try a bigger number`, or `Try a smaller number` using `if / else if / else`.
4. Count how many tries it took and show that number when they win (hint: a counter variable that goes `+1` each guess).

**Stretch:** add a special message that needs *two* things true with `&&` — for example, the right answer **and** fewer than 5 tries.

When you finish, come back here. Send a **photo or video** of a full round (a few wrong guesses, then the win), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I picked a secret number and …
>
> My `if / else` checks …
>
> To count the tries, I …
>
> The game tells the user "bigger" or "smaller" by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your game runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **if**, **else**, **condition**, **compare**, **guess**.

> 1. Make a guess that is too low and show the message.
> 2. Make a guess that is too high and show the message.
> 3. Win the game and show the try count.
> 4. Read one condition out loud and say what makes it true.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
