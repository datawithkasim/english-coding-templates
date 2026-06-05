# 🔴 RS002 Week 9 — English Worksheet

**Topic:** Dictionaries — Real Pokémon Data · **Course:** Pokédex App · **Time:** about 45 minutes

This week you meet the **dictionary** — a way to keep all of one Pokémon's facts together with **named keys** instead of four loose parallel lists. `pikachu["name"]` reads the value behind the key `"name"`. No more lining up indexes!

---

## 1 · Recall 🧠

From memory:

**Write four parallel lists holding the name, type, HP, and attack of two Pokémon, then print the first Pokémon's type.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

**There is no `"attack"` key. What happens when this runs?**

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

## 4 · Modify It ✏️

Start from this working dictionary search:

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

Make these changes one at a time and run after each:

1. Add one more Pokémon dictionary to the list (all four keys).
2. Add an `"id"` key to each Pokémon and print it in the search result.
3. Change the exact-match `==` to a partial match with `in` (so `피카` finds 피카츄).

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Rebuild your Week 4 Pokédex (the four parallel lists) as a **list of dictionaries**. Each Pokémon is one dictionary with keys `name`, `type`, `hp`, `attack`. Keep your search working on the new structure.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I turned each Pokémon into a dictionary with keys …
>
> I read a value using `pokemon[...]` where … is the key.
>
> A dictionary is tidier than parallel lists because …
>
> My search loop now reads …
>
> The trickiest part was …
>
> A `KeyError` happens when …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film it running. Teach it like the viewer is new. Try to use: **dictionary**, **key**, **value**, **KeyError**, **list of dictionaries**.

> 1. Show one Pokémon dictionary and read its keys out loud.
> 2. Run a search and show the matching Pokémon's full info.
> 3. Explain why `pokemon["name"]` is clearer than `names[i]`.
> 4. Mention one `KeyError` you hit (or could hit) and how to avoid it.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
