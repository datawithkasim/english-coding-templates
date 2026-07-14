# 📖 Extra — Creating Dictionaries: Add & Update

**Topic:** Building & Changing a Dictionary · **Course:** Extra Worksheet · **Time:** about 35 minutes

You can start with an empty dictionary and fill it later, and you can change a value after you set it. `player["score"] = 10` adds a new key, or updates one that already exists. On paper you will read, predict, fix, and explain. Then you will write and run your own code in the IDE.

> Keep these words handy: **key**, **value**, **add a key**, **update**, **dict[key] = value**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it will print.

```python
player = {"name": "Leo"}
player["score"] = 0
player["score"] = 50
print(player["score"])
```

**What prints? The score was set twice — which value wins?**

<div class="write-space"></div>

```python
pet = {}
pet["kind"] = "dog"
pet["age"] = 4
print(pet)
```

**What does the whole dictionary look like when it prints?**

<div class="write-space"></div>

```python
car = {"color": "red", "speed": 100}
car["speed"] = car["speed"] + 20
print(car["speed"])
```

**What prints? Work out the right side first, then the left.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each snippet is broken. Read what it should do, then rewrite it so it works. Explain why the original was wrong.

**Bug A** — This should add a `"level"` key to the player. Instead it rebuilds the whole dictionary and loses the name.

```python
player = {"name": "Leo"}
player = {"level": 1}
print(player["name"])
```

**Hint:** to add a key, set `player["level"] = 1` — don't make a brand-new dictionary.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should raise the score by `100`. Right now it crashes, because it reads a key that was never created.

```python
game = {"lives": 3}
game["score"] = game["score"] + 100
```

**Hint:** you can't add to a `"score"` that doesn't exist yet. Give it a starting value first.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

```python
profile = {}
profile["username"] = "coder_kim"
profile["wins"] = 0

profile["wins"] = profile["wins"] + 1
profile["wins"] = profile["wins"] + 1

print(f"{profile['username']} has {profile['wins']} wins")
```

**`profile` starts empty. What is inside it after the first two lines?**

<div class="write-space"></div>

**The two `wins` lines look almost the same. What do they do to `wins` each time?**

<div class="write-space"></div>

**What is the final printout, and why is `wins` `2` and not `1`?**

<div class="write-space"></div>

---

## 4 · Code It 💻

Open the IDE at **app.english-coding.co.uk** and write your own program.

Write code that:
- makes an **empty dictionary** called `character`
- adds a `"name"` key and an `"hp"` key with values you choose
- then **updates** `"hp"` to a new value
- prints the character's name and final HP

Run it, then write your code and what it printed.

<div class="write-space tall" style="min-height: 260px"></div>

---

### Submit ✅

Send this worksheet + a screenshot of your working code to teacher on KakaoTalk.
