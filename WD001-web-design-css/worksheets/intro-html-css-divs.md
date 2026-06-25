# 🧱 WD001 — Build, Style & Box It Up

**Topic:** Make a real web page, style it from a `main.css` file, then group it with `<div>`s · **Course:** Web Design: CSS · **Time:** about 90 minutes

In this worksheet you build a small web page from nothing, then style it with **CSS** kept in its own file called **`main.css`**. Real websites keep their styles in a separate file so the HTML stays clean and one stylesheet can paint the whole site. You will do it that way from day one.

Your page will have a heading, a few paragraphs, a **weekly timetable**, some **buttons**, and a couple of **inputs**. Then you will learn the most useful container in web design: the **`<div>`** — an invisible box you put things inside so you can move and style them **as a group**.

---

## 1 · Predict 🔮

Read each bit of code. Before you imagine the browser drawing it, write what you think shows up.

```html
<head>
  <link rel="stylesheet" href="main.css">
</head>
```

**This line connects an HTML page to a separate file called `main.css`. If `main.css` is empty, does the page change? When does the styling actually appear?**

<div class="write-space"></div>

```html
<button>Click me</button>
<input placeholder="your name">
```

**What do you think these two look like on the page? Which one can you type into?**

<div class="write-space"></div>

In `main.css`:

```css
button {
  background-color: tomato;
  color: white;
}
```

**The HTML did not change — only `main.css` did. What happens to every button on the page? Why does the HTML not need editing?**

<div class="write-space"></div>

```html
<div>
  <h1>Coco</h1>
  <p>My cat.</p>
</div>
```

**A `<div>` is invisible. Do you think you will *see* a box on screen? Write your guess.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of code below was meant to do something but is broken. Read what it is **supposed** to do, rewrite it so it works, then explain why the original was wrong.

**Bug A** — This is supposed to connect the page to its stylesheet, but no styles ever show up.

```html
<link rel="stylesheet" href="mian.css">
```

**Hint:** the file is named `main.css`. Read the filename letter by letter.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This CSS in `main.css` is supposed to make all paragraphs gray.

```css
p {
  color = gray;
}
```

**Hint:** in CSS you do not use `=`. Look at how `color: white;` was written above.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This `<div>` is supposed to wrap a heading and a paragraph together, but the box never closes.

```html
<div>
  <h1>About Me</h1>
  <p>I like coding.</p>
```

**Hint:** every `<div>` needs a matching `</div>`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build the Page 🏗️

Open Replit and start a new HTML project. You will make **two files**: `index.html` for the content and `main.css` for the styles. Link them in the `<head>`.

Your page is a little "My Week" page. It needs all of these:

- a **heading** with a title,
- a few **paragraphs** about your week,
- a **weekly timetable** (a table with the days and what you do),
- two **buttons**,
- two **inputs** people can type into.

Start from this and change the words to be about you:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Week</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <h1>My Week</h1>
  <p>Hi, I'm ___. Here is what my week looks like.</p>
  <p>My favorite day is ___ because ___.</p>

  <table>
    <tr>
      <th>Day</th>
      <th>What I do</th>
    </tr>
    <tr>
      <td>Monday</td>
      <td>___</td>
    </tr>
    <tr>
      <td>Tuesday</td>
      <td>___</td>
    </tr>
    <tr>
      <td>Wednesday</td>
      <td>___</td>
    </tr>
  </table>

  <p>Sign up to hear about my week:</p>
  <input placeholder="your name">
  <input placeholder="your email">
  <button>Sign up</button>
  <button>Clear</button>
</body>
</html>
```

A `<table>` is made of rows (`<tr>`). Header cells use `<th>`, normal cells use `<td>`. Add more days if you like.

Run it. Right now it looks plain — that is fine. We style it next.

**Write one sentence: what does your timetable show, and what do your two buttons say?**

<div class="write-space"></div>

---

## 4 · Style It With `main.css` 🎨

Now open `main.css` (the empty file) and make the page look good. Everything you write here paints the page through the `<link>` you already added — you do **not** touch `index.html` again.

Each rule picks an element (`body`, `h1`, `table`, `button`, `input`) and changes how it looks:

```css
body {
  background-color: beige;
  font-family: Arial;
}

h1 {
  color: darkblue;
}

p {
  color: gray;
}

table {
  border: 1px solid darkblue;
}

th, td {
  padding: 8px;
}

button {
  background-color: tomato;
  color: white;
  padding: 10px;
  border-radius: 8px;
}

input {
  padding: 8px;
}
```

Type these into `main.css`, run the page, then make it yours:

- change the `background-color` and the `h1` color,
- give the `button` a color you like,
- add `padding` to a cell or input to space it out.

`padding` adds space **inside** an element so text does not touch the edge.

**Write the three colors you chose and where each one goes:**

<div class="write-space"></div>

**Run the page. What changed the moment you saved `main.css`? Did any rule not work the way you expected?**

<div class="write-space"></div>

---

## 5 · Group It With a `<div>` 📦

Right now everything floats down the page on its own. A `<div>` lets you wrap parts into one box you can style as a group.

In `index.html`, wrap your sign-up parts in a `<div>` with a class name:

```html
<div class="signup">
  <p>Sign up to hear about my week:</p>
  <input placeholder="your name">
  <input placeholder="your email">
  <button>Sign up</button>
  <button>Clear</button>
</div>
```

Then style that box in `main.css`. A `.` before the name means "the element with this class":

```css
.signup {
  background-color: white;
  padding: 20px;
  border: 2px solid darkblue;
  border-radius: 12px;
}
```

Run it. Your sign-up section is now one tidy card, and everything inside moved together.

**In your own words: what does a `<div>` do, and why is it useful to wrap things in one?**

<div class="write-space tall" style="min-height: 220px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a photo or short video of your finished page and show both files. Talk through it like you are teaching someone new. Try to use these words: **HTML**, **main.css**, **link**, **table**, **div**.

> 1. Show your finished page in the browser.
> 2. Show `main.css` and read one rule, then point to what it changes on the page.
> 3. Point to your timetable and your `<div>` and say what is inside each.
> 4. Explain why the styles live in a separate file.

**Plan what you will say below before you record — you can read from it while filming.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your page (photo or video) to teacher on KakaoTalk.
