# 🌀 M002 Week 2 — English Worksheet (Beginner)

**Topic:** Turning at Walls · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 30 minutes

This week your agent follows one simple rule: **if** there's a wall in front, turn; **otherwise**, move forward.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
if wall ahead:
    turn right
otherwise:
    move forward
```

**There is a wall in front of the agent. What does it do? Circle one:** turn right · move forward · nothing

**What does it do if the path is clear?**

<div class="write-space short"></div>

```
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**In plain English, what is the agent doing over and over?**

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should turn when there is a **wall** ahead.

```
# clean
if wall ahead:
    turn right
otherwise:
    move forward
```

```
# buggy
if path is clear:
    turn right
otherwise:
    move forward
```

**What is wrong? When does the buggy agent turn?**

<div class="write-space short"></div>

**Pair B** — Turning and moving should be in **different** branches — one or the other, not both.

```
# clean
if wall ahead:
    turn right
otherwise:
    move forward
```

```
# buggy
if wall ahead:
    turn right
    move forward
```

**What is wrong? What does the buggy agent do right after turning?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should move forward when there is **no** wall. One word is missing. Fill it in using the word bank.

```
if wall ahead:
    turn right
____________:
    move forward
```

**Word bank:** `otherwise` · `repeat` · `while`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. Get your agent through this week's maze using `if` / `otherwise`. When you finish, come back here.

Send a photo or video of your agent solving the maze, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> The condition I checked was …
>
> My agent got stuck when …
>
> I fixed it by …

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + a photo or video of your agent solving the maze to teacher on KakaoTalk.
