# 🔴 RS002 Week 3 — English Worksheet

**Topic:** Lists + Indexing — A Menu of Pokémon · **Course:** Pokédex App · **Time:** about 45 minutes

This week you store **many Pokémon in one list** instead of many separate variables. You pull values back out with an **index** (`[0]`, `[1]`, `[2]`), and you learn that the first item lives at index `0`, not `1`.

---

## 1 · Recall 🧠

From memory:

**Write the line that asks the trainer's name and stores it (cleaned) in `trainer_name`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

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

Read what each block is **supposed** to do, fix it, then explain the fix.

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

## 4 · Modify It ✏️

Start from this working starter menu:

```python
starters = ["피카츄", "이상해씨", "파이리"]

print("=== 시작 포켓몬을 골라주세요 ===")
print(f"1. {starters[0]} — 전기 타입")
print(f"2. {starters[1]} — 풀 타입")
print(f"3. {starters[2]} — 불 타입")
```

Make these changes one at a time and run after each:

1. Add a fourth starter (꼬부기, 물 타입) to the list and add its menu line.
2. Change the order of the list and watch the menu numbers follow.
3. Add a `types` list and use `types[0]` instead of writing `전기` by hand.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

In your homework world, show your **Week 2 trainer card first**, then below it a **starter menu of at least three Pokémon** pulled from a list by index. Use a matching `types` list so each line shows the right type.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I made a list called … with …
>
> I pulled each Pokémon out using …
>
> Index `0` gave me … because …
>
> To keep the name and type matched, I …
>
> The trickiest part was …
>
> A list is better than three separate variables because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film your menu running. Teach it like the viewer is new. Try to use: **list**, **index**, **zero**, **parallel list**, **menu**.

> 1. Run your program and show the starter menu.
> 2. Point to your list and read it out loud.
> 3. Explain why `starters[0]` is the first Pokémon, not the second.
> 4. Show how name and type stay matched by using the same index.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
