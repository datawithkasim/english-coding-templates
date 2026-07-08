# 🎮 M004 Week 3 — English Worksheet (Beginner)

**Topic:** Sensing the World · **Course:** Functions & Games · **Level:** Beginner · **Time:** about 30 minutes

This week your agent **senses** the world before it acts. It can detect a block **ahead** and check what is **below**.

---

## 1 · Predict 🔮

```
if agent detects block ahead:
    turn left
otherwise:
    move forward
```

**A wall is right in front of the agent. Does it turn left? Circle one:** yes · no

**Why? Circle one:** it detects the block ahead · the path is open

```
if block below is lava:
    place block below
move forward
```

**The agent is standing over lava. Does it place a safe block before moving? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

**Pair A** — The lava is **below** the agent, so the check should look below.

```
# clean
if block below is lava:
    place block below
```

```
# buggy
if agent detects block ahead:
    place block below
```

**What is wrong? Circle one:** looks ahead not below · looks below not ahead

**Pair B** — On safe ground the agent should still **move**. It needs an `otherwise`.

```
# clean
if block below is lava:
    place block below
otherwise:
    move forward
```

```
# buggy
if block below is lava:
    place block below
```

**What is wrong? Circle one:** no `otherwise` to move · no `if` check

---

## 3 · Fill the Gap ✏️

One word is missing.

```
if block ____ is lava:
    place block below
otherwise:
    move forward
```

**Fill the gap. Circle one:** `below` · `ahead` · `repeat`

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Send your agent across the danger field using an `if block below is …` check.

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
