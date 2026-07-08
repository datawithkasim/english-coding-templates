# 🎮 M004 Week 2 — English Worksheet (Beginner)

**Topic:** Chat Commands · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week you type a word in chat and your code runs. A **chat command** can take a number — `tower 5` builds a 5-block tower.

---

## 1 · Predict 🔮

```
on chat command "bridge":
    repeat 6 times:
        place block
        move forward
```

**You type `bridge`. Does the agent build the bridge? Circle one:** yes · no

**Why? Circle one:** the command name matches · the command name is wrong

```
on chat command "tower" with number n:
    repeat n times:
        place block
        move up
```

**You type `tower 4`. Is the tower 4 blocks tall? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

**Pair A** — Typing `bridge` should run the code. The command **name** must match what you type.

```
# clean
on chat command "bridge":
    repeat 6 times:
        place block
        move forward
```

```
# buggy
on chat command "brige":
    repeat 6 times:
        place block
        move forward
```

**What is wrong? Circle one:** command name misspelled · wrong number

**Pair B** — The number from chat should go **into** the function.

```
# clean
on chat command "tower" with number n:
    build_tower(n)
```

```
# buggy
on chat command "tower" with number n:
    build_tower(3)
```

**What is wrong? Circle one:** uses `3` not `n` · uses `n` not `3`

---

## 3 · Fill the Gap ✏️

One word is missing.

```
on chat command "tower" with number n:
    repeat ____ times:
        place block
        move up
```

**Fill the gap. Circle one:** `n` · `tower` · `chat`

---

## 4 · Show Your Work 📸🎥

Now switch to your homework world. Make one chat command with a number that builds something. When you finish, come back here.

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
