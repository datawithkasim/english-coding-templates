# 🔴 RS002 Week 11 — English Worksheet

**Topic:** Functions — Reusing Code · **Course:** Pokédex App · **Time:** about 45 minutes

This week you learn `def` properly. A **function** is a named block of code you can run again and again. You pass it **parameters** (the values it works on) and you get back a result with `return`. Functions are how you stop copying and pasting the same lines.

---

## 1 · Recall 🧠

From memory:

**Write a helper that takes a dictionary `p` and prints `p['name']` and `p['type']`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
def greet_trainer(name):
    print(f"안녕하세요, {name} 트레이너님!")

greet_trainer("지우")
greet_trainer("이슬")
```

**What two lines print?**

<div class="write-space"></div>

```python
def add_stats(p):
    return p["hp"] + p["attack"]

pikachu = {"hp": 35, "attack": 55}
total = add_stats(pikachu)
print(total)
```

**`return` hands a value back. What number does `print(total)` show?**

<div class="write-space"></div>

```python
def find(pokedex, target):
    for p in pokedex:
        if p["name"] == target:
            return p
    return None

dex = [{"name": "피카츄"}, {"name": "파이리"}]
print(find(dex, "리자몽"))
```

**`리자몽` is not in the dex. What does the function return, and what prints?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This function should be **called** so the greeting prints. Right now it is only defined, so nothing happens.

```python
def greet_trainer(name):
    print(f"안녕하세요, {name} 트레이너님!")
```

**Hint:** define is not the same as call — add a line that runs it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should **return** the total so the caller can use it. Right now it prints inside and returns nothing, so `total` is `None`.

```python
def add_stats(p):
    print(p["hp"] + p["attack"])

pikachu = {"hp": 35, "attack": 55}
total = add_stats(pikachu)
print(f"총합: {total}")
```

**Hint:** use `return` instead of `print` inside the function.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — `find` should give back `None` when nothing matches, so the caller can react. Right now it returns nothing after the loop and the `if result` check breaks.

```python
def find(pokedex, target):
    for p in pokedex:
        if p["name"] == target:
            return p

dex = [{"name": "피카츄"}]
result = find(dex, "리자몽")
if result != None:
    print("찾음")
else:
    print("못 찾음")
```

**Hint:** add `return None` after the loop.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from these working functions:

```python
def show_pokemon(pokemon):
    print(f"\n=== {pokemon['name']} ===")
    print(f"타입: {pokemon['type']}")
    print(f"체력: {pokemon['hp']}")
    print(f"공격력: {pokemon['attack']}")

def find_pokemon(pokedex, search_name):
    for pokemon in pokedex:
        if pokemon["name"] == search_name:
            return pokemon
    return None

pokedex = [
    {"name": "피카츄", "type": "전기", "hp": 35, "attack": 55},
    {"name": "이상해씨", "type": "풀", "hp": 45, "attack": 49},
]

result = find_pokemon(pokedex, "피카츄")
if result != None:
    show_pokemon(result)
else:
    print("도감에 없습니다.")
```

Make these changes one at a time and run after each:

1. Call `find_pokemon` with a name that is **not** in the dex and watch the `else` branch run.
2. Add a line inside `show_pokemon` that prints a power total (`hp + attack`).
3. Write a tiny new function `count_dex(pokedex)` that **returns** how many Pokémon there are, then print it.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Take your Week 10 app and pull its **two core actions** — showing a Pokémon and searching the dex — into **functions**. `find_pokemon` should `return` the match (or `None`); `show_pokemon` should print one Pokémon's card.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I wrote a function called … that …
>
> I passed it the parameter(s) …
>
> My `find_pokemon` returned … when nothing matched.
>
> A function with `return` is different from one without because …
>
> The trickiest part was …
>
> Functions make my code cleaner because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film it running. Teach it like the viewer is new. Try to use: **function**, **def**, **parameter**, **return**, **None**.

> 1. Run a search that finds a Pokémon, then one that does not.
> 2. Read your `find_pokemon` out loud and point to the `return`.
> 3. Explain the difference between a function that returns and one that just prints.
> 4. Show how calling a function twice saves you from copying code.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
