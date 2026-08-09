# 📖 Extra — Nested Data: Searching a Real Pokédex

**Topic:** Nested Dictionaries + Lists of Dictionaries · **Course:** Extra Worksheet · **Time:** about 45 minutes

> Keep these words handy: **nested**, **key**, **index**, **unpack**, **.get()**, **KeyError**

A real Pokédex file is not flat. A name gives you a dictionary. Inside it, `"stats"` gives you another dictionary, and `"moves"` gives you a **list** of dictionaries. Each step down is one more `[ ]`. This worksheet is about reading those steps on paper, then adding one layer to your own app.

This is the shape of the data your app imports:

```python
# pokemon_info.py
pokedex = {
    "bulbasaur": {
        "id": 1,
        "types": ["grass", "poison"],
        "description": "A strange seed was planted on its back at birth.",
        "stats": {"hp": 45, "attack": 49, "defense": 49, "speed": 45},
        "habitat": "grassland",
        "moves": [
            {"name": "tackle", "level_learned": 1},
            {"name": "growl", "level_learned": 1},
            {"name": "leech seed", "level_learned": 7},
            {"name": "vine whip", "level_learned": 13},
            {"name": "poison powder", "level_learned": 20},
            {"name": "razor leaf", "level_learned": 27},
            {"name": "growth", "level_learned": 34},
            {"name": "sleep powder", "level_learned": 41},
            {"name": "solar beam", "level_learned": 48},
        ],
    },
}
```

---

## 1 · Predict 🔮

Read each line. Write what it prints — just from reading.

```python
print(pokedex["bulbasaur"]["habitat"])
```

**One key, then one more key. What prints?**

<div class="write-space"></div>

```python
print(pokedex["bulbasaur"]["types"][0])
```

**`"types"` holds a list. What does `[0]` pick out?**

<div class="write-space"></div>

```python
print(pokedex["bulbasaur"]["moves"][2]["name"])
```

**Three steps: key, index, key. What prints?**

<div class="write-space"></div>

```python
print(len(pokedex["bulbasaur"]["moves"]))
```

**What number prints, and what is it counting?**

<div class="write-space"></div>

```python
for k in pokedex["bulbasaur"].keys():
    print(k)
```

**How many lines print? Write them all.**

<div class="write-space"></div>

---

## 2 · Find the Path 🧭

Write the code that reaches each value. Use the data on page 1.

**The `speed` stat of bulbasaur.**

<div class="write-space"></div>

**The level at which bulbasaur learns `vine whip`.**

<div class="write-space"></div>

**The second type in the `types` list.**

<div class="write-space"></div>

**The name of the last move in the list — without counting the moves yourself.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block should do. Fix it on paper, then explain the fix.

**Bug A** — This should show move number 3. The user types `3`, but the wrong move appears.

```python
number = int(input("which move? "))
print(pokedex["bulbasaur"]["moves"][number]["name"])
```

**Hint:** the user counts from 1. Python counts from 0.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should find bulbasaur. The user types `Bulbasaur ` with a capital letter and a space, and the app says it is not a Pokémon.

```python
search = input("what pokemon? ")
if search not in pokedex:
    print("not a pokemon")
```

**Hint:** clean the text before you search with it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should print the level of the first move. It crashes.

```python
print(pokedex["bulbasaur"]["moves"]["level_learned"])
```

**Hint:** `"moves"` is a list, not a dictionary. Which move do you mean?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug D** — The user types `type` instead of `types`. The app crashes with a `KeyError` instead of saying something helpful.

```python
more_info = input("what info? ")
print(pokedex["bulbasaur"][more_info])
```

**Hint:** `.get(key, default)` returns the default instead of crashing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

This is the search app you built in your lesson. Read it, then answer from reading only.

```python
import pokemon_info

search = input('what pokemon do you like?')

if search not in pokemon_info.pokedex:
    print(f'you searched {search}')
    print("not a pokemon. try again and check your spelling.")
else:
    print(f'you searched {search}')

    for pokemon_key in pokemon_info.pokedex[search].keys():
        print(pokemon_key)

    more_info = input('what piece of info do you want')

    if more_info == 'moves':
        print('you have a lot of moves. what info will you unpack?')
        print(f'The number of things to unpack is ... {len(pokemon_info.pokedex[search][more_info])}')

        moves = int(input('what move do you want to unpack? [1-8]'))

        print(pokemon_info.pokedex[search][more_info][moves-1])

        moves_more_info = input('what are you going to know more about? the levels learned or the name of that move?')

        if moves_more_info == 'name':
            print(pokemon_info.pokedex[search][more_info][moves-1][moves_more_info])
        elif moves_more_info == 'levels learned':
            print(pokemon_info.pokedex[search][more_info][moves-1]['level_learned'])

    else:
        print(pokemon_info.pokedex[search][more_info])
```

**What does the `if search not in pokemon_info.pokedex:` line protect the program from?**

<div class="write-space"></div>

**The `.keys()` loop runs before the second question. Why is that helpful to the user?**

<div class="write-space"></div>

**Explain `moves-1` to someone who has never coded. Why not just `moves`?**

<div class="write-space"></div>

**The prompt says `[1-8]`, but bulbasaur has 9 moves. What can the user never reach?**

<div class="write-space"></div>

**If the user answers `stats`, the last `else` line runs. What exactly appears on the screen?**

<div class="write-space"></div>

**Where in this program could a `KeyError` still happen? Point at the line.**

<div class="write-space"></div>

---

## 5 · Code It 💻

Open your project in the IDE at **app.english-coding.co.uk** and grow `main.py`. Plan it on paper first, then type it.

**1. Clean the search.** Make `Bulbasaur ` and `BULBASAUR` both work.

**2. Number the moves.** Before asking which move, print a numbered list of every move name, so the user can see the real choices instead of guessing `[1-8]`.

**3. No crashes.** If the user asks for a key that does not exist, print a friendly message instead of letting the program die.

**Stretch:** after showing one Pokémon, ask "search again?" and go back to the top instead of ending.

**Write your plan here before you code.**

<div class="write-space tall" style="min-height: 300px"></div>

---

## 6 · Explain Your Code 🎥

Record a short video on your phone explaining the code **you** wrote. Try to use these words: **nested**, **key**, **index**, **unpack**, **.get()**.

> 1. Show `pokemon_info.py` and point at one Pokémon's `moves` list.
> 2. Run your app and search for a Pokémon.
> 3. Walk through how one value travels from the data file to the screen.
> 4. Show the numbered move list and say why it is better than `[1-8]`.

**Plan what you will say here before you record.**

<div class="write-space tall" style="min-height: 300px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
