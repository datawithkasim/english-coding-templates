# 🔀 Extra — If Statements: Advanced

**Topic:** Nested If + Boolean Logic · **Course:** Extra Worksheet · **Time:** about 40 minutes

An `if` can live **inside** another `if`. The inner one only runs when the outer one is true. On paper you will read, predict, fix, and explain. Then you will write and run your own code in the IDE.

> Keep these words handy: **nested**, **and / or / not**, **return**, **indent level**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Welcome, admin!")
    else:
        print("Welcome, user!")
else:
    print("Please log in.")
```

**What prints? Which `if` runs first — the outer one or the inner one?**

<div class="write-space"></div>

```python
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age < 13:
        return "Kid"
    elif age < 20:
        return "Teen"
    else:
        return "Adult"

print(check_age(15))
```

**What does this print? Why does the function stop at the first `return` it hits?**

<div class="write-space"></div>

```python
health = 30
shield = True

if health > 0:
    if health < 50 and shield:
        print("Low health, but shielded")
    elif health < 50:
        print("Low health, no shield!")
    else:
        print("Healthy")
else:
    print("Defeated")
```

**What prints? What would print if `shield` was `False`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should only check `is_admin` when the user is logged in. Right now it crashes / checks `is_admin` even when logged out, because the inner `if` isn't nested inside the outer one — it just runs alongside it.

```python
logged_in = False
is_admin = True

if logged_in:
    print("Logged in")
if is_admin:
    print("Welcome, admin!")
```

**Hint:** where should the second `if` be indented?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This function should return `"Adult"` for age `20` and up. Right now, calling it with `age = 20` returns `"Teen"`.

```python
def check_age(age):
    if age < 13:
        return "Kid"
    elif age < 20:
        return "Teen"
    elif age <= 20:
        return "Adult"
    else:
        return "Adult"
```

**Hint:** two branches both try to catch `20` — which one does Python reach first?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

```python
def get_ticket_price(age, is_member):
    if age < 5:
        return 0
    else:
        if is_member:
            if age < 18:
                return 5
            else:
                return 8
        else:
            if age < 18:
                return 10
            else:
                return 15

print(get_ticket_price(25, True))
```

**Walk through this step by step for `age = 25`, `is_member = True`. Which branch does it take at each nested level?**

<div class="write-space"></div>

**What would this return for `age = 3`, `is_member = False`? Why does it not even check `is_member`?**

<div class="write-space"></div>

**Why nest the `if`s instead of writing one long `elif` chain? What would happen if you removed one level of indent by mistake?**

<div class="write-space"></div>

---

## 4 · Code It 💻

Open the IDE at **app.english-coding.co.uk** and write your own program.

Write a function `check_login(username, password, is_banned)` that:
- returns `"Banned"` if `is_banned` is `True`
- otherwise, if `username == "admin"` and `password == "1234"`, returns `"Admin login"`
- otherwise, if `password == "1234"`, returns `"User login"`
- otherwise returns `"Access denied"`

Use **nested if statements** for at least one part of the logic. Test it by calling the function with 3 different sets of values and printing the result.

Run it, then write your function code and what each test printed.

<div class="write-space tall" style="min-height: 280px"></div>

---

### Submit ✅

Send this worksheet + a screenshot of your working code to teacher on KakaoTalk.
