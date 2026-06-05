# 🔴 RS002 Week 10 — English Worksheet

**Topic:** Expanding the Dex — Evolution + Region Keys · **Course:** Pokédex App · **Time:** about 45 minutes

This week each Pokémon grows from 4 facts to **7**: you add `evolution`, `region`, and `description` keys. Because you are using dictionaries now, adding facts is easy — no new parallel lists to keep in sync. You also write a helper that prints a full Pokémon card, and filter the dex by region.

---

## 1 · Recall 🧠

From memory:

**Write a single Pokémon as a dictionary with keys `name`, `type`, `hp`, and `attack`, then print its name.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

Read what each block is **supposed** to do, fix it, then explain the fix.

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

## 4 · Modify It ✏️

Start from this working full-card helper:

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

Make these changes one at a time and run after each:

1. Call `show_full` on the **second** Pokémon too.
2. Add a `"weight"` key to both Pokémon and print it inside `show_full`.
3. Loop over the whole dex and call `show_full` on every Pokémon.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Grow your Week 9 dex so every Pokémon has all **seven keys** (`name`, `type`, `hp`, `attack`, `evolution`, `region`, `description`). Have **at least eight Pokémon**. Add a "view by region" feature that lists only the Pokémon from a chosen region.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I added the keys … to every Pokémon.
>
> Adding facts was easy because dictionaries let me …
>
> My region filter worked by …
>
> My `show_full` helper printed …
>
> The trickiest part was …
>
> If I had more time, I would add the key …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film it running. Teach it like the viewer is new. Try to use: **key**, **dictionary**, **filter**, **region**, **KeyError**.

> 1. Show one Pokémon with all seven keys and read them out loud.
> 2. Run the "view by region" feature for one region.
> 3. Explain why adding a key is easier than adding a fifth parallel list.
> 4. Show what happens (or could happen) if one Pokémon is missing a key.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
