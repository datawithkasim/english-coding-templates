# 🎮 M004 Week 6 — English Worksheet (Beginner)

**Topic:** A Space that Reacts — Event → Check → Action · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week your world **reacts to the player**. The pattern is: an **event** happens (the player walks somewhere) → the code **checks** something → an **action** runs (a message, a door, a trap).

---

## 1 · Predict 🔮

Read the steps. Before you imagine the player doing it, circle or write your answer.

```
on player walks on gold block:
    say "Welcome to my world!"
```

**The player walks on grass. Does the message appear? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
on player walks on red carpet:
    replace block below with air
    say "You fell in my trap!"
```

**Now the player steps on red carpet. Does the trap fire? Circle one:** yes · no

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

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

**What is wrong? Where does the buggy message appear?**

<div class="write-space short"></div>

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

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The message should appear only on the gold block. One word is missing. Fill it in using the word bank.

```
on player walks on ____ block:
    say "You found the secret room!"
```

**Word bank:** `gold` · `say` · `walk`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build one spot that reacts when the player walks on it. When you finish, come back here.

Send a photo or video of your space reacting, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My space reacts when the player …
>
> The action that runs is …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you walk through your reacting space. Talk like you are teaching a friend. Try to use these words: **event**, **check**, **action**.

> 1. Show your space, then walk into the spot that reacts.
> 2. Say which **event** made it happen.
> 3. Say in your own words what event → check → action means.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
