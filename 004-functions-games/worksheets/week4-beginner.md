# 🎮 M004 Week 4 — English Worksheet (Beginner)

**Topic:** Player Events · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week your code reacts to **you**, the player. An **event** like `on player walk:` runs by itself when the player does something — perfect for traps and rewards.

---

## 1 · Predict 🔮

Read the steps. Before you imagine it happening, circle or write your answer.

```
on player walk:
    if block below is gold:
        say "Treasure room!"
```

**The player walks onto a gold block. Does the message appear? Circle one:** yes · no

**Why?**

<div class="write-space short"></div>

```
on player place block:
    say "You built something!"
```

**The player only walks around and places nothing. Does the message appear? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The trap should run **by itself** when the player walks, not wait for a chat command.

```
# clean
on player walk:
    if block below is gold:
        say "Trap!"
```

```
# buggy
on chat command "trap":
    if block below is gold:
        say "Trap!"
```

**What is wrong? When does the buggy trap run?**

<div class="write-space short"></div>

**Pair B** — The message should celebrate **placing a block**, so it needs the right event.

```
# clean
on player place block:
    say "Nice building!"
```

```
# buggy
on player walk:
    say "Nice building!"
```

**What is wrong?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The message should appear when the player walks onto gold. One word is missing. Fill it in using the word bank.

```
on player ____:
    if block below is gold:
        say "Treasure room!"
```

**Word bank:** `walk` · `gold` · `say`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Build one trap or one reward that fires with `on player walk:`. When you finish, come back here.

Send a photo or video of your trigger firing, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> My trigger fires when the player …
>
> When I stepped on …, my code …
>
> One tricky moment was when …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while you walk through your world and set off your trigger. Talk like you are teaching a friend. Try to use these words: **event**, **trigger**, **player**.

> 1. Show your world, then start walking.
> 2. Set off your trigger and read its event line out loud.
> 3. Say in your own words what an **event** is.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
