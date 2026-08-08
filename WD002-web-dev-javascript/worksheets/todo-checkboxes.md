# ⚡ Daily Planner — Make the Tick Marks Count

**Topic:** Make each checkbox count its own task — `checked`, `change`, `if / else`, `classList` · **Course:** Web Dev: JavaScript · **Time:** about 50 minutes

Your Daily Planner has four tasks, each with a checkbox. Right now ticking one does not really count anything. In this worksheet you make the page show **TASKS DONE - 2** when two boxes are ticked, and go back down when you untick. You also fade a finished task using the `.done` style you already wrote in your CSS.

> 🧠 Words to know: **checkbox**, **checked**, **change**, **if / else**, **classList**

---

## 1 · Predict 🔮

Read each piece of code. Work out what happens, then write your prediction.

```javascript
let tasksDone = 0;
tasksDone = tasksDone + 1;
tasksDone = tasksDone + 1;
tasksDone = tasksDone - 1;
console.log(tasksDone);
```

**What number prints?**

<div class="write-space"></div>

```javascript
chk1.addEventListener("change", function () {
  console.log(chk1.checked);
});
```

**You tick the box, then untick it. What two values print, in order?**

<div class="write-space"></div>

```javascript
let tasksDone = 2;
statusText.textContent = "TASKS DONE - " + tasksDone;
```

**What words show on the page?**

<div class="write-space"></div>

```javascript
if (chk1.checked) {
  tasksDone = tasksDone + 1;
} else {
  // nothing here
}
```

**`tasksDone` is 1. You untick the box. What is `tasksDone` now — and is that right?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

These are from your own To-Do list code. Read what each is **supposed** to do, write the fix, then explain why the original was wrong.

**Bug A** — This is the listener for the **second** checkbox. Tick box 2 and nothing happens, but tick box 1 and box 2's text changes too.

```javascript
chk2.addEventListener("change", function () {
  statusText.textContent = "Checked: " + chk1.checked;
  if (chk1.checked) {
    tasksDone = tasksDone + 1;
  }
});
```

**Hint:** which checkbox is this listener for? Which checkbox is it reading?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The page should show **TASKS DONE - 1**. Instead it shows **Checked: true**.

```javascript
let tasksDone = 0;

chk1.addEventListener("change", function () {
  statusText.textContent = "Checked: " + chk1.checked;
  if (chk1.checked) {
    tasksDone = tasksDone + 1;
  }
});
```

**Hint:** `tasksDone` is counted, but is it ever put on the page?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Tick a box and the count goes up. Untick it and the count **stays** up. Tick and untick the same box five times and it says 5 tasks done.

```javascript
chk1.addEventListener("change", function () {
  if (chk1.checked) {
    tasksDone = tasksDone + 1;
  } else {
    // not ticked
  }
  statusText.textContent = "TASKS DONE - " + tasksDone;
});
```

**Hint:** the `else` branch runs when the box is unticked. What should happen to the count there?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

This is one finished checkbox. It is the pattern you will copy for all four.

```html
<div class="todo-item">
  <input type="text" class="content-gen" placeholder="Add a task...">
  <input type="checkbox" id="chk1">
</div>
<p id="statusText">TASKS DONE - 0</p>

<script>
  const chk1 = document.getElementById("chk1");
  const statusText = document.getElementById("statusText");
  let tasksDone = 0;

  chk1.addEventListener("change", function () {
    if (chk1.checked) {
      tasksDone = tasksDone + 1;
      chk1.parentElement.classList.add("done");
    } else {
      tasksDone = tasksDone - 1;
      chk1.parentElement.classList.remove("done");
    }
    statusText.textContent = "TASKS DONE - " + tasksDone;
  });
</script>
```

**You used `"click"` for your buttons. Why does a checkbox use `"change"` instead?**

<div class="write-space"></div>

**`chk1.checked` is not a number or words. What kind of value is it, and what are its only two possible values?**

<div class="write-space"></div>

**Which branch runs when you untick the box — `if` or `else`? What does it do to `tasksDone`?**

<div class="write-space"></div>

**`chk1.parentElement` is the `<div class="todo-item">` around the checkbox. So what exactly does `classList.add("done")` change on the page?**

<div class="write-space"></div>

---

## 4 · Your Assignment: Make All Four Count 🔨

Open your `scripts.js` and make the whole To-Do list work.

Your page already has `chk1`, `chk2`, `chk3`, `chk4` and `<p id="statusText">`. Your `main.css` already has this style — you wrote it, and nothing uses it yet:

```css
.done { opacity: .4; text-decoration: line-through; }
```

Every checkbox must do all three:

- **Tick** — add 1 to `tasksDone` and add the `done` class to that task's row.
- **Untick** — take 1 away from `tasksDone` and remove the `done` class from that row.
- **Always** — show `TASKS DONE - ` and the number in `statusText`.

Careful: each listener must read and change **its own** checkbox, not `chk1`.

**Write the listener you wrote for `chk3`:**

<div class="write-space tall" style="min-height: 260px"></div>

**Test it. Tick boxes 1, 2 and 3, then untick box 2. What does the page show?**

<div class="write-space"></div>

**When a row gets the `done` class, what do you see change about that row?**

<div class="write-space"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on a phone while your page runs. Talk like you are teaching someone new. Try to use these words: **checkbox**, **checked**, **change**, **if / else**, **classList**.

> 1. Show your page, then tick two boxes and read the count out loud.
> 2. Untick one box and say what the `else` part of your code just did.
> 3. Read your `chk4` listener out loud and say what each line does.
> 4. Say what would break if `chk4` read `chk1.checked` instead.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video of the four checkboxes counting to teacher on KakaoTalk.
