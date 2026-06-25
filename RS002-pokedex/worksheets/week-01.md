# 🔴 RS002 Week 1 — English Worksheet

**Topic:** input + Variables — Welcome, Trainer! · **Course:** Pokédex App · **Time:** about 45 minutes

This week your program **asks the user a question** with `input()`, **stores the answer** in a variable, and **prints a welcome screen** with an f-string. This worksheet is about *thinking through* and *explaining* that code — the first screen of the Pokédex app you wrote together in your live lesson.

> 🧠 Words to know: **input**, **variable**, **f-string**, **default**, **print**

> Coming from RS001? You used `game.ask()` before. This week we use plain Python `input()`. Same idea — ask, remember, use — but it is the standard Python way.

---

## 1 · Predict 🔮

Read each block. Without running it, write what you think will happen.

```python
trainer_name = input("트레이너님, 이름을 알려주세요: ")
print(f"환영합니다, {trainer_name} 트레이너님!")
```

**If the user types `지우`, what does the program print? Where does `지우` get stored?**

<div class="write-space"></div>

```python
trainer_name = input("이름: ")
print("환영합니다, trainer_name 트레이너님!")
```

**Careful — there is no `f` and no `{ }` here. What does this print, exactly?**

<div class="write-space"></div>

```python
trainer_name = input("이름을 알려주세요: ")

if trainer_name == "":
    trainer_name = "이름 모를 트레이너"

print(f"환영합니다, {trainer_name} 트레이너님!")
```

**The user just presses Enter without typing anything. What name gets printed? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, write the fixed code on paper, then explain why the original was wrong.

**Bug A** — This should print `환영합니다, 이슬 트레이너님!` when the user types `이슬`. Right now it prints the variable name instead of the value.

```python
trainer_name = input("이름: ")
print("환영합니다, trainer_name 트레이너님!")
```

**Hint:** an f-string needs both the `f` and curly braces around the variable.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should store the trainer's name, then greet them. Right now it greets *before* it ever asks.

```python
print(f"환영합니다, {trainer_name} 트레이너님!")
trainer_name = input("이름: ")
```

**Hint:** you can only use a variable *after* you have made it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When the user types nothing, this should fall back to `이름 모를 트레이너`. Right now an empty answer prints an empty name.

```python
trainer_name = input("이름: ")
print(f"환영합니다, {trainer_name} 트레이너님!")
```

**Hint:** check for `""` and set a default before you print.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working Pokédex intro screen carefully. Answer each question in your own words.

```python
trainer_name = input("트레이너님, 이름을 알려주세요: ")

if trainer_name == "":
    trainer_name = "이름 모를 트레이너"

print(f"\n=== 포켓몬 도감 ===")
print(f"환영합니다, {trainer_name} 트레이너님!")
print(f"오늘도 새로운 포켓몬을 만날 준비가 되셨나요?\n")
```

**What does the first line do, and where does the trainer's answer go?**

<div class="write-space"></div>

**What is the `if trainer_name == "":` block checking for, and what happens when it is true?**

<div class="write-space"></div>

**In the welcome line, how do the `{ }` change what gets printed? What would happen if you removed the `f`?**

<div class="write-space"></div>

**What does the `\n` do inside the print lines?**

<div class="write-space"></div>

**Which line is the "default" name, and why is having a default useful?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the Pokédex intro code **you wrote in today's lesson** in a short phone video. You may show it running. Talk through it like you are teaching someone new, and use these words: **input**, **variable**, **f-string**, **default**, **print**.

> Run your program and type your name.
>
> Read your `input()` line out loud and say what variable it stores into.
>
> Read your f-string out loud and point to the `{ }` part.
>
> Run it again, type nothing, and show the default name appear.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
