# ⚡ WD002 Week 7 — English Worksheet

**Topic:** Functions — Organizing Your Code · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This week you wrap code into reusable chunks. A *function* is a named block you can run again and again. **Parameters** are the values you hand it; **`return`** is the answer it hands back. You will build a calculator that shares one tidy set of functions.

---

## 1 · Predict 🔮

Read each piece of code. Before you run it, write what you think will happen.

```html
<script>
  function add(a, b) {
    return a + b;
  }
  console.log(add(2, 3));
</script>
```

**What number prints?**

<div class="write-space"></div>

```html
<script>
  function greet(name) {
    return "Hi, " + name + "!";
  }
  console.log(greet("Dami"));
</script>
```

**What sentence prints?**

<div class="write-space"></div>

```html
<script>
  function double(n) {
    return n * 2;
  }
  console.log(double(5));
  console.log(double(10));
</script>
```

**The same function is called twice with different inputs. What two numbers print?**

<div class="write-space"></div>

```html
<script>
  function add(a, b) {
    let total = a + b;
  }
  console.log(add(4, 4));
</script>
```

**This function has no `return`. What does `console.log` show? (Hint: a function that returns nothing gives back `undefined`.)**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — `add(3, 4)` should give back `7`. Right now it prints `undefined`.

```html
<script>
  function add(a, b) {
    a + b;
  }
  console.log(add(3, 4));
</script>
```

**Hint:** the function adds the numbers but never hands the answer back. One keyword is missing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should multiply two numbers. Right now it always gives the **same** answer no matter what you pass in.

```html
<script>
  let a = 2;
  let b = 3;
  function multiply(a, b) {
    return 2 * 3;
  }
  console.log(multiply(5, 5));
</script>
```

**Hint:** the function ignores its parameters and uses fixed numbers instead. Use `a` and `b`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Clicking should show the sum on the page. Right now you get an error because the function name does not match.

```html
<input id="n1" type="number">
<input id="n2" type="number">
<button onclick="showSum()">Add</button>
<p id="out"></p>

<script>
  function showsum() {
    let a = Number(document.querySelector("#n1").value);
    let b = Number(document.querySelector("#n2").value);
    document.querySelector("#out").textContent = a + b;
  }
</script>
```

**Hint:** the button calls one name; the function is spelled with different capitals. Match them exactly.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Make It Yours 📸

Build a **calculator** page with three functions: add, subtract, and multiply.

1. Make two input boxes for numbers.
2. Write three functions — `add(a, b)`, `subtract(a, b)`, `multiply(a, b)` — each one `return`s its answer.
3. Add three buttons. Each button reads both inputs (as `Number`), calls the right function, and shows the result on the page.
4. Notice how all three buttons share the same way of reading inputs — that is what functions are for.

**Stretch:** add a divide button, and show a friendly message if someone tries to divide by 0.

When you finish, come back here. Send a **photo or video** of all three operations working, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I wrote a function called …
>
> Each function takes parameters, which are …
>
> I used `return` to …
>
> The three buttons share code because …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while your calculator runs. Talk through it like you are teaching someone who has never seen it. Try to use these words: **function**, **parameter**, **return**, **reuse**, **calculator**.

> 1. Type two numbers and click each operation.
> 2. Read one function out loud and point to its parameters.
> 3. Show where `return` hands the answer back.
> 4. Explain why functions are tidier than repeating the same code.

**Write what you will say in your video.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
