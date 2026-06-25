# 🔴 RS002 Week 10 — English Worksheet

**Topic:** Expanding the Dex — Evolution + Region Keys · **Course:** Pokédex App · **Time:** about 45 minutes

This week is about **reading and explaining** the code that grows each Pokémon from 4 facts to **7** — adding the `evolution`, `region`, and `description` keys. You will think through how dictionaries make adding facts easy, trace a full-card helper, and explain the code you wrote in your live lesson out loud.

> 🧠 Words to know: **key**, **dictionary**, **filter**, **region**, **KeyError**

---

## 1 · Recall 🧠

From memory:

**Write a single Pokémon as a dictionary with keys `name`, `type`, `hp`, and `attack`, then print its name.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen.

```python
pikachu = {"name": "피카츄", "region": "관동", "evolution": "라이츄"}
print(f"{pikachu['name']} → {pikachu['evolution']} ({pikachu['region']})")
```

**What single line prints?**

<div class="write-space"></div>

```python
pokedex = [
    {"name": "피카츄", "region": "관동"},
    {"name": "롱스톤", "region": "성도"},
    {"name": "꼬부기", "region": "관동"},
]

for p in pokedex:
    if p["region"] == "관동":
        print(p["name"])
```

**Which names print? Why?**

<div class="write-space"></div>

```python
def show(p):
    print(f"=== {p['name']} ===")
    print(f"타입: {p['type']}")

show({"name": "파이리", "type": "불"})
```

**The function takes a dictionary `p`. What does it print?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

**Bug A** — Every Pokémon should have the same keys. This one is missing `region`, so the loop crashes when it reaches it.

```python
pokedex = [
    {"name": "피카츄", "region": "관동"},
    {"name": "이상해씨"},
]

for p in pokedex:
    print(f"{p['name']} — {p['region']}")
```

**Hint:** add the missing key to the second Pokémon.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This filter should show only 관동 Pokémon. Right now it shows all of them.

```python
pokedex = [
    {"name": "피카츄", "region": "관동"},
    {"name": "롱스톤", "region": "성도"},
]

for p in pokedex:
    print(p["name"])
```

**Hint:** add an `if` that checks the region before printing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The card function should print the `description`. The key is spelled wrong, causing a `KeyError`.

```python
def show(p):
    print(f"=== {p['name']} ===")
    print(f"설명: {p['describe']}")

show({"name": "피카츄", "description": "전기 쥐 포켓몬"})
```

**Hint:** the key in the data is `description`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working full-card helper carefully.

```python
pokedex = [
    {
        "name": "피카츄", "type": "전기", "hp": 35, "attack": 55,
        "evolution": "라이츄", "region": "관동",
        "description": "전기를 모으는 쥐 포켓몬. 볼이 빨개지면 위험!"
    },
    {
        "name": "이상해씨", "type": "풀", "hp": 45, "attack": 49,
        "evolution": "이상해풀", "region": "관동",
        "description": "등에 식물 씨앗을 지고 다닙니다."
    },
]

def show_full(pokemon):
    print(f"\n=== {pokemon['name']} ({pokemon['region']}) ===")
    print(f"타입: {pokemon['type']}  |  진화: {pokemon['evolution']}")
    print(f"체력: {pokemon['hp']}  |  공격력: {pokemon['attack']}")
    print(f"설명: {pokemon['description']}")
    print("=" * 40)

show_full(pokedex[0])
```

**How many keys does each Pokémon dictionary have? Name them.**

<div class="write-space"></div>

**The function uses `pokemon['region']`. What is `region` here — a key or a value?**

<div class="write-space"></div>

**`show_full(pokedex[0])` runs once. Which Pokémon's card prints, and why that one?**

<div class="write-space"></div>

**If a Pokémon was missing the `evolution` key, which line would crash, and what error would Python give?**

<div class="write-space"></div>

**Why is adding a new fact (like `weight`) to every Pokémon easier with dictionaries than with separate parallel lists?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the code **you wrote in today's lesson** in a short phone video. You may show it running. Teach it like the viewer is new, and use these words: **key**, **dictionary**, **filter**, **region**, **KeyError**.

> 1. Show one Pokémon from your dex with all seven keys and read them out loud.
> 2. Run your "view by region" feature for one region and explain how the filter chooses which Pokémon to show.
> 3. Explain why adding a key is easier than adding a fifth parallel list.
> 4. Show what happens (or could happen) if one Pokémon is missing a key.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
