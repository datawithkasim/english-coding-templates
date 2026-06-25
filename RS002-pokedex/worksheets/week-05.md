# 🔴 RS002 Week 5 — English Worksheet

**Topic:** Cleaning Input — `.strip()` and `.lower()` · **Course:** Pokédex App · **Time:** about 45 minutes

This week your Pokédex lets the trainer **search by name**. But people type messily — extra spaces, mixed capitals. In the live lesson you cleaned their input with `.strip()` and `.lower()` so the search still works, then used `if` / `elif` / `else` to react to the choice. This worksheet is for **thinking about and explaining that code** — reading it closely, predicting what it does, and putting it into your own words.

> 🧠 Words to know: **strip**, **lower**, **clean**, **search**, **if / elif / else**

---

## 1 · Recall 🧠

From memory:

**Write a `for` loop that prints every name in a list called `names`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Without running it, write what you think will happen.

```python
choice = "  Pikachu  "
choice = choice.strip()
print(f"[{choice}]")
```

**What prints between the brackets, exactly?**

<div class="write-space"></div>

```python
choice = "PIKACHU"
choice = choice.lower()
print(choice)
```

**What does `.lower()` turn the text into?**

<div class="write-space"></div>

```python
choice = input("이름: ").strip().lower()

if choice == "pikachu":
    print("⚡ 피카츄!")
else:
    print("없는 포켓몬")
```

**The user types `  Pikachu `. Does the `if` match? Why or why not?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

**Bug A** — This should match even if the user types extra spaces. Right now `"  pikachu"` does not match.

```python
choice = input("이름: ").lower()

if choice == "pikachu":
    print("찾음!")
else:
    print("못 찾음")
```

**Hint:** spaces are still there — clean them too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should match whether the user types `Pikachu`, `PIKACHU`, or `pikachu`. Right now only the exact lowercase word works.

```python
choice = input("이름: ").strip()

if choice == "pikachu":
    print("찾음!")
else:
    print("못 찾음")
```

**Hint:** make both sides lowercase before comparing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should show a different message for each of three Pokémon, and one message for anything else. Right now the last branch runs even for known Pokémon.

```python
choice = input("이름: ").strip().lower()

if choice == "pikachu":
    print("⚡ 피카츄!")
if choice == "bulbasaur":
    print("🌱 이상해씨!")
else:
    print("없는 포켓몬")
```

**Hint:** the second check should be `elif`, not a fresh `if`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working search carefully. It is the kind of code you built in the live lesson.

```python
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
choice = input("Enter Pokémon name: ").strip().lower()

if choice == "pikachu":
    print("⚡ 피카츄를 골랐어요!")
elif choice == "bulbasaur":
    print("🌱 이상해씨를 골랐어요!")
elif choice == "charmander":
    print("🔥 파이리를 골랐어요!")
else:
    print("그 포켓몬은 도감에 없어요.")
```

**What do `.strip()` and `.lower()` each do to the trainer's input?**

<div class="write-space"></div>

**Why are the names in the `if` checks (like `"pikachu"`) written in lowercase?**

<div class="write-space"></div>

**If the trainer types `  BULBASAUR  `, which line prints, and why?**

<div class="write-space"></div>

**When does the `else` branch run?**

<div class="write-space"></div>

**Why is the second check `elif` and not another `if`?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the search code **you wrote in today's lesson** in a short phone video. You may show it running. Teach it like the viewer is new, and try to use: **strip**, **lower**, **clean**, **search**, **if / elif / else**.

> 1. Show your search code and run it with a name that has extra spaces and capitals.
> 2. Point to where you cleaned the input, and say which method fixed the spaces and which fixed the capitals.
> 3. Read your `if / elif / else` out loud and explain what each branch does.
> 4. Type a Pokémon that is not in the dex and show the `else` message.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
