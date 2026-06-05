# 🔴 RS002 Week 7 — English Worksheet

**Topic:** Validating Input — `in` / `not in` · **Course:** Pokédex App · **Time:** about 45 minutes

This week you make your program **safe**. When the trainer types a Pokémon that is not in the dex, you do not crash — you check with `in` / `not in`, give them a clear message, and fall back to a safe **default**.

---

## 1 · Recall 🧠

From memory:

**Write a loop that prints every name in `names` that contains the text in `search`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
pokedex = ["피카츄", "이상해씨", "파이리"]
print("피카츄" in pokedex)
print("리자몽" in pokedex)
```

**Write `True` or `False` for each line.**

<div class="write-space"></div>

```python
pokedex = ["피카츄", "이상해씨", "파이리"]
choice = "리자몽"

if choice not in pokedex:
    print("도감에 없어요")
```

**Does the message print? Why?**

<div class="write-space"></div>

```python
pokedex = ["피카츄", "이상해씨"]
choice = input("이름: ").strip()

if choice not in pokedex:
    choice = "피카츄"

print(f"선택: {choice}")
```

**The user types `없는포켓몬`. What does the last line print? Why?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This should warn the user when their choice is **not** in the dex. Right now it warns when the choice **is** in the dex.

```python
pokedex = ["피카츄", "이상해씨", "파이리"]
choice = input("이름: ").strip()

if choice in pokedex:
    print("도감에 없어요")
```

**Hint:** the condition is backwards.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — When the choice is missing, this should fall back to a default Pokémon. Right now it sets the default but then the rest of the program still uses the bad choice.

```python
pokedex = ["피카츄", "이상해씨", "파이리"]
choice = input("이름: ").strip()

if choice not in pokedex:
    print("기본값으로 진행합니다.")
    default = "피카츄"

print(f"선택된 포켓몬: {choice}")
```

**Hint:** assign the default back into `choice`, not a new unused variable.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should give the user a second chance, then fall back. Right now it never re-asks; it just keeps the first bad answer.

```python
pokedex = ["피카츄", "이상해씨", "파이리"]
choice = input("이름: ").strip()

if choice not in pokedex:
    print("다시 시도해보세요.")

if choice in pokedex:
    print(f"✅ {choice}")
else:
    print("❌ 못 찾음")
```

**Hint:** after the warning, ask again with another `input(...)`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from this working validation:

```python
pokedex = ["피카츄", "이상해씨", "파이리", "꼬부기"]

choice = input("포켓몬 이름: ").strip()

if choice not in pokedex:
    print(f"'{choice}'을(를) 찾을 수 없어 기본 포켓몬으로 진행합니다.")
    choice = "피카츄"

print(f"\n선택된 포켓몬: {choice}")
```

Make these changes one at a time and run after each:

1. Add a second chance: after the warning, re-ask once before falling back.
2. Change the default Pokémon to a different one in your dex.
3. Add a friendly success line when the choice **is** valid the first time.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Add **validation** to your Week 6 search. If the trainer's choice is not in the dex, warn them and fall back to a safe default. The program should never crash, no matter what they type.

When it works, send a **photo or video** on KakaoTalk showing both a **valid** choice and an **invalid** one. Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I checked the choice with `not in` so that …
>
> When the Pokémon was missing, my program …
>
> My safe default was … because …
>
> I tested it by typing …
>
> The trickiest part was …
>
> Validating input matters because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film your validation running. Teach it like the viewer is new. Try to use: **in**, **not in**, **validate**, **default**, **safe**.

> 1. Type a valid Pokémon and show it works.
> 2. Type something fake and show the warning + default.
> 3. Read your `not in` line out loud and explain it.
> 4. Say why a program should never crash on bad input.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
