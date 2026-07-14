# 📖 Extra — Creating Dictionaries: Facts With Names

**Topic:** Making a Dictionary · **Course:** Extra Worksheet · **Time:** about 30 minutes

A list keeps things in a row, and you reach them by number. A **dictionary** keeps facts with **names**, so you reach them by name instead of counting. On paper you will read dictionary code, predict it, fix it, and explain it in your own words.

> Keep these words handy: **dictionary**, **key**, **value**, **{ }**, **key:value pair**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
player = {"name": "Mia", "level": 3}
print(player["name"])
```

**What prints? How does Python know which fact to grab?**

<div class="write-space"></div>

```python
pet = {"kind": "cat", "age": 2, "hungry": True}
print(pet["age"])
print(pet["hungry"])
```

**What two lines print?**

<div class="write-space"></div>

```python
player = {"name": "Mia", "level": 3}
print(player["score"])
```

**There is no `"score"` key. What happens?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should print the player's name. Instead it reads a number, and dictionaries are not read that way.

```python
player = {"name": "Mia", "level": 3}
print(player[0])
```

**Hint:** dictionaries are read by **key name**, not by position number.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should make a dictionary, but it uses the wrong brackets, so it is really a broken list.

```python
player = ["name": "Mia", "level": 3]
```

**Hint:** a dictionary is wrapped in curly braces `{ }`, not square brackets `[ ]`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should hold two facts about a pet, but a colon is missing, so it crashes.

```python
pet = {"kind" "cat", "age": 2}
```

**Hint:** every key needs a `:` between it and its value.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

Read this working dictionary carefully.

```python
hero = {
    "name": "Aria",
    "hp": 100,
    "weapon": "bow",
}

print(f"{hero['name']} has {hero['hp']} HP")
print(f"Weapon: {hero['weapon']}")
```

**What is `hero`? How many key:value pairs does it hold?**

<div class="write-space"></div>

**What does `hero["name"]` read? What about `hero["weapon"]`?**

<div class="write-space"></div>

**Why is `hero["hp"]` clearer than remembering that HP is "the second thing" in a list?**

<div class="write-space"></div>

---

### Submit ✅

Send this worksheet to teacher on KakaoTalk.
