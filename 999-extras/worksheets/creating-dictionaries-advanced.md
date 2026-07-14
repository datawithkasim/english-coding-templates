# 📖 Extra — Creating Dictionaries: Advanced

**Topic:** Lists of Dictionaries + Nesting · **Course:** Extra Worksheet · **Time:** about 40 minutes

Real programs hold many records at once — a whole team, not just one hero. You put a **dictionary inside a list**, or even a **dictionary inside a dictionary**. On paper you will read, predict, fix, and explain. Then you will write and run your own code in the IDE.

> Keep these words handy: **list of dictionaries**, **nested**, **.get()**, **KeyError**, **update**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
team = [
    {"name": "Aria", "hp": 100},
    {"name": "Leo", "hp": 80},
]
print(team[1]["name"])
```

**Two steps: first `[1]`, then `["name"]`. What prints?**

<div class="write-space"></div>

```python
player = {
    "name": "Mia",
    "stats": {"hp": 100, "attack": 30},
}
print(player["stats"]["attack"])
```

**This is a dictionary inside a dictionary. What prints?**

<div class="write-space"></div>

```python
player = {"name": "Mia"}
print(player.get("score", 0))
```

**There is no `"score"` key, but this does not crash. What prints, and why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should print **every** member's name. Right now it prints the same one three times.

```python
team = [
    {"name": "Aria"},
    {"name": "Leo"},
    {"name": "Mia"},
]

for member in team:
    print(team[0]["name"])
```

**Hint:** use the loop variable `member`, not `team[0]`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should read the nested attack value. It crashes because it reaches for `"attack"` at the wrong level.

```python
player = {"name": "Mia", "stats": {"hp": 100, "attack": 30}}
print(player["attack"])
```

**Hint:** `"attack"` lives inside `"stats"`, not directly inside `player`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

```python
roster = [
    {"name": "Aria", "role": "healer"},
    {"name": "Leo", "role": "tank"},
]

new_hero = {}
new_hero["name"] = "Mia"
new_hero["role"] = "mage"
roster.append(new_hero)

for hero in roster:
    print(f"{hero['name']} — {hero['role']}")
```

**What is `roster` — and what is each item inside it?**

<div class="write-space"></div>

**How is `new_hero` built before it joins the roster?**

<div class="write-space"></div>

**What does the loop print, and why does it now include Mia?**

<div class="write-space"></div>

---

## 4 · Code It 💻

Open the IDE at **app.english-coding.co.uk** and write your own program.

Build a **list of dictionaries** called `shop`, where each item is a dictionary with a `"name"` key and a `"price"` key. Put three items in it.

Then **loop over** the shop and print each item's name and price on its own line.

Run it, then write your code and what it printed.

<div class="write-space tall" style="min-height: 280px"></div>

---

### Submit ✅

Send this worksheet + a screenshot of your working code to teacher on KakaoTalk.
