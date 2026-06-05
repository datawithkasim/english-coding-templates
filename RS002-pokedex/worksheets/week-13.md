# 🔴 RS002 Week 13 — English Worksheet

**Topic:** Random Battles — `import random` · **Course:** Pokédex App · **Time:** about 45 minutes

This week your dex becomes a game. You `import random` to pick wild Pokémon out of nowhere, then compare stats with `if` / `elif` / `else` to decide a winner. Run it twice and you get two different battles — that is **randomness**.

---

## 1 · Recall 🧠

From memory:

**Write a function that takes a dictionary `p` and prints its name and attack.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

Read what each block is **supposed** to do, fix it, then explain the fix.

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

## 4 · Modify It ✏️

Start from this working stat battle:

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

Make these changes one at a time and run after each:

1. Print each Pokémon's `attack` as well as its `hp` before the result.
2. Change the score formula to weight attack more (for example `attack * 2 + hp`).
3. Run the program five times and write down how many times you won.

**Write your changed / added lines here, and your win count:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Add a **Battle!** option to your Week 12 menu. When chosen, it picks a random enemy from the dex and battles your Pokémon by comparing stats, printing the winner.

When it works, send a **video** on KakaoTalk showing the **battle run at least three times** so we can see the random results change. Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I imported … so I could …
>
> `random.choice` picked … from my dex.
>
> I decided the winner by comparing …
>
> Running it again gave a different result because …
>
> The trickiest part was …
>
> If I had more time, I would make the battle …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film several battles. Teach it like the viewer is new. Try to use: **import**, **random**, **choice**, **score**, **if / elif / else**.

> 1. Run the battle three times and point out the different match-ups.
> 2. Read your `random.choice` line out loud.
> 3. Explain how the winner is decided from the stats.
> 4. Say why the result changes each run.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
