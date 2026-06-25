# 🔴 RS002 Week 7 — English Worksheet

**Topic:** Validating Input — `in` / `not in` · **Course:** Pokédex App · **Time:** about 45 minutes

This week you think about how a program stays **safe**. When a trainer types a Pokémon that is not in the dex, the program should not crash — it checks with `in` / `not in`, gives a clear message, and falls back to a safe **default**. On this worksheet you read code, predict it, fix bugs on paper, and explain the code you wrote in your live lesson.

> 🧠 Words to know: **in**, **not in**, **validate**, **default**, **safe**

---

## 1 · Recall 🧠

From memory:

**Write a loop that prints every name in `names` that contains the text in `search`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen — no running.

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

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

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

## 4 · Explain the Code 📖

Read this working validation closely.

```python
pokedex = ["피카츄", "이상해씨", "파이리", "꼬부기"]

choice = input("포켓몬 이름: ").strip()

if choice not in pokedex:
    print(f"'{choice}'을(를) 찾을 수 없어 기본 포켓몬으로 진행합니다.")
    choice = "피카츄"

print(f"\n선택된 포켓몬: {choice}")
```

**What does `.strip()` do to the trainer's input, and why does it help the `not in` check?**

<div class="write-space"></div>

**When is the `if` block's code run, and when is it skipped?**

<div class="write-space"></div>

**Why does the line `choice = "피카츄"` sit inside the `if`, and what would change if it were outside?**

<div class="write-space"></div>

**If the trainer types `꼬부기`, what does the last line print? Walk through why.**

<div class="write-space"></div>

**Where does this code make the program "safe", and what bad input is it protecting against?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the validation code **you** wrote in today's live lesson. Record a short phone video — you may show it running. Try to use: **in**, **not in**, **validate**, **default**, **safe**.

> 1. Show your code and type a valid Pokémon to show it works.
> 2. Type something fake and show your warning + default.
> 3. Read your own `not in` line out loud and explain it.
> 4. Say why a program should never crash on bad input.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
