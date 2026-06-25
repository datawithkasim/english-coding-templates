# 🔴 RS002 Week 11 — English Worksheet

**Topic:** Functions — Reusing Code · **Course:** Pokédex App · **Time:** about 45 minutes

This week you think about `def`. A **function** is a named block of code you can run again and again. You pass it **parameters** (the values it works on) and you get back a result with `return`. This worksheet is about reading function code and explaining the code you wrote in your live lesson — no typing in the app.

> 🧠 Words to know: **function**, **def**, **parameter**, **return**, **None**

---

## 1 · Recall 🧠

From memory:

**Write a helper that takes a dictionary `p` and prints `p['name']` and `p['type']`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen.

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

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

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

## 4 · Explain the Code 📖

Read these working functions carefully.

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

**What parameter does `show_pokemon` take, and what does it print?**

<div class="write-space"></div>

**Inside `find_pokemon`, what does the line `return pokemon` do, and when does it run?**

<div class="write-space"></div>

**When does `find_pokemon` reach `return None`?**

<div class="write-space"></div>

**The last block checks `if result != None`. Why does it need to check this before calling `show_pokemon`?**

<div class="write-space"></div>

**Why is it useful that `find_pokemon` returns a value instead of just printing one?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the code **you wrote in today's lesson** in a short phone video. You may show it running. Teach it like the viewer is new, and try to use: **function**, **def**, **parameter**, **return**, **None**.

> 1. Show your `find_pokemon` and read it out loud, pointing to the `return`.
> 2. Run a search that finds a Pokémon, then one that does not.
> 3. Explain the difference between a function that returns and one that just prints.
> 4. Show how calling a function twice saves you from copying code.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
