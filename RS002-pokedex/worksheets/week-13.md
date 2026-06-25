# 🔴 RS002 Week 13 — English Worksheet

**Topic:** Random Battles — `import random` · **Course:** Pokédex App · **Time:** about 45 minutes

> 🧠 Words to know: **import**, **random**, **choice**, **score**, **if / elif / else**

This week your dex becomes a game. In your live lesson you used `import random` to pick wild Pokémon out of nowhere, then compared stats with `if` / `elif` / `else` to decide a winner. This worksheet is about reading that code, thinking about what it does, and explaining it in your own words.

---

## 1 · Recall 🧠

From memory:

**Write a function that takes a dictionary `p` and prints its name and attack.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen.

```python
import random

wild = ["꼬렛", "구구", "캐터피"]
print(random.choice(wild))
print(random.choice(wild))
```

**Could the two printed names be different? Could they be the same? Why?**

<div class="write-space"></div>

```python
a = {"name": "피카츄", "attack": 55}
b = {"name": "이상해씨", "attack": 49}

if a["attack"] > b["attack"]:
    print(f"{a['name']} 승리!")
else:
    print(f"{b['name']} 승리!")
```

**Which name is printed? Why?**

<div class="write-space"></div>

```python
import random

dex = [{"name": "피카츄"}, {"name": "파이리"}]
mine = random.choice(dex)
print(mine["name"])
```

**`random.choice` here picks a whole dictionary. What kind of thing is `mine`, and what prints?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, find the problem, then explain the fix on paper.

**Bug A** — This should pick a random Pokémon. Right now `random` was never imported, so it crashes.

```python
dex = ["피카츄", "이상해씨", "파이리"]
print(random.choice(dex))
```

**Hint:** you must bring the tool in before using it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A draw (equal attack) should print `무승부`. Right now equal stats wrongly count as a loss.

```python
a = {"name": "피카츄", "attack": 50}
b = {"name": "파이리", "attack": 50}

if a["attack"] > b["attack"]:
    print(f"{a['name']} 승리!")
else:
    print(f"{b['name']} 승리!")
```

**Hint:** add an `elif` for `<` and an `else` for the tie.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should compare two Pokémon's stats. Right now it compares a Pokémon to its own name string and crashes.

```python
import random
dex = [{"name": "피카츄", "attack": 55}, {"name": "파이리", "attack": 52}]

mine = random.choice(dex)
enemy = random.choice(dex)

if mine["attack"] > enemy:
    print("승리!")
```

**Hint:** compare `enemy["attack"]`, not `enemy` itself.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working stat battle. You do not need to run it — read it and answer.

```python
import random

pokedex = [
    {"name": "피카츄", "hp": 35, "attack": 55},
    {"name": "이상해씨", "hp": 45, "attack": 49},
    {"name": "파이리", "hp": 39, "attack": 52},
]

my_pokemon = random.choice(pokedex)
enemy = random.choice(pokedex)

print(f"\n🥊 {my_pokemon['name']} vs {enemy['name']}")
print(f"   체력: {my_pokemon['hp']} vs {enemy['hp']}")

my_score = my_pokemon["hp"] + my_pokemon["attack"]
enemy_score = enemy["hp"] + enemy["attack"]

if my_score > enemy_score:
    print(f"\n🏆 {my_pokemon['name']}의 승리!")
elif my_score < enemy_score:
    print(f"\n😢 {enemy['name']}에게 졌습니다...")
else:
    print(f"\n⚖️ 무승부!")
```

**What does `random.choice(pokedex)` give back — a name, a number, or a whole dictionary?**

<div class="write-space"></div>

**How is `my_score` calculated? Which two stats are added together?**

<div class="write-space"></div>

**When does the program reach the `elif` line instead of the first `if`?**

<div class="write-space"></div>

**When does the `else` line run, and what does it print?**

<div class="write-space"></div>

**If you ran this program twice, why might you see a different match-up each time?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

In your live lesson you wrote a **Battle!** feature. Now explain *that* code — the one you wrote — in a short phone video. You may show it running. Teach it like the viewer is new, and use these key words: **import**, **random**, **choice**, **score**, **if / elif / else**.

> 1. Run your battle a few times and point out the different match-ups.
> 2. Read your `random.choice` line out loud and say what it picks.
> 3. Explain how your code decides the winner from the stats.
> 4. Say why the result changes each run.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
