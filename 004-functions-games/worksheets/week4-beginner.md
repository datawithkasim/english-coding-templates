# 🎮 M004 Week 4 — English Worksheet (Beginner)

**Topic:** Player Events · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week your code reacts to **you**, the player. An **event** like `on player walk:` runs by itself when the player does something.

---

## 1 · Predict 🔮

```
on player walk:
    if block below is gold:
        say "Treasure room!"
```

**The player walks onto a gold block. Does the message appear? Circle one:** yes · no

**Why? Circle one:** the block below is gold · the block below is stone

```
on player place block:
    say "You built something!"
```

**The player walks around and places nothing. Does the message appear? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

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

**What is wrong? Circle one:** waits for a chat command · runs by itself

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

**What is wrong? Circle one:** wrong event, walk not place · wrong message

---

## 3 · Fill the Gap ✏️

One word is missing.

```
on player ____:
    if block below is gold:
        say "Treasure room!"
```

**Fill the gap. Circle one:** `walk` · `gold` · `say`

---

## 4 · Show Your Work 📸🎥

Now switch to your homework world. Build one trap or one reward that fires with `on player walk:`. When you finish, come back here.

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
