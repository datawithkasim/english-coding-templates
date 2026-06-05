# 🔴 RS002 Week 8 — English Worksheet

**Topic:** Validation Everywhere + Logging Bad Input · **Course:** Pokédex App · **Time:** about 45 minutes

This week you apply the validation pattern to **every** input in your app — name, region, search — and you **log** every bad attempt into a list. At the end you print a little session report. You will meet your first **function** here too: a reusable `safe_input`.

---

## 1 · Recall 🧠

From memory:

**Write an `if` that warns and falls back to `"피카츄"` when `choice` is `not in` the list `pokedex`.**

<div class="write-space"></div>

---

## 2 · Predict 🔮

Read each block. Before you run it, write what you think will happen.

```python
invalid_attempts = []
invalid_attempts.append("리자몽")
invalid_attempts.append("타입null")
print(len(invalid_attempts))
print(invalid_attempts)
```

**What two lines print?**

<div class="write-space"></div>

```python
invalid_attempts = ["리자몽", "타입null"]
print(f"잘못 입력: {', '.join(invalid_attempts)}")
```

**`', '.join(...)` glues list items with a comma between them. What prints?**

<div class="write-space"></div>

```python
def safe_input(prompt, default=""):
    answer = input(prompt).strip()
    if answer == "":
        answer = default
    return answer

name = safe_input("이름: ", "이름 모를 트레이너")
print(name)
```

**The user presses Enter. What gets printed? Trace the path through the function.**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Read what each block is **supposed** to do, fix it, then explain the fix.

**Bug A** — Each bad answer should be **added** to the log. Right now it replaces the whole log every time, so only the last one survives.

```python
invalid_attempts = []
invalid_attempts = "리자몽"
invalid_attempts = "타입null"
print(invalid_attempts)
```

**Hint:** use `.append(...)` to add to a list.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — This function should **return** the cleaned answer so the caller can use it. Right now it prints inside and returns nothing.

```python
def safe_input(prompt, default=""):
    answer = input(prompt).strip()
    if answer == "":
        answer = default
    print(answer)

name = safe_input("이름: ", "트레이너")
print(f"환영합니다, {name}!")
```

**Hint:** swap the `print` for a `return`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The report should only list bad attempts **if there were any**. Right now it prints an empty list and a confusing message even when everything was fine.

```python
invalid_attempts = []
print(f"잘못 입력한 내용: {', '.join(invalid_attempts)}")
```

**Hint:** wrap the report in `if invalid_attempts:`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Modify It ✏️

Start from this working safe-input + log:

```python
invalid_attempts = []

def safe_input(prompt, valid_list=None, default=""):
    answer = input(prompt).strip()

    if valid_list and answer not in valid_list:
        invalid_attempts.append(answer)
        print(f"  ⚠️ '{answer}' 은(는) 인식 못해요. 다시 시도하세요.")
        answer = input(prompt).strip()
        if valid_list and answer not in valid_list:
            invalid_attempts.append(answer)
            print(f"  기본값 ({default})으로 진행합니다.")
            answer = default

    if answer == "" and default:
        answer = default

    return answer

pokedex = ["피카츄", "이상해씨", "파이리"]
choice = safe_input("포켓몬 이름: ", pokedex, "피카츄")
print(f"선택: {choice}")

print(f"\n=== 세션 통계 ===")
print(f"잘못된 입력 횟수: {len(invalid_attempts)}")
if invalid_attempts:
    print(f"잘못 입력한 내용: {', '.join(invalid_attempts)}")
```

Make these changes one at a time and run after each:

1. Call `safe_input` a second time for the trainer's **region** (no `valid_list`, just a default).
2. Change the warning emoji or message to your own style.
3. Make the report also print a friendly line when there were **zero** bad attempts.

**Write your changed / added lines here:**

<div class="write-space"></div>

---

## 5 · Make It 📸

Apply `safe_input` to **every** input in your Pokédex (name, region, type, search). Log every bad attempt and print a session report at the end.

When it works, send a **video** on KakaoTalk where you **deliberately type some bad input** so the report has something to show. Then explain what you did. Use these starters — write 4 to 6 sentences.

> First, I wrote a function called `safe_input` that …
>
> I logged bad attempts by …
>
> I used the same function for … different inputs.
>
> My session report showed …
>
> The trickiest part was …
>
> Reusing one function for every input is better than copying code because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Film it running with some bad input on purpose. Try to use: **function**, **safe_input**, **log**, **append**, **report**.

> 1. Run the app and type a few bad answers on purpose.
> 2. Show the warnings appear and the defaults kick in.
> 3. Read your `safe_input` function out loud and explain `return`.
> 4. Show the session report at the end with the logged attempts.

**Plan what you will say here first:**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
</content>
