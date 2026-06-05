# 🏗️ WD001 Week 1 — English Worksheet

**Topic:** HTML Basics — The Skeleton of a Page · **Course:** Web Design: CSS · **Time:** about 45 minutes

This week you build the **skeleton** of a web page with HTML. Every page is made of **tags**. Most tags come in pairs — an **opening tag** like `<p>` and a **closing tag** like `</p>` — and your text goes in between.

---

## 1 · Predict 🔮

Read each bit of HTML. Before you imagine the browser drawing it, write what you think will show up on the screen.

```html
<h1>My Pets</h1>
<p>I have a cat named Coco.</p>
```

**What appears on the page? Which line looks bigger, and why?**

<div class="write-space"></div>

```html
<p>I love pizza
<p>I love games
```

**These paragraphs are missing their closing `</p>` tags. Do you think the browser still shows the text? What might look messy?**

<div class="write-space"></div>

```html
<body>
  <h1>Welcome</h1>
  <img src="dog.jpg" alt="my dog">
  <p>This is my dog.</p>
</body>
```

**Describe in plain English what shows up, from top to bottom.**

<div class="write-space"></div>

```html
<h1>Hello</h1>
```

**`<img>` does not need a closing tag, but `<h1>` does. What do you think happens if you forget `</h1>`? Write your guess, then test it later.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each bit of HTML below was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — This is supposed to be one big heading that says **About Me**.

```html
<h1>About Me</p>
```

**Hint:** the opening and closing tags should match.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This is supposed to show a photo named `me.jpg`.

```html
<img scr="me.jpg">
```

**Hint:** read the attribute name out loud, letter by letter.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This is supposed to be a heading **and then** a paragraph. Right now everything ends up inside the heading.

```html
<h1>My Hobbies
I like drawing and coding.</h1>
```

**Hint:** the paragraph needs its own tags.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your About Me Page 📸

Open Replit and start a new HTML project. Build an **About Me** page with these parts:

1. a big heading with your name (`<h1>`),
2. a paragraph with **3 things you like** (`<p>`),
3. one photo of you or something you like (`<img>`).

You can build it like this and change the words to be about you:

```html
<!DOCTYPE html>
<html>
<head>
  <title>About Me</title>
</head>
<body>
  <h1>Hi, I'm ___</h1>
  <p>I like ___, ___, and ___.</p>
  <img src="my-photo.jpg" alt="my photo">
</body>
</html>
```

When you finish, send a **photo or video** of your page (or a picture of your code), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I made the page with …
>
> My `<h1>` says …
>
> The three things I put in my paragraph were …
>
> I added a photo by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you show your page. Talk through it like you are teaching someone who has never seen HTML. Try to use these words: **tag**, **heading**, **paragraph**, **image**, **browser**.

> 1. Show your finished page in the browser.
> 2. Point to your `<h1>` and read it out loud.
> 3. Point to your `<p>` and say what is inside.
> 4. Show one tag you got wrong at first and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
