# ⚡ Daily Planner — Make the Counter Buttons

**Topic:** Wire three buttons to change a number and show it on the page — `getElementById`, `addEventListener`, `count`, `textContent` · **Course:** Web Dev: JavaScript · **Time:** about 50 minutes

You built a Daily Planner page with three buttons: **increase**, **decrease**, and **square**. Now you make them work. Each button changes a **count**, and a text field shows the new number. First you read code and predict, then you fix broken code, then you wire all three buttons yourself.

> 🧠 Words to know: **getElementById**, **addEventListener**, **count**, **textContent**, **square**

---

## 1 · Predict 🔮

Read each piece of code. Work out what happens, then write your prediction.

```javascript
let count = 0;
count = count + 1;
count = count + 1;
console.log(count);
```

**What number prints?**

<div class="write-space"></div>

```javascript
let count = 3;
count = count * count;
console.log(count);
```

**What does `count` become? What does "square" mean here?**

<div class="write-space"></div>

```html
<p id="clicksCounter"></p>

<script>
  const clicksCounter = document.getElementById("clicksCounter");
  clicksCounter.textContent = "Clicks: 5";
</script>
```

**The `<p>` started empty. What text shows on the page now?**

<div class="write-space"></div>

```javascript
btnInc.addEventListener("click", function () {
  count = count + 1;
  clicksCounter.textContent = "Clicks: " + count;
});
```

**The page shows `Clicks: 0`. You click the button three times. What does it show?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block is broken. Read what it is **supposed** to do, write the fix, then explain why the original was wrong.

**Bug A** — This should grab the increase button, whose id in the HTML is `btnInc`. Right now `btn` ends up empty, so nothing works.

```javascript
const btn = document.getElementById("btn");
```

**Hint:** the id inside `getElementById(" ")` must match the id in the HTML exactly.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Clicking Increase should add **1**. Right now it adds **3** every click.

```javascript
btnInc.addEventListener("click", function () {
  count = count + 1;
});
btnInc.addEventListener("click", function () {
  count = count + 1;
});
btnInc.addEventListener("click", function () {
  count = count + 1;
});
```

**Hint:** how many times did you tell the button to listen? Every listener runs on every click.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The Decrease button should take **1** away from count. Right now clicking it does nothing.

```javascript
const btnDec = document.getElementById("btnDec");

// the increase button is wired, but nothing here talks to btnDec
```

**Hint:** a button only reacts if you add an `addEventListener` to it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working **increase** button carefully. It is the pattern you will copy for the other two.

```html
<button id="btnInc">increase</button>
<p id="clicksCounter">Count: 0</p>

<script>
  const btnInc = document.getElementById("btnInc");
  const clicksCounter = document.getElementById("clicksCounter");
  let count = 0;

  btnInc.addEventListener("click", function () {
    count = count + 1;
    clicksCounter.textContent = "Count: " + count;
  });
</script>
```

**Which line makes the starting count, and what number does it start at?**

<div class="write-space"></div>

**What does `document.getElementById("btnInc")` give you?**

<div class="write-space"></div>

**Inside the click function, two things happen every click. Name both, in order.**

<div class="write-space"></div>

**What does `textContent` change — the code, or the words shown on the page?**

<div class="write-space"></div>

---

## 4 · Your Assignment: Three Buttons 🔨

Now make all three buttons work on your Daily Planner. Open your `scripts.js`.

Your page already has these:

```html
<button id="btnInc">increase</button>
<button id="btnDec">decrease</button>
<button id="btnSqu">square</button>
<p id="clicksCounter"></p>
```

Make each button change `count`, then show the new number in `clicksCounter`:

- **Increase** — `btnInc` adds 1 to count.
- **Decrease** — `btnDec` takes 1 away from count.
- **Square** — `btnSqu` multiplies count by itself: `count = count * count`.

Start from this. Finish the two `TODO` buttons the same way as increase:

```javascript
const btnInc = document.getElementById("btnInc");
const btnDec = document.getElementById("btnDec");
const btnSqu = document.getElementById("btnSqu");
const clicksCounter = document.getElementById("clicksCounter");
let count = 0;

btnInc.addEventListener("click", function () {
  count = count + 1;
  clicksCounter.textContent = "Count: " + count;
});

// TODO: btnDec — take 1 away from count, then show it
// TODO: btnSqu — multiply count by itself, then show it
```

**Write the two listeners you added (decrease and square):**

<div class="write-space tall" style="min-height: 260px"></div>

**Test it: set count to 3, then click square. What number shows? Click square again — what shows now?**

<div class="write-space"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on a phone while your page runs. Talk like you are teaching someone new. Try to use these words: **button**, **addEventListener**, **count**, **textContent**, **square**.

> 1. Show your page, then click each button and watch the number change.
> 2. Read your **square** button's code out loud and say what it does.
> 3. Point to the line that shows the number on the page.
> 4. Say what happens to the count when you click square twice.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video of the three buttons working to teacher on KakaoTalk.
