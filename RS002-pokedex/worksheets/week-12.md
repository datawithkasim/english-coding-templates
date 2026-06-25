# 🔴 RS002 Week 12 — English Worksheet

**Topic:** Refactor the Whole App into Functions · **Course:** Pokédex App · **Time:** about 45 minutes

This week you think about how a whole app gets tidied up. All those lines written one by one over the last 11 weeks get grouped into **named functions**, and the main code shrinks to a short **menu loop** that just *calls* them. This is called **refactoring** — same behaviour, cleaner shape. On this worksheet you read code, predict it, fix it on paper, and explain the code you wrote in the live lesson.

> 🧠 Words to know: **refactor**, **function**, **menu loop**, **call**, **break**

---

## 1 · Recall 🧠

From memory:

**Write a function `count_dex(pokedex)` that returns how many Pokémon are in the list.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen — just from reading, no running.

```python
def show_menu():
    print("1. 도감 보기")
    print("2. 종료")

show_menu()
choice = input("선택: ").strip()
print(f"고른 메뉴: {choice}")
```

**The user types `1`. What is printed in total?**

<div class="write-space"></div>

```python
while True:
    cmd = input("명령 (q로 종료): ").strip()
    if cmd == "q":
        break
    print(f"입력: {cmd}")
```

**The user types `a`, then `b`, then `q`. What does each round do, and when does it stop?**

<div class="write-space"></div>

```python
trainer = input("이름: ").strip() or "이름 모를 트레이너"
print(trainer)
```

**The user presses Enter without typing. What prints? What does `or` do here?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

**Bug A** — A function must be **defined above** where it is called. Right now `show_menu` is called before it exists, so the program crashes.

```python
show_menu()

def show_menu():
    print("=== 메뉴 ===")
```

**Hint:** move the definition above the call.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This menu loop should keep running until the user picks `3`. Right now it runs once and stops.

```python
choice = input("선택: ").strip()
if choice == "1":
    print("도감 보기")
elif choice == "3":
    print("종료")
```

**Hint:** wrap it in `while True:` and `break` on `3`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When the user types something that is not a menu number, the app should say so. Right now an unknown choice silently does nothing.

```python
while True:
    choice = input("선택: ").strip()
    if choice == "1":
        print("도감 보기")
    elif choice == "2":
        break
```

**Hint:** add an `else` for unknown input.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working function-based app, then answer the questions below.

```python
def show_intro(trainer_name):
    print(f"\n=== 포켓몬 도감 ===")
    print(f"환영합니다, {trainer_name} 트레이너님!\n")

def show_menu():
    print("\n--- 메뉴 ---")
    print("1. 도감 보기")
    print("2. 포켓몬 검색")
    print("3. 종료")

def list_all(pokedex):
    for p in pokedex:
        print(f"  {p['name']}  타입:{p['type']}  HP:{p['hp']}")

def search_pokemon(pokedex):
    keyword = input("검색어: ").strip().lower()
    matches = [p for p in pokedex if keyword in p["name"].lower()]
    if matches:
        for p in matches:
            print(f"  {p['name']} ({p['type']})")
    else:
        print("검색 결과 없음")

pokedex = [
    {"name": "피카츄", "type": "전기", "hp": 35},
    {"name": "이상해씨", "type": "풀", "hp": 45},
]

trainer = input("트레이너 이름: ").strip() or "이름 모를 트레이너"
show_intro(trainer)

while True:
    show_menu()
    choice = input("선택: ").strip()
    if choice == "1":
        list_all(pokedex)
    elif choice == "2":
        search_pokemon(pokedex)
    elif choice == "3":
        print("또 만나요!")
        break
    else:
        print("1~3 중에서 골라주세요.")
```

**What does the `while True:` loop do, and which line stops it?**

<div class="write-space"></div>

**When the user types `1`, which function gets called, and what does it print?**

<div class="write-space"></div>

**Why is each action (intro, menu, list, search) written as its own function instead of all in the loop?**

<div class="write-space"></div>

**`search_pokemon` builds `matches` with a list comprehension. In your own words, what ends up inside `matches`?**

<div class="write-space"></div>

**What happens if the user types `7`, and which line handles that?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

In the live lesson you refactored your Pokédex app into functions. Make a short phone video explaining the code **you** wrote today. You may show it running. Try to use: **refactor**, **function**, **menu loop**, **call**, **break**.

> 1. Run your app and try every menu option, including quit.
> 2. Scroll to your main loop and show how short it is.
> 3. Point to one of your functions and explain what the loop *calls*.
> 4. Say why grouping code into functions made it easier to read and fix.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
