# 🔴 RS002 Week 6 — English Worksheet

**Topic:** Partial-Match Search (KR/EN) — `in` inside a Loop · **Course:** Pokédex App · **Time:** about 45 minutes

> 🧠 Words to know: **in**, **partial match**, **loop**, **bilingual**, **found count**

This week your search gets smart. Typing just `피카` should still find `피카츄`. In the live lesson you wrote code that uses the `in` keyword to check **partial matches**, loops over the whole dex, and supports **both Korean and English** names at once. This worksheet is about reading that code closely and explaining how it works.

---

## 1 · Recall 🧠

From memory:

**Write the line that reads a search word from the user and cleans it with both `.strip()` and `.lower()`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Write what you think will happen — no need to run anything.

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

Read what each block is **supposed** to do, fix it on paper, then explain the fix.

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

## 4 · Explain the Code 📖

Read this working bilingual search carefully. It is the same shape as the code you wrote in the live lesson.

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

**The four lists `names_kr`, `names_en`, `types`, and `hp` are kept in the same order. Why does index `i` give you one full Pokémon across all four lists?**

<div class="write-space"></div>

**The `if` line uses `or` with two `in` checks. In plain English, when is this `if` line `True`?**

<div class="write-space"></div>

**Why is `.lower()` used on both `search` and `names_en[i]`, but not on `names_kr[i]`?**

<div class="write-space"></div>

**What does `found_count` do, and how does the code use it to decide which final message to print?**

<div class="write-space"></div>

**Why does partial-match search (`in`) feel friendlier to the user than exact-match search (`==`)?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

Explain the code **you wrote in today's lesson**. Film a short video on your phone where you walk through your own bilingual search (you may show it running). Teach it like the viewer is new. Try to use: **in**, **partial match**, **loop**, **bilingual**, **found count**.

> 1. Show your two parallel name lists and say why they stay in the same order.
> 2. Read your `if` line with `or` out loud and explain why two checks are needed.
> 3. Search `피카`, then an English partial, and show both find a match.
> 4. Search something fake and show how `found_count` triggers the "not found" message.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your lesson code to teacher on KakaoTalk.
