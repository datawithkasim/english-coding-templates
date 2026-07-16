# ↔️ Extra — CSS Flexbox Layout

**Topic:** Flex Container, Direction & Spacing · **Course:** Extra Worksheet · **Time:** about 30 minutes

One line — `display: flex` — turns a box into a **flex container**. The boxes inside it become **flex items** and line up in a row. Then you steer them: `justify-content` slides them along the row, `align-items` moves them up and down, and `gap` puts space between them. On paper you will read Flexbox, predict it, fix it, and explain it in your own words.

> Keep these words handy: **flex container**, **flex item**, **flex-direction**, **justify-content**, **align-items**, **gap**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think the page will look like.

```html
<style>
  .container { display: flex; }
</style>
<div class="container">
  <div class="box">A</div>
  <div class="box">B</div>
  <div class="box">C</div>
</div>
```

**Without `display: flex`, A, B and C stack one per line. With it, where do they go?**

<div class="write-space"></div>

```html
<style>
  .container {
    display: flex;
    flex-direction: column;
  }
</style>
```

**The same three boxes. What does `column` do to them?**

<div class="write-space"></div>

```html
<style>
  .container {
    display: flex;
    justify-content: space-between;
  }
</style>
```

**Three boxes, one wide container. Where does the empty space go?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — The boxes should sit side by side. They stay stacked.

```html
.container { flex; }
```

**Hint:** `flex` is the value. Something is missing in front of it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The boxes are in a row but squashed together. There should be 24px between them.

```html
.container {
  display: flex;
  gap 24px;
}
```

**Hint:** every property needs a `:` between it and its value.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The three boxes should spread across the row. Nothing moves.

```html
<div class="container">
  <div class="box" style="justify-content: space-between;">A</div>
  <div class="box">B</div>
  <div class="box">C</div>
</div>
```

**Hint:** `justify-content` is a rule for the **container**, not for one item.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

This is the centred toolbar from your lesson.

```html
<style>
  .toolbar {
    height: 90px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
    background: #1f2937;
  }
  .btn {
    padding: 10px 18px;
    background: #f97316;
    color: white;
    border-radius: 6px;
  }
</style>
<div class="toolbar">
  <button class="btn">Cut</button>
  <button class="btn">Copy</button>
  <button class="btn">Paste</button>
</div>
```

<table style="border-collapse:collapse;width:100%;max-width:460px;margin:16px auto;text-align:center;font-size:13px"><tr><td style="padding:10px 0"><strong>justify-content</strong> — moves items along this way ⟷</td></tr><tr><td style="background:#1f2937;padding:22px 12px"><table style="border-collapse:collapse;margin:0 auto"><tr><td style="background:#f97316;color:#fff;padding:8px 14px;border-radius:6px">Cut</td><td style="width:16px"></td><td style="background:#f97316;color:#fff;padding:8px 14px;border-radius:6px">Copy</td><td style="width:16px"></td><td style="background:#f97316;color:#fff;padding:8px 14px;border-radius:6px">Paste</td></tr></table><div style="color:#e5e7eb;margin-top:10px">↕ <strong style="color:#ffffff">align-items</strong> — moves items this way</div></td></tr><tr><td style="padding:8px 0;color:#6b7280">the gaps between the buttons = <strong>gap: 16px</strong></td></tr></table>

**Which box is the flex container — `.toolbar` or `.btn`? How do you know?**

<div class="write-space"></div>

**`justify-content: center` and `align-items: center` both say `center`. What is different about the two?**

<div class="write-space"></div>

**If you deleted `gap: 16px`, what would change? What would stay the same?**

<div class="write-space"></div>

---

### Submit ✅

Send this worksheet to teacher on KakaoTalk.
