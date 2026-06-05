# 🔴 RS002 Week 14 — English Worksheet

**Topic:** Best-of-3 Tournament + Type Advantage · **Course:** Pokédex App · **Time:** about 45 minutes

This week one battle becomes a **best-of-3 tournament**. You track wins and losses in a `while` loop, and you add a **type-advantage** bonus using a small dictionary (water beats fire, and so on). Lots of pieces working together — functions, dictionaries, loops, randomness.

---

## 1 · Recall 🧠

From memory:

**Write the line that picks a random Pokémon dictionary from a list called `pokedex` (assume `random` is imported).**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
TYPE_ADVANTAGE = {"물": "불", "불": "풀"}
print(TYPE_ADVANTAGE.get("물"))
print(TYPE_ADVANTAGE.get("전기"))
```

**`.get` returns the value, or `None` if the key is missing. What two lines print?**

<div class="write-space"></div>

```python
wins = 0
losses = 0
while wins < 2 and losses < 2:
    wins = wins + 1
    print(f"{wins}승 {losses}패")
```

**The loop keeps going while BOTH are under 2. Write every line it prints, and say when it stops.**

<div class="write-space"></div>

```python
attacker = {"type": "물"}
defender = {"type": "불"}
TYPE_ADVANTAGE = {"물": "불"}

if TYPE_ADVANTAGE.get(attacker["type"]) == defender["type"]:
    print("효과적!")
else:
    print("보통")
```

**Does `효과적!` print? Walk through the comparison.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This loop should stop once **either** side reaches 2. Right now it stops only when both reach 2, which can loop forever.

```python
wins = 0
losses = 0
while wins < 2 or losses < 2:
    pass  # battle happens here
```

**Hint:** swap `or` for `and`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The advantage check should be safe even when the type is not in the table. Right now an unlisted type crashes with a `KeyError`.

```python
TYPE_ADVANTAGE = {"물": "불", "불": "풀"}
attacker = {"type": "전기"}
defender = {"type": "물"}

if TYPE_ADVANTAGE[attacker["type"]] == defender["type"]:
    print("효과적!")
```

**Hint:** use `.get(...)` instead of `[...]` so a missing key returns `None`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A win should add **one** to `wins`. Right now it resets `wins` to 1 every round, so the trainer can never reach 2.

```python
wins = 0
# round 1 won
wins = 1
# round 2 won
wins = 1
print(f"{wins}승")
```

**Hint:** add to the current value with `wins = wins + 1`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from this working tournament:

```python
import random

TYPE_ADVANTAGE = {"물": "불", "불": "풀", "풀": "전기", "전기": "물"}

def calculate_score(attacker, defender):
    base = attacker["hp"] + attacker["attack"]
    if TYPE_ADVANTAGE.get(attacker["type"]) == defender["type"]:
        base = int(base * 1.2)
        print(f"  ✨ {attacker['name']}의 {attacker['type']} 타입이 효과적입니다!")
    return base

def battle_round(my_p, enemy_p):
    my_score = calculate_score(my_p, enemy_p)
    enemy_score = calculate_score(enemy_p, my_p)
    if my_score > enemy_score:
        return "win"
    elif my_score < enemy_score:
        return "lose"
    else:
        return "draw"

def tournament(my_pokemon, pokedex):
    wins = 0
    losses = 0
    print(f"\n=== 토너먼트 시작! 내 포켓몬: {my_pokemon['name']} ===")
    while wins < 2 and losses < 2:
        enemy = random.choice(pokedex)
        print(f"\n🥊 {my_pokemon['name']} vs {enemy['name']}")
        result = battle_round(my_pokemon, enemy)
        if result == "win":
            wins = wins + 1
            print(f"  → 승리! ({wins}승 {losses}패)")
        elif result == "lose":
            losses = losses + 1
            print(f"  → 패배... ({wins}승 {losses}패)")
        else:
            print("  → 무승부, 재경기!")
    if wins == 2:
        print(f"\n🏆 토너먼트 우승! {my_pokemon['name']} 최강!")
    else:
        print(f"\n😢 토너먼트 패배. 다음 기회에...")

pokedex = [
    {"name": "피카츄", "type": "전기", "hp": 35, "attack": 55},
    {"name": "이상해씨", "type": "풀", "hp": 45, "attack": 49},
    {"name": "꼬부기", "type": "물", "hp": 44, "attack": 48},
    {"name": "파이리", "type": "불", "hp": 39, "attack": 52},
]

tournament(pokedex[0], pokedex)
```

Make these changes one at a time and run after each:

1. Add one more pair to `TYPE_ADVANTAGE`.
2. Change the bonus from `1.2` (20%) to a stronger number and see how it changes results.
3. Make the tournament best-of-5 (first to 3 wins).

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Add a **Tournament** mode to your app: best-of-3 random battles with a type-advantage bonus. Track wins and losses and announce the champion.

When it works, send a **video** on KakaoTalk showing **one full tournament** from start to result. Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I tracked wins and losses with …
>
> My `while` loop kept going while …
>
> I gave a type bonus by checking …
>
> I used `.get` instead of `[...]` so that …
>
> The trickiest part was …
>
> If I had more time, I would add the rule …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film a full tournament. Teach it like the viewer is new. Try to use: **tournament**, **while loop**, **type advantage**, **get**, **best of three**.

> 1. Run one complete tournament and narrate each round.
> 2. Point to the `while wins < 2 and losses < 2` line and explain it.
> 3. Show a round where the type bonus kicks in.
> 4. Explain why `.get` keeps the program from crashing.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
