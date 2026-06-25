# 🔴 RS002 Week 4 — English Worksheet

**Topic:** Parallel Lists + Loops — A Full Pokédex · **Course:** Pokédex App · **Time:** about 45 minutes

In the live lesson your three starters grew into a **full Pokédex of 12+ Pokémon** across four parallel lists — name, type, HP, attack. This worksheet is about *thinking through* that code and being able to **explain it in your own words**: how a **`for` loop** walks every Pokémon by index, and why the parallel lists must stay the same length.

> 🧠 Words to know: **parallel list**, **for loop**, **index**, **len**, **same length**

---

## 1 · Recall 🧠

From memory:

**Write a list called `names` holding three Pokémon, then write the line that prints the second one.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen — just from reading, no running.

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

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

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

## 4 · Explain the Code 📖

Read this working Pokédex closely. You do not run it — you read it and answer.

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

**There are four lists. What makes them "parallel" — how do they line up with each other?**

<div class="write-space"></div>

**`len(names)` is 4. What does `range(len(names))` give the loop, and how many times does the loop run?**

<div class="write-space"></div>

**Inside the loop, `i` is used in all four lists at once. On the third time through the loop, what is `i`, and which Pokémon's data gets printed?**

<div class="write-space"></div>

**Why does the line use `#{i+1}` instead of `#{i}`?**

<div class="write-space"></div>

**If you added a 5th Pokémon to `names` but forgot the other three lists, what would break, and on which loop?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the Pokédex code **you wrote in today's live lesson** in a short phone video. You may show it running on screen. Teach it like the viewer is new. Try to use: **parallel list**, **for loop**, **index**, **len**, **same length**.

> 1. Show your full numbered Pokédex on screen.
> 2. Read your `for` loop out loud and say what `i` does each time through.
> 3. Point to your four lists and explain why they must all be the same length.
> 4. Show what changes when one Pokémon is added.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
