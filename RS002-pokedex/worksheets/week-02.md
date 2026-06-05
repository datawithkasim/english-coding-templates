# 🔴 RS002 Week 2 — English Worksheet

**Topic:** Trainer Profile — More Variables · **Course:** Pokédex App · **Time:** about 45 minutes

This week you grow last week's intro into a full **trainer card**. You ask for more details — region and favourite type — clean each answer with `.strip()`, give every answer a default, and print a tidy card. Same pattern as Week 1, just repeated for more fields.

---

## 1 · Recall 🧠

From memory — no peeking at Week 1:

**Write the line that asks the user for their name and stores it in `trainer_name`.**

<div class="write-space"></div>

**Write the line that prints `환영합니다, 지우 트레이너님!` using an f-string (the name is in `trainer_name`).**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

Read what each block is **supposed** to do, fix it, then explain the fix.

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

## 4 · Modify It ✏️

Start from this working trainer card:

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

Make these changes one at a time and run after each:

1. Add a friendly closing line that uses both `region` and `trainer_name`.
2. Change the region default to something fun.
3. Add a blank line (`\n`) somewhere to make the card easier to read.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Build your own **trainer card** with **at least four fields** (for example: name, region, favourite type, favourite Pokémon, years of adventuring — your choice). Every field should:

- be cleaned with `.strip()`,
- have a sensible default when the user types nothing.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I asked the trainer for …
>
> I used `.strip()` so that …
>
> For empty answers, my program …
>
> My fourth field was … and I added it by …
>
> The trickiest part was …
>
> If I had more time, I would add …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film your program running. Teach it like the viewer has never seen it. Try to use: **variable**, **strip**, **default**, **field**, **trainer card**.

> 1. Run your program and fill in every field.
> 2. Read one `input(...).strip()` line out loud and say what `.strip()` does.
> 3. Run it again and leave a field blank to show the default.
> 4. Show your finished trainer card on screen.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
