# 🔴 RS002 Week 16 — English Worksheet

**Topic:** Final Polish + Presentation · **Course:** Pokédex App · **Time:** about 45 minutes

This is the last week. You bring **everything** — intro, list, search, battle, tournament, two files — together into one menu-driven Pokédex app, polish it, and prepare a **5-minute demo** to present to your friends. Nothing new to learn; everything to combine.

---

## 1 · Recall 🧠

From memory:

**Write the two `import` lines a `main.py` needs: one for the random module, one to bring in `pokedex` from `pokemon_data`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

## 4 · Modify It ✏️

Start from this near-final app (`main.py`, using `pokemon_data.py` from last week):

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

Make these changes one at a time and run after each:

1. Add a `5. 토너먼트` option that calls your Week 14 tournament function.
2. Add an ASCII-art logo that prints once when the app starts.
3. Make the goodbye line show how many Pokémon were registered.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Assemble your **final Pokédex app**: a menu loop offering list, search, battle, and tournament, reading data from `pokemon_data.py`. Polish the wording and layout so it feels finished. Then prepare a **5-minute demo**.

When it works, send a **video** on KakaoTalk of the whole app running, **both files**, and your **presentation notes**. Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I combined … into one menu app.
>
> The function I am most proud of is … because …
>
> Splitting into two files helped me …
>
> The hardest problem this term was … and I solved it by …
>
> The feature I would add next is …
>
> Two weeks ago I could not … but now I can …

<div class="write-space tall" style="min-height: 360px"></div>

---

## 6 · Present It 🎤

Prepare a **5-minute demo** for your friends. Use this checklist — tick each before you present:

> ☐ Run the Pokédex app from start to finish once.
> ☐ Explain one or two functions you are most proud of.
> ☐ Explain why splitting into two files helped.
> ☐ Share the hardest problem you hit and how you solved it.

**Write your presentation script here.** You can read from it while presenting and while you record.

<div class="write-space tall" style="min-height: 360px"></div>

---

### Submit ✅

Send your finished app **video**, **both code files**, and your **presentation notes** to teacher on KakaoTalk.
</content>
