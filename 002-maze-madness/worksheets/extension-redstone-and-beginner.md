# 🧩 M002 Extension 5 — Redstone AND Solver

**Topic:** AND — two redstones both true · **Course:** Maze Madness · **Level:** Extension (Beginner) · **Time:** about 30 minutes

Same **Week 3 world**. Find the **hardest maze**, the big one **your teacher shows a picture of**, packed with redstone. Some tiles have **two** redstones, so the agent needs **both** true: an **AND**. Type `run` to start.

---

## 1 · Chat Words 🎛️

A chat word makes the agent move.

```
type "l":
    turn left
```

**Type `l`. Circle one:** left · right · jump

```
type "rl":
    come back to you
```

**Type `rl`. Circle one:** to goal · back to you

---

## 2 · Both Must Be True 🔗

Rule #1 needs **two** redstones. It runs only when **both** are true.

```
redstone on left AND redstone below:
    move up 1, turn right
```

Redstone on left. Nothing below. **Does it run? Circle one:** yes · no


Redstone on left AND redstone below. **Does it run? Circle one:** yes · no


---

## 3 · Spot the Trick 🐛

Rule #1 needs **both** redstones. This one checks only the left.

```
# clean — needs BOTH
redstone on left AND redstone below:
    move up 1, turn right
```

```
# buggy — only checks left
redstone on left:
    move up 1, turn right
```

The buggy one runs even when there is **no** redstone below. **Why is that wrong? Circle one:** it needs both redstones · it needs no redstone · it turns twice

---

## 4 · Fill the Gap ✏️

Run the rule only when **both** redstones are there. One word is missing.

```
redstone on left ____ redstone below:
    move up 1, turn right
```

**Missing word? Circle one:** AND · IF · OR

---

## 5 · Show Your Work 📸🎥

Open the Week 3 world. Find the maze from the picture. Type `run`. Watch the agent reach the **diamond** goal.

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
