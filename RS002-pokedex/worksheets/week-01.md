# 🔴 RS002 Week 1 — English Worksheet

**Topic:** input + Variables — Welcome, Trainer! · **Course:** Pokédex App · **Time:** about 45 minutes

This week your program **asks the user a question** with `input()`, **stores the answer** in a variable, and **prints a welcome screen** with an f-string. This is the very first screen of your Pokédex app — you will build on it for the next 15 weeks.

> Coming from RS001? You used `game.ask()` before. This week we use plain Python `input()`. Same idea — ask, remember, use — but it is the standard Python way.

---

## 1 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

Each block was meant to do something, but it is broken. Read what it is **supposed** to do, rewrite it so it works, then explain why the original was wrong.

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

## 3 · Modify It ✏️

Start from this working intro:

```python
trainer_name = input("트레이너님, 이름을 알려주세요: ")

if trainer_name == "":
    trainer_name = "이름 모를 트레이너"

print(f"\n=== 포켓몬 도감 ===")
print(f"환영합니다, {trainer_name} 트레이너님!")
print(f"오늘도 새로운 포켓몬을 만날 준비가 되셨나요?\n")
```

Make these changes one at a time and run after each:

1. Change the title line so it reads `=== 나만의 포켓몬 도감 ===`.
2. Add one more `print` line that says something friendly to the trainer using their name again.
3. Change the empty-name default to a funny name of your choice.

**Write your three changed lines here:**

<div class="write-space"></div>

---

## 4 · Make It 📸

Open your homework world. Build your own **Pokédex intro screen** from scratch. It should:

- ask the trainer for their name with `input()`,
- give a default name if they type nothing,
- print a welcome screen that uses the name in an f-string.

When it works, send a **photo or video** of your screen on KakaoTalk, then explain what you did. Use these sentence starters — write 4 to 6 sentences.

> First, I used `input()` to …
>
> I stored the answer in a variable called …
>
> My f-string put the name into the message by …
>
> When the user types nothing, my program …
>
> The trickiest part was …
>
> `input()` is different from RS001's `game.ask()` because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone while your program runs. Talk through it like you are teaching someone new. Try to use these words: **input**, **variable**, **f-string**, **default**, **print**.

> 1. Run your program and type your name.
> 2. Read your `input()` line out loud and say what it stores.
> 3. Read your f-string out loud and point to the `{ }` part.
> 4. Run it again, type nothing, and show the default name appear.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
