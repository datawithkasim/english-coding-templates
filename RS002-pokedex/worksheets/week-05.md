# 🔴 RS002 Week 5 — English Worksheet

**Topic:** Cleaning Input — `.strip()` and `.lower()` · **Course:** Pokédex App · **Time:** about 45 minutes

This week your Pokédex lets the trainer **search by name**. But people type messily — extra spaces, mixed capitals. You clean their input with `.strip()` and `.lower()` so the search still works, then use `if` / `elif` / `else` to react to the choice.

---

## 1 · Recall 🧠

From memory:

**Write a `for` loop that prints every name in a list called `names`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
choice = "  Pikachu  "
choice = choice.strip()
print(f"[{choice}]")
```

**What prints between the brackets, exactly?**

<div class="write-space"></div>

```python
choice = "PIKACHU"
choice = choice.lower()
print(choice)
```

**What does `.lower()` turn the text into?**

<div class="write-space"></div>

```python
choice = input("이름: ").strip().lower()

if choice == "pikachu":
    print("⚡ 피카츄!")
else:
    print("없는 포켓몬")
```

**The user types `  Pikachu `. Does the `if` match? Why or why not?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This should match even if the user types extra spaces. Right now `"  pikachu"` does not match.

```python
choice = input("이름: ").lower()

if choice == "pikachu":
    print("찾음!")
else:
    print("못 찾음")
```

**Hint:** spaces are still there — clean them too.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should match whether the user types `Pikachu`, `PIKACHU`, or `pikachu`. Right now only the exact lowercase word works.

```python
choice = input("이름: ").strip()

if choice == "pikachu":
    print("찾음!")
else:
    print("못 찾음")
```

**Hint:** make both sides lowercase before comparing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — This should show a different message for each of three Pokémon, and one message for anything else. Right now the last branch runs even for known Pokémon.

```python
choice = input("이름: ").strip().lower()

if choice == "pikachu":
    print("⚡ 피카츄!")
if choice == "bulbasaur":
    print("🌱 이상해씨!")
else:
    print("없는 포켓몬")
```

**Hint:** the second check should be `elif`, not a fresh `if`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from this working search:

```python
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
choice = input("Enter Pokémon name: ").strip().lower()

if choice == "pikachu":
    print("⚡ 피카츄를 골랐어요!")
elif choice == "bulbasaur":
    print("🌱 이상해씨를 골랐어요!")
elif choice == "charmander":
    print("🔥 파이리를 골랐어요!")
else:
    print("그 포켓몬은 도감에 없어요.")
```

Make these changes one at a time and run after each:

1. Add a fourth branch for `squirtle` (꼬부기).
2. Change the `else` message to suggest the trainer try again.
3. Remove the `.lower()` and test typing `PIKACHU` — see what breaks. Then put it back.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Add a **search feature** to your Week 4 Pokédex. The trainer types a name; you clean it with `.strip().lower()`; then you tell them which Pokémon they picked, or that it is not in the dex.

When it works, send a **photo or video** on KakaoTalk, then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I asked the trainer to type …
>
> I cleaned their input with … so that …
>
> `.strip()` handled … and `.lower()` handled …
>
> I used `if` / `elif` / `else` to …
>
> The trickiest part was …
>
> Cleaning input matters because real people type …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film your search running. Teach it like the viewer is new. Try to use: **strip**, **lower**, **clean**, **if / elif / else**, **search**.

> 1. Run your search and type a name with extra spaces and capitals.
> 2. Show it still works, then explain which method fixed the spaces and which fixed the capitals.
> 3. Read your `if / elif / else` out loud.
> 4. Type a Pokémon that is not in the dex and show the `else` message.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
