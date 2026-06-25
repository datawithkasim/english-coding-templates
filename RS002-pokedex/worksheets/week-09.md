# 🔴 RS002 Week 9 — English Worksheet

**Topic:** Dictionaries — Real Pokémon Data · **Course:** Pokédex App · **Time:** about 45 minutes

This week you think about the **dictionary** — a way to keep all of one Pokémon's facts together with **named keys** instead of four loose parallel lists. `pikachu["name"]` reads the value behind the key `"name"`. No more lining up indexes! In this worksheet you read code, debug on paper, and explain the dictionary code you wrote in your live lesson.

> 🧠 Words to know: dictionary, key, value, KeyError, list of dictionaries

---

## 1 · Recall 🧠

From memory:

**Write four parallel lists holding the name, type, HP, and attack of two Pokémon, then print the first Pokémon's type.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think it would print.

```python
pikachu = {"name": "피카츄", "type": "전기", "hp": 35}
print(pikachu["name"])
print(pikachu["hp"])
```

**What two lines print?**

<div class="write-space"></div>

```python
pikachu = {"name": "피카츄", "type": "전기", "hp": 35}
print(pikachu["attack"])
```

**There is no `"attack"` key. What happens with this block?**

<div class="write-space"></div>

```python
pokedex = [
    {"name": "피카츄", "type": "전기"},
    {"name": "이상해씨", "type": "풀"},
]
print(pokedex[1]["name"])
```

**Two steps: first `[1]`, then `["name"]`. What gets printed?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This should print the Pokémon's type. Right now it uses a list index on a dictionary and crashes.

```python
pikachu = {"name": "피카츄", "type": "전기", "hp": 35}
print(pikachu[1])
```

**Hint:** dictionaries are read by **key name**, not by position number.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should print HP, but the key name has a typo, so it crashes with a `KeyError`.

```python
pikachu = {"name": "피카츄", "type": "전기", "hp": 35}
print(pikachu["HP"])
```

**Hint:** keys are case-sensitive — match them exactly.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should print the type of **every** Pokémon in the dex. Right now it prints the same one three times.

```python
pokedex = [
    {"name": "피카츄", "type": "전기"},
    {"name": "이상해씨", "type": "풀"},
    {"name": "파이리", "type": "불"},
]

for pokemon in pokedex:
    print(pokedex[0]["type"])
```

**Hint:** use the loop variable `pokemon`, not `pokedex[0]`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working dictionary search carefully.

```python
pokedex = [
    {"name": "피카츄", "type": "전기", "hp": 35, "attack": 55},
    {"name": "이상해씨", "type": "풀", "hp": 45, "attack": 49},
    {"name": "파이리", "type": "불", "hp": 39, "attack": 52},
]

search = input("어떤 포켓몬을 찾으시나요? ").strip()

found = False
for pokemon in pokedex:
    if pokemon["name"] == search:
        print(f"\n=== {pokemon['name']} ===")
        print(f"타입: {pokemon['type']}")
        print(f"체력: {pokemon['hp']}")
        print(f"공격력: {pokemon['attack']}")
        found = True

if found == False:
    print("도감에서 찾을 수 없습니다.")
```

**What is `pokedex` — and what is each item inside it?**

<div class="write-space"></div>

**The loop variable is `pokemon`. What does `pokemon["name"]` read on each pass?**

<div class="write-space"></div>

**What is the job of the `found` variable, and when does it become `True`?**

<div class="write-space"></div>

**If the user types a name that is not in the dex, which line runs and why?**

<div class="write-space"></div>

**Why is this dictionary version clearer than four parallel lists with `names[i]`, `types[i]`, and so on?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

In your live lesson you wrote dictionary code. Now explain **that** code in a short phone video. You may show it running. Teach it like the viewer is new, and try to use: **dictionary**, **key**, **value**, **KeyError**, **list of dictionaries**.

> 1. Show one Pokémon dictionary from your lesson and read its keys out loud.
> 2. Run your search and show the matching Pokémon's full info.
> 3. Explain why `pokemon["name"]` is clearer than `names[i]`.
> 4. Mention one `KeyError` you hit (or could hit) and how to avoid it.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
