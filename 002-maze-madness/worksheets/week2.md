# 🌀 M002 Week 2 — English Worksheet

**Topic:** Turning at Walls · **Course:** Maze Madness · **Time:** about 45 minutes

This week your agent follows one simple rule: if there's a wall in front, turn; if not, move forward.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
if wall ahead:
    turn right
otherwise:
    move forward
```

**What does the agent do if there's a wall in front? What if the path is clear?**

<div class="write-space"></div>

```
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**What is the agent doing in plain English?**

<div class="write-space"></div>

```
direction = "right"

if direction is "left":
    turn left
otherwise if direction is "right":
    turn right
otherwise:
    move forward
```

**What does the agent do? What would change if `direction` was set to `"back"`?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and explain the bug in one short sentence.

**Pair A**

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

**What is wrong?**

<div class="write-space"></div>

**Pair B**

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

**What is wrong?**

<div class="write-space"></div>

**Pair C**

```
# clean
if direction is "left":
    turn left
otherwise if direction is "right":
    turn right
otherwise:
    move forward
```

```
# buggy
if direction is "left":
    turn right
otherwise if direction is "right":
    turn left
otherwise:
    move forward
```

**What is wrong?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Get your agent through this week's maze using `if` / `otherwise`. When you finish, come back here.

Send a photo or video of your agent solving the maze, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I read the maze and noticed …
>
> I chose `if` / `otherwise` because …
>
> The condition I checked was …
>
> My agent got stuck when …
>
> I fixed it by …
>
> Next time, I want to try …

<div class="write-space tall"></div>

---

### Submit ✅

Send this worksheet + a photo or video of your agent solving the maze to teacher on KakaoTalk.
