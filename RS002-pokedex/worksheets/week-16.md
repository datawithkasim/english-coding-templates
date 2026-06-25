# 🔴 RS002 Week 16 — English Worksheet

**Topic:** Final Polish + Presentation · **Course:** Pokédex App · **Time:** about 45 minutes

This is the last week. In the live lesson you brought **everything** together — intro, list, search, battle, tournament, two files — into one menu-driven Pokédex app. This worksheet is about **thinking through** that finished app and **explaining** the code you built. Nothing new to learn; just read, predict, debug on paper, and get ready to present.

> 🧠 Words to know: menu loop, function, return, import, two files, demo

---

## 1 · Recall 🧠

From memory:

**Write the two `import` lines a `main.py` needs: one for the random module, one to bring in `pokedex` from `pokemon_data`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think it does.

```python
def main_menu():
    print("1. 도감 보기")
    print("2. 종료")
    return input("선택: ").strip()

choice = main_menu()
print(f"고른 것: {choice}")
```

**`main_menu` both prints **and** returns. The user types `1`. What prints in total?**

<div class="write-space"></div>

```python
while True:
    choice = input("선택: ").strip()
    if choice == "5":
        print("종료합니다")
        break
    else:
        print("계속")
```

**The user types `2`, then `5`. What happens each round?**

<div class="write-space"></div>

```python
pokedex = [{"name": "피카츄"}, {"name": "파이리"}, {"name": "꼬부기"}]
print(f"{len(pokedex)}마리 등록")
```

**What single line prints?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — The menu loop should keep running until `5`. Right now it breaks on **every** choice because `break` is outside the `if`.

```python
while True:
    choice = input("선택: ").strip()
    if choice == "1":
        print("도감 보기")
    break
```

**Hint:** the `break` should only run when the user picks quit.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — `main_menu` should hand the choice back to the loop. Right now it prints the choice but returns nothing, so the loop never sees it.

```python
def main_menu():
    print("1. 도감 보기")
    print("2. 종료")
    choice = input("선택: ").strip()
    print(choice)

c = main_menu()
if c == "2":
    print("종료")
```

**Hint:** `return` the choice.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When the user picks an option that does not exist, the app should say so. Right now unknown input silently loops with no feedback.

```python
while True:
    choice = input("선택: ").strip()
    if choice == "1":
        print("도감 보기")
    elif choice == "5":
        break
```

**Hint:** add an `else` for anything that is not a valid option.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

This is the finished Pokédex app you built in the live lesson (`main.py`, reading data from `pokemon_data.py`). Read it carefully and answer the questions below.

```python
import random
from pokemon_data import pokedex

def main_menu():
    print("\n=== 메인 메뉴 ===")
    print("1. 도감 보기")
    print("2. 검색")
    print("3. 배틀!")
    print("4. 종료")
    return input("선택: ").strip()

def list_pokedex(pokedex):
    for i, p in enumerate(pokedex):
        print(f"  #{i+1} {p['name']}  타입:{p['type']}")

def search_pokedex(pokedex):
    kw = input("검색어: ").strip().lower()
    found = [p for p in pokedex if kw in p["name"].lower()]
    for p in found:
        print(f"  {p['name']} ({p['type']}) — HP:{p['hp']} ATK:{p['attack']}")
    if not found:
        print("  결과 없음")

def quick_battle(pokedex):
    my_p = random.choice(pokedex)
    enemy = random.choice(pokedex)
    print(f"\n{my_p['name']} vs {enemy['name']}")
    if my_p["hp"] + my_p["attack"] > enemy["hp"] + enemy["attack"]:
        print(f"🏆 {my_p['name']} 승리!")
    else:
        print(f"😢 {enemy['name']} 승리...")

trainer = input("트레이너 이름: ").strip() or "이름 모를 트레이너"
print(f"\n환영합니다, {trainer} 트레이너님! ({len(pokedex)}마리 등록)\n")

while True:
    choice = main_menu()
    if choice == "1":
        list_pokedex(pokedex)
    elif choice == "2":
        search_pokedex(pokedex)
    elif choice == "3":
        quick_battle(pokedex)
    elif choice == "4":
        print(f"\n또 만나요, {trainer} 트레이너님!")
        break
    else:
        print("1~4 중에서 골라주세요.")
```

**The `import` line brings `pokedex` from another file. Why is the data kept in `pokemon_data.py` instead of inside `main.py`?**

<div class="write-space"></div>

**`main_menu` ends with `return input(...)`. What does the value it returns become in the loop below?**

<div class="write-space"></div>

**In `search_pokedex`, what does `kw in p["name"].lower()` check, and why are both sides made lowercase?**

<div class="write-space"></div>

**Trace the `while True` loop: what makes it stop, and what would happen if that line were missing?**

<div class="write-space"></div>

**The last `else` runs when the user types something like `9`. Why is it useful to have it there?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Present the **finished Pokédex app you built across this whole course**. Record a video on your phone: show the app **running** from start to finish, then explain the key parts in your own words. Use the words you know.

> First, I run my Pokédex app and show the menu, then I pick …
>
> The function I am most proud of is … because …
>
> I split the code into two files so that …
>
> The hardest problem this term was … and I solved it by …

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your finished-Pokédex presentation video to teacher on KakaoTalk.
