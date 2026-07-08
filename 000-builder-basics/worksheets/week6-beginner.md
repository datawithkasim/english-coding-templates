# 🪣 M000 Week 6 — English Worksheet (Beginner)

**Topic:** Building a Well · **Course:** Builder Basics · **Level:** Beginner · **Time:** about 30 minutes

---

## 1 · Predict 🔮

Read the steps. Circle your answer.

```
repeat 2 times:
    destroy block down
    move down by 1
```

**Does the agent build up or dig down? Circle one:** build up · dig down

**How deep is the hole? Circle one:** 2 blocks deep · 5 blocks deep · 1 block deep

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
```

**What shape does this make on the ground? Circle one:** line · square · hole

---

## 2 · Find the Difference 🐛

Clean steps first, then a broken version. Circle the bug.

**Pair A** — The agent should dig down 3 blocks. After each `destroy`, it must move down into the hole.

```
# clean
repeat 3 times:
    destroy block down
    move down by 1
```

```
# buggy
repeat 3 times:
    destroy block down
```

**What is wrong? Circle one:** the move down is missing · a destroy is missing · it builds up

**Pair B** — The agent should build the square wall **first**, then dig.

```
# clean
[build square wall]
[dig down]
```

```
# buggy
[dig down]
[build square wall]
```

**What is wrong? Circle one:** it digs before building the wall · it builds two walls · it never digs

---

## 3 · Fill the Gap ✏️

The agent should dig a hole 2 blocks deep. One line is missing.

```
destroy block down
move down by 1
____________
move down by 1
```

**Which line is missing? Circle one:** destroy block down · place block down · move forward

---

## 4 · Show Your Work 📸🎥

Switch to your homework world. Build a **small well** — a square wall on top, and a hole **2 or 3 blocks deep** inside it.

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
