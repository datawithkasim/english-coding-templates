# 🔴 RS002 Week 6 — English Worksheet

**Topic:** Partial-Match Search (KR/EN) — `in` inside a Loop · **Course:** Pokédex App · **Time:** about 45 minutes

This week your search gets smart. Typing just `피카` should still find `피카츄`. You use the `in` keyword to check **partial matches**, loop over the whole dex, and support **both Korean and English** names at once.

---

## 1 · Recall 🧠

From memory:

**Write the line that reads a search word from the user and cleans it with both `.strip()` and `.lower()`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
print("피카" in "피카츄")
print("츄" in "피카츄")
print("리자몽" in "피카츄")
```

**`in` checks if the small text is *inside* the big text. Write `True` or `False` for each line.**

<div class="write-space"></div>

```python
names_kr = ["피카츄", "이상해씨", "파이리"]
search = "이상"

for name in names_kr:
    if search in name:
        print(name)
```

**Which names get printed? Why?**

<div class="write-space"></div>

```python
names_en = ["pikachu", "bulbasaur", "charmander"]
search = "CHAR".lower()

for name in names_en:
    if search in name.lower():
        print(name)
```

**The search is lowered, and each name is lowered before checking. Which name matches?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — This should find any name **containing** the search word. Right now it only matches an **exact** full name.

```python
names = ["피카츄", "이상해씨", "파이리"]
search = input("검색: ").strip()

for name in names:
    if search == name:
        print(name)
```

**Hint:** swap the exact-match check for a partial-match check.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This should match English names no matter the capitals. Typing `CHAR` finds nothing.

```python
names_en = ["pikachu", "bulbasaur", "charmander"]
search = input("search: ").strip()

for name in names_en:
    if search in name:
        print(name)
```

**Hint:** lower **both** the search word and each name before comparing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — When nothing matches, this should tell the user. Right now it prints nothing at all and looks broken.

```python
names = ["피카츄", "이상해씨", "파이리"]
search = input("검색: ").strip().lower()

for name in names:
    if search in name.lower():
        print(name)
```

**Hint:** count matches with a `found_count` variable, and print a message if it stays `0`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from this working bilingual search:

```python
names_kr = ["피카츄", "이상해씨", "파이리", "꼬부기"]
names_en = ["pikachu", "bulbasaur", "charmander", "squirtle"]
types = ["전기", "풀", "불", "물"]
hp = [35, 45, 39, 44]

search = input("\n포켓몬 검색 (한국어/영어, 부분 입력 OK): ").strip().lower()

found_count = 0
for i in range(len(names_kr)):
    if search in names_kr[i] or search in names_en[i].lower():
        print(f"  #{i+1}  {names_kr[i]} ({names_en[i]})  타입:{types[i]}  HP:{hp[i]}")
        found_count = found_count + 1

if found_count == 0:
    print(f"  '{search}' 와 일치하는 포켓몬이 없습니다.")
else:
    print(f"\n총 {found_count}마리 발견!")
```

Make these changes one at a time and run after each:

1. Add one more Pokémon to all four lists and test searching for it in both Korean and English.
2. Make the search also match the **type** (so typing `전기` lists all electric Pokémon).
3. Change the "not found" message to suggest checking the spelling.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Add **partial KR/EN search** to your own Pokédex. Typing part of a name in either language should list every match, with a clear message when nothing matches.

When it works, send a **photo or video** on KakaoTalk showing **three different searches** (a Korean partial, an English partial, and one with no match). Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I kept two parallel name lists for …
>
> The `in` keyword let me match …
>
> I supported both languages by …
>
> I knew nothing matched when …
>
> The trickiest part was …
>
> Partial search is friendlier than exact search because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film your search running. Teach it like the viewer is new. Try to use: **in**, **partial match**, **loop**, **bilingual**, **found count**.

> 1. Search `피카` and show it finds 피카츄.
> 2. Search an English partial and show it works.
> 3. Read the line with `or` out loud and explain why two checks are needed.
> 4. Search something fake and show the "not found" message.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
