# 🔴 RS002 Week 4 — English Worksheet

**Topic:** Parallel Lists + Loops — A Full Pokédex · **Course:** Pokédex App · **Time:** about 45 minutes

This week your three starters grow into a **full Pokédex of 12+ Pokémon** across four parallel lists — name, type, HP, attack. Instead of writing a print line for each one, you use a **`for` loop** to walk through them all by index.

---

## 1 · Recall 🧠

From memory:

**Write a list called `names` holding three Pokémon, then print the second one.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
names = ["피카츄", "이상해씨", "파이리"]
for i in range(len(names)):
    print(names[i])
```

**`len(names)` is 3, so `range(len(names))` gives `0, 1, 2`. What three lines print?**

<div class="write-space"></div>

```python
names = ["피카츄", "이상해씨", "파이리"]
types = ["전기", "풀", "불"]

for i in range(len(names)):
    print(f"{names[i]} — {types[i]}")
```

**The loop uses `i` in both lists. Write out every line it prints.**

<div class="write-space"></div>

```python
names = ["피카츄", "이상해씨", "파이리"]
hp = [35, 45]

for i in range(len(names)):
    print(f"{names[i]}: HP {hp[i]}")
```

**`names` has 3 items but `hp` has only 2. What happens on the last loop? Why?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This should print **every** name in the list. Right now it only ever prints the first one.

```python
names = ["피카츄", "이상해씨", "파이리"]
for i in range(len(names)):
    print(names[0])
```

**Hint:** the loop variable `i` changes each time — use it.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A new Pokémon was added to `names` but not to the other lists. When the loop reaches the new one, the program crashes.

```python
names = ["피카츄", "이상해씨", "파이리", "꼬부기"]
types = ["전기", "풀", "불"]

for i in range(len(names)):
    print(f"{names[i]} — {types[i]}")
```

**Hint:** parallel lists must all be the **same length**.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should number the Pokédex starting at `#1`. Right now the first entry shows `#0`.

```python
names = ["피카츄", "이상해씨", "파이리"]
for i in range(len(names)):
    print(f"#{i}  {names[i]}")
```

**Hint:** the index starts at 0, but humans count from 1.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from this working Pokédex:

```python
names = ["피카츄", "이상해씨", "파이리", "꼬부기"]
types = ["전기", "풀", "불", "물"]
hp = [35, 45, 39, 44]
attack = [55, 49, 52, 48]

print(f"\n=== 도감 ===")
print(f"등록된 포켓몬: {len(names)}마리\n")

for i in range(len(names)):
    print(f"#{i+1}  {names[i]}  타입:{types[i]}  HP:{hp[i]}  공격:{attack[i]}")
```

Make these changes one at a time and run after each:

1. Add one Pokémon — remember to add to **all four lists**.
2. Add the word `마리` after the HP so it reads `HP:35` → `HP:35`. (Try it; see how f-strings let you wrap text around values.)
3. Print only the **name and type** inside the loop, dropping HP and attack.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Build your own **full Pokédex of at least 12 Pokémon** across four parallel lists (name, type, HP, attack). Use a `for` loop to print them all as a numbered list. Show your **trainer name from earlier weeks** at the top.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I made four lists called …
>
> My `for` loop walked through them by …
>
> `len(names)` told me … so the loop ran … times.
>
> To add a new Pokémon I had to …
>
> The trickiest part was …
>
> A loop is better than writing 12 print lines because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film your Pokédex printing. Teach it like the viewer is new. Try to use: **parallel list**, **for loop**, **index**, **len**, **same length**.

> 1. Run your program and show the full numbered Pokédex.
> 2. Read your `for` loop out loud and say what `i` does each time.
> 3. Explain why all four lists must be the same length.
> 4. Add one Pokémon live and show it appear at the bottom.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
