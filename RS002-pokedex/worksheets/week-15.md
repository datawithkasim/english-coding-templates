# 🔴 RS002 Week 15 — English Worksheet

**Topic:** Multiple Files — `import` Your Own Data · **Course:** Pokédex App · **Time:** about 45 minutes

> 🧠 Words to know: **import**, **module**, **from import**, **data file**, **main file**

This week your project grows into **two files**. The Pokémon data lives in `pokemon_data.py`, and your game lives in `main.py`, which pulls the data in with `from pokemon_data import pokedex`. This worksheet is all about **reading and thinking about** that code — and then **explaining** the code you wrote in your lesson. Splitting files is how real programs stay organised.

---

## 1 · Recall 🧠

From memory:

**Write a function `battle(p1, p2)` that returns whichever Pokémon has the higher `hp + attack` (return `None` on a tie).**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen — just from reading.

Two files:

```python
# pokemon_data.py
pokedex = [
    {"name": "피카츄", "type": "전기"},
    {"name": "파이리", "type": "불"},
]
```

```python
# main.py
from pokemon_data import pokedex
print(len(pokedex))
print(pokedex[0]["name"])
```

**When `main.py` runs, what two lines print?**

<div class="write-space"></div>

```python
# main.py
import random
from pokemon_data import pokedex

print(random.choice(pokedex)["name"])
```

**Both `import` styles appear here. What does this line print? Could it change each run?**

<div class="write-space"></div>

```python
# main.py
from pokemon_data import pokedex
print(pokemon_data)
```

**`from ... import pokedex` only brings in `pokedex`. What happens on the `print` line?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

**Bug A** — `main.py` should pull in the dex from the data file. Right now nothing is imported, so `pokedex` does not exist.

```python
# main.py
print(len(pokedex))
```

**Hint:** add a `from pokemon_data import pokedex` line at the top.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The data lives in `pokemon_data.py`, but this import names the wrong file.

```python
# main.py
from pokemon import pokedex
print(pokedex[0]["name"])
```

**Hint:** the module name must match the file name (without `.py`).

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `random.choice` is used but only the data is imported. The program crashes on `random`.

```python
# main.py
from pokemon_data import pokedex
print(random.choice(pokedex)["name"])
```

**Hint:** `random` is a separate module — import it too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working two-file Pokédex app. Then answer the questions below — just from reading.

```python
# pokemon_data.py — data only
pokedex = [
    {"name": "피카츄", "type": "전기", "hp": 35, "attack": 55},
    {"name": "이상해씨", "type": "풀", "hp": 45, "attack": 49},
    {"name": "파이리", "type": "불", "hp": 39, "attack": 52},
    {"name": "꼬부기", "type": "물", "hp": 44, "attack": 48},
]
```

```python
# main.py — the game
import random
from pokemon_data import pokedex

def show_pokemon(p):
    print(f"{p['name']} ({p['type']}) — HP {p['hp']}, ATK {p['attack']}")

def battle(p1, p2):
    score1 = p1["hp"] + p1["attack"]
    score2 = p2["hp"] + p2["attack"]
    if score1 > score2:
        return p1
    elif score2 > score1:
        return p2
    return None

trainer = input("트레이너 이름: ").strip() or "이름 모를 트레이너"
print(f"\n환영합니다, {trainer} 트레이너님!")

print("\n=== 포켓몬 도감 ===")
for i, p in enumerate(pokedex):
    print(f"{i+1}. {p['name']}")

choice = input("\n원하는 포켓몬 이름: ").strip()
my_pokemon = None
for p in pokedex:
    if p["name"] == choice:
        my_pokemon = p
        break

if my_pokemon == None:
    print("도감에 없는 포켓몬이어서 피카츄로 시작합니다.")
    my_pokemon = pokedex[0]

enemy = random.choice(pokedex)
print(f"\n🥊 배틀 시작!")
show_pokemon(my_pokemon)
print("   vs")
show_pokemon(enemy)

winner = battle(my_pokemon, enemy)
if winner == my_pokemon:
    print(f"\n🏆 {trainer} 트레이너님의 승리!")
elif winner == enemy:
    print(f"\n😢 졌습니다... 다시 도전해보세요!")
else:
    print(f"\n⚖️ 무승부!")
```

**The line `from pokemon_data import pokedex` is in `main.py`. Where does `pokedex` actually come from, and why can `main.py` use it?**

<div class="write-space"></div>

**Why does this program need `import random` as well as the `from ... import` line? What would break without it?**

<div class="write-space"></div>

**What does `enemy = random.choice(pokedex)` do, and why might the enemy be different each time you run the program?**

<div class="write-space"></div>

**Look at the loop that sets `my_pokemon`. What happens if the trainer types a name that is not in the dex?**

<div class="write-space"></div>

**If you added a new Pokémon to `pokemon_data.py` only, would it show up in `main.py`? Explain why.**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Today in your lesson you split your app into two files: `pokemon_data.py` and `main.py`. Now **explain the code you wrote**. Record a short video on your phone. You can show it running. Try to use these words: **import**, **module**, **from import**, **data file**, **main file**.

> 1. Show `pokemon_data.py` and read out your `pokedex`.
> 2. Show the `import` line in `main.py` and explain what it brings in.
> 3. Run `main.py` and walk through one battle, saying what each part does.
> 4. Explain why splitting the data file and the main file is helpful.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
