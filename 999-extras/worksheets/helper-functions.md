# 🧩 Extra — Helper Functions: Teach It Once, Use It Anywhere

**Topic:** Helper Functions · **Course:** Extra Worksheet · **Time:** about 30 minutes

When you copy the same lines again and again, your code gets long and hard to fix. A **helper function** lets you teach the computer a small job **once**, give it a name, then **call** that name whenever you need it. On paper you will read helper functions, predict them, fix them, and explain them in your own words.

> Keep these words handy: **function**, **`def`**, **call**, **parameter**, **reuse**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
def say_hello():
    print("Hello!")

say_hello()
```

**What prints? Does the line inside run when you *define* the helper, or when you *call* it?**

<div class="write-space"></div>

```python
def cheer():
    print("Go team!")

cheer()
cheer()
cheer()
```

**How many lines print? You only wrote the message once — how did it print more times?**

<div class="write-space"></div>

```python
def greet(name):
    print("Hi " + name)

greet("Mia")
greet("Sam")
```

**What two lines print? What is different between the two calls?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should print `Hello!`. Instead, when you run it, **nothing happens at all**.

```python
def say_hello():
    print("Hello!")
```

**Hint:** writing `def` only **teaches** the helper. Something is missing after it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should print `Go team!`. But when you run it, still **nothing prints**.

```python
def cheer():
    print("Go team!")

cheer
```

**Hint:** to **call** a helper you need `( )` after its name.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This helper needs a name to say hi to. But the call forgot to give one, so the code crashes.

```python
def greet(name):
    print("Hi " + name)

greet()
```

**Hint:** the helper has a **parameter** `name`. Put a value for it inside the `( )` when you call.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working helper carefully.

```python
def welcome(name):
    print("Welcome, " + name + "!")
    print("Glad you are here.")

welcome("Mia")
welcome("Sam")
welcome("Ava")
```

**`welcome` is written once but called three times. How many lines print in total?**

<div class="write-space"></div>

**Both `print` lines live inside `welcome`. If you wanted to change `"Glad you are here."`, how many places do you edit? Why is that better than copying those two lines under every name?**

<div class="write-space"></div>

**What job does `name` do each time `welcome` is called?**

<div class="write-space"></div>

---

### Submit ✅

Send this worksheet to teacher on KakaoTalk.
