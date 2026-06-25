# 🔴 RS002 Week 3 — English Worksheet

**Topic:** Lists + Indexing — A Menu of Pokémon · **Course:** Pokédex App · **Time:** about 45 minutes

This week you think about how to store **many Pokémon in one list** instead of many separate variables, and how to pull values back out with an **index** (`[0]`, `[1]`, `[2]`). You will read code, find bugs on paper, and explain the code you wrote in your live lesson — remember the first item lives at index `0`, not `1`.

> 🧠 Words to know: **list**, **index**, **zero**, **parallel list**, **menu**

---

## 1 · Recall 🧠

From memory:

**Write the line that asks the trainer's name and stores it (cleaned) in `trainer_name`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen.

```python
starters = ["피카츄", "이상해씨", "파이리"]
print(starters[0])
```

**What gets printed? Which Pokémon is at index `0`?**

<div class="write-space"></div>

```python
starters = ["피카츄", "이상해씨", "파이리"]
print(starters[1])
print(starters[3])
```

**The first `print` is fine. What happens on the second one? Why?**

<div class="write-space"></div>

```python
names = ["피카츄", "이상해씨", "파이리"]
types = ["전기", "풀", "불"]
hp = [35, 45, 39]

print(f"이름: {names[1]}")
print(f"타입: {types[1]}")
print(f"체력: {hp[1]}")
```

**These three lists line up by position. Which Pokémon's info is printed? Write out the three lines it prints.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, then fix it on paper and explain the fix.

**Bug A** — This should print the **first** Pokémon, `피카츄`. Right now it prints the second one.

```python
starters = ["피카츄", "이상해씨", "파이리"]
print(starters[1])
```

**Hint:** the first item is not at index `1`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should print all three starters as a numbered menu. Right now line 3 reaches for an item that does not exist and crashes.

```python
starters = ["피카츄", "이상해씨", "파이리"]
print(f"1. {starters[0]}")
print(f"2. {starters[1]}")
print(f"3. {starters[3]}")
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — These parallel lists should show 피카츄's matching type. Right now name and type do not line up.

```python
names = ["피카츄", "이상해씨", "파이리"]
types = ["전기", "풀", "불"]

print(f"이름: {names[0]}")
print(f"타입: {types[2]}")
```

**Hint:** to keep one Pokémon together, use the **same index** in every list.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

Read this working starter menu carefully.

```python
starters = ["피카츄", "이상해씨", "파이리"]
types = ["전기", "풀", "불"]

print("=== 시작 포켓몬을 골라주세요 ===")
print(f"1. {starters[0]} — {types[0]} 타입")
print(f"2. {starters[1]} — {types[1]} 타입")
print(f"3. {starters[2]} — {types[2]} 타입")
```

**What does the first line do, and why is `starters` better than three separate name variables?**

<div class="write-space"></div>

**`starters[0]` and `types[0]` both use index `0`. Which Pokémon and which type do they give, and why do they match?**

<div class="write-space"></div>

**Line 2 of the menu uses `[1]`. Which Pokémon is that — the first or the second? Explain.**

<div class="write-space"></div>

**If you wrote `starters[3]`, what would happen and why?**

<div class="write-space"></div>

**Why is using the same index in `starters` and `types` important for keeping each Pokémon's info correct?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the code **you** wrote in today's live lesson. Record a short video on your phone (you may show it running) and teach it like the viewer is new. Try to use these words: **list**, **index**, **zero**, **parallel list**, **menu**.

> 1. Show the starter menu code you wrote in the lesson and read your list out loud.
> 2. Explain why `starters[0]` is the first Pokémon, not the second.
> 3. Show how the name and type stay matched by using the same index.
> 4. Say why a list is better than three separate variables.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
