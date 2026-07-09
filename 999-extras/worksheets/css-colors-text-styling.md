# 🎨 Extra — CSS Colors & Text Styling

**Topic:** Selectors, Colors & the Box Model · **Course:** Extra Worksheet · **Time:** about 30 minutes

CSS picks a part of the page with a **selector**, then changes it with a **property** and a **value**. On paper you will read CSS, predict it, fix it, and explain it in your own words.

> Keep these words handy: **selector**, **property**, **value**, **padding**, **border**, **margin**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think the page will look like.

```html
<style>
  h1 { color: blue; }
</style>
<h1>My Profile</h1>
```

**What color is the heading? What does the `h1` before the `{` pick?**

<div class="write-space"></div>

```html
<style>
  .note { background-color: #fef9c3; }
</style>
<div class="note">Revise CSS selectors.</div>
<div class="note">Practice the box model.</div>
<div>Feed the cat.</div>
```

**How many boxes turn yellow? Why?**

<div class="write-space"></div>

```html
<style>
  h1 {
    font-size: 36px;
    text-align: center;
  }
</style>
<h1>My Study Notes</h1>
<p>Today I learned about CSS.</p>
```

**Which line moves to the middle of the page, the `h1` or the `p`? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should turn the heading blue. Nothing changes.

```html
h1 { color blue; }
```

**Hint:** every property needs a `:` between it and its value.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should turn `<div class="note">` yellow. It stays white.

```html
note { background-color: #fef9c3; }
```

**Hint:** a class selector starts with a dot.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should make the title 32 pixels tall. The size does not change.

```html
h1 { font-size: 32; }
```

**Hint:** a size needs a unit.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

This is the finished profile card from your lesson.

```html
<style>
  #card {
    width: 300px;
    background-color: #fff7ed;
    padding: 24px;
    border: 3px solid #f97316;
    margin: 40px auto;
  }
</style>
<div id="card">
  <h1>Mina</h1>
  <p>Loves coding and cats.</p>
</div>
```

<table style="border-collapse:collapse;width:100%;max-width:460px;margin:16px auto;text-align:center;font-size:13px"><tr><td style="background:#fee2e2;padding:16px"><strong>margin</strong> — space outside<div style="border:4px solid #f97316;background:#fed7aa;margin-top:8px;padding:8px"><strong>border</strong> — the line<div style="background:#fff7ed;padding:16px;margin-top:8px"><strong>padding</strong> — space inside<div style="background:#ffffff;border:1px dashed #9ca3af;padding:12px;margin-top:8px"><strong>content</strong> — Mina</div></div></div></td></tr></table>

**What does `#card` pick? How would `.card` be different?**

<div class="write-space"></div>

**`padding: 24px` and `margin: 40px auto` both add space. Which space is inside the border?**

<div class="write-space"></div>

**In `margin: 40px auto`, what does `auto` do to the card sideways?**

<div class="write-space"></div>

---

### Submit ✅

Send this worksheet to teacher on KakaoTalk.
