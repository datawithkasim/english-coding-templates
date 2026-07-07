# 🧩 M002 Extension 5 — Redstone AND Solver

**Topic:** AND — two redstones both true · **Course:** Maze Madness · **Level:** Extension (Beginner) · **Time:** about 30 minutes

Same **Week 3 world**. Find the **hardest maze** — the big one **your teacher will show you a picture of**, packed with redstone. The agent reads **redstone**. Some tiles have **two** redstones. Then the agent needs **both** to be true — an **AND**. Type `run` to start it.

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

<div class="write-space short"></div>

Redstone on left AND redstone below. **Does it run? Circle one:** yes · no

<div class="write-space short"></div>

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

The buggy one runs even when there is **no** redstone below. **Why is that wrong?**

<div class="write-space short"></div>

---

## 4 · Fill the Gap ✏️

Run the rule only when **both** redstones are there. One word is missing.

```
redstone on left ____ redstone below:
    move up 1, turn right
```

**Word bank:** `AND` · `IF` · `OR`

**Write it:**

<div class="write-space short"></div>

---

## 5 · Show Me 📸

Open the Week 3 world. Find the maze from the picture. Type `run`. Watch the agent reach the **diamond** goal.

Send a photo OR video of the agent at the goal. Write 2 short lines.

> The agent moved when there were two redstones: left AND …
>
> One tricky tile was …

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
