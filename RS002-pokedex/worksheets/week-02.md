# 🔴 RS002 Week 2 — English Worksheet

**Topic:** Trainer Profile — More Variables · **Course:** Pokédex App · **Time:** about 45 minutes

> 🧠 Words to know: **variable**, **strip**, **default**, **field**, **trainer card**

This week you read and think about a full **trainer card**. It asks for more details — region and favourite type — cleans each answer with `.strip()`, gives every answer a default, and prints a tidy card. You will trace the code on paper, fix some bugs in your head, and then explain the code you wrote in the live lesson.

---

## 1 · Recall 🧠

From memory — no peeking at Week 1:

**Write the line that asks the user for their name and stores it in `trainer_name`.**

<div class="write-space"></div>

**Write the line that prints `환영합니다, 지우 트레이너님!` using an f-string (the name is in `trainer_name`).**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen — no need to run it.

```python
region = input("어느 지역에서 오셨나요? ").strip()
print(f"[{region}]")
```

**The user types `  관동  ` (with spaces before and after). What prints between the brackets, exactly?**

<div class="write-space"></div>

```python
fav_type = input("좋아하는 타입은? ").strip()
if fav_type == "":
    fav_type = "비밀"
print(f"선호 타입: {fav_type}")
```

**The user presses Enter without typing. What is printed?**

<div class="write-space"></div>

```python
print(f"이름: {trainer_name}")
print(f"지역: {region}")
print(f"선호 타입: {fav_type}")
```

**Three lines, three variables. Describe what kind of screen this makes.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

**Bug A** — Every answer should have its spaces trimmed. This one forgets `.strip()` on the region.

```python
trainer_name = input("이름: ").strip()
region = input("지역: ")
```

**Hint:** add the same cleaning step you used for the name.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — When the user leaves the type blank, it should become `비밀`. Right now the check happens *after* the card is printed, so it is too late.

```python
fav_type = input("타입: ").strip()
print(f"선호 타입: {fav_type}")

if fav_type == "":
    fav_type = "비밀"
```

**Hint:** set the default *before* you print.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The card should print three different fields. Right now it prints the name three times by mistake.

```python
print(f"이름: {trainer_name}")
print(f"지역: {trainer_name}")
print(f"선호 타입: {trainer_name}")
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Here is a complete, working trainer card. Read it carefully, then answer the questions.

```python
trainer_name = input("트레이너 이름: ").strip()
if trainer_name == "":
    trainer_name = "이름 모를 트레이너"

region = input("어느 지역에서 오셨나요? ").strip()
if region == "":
    region = "이름 모를 지역"

fav_type = input("좋아하는 포켓몬 타입은? ").strip()
if fav_type == "":
    fav_type = "비밀"

print(f"\n=== 트레이너 카드 ===")
print(f"이름: {trainer_name}")
print(f"지역: {region}")
print(f"선호 타입: {fav_type}")
```

**What does `.strip()` do to the user's answer, and why do we add it to every `input(...)` line?**

<div class="write-space"></div>

**Look at the line `if trainer_name == "":`. When is this True, and what does the program do when it is?**

<div class="write-space"></div>

**This card has three fields. Name them, and name the variable that holds each one.**

<div class="write-space"></div>

**The first print line has `\n` in it. What does `\n` do to the trainer card on screen?**

<div class="write-space"></div>

**If the user types nothing for all three questions, what does the finished trainer card show?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

In today's live lesson you wrote your own trainer card. Now explain **the code you wrote** in a short phone video. You may show it running. Teach it like the viewer has never seen it, and use these key words: **variable**, **strip**, **default**, **field**, **trainer card**.

> 1. Show your code and point to one `input(...).strip()` line — say what the **variable** holds and what `.strip()` does.
> 2. Point to one `if ... == "":` block and explain the **default** for that **field**.
> 3. Run your program once and leave a field blank to show the default working.
> 4. Show your finished **trainer card** on screen and read it out.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
