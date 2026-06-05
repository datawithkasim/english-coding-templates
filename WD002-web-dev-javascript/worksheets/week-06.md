# ⚡ WD002 Week 6 — English Worksheet

**Topic:** Arrays and Loops — Handling Many Items · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week you hold **many things at once**. An *array* is a list of values. `array[0]` reads the first item, `array.length` counts them, and a `for` loop visits every item in turn. You will pick a random item and print a whole list to the page.

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<script>
  let fruits = ["apple", "banana", "cherry"];
  console.log(fruits[0]);
  console.log(fruits[2]);
</script>
```

**Index counting starts at 0. Which two words print?**

<div class="write-space"></div>

```html
<script>
  let colors = ["red", "green", "blue", "yellow"];
  console.log(colors.length);
</script>
```

**What number prints?**

<div class="write-space"></div>

```html
<script>
  let names = ["Suji", "Hana", "Tae"];
  for (let i = 0; i < names.length; i = i + 1) {
    console.log(names[i]);
  }
</script>
```

**How many lines print, and in what order?**

<div class="write-space"></div>

```html
<script>
  let items = ["🍎", "🍌", "🍇"];
  let i = Math.floor(Math.random() * items.length);
  console.log(items[i]);
</script>
```

**`Math.random()` gives a number between 0 and almost 1. After multiplying and rounding down, which items could `i` be? What gets printed?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This should print the **first** item, `cat`. Right now it prints `dog`.

```html
<script>
  let pets = ["cat", "dog", "bird"];
  console.log(pets[1]);
</script>
```

**Hint:** index counting starts at 0, not 1. Which index is the first item?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should print **every** name in the list. Right now it skips the last one.

```html
<script>
  let names = ["Yuna", "Joon", "Sera"];
  for (let i = 0; i < names.length - 1; i = i + 1) {
    console.log(names[i]);
  }
</script>
```

**Hint:** the loop stops one item too early. Compare `i` against the real length of the list.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should pick a **random** item from the list. Right now it crashes with `undefined` sometimes because the index can be too big.

```html
<script>
  let snacks = ["chip", "candy", "gum"];
  let i = Math.floor(Math.random() * 5);
  console.log(snacks[i]);
</script>
```

**Hint:** the list has 3 items, but the code rolls a number up to 5. Multiply by the list's real length instead.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Build a page that stores **5 of your favorite emojis** in an array and picks one at random when a button is clicked.

1. Make an array with 5 emojis (or words you like).
2. Add a button. When clicked, pick a random index with `Math.floor(Math.random() * array.length)`.
3. Show the chosen emoji on the page.
4. Add a second button that uses a `for` loop to print **every** item on the page.

**Stretch:** keep a count of how many times each emoji has been picked, or never show the same one twice in a row.

When you finish, come back here. Send a **photo or video** of both buttons working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I filled my array with …
>
> To pick a random one, I …
>
> My `for` loop goes through the list by …
>
> `array.length` is useful because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your page runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **array**, **index**, **length**, **loop**, **random**.

> 1. Show your array in the code.
> 2. Click the random button a few times and show different results.
> 3. Click the list button and show every item printed.
> 4. Read your `for` loop out loud and say what makes it stop.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
