# 🎮 M004 Week 6 — English Worksheet (Beginner)

**Topic:** A Space that Reacts — Event → Check → Action · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week your world **reacts to the player**: an **event** happens → the code **checks** something → an **action** runs.

---

## 1 · Predict 🔮

```
on player walks on gold block:
    say "Welcome to my world!"
```

**The player walks on grass. Does the message appear? Circle one:** yes · no

**Why? Circle one:** grass is not gold · grass is gold

```
on player walks on red carpet:
    replace block below with air
    say "You fell in my trap!"
```

**The player steps on red carpet. Does the trap fire? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

**Pair A** — The secret message should appear **only** on the gold block.

```
# clean
on player walks on gold block:
    say "You found the secret room!"
```

```
# buggy
on player walks:
    say "You found the secret room!"
```

**What is wrong? Circle one:** fires on every block · fires only on gold

**Pair B** — The trap should fire on **red** carpet, not the safe blue path.

```
# clean
on player walks on red carpet:
    spring_trap()
```

```
# buggy
on player walks on blue carpet:
    spring_trap()
```

**What is wrong? Circle one:** wrong carpet, blue not red · wrong message

---

## 3 · Fill the Gap ✏️

One word is missing.

```
on player walks on ____ block:
    say "You found the secret room!"
```

**Fill the gap. Circle one:** `gold` · `say` · `walk`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Build one spot that reacts when the player walks on it.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Say these out loud, filling in the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
