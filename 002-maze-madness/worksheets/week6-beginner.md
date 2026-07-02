# 🔴 M002 Week 6 — Redstone & Levers

**Topic:** Redstone Levers · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 25 minutes

The maze has a **lever**. The agent flips it. The door opens.

---

## 1 · Predict 🔮

```
move forward
interact ahead
move forward
```

**Agent flips the lever. The door does what? Circle one:** opens · closes · nothing

```
interact ahead
```

**No lever here. What happens? Circle one:** door opens · nothing

---

## 2 · Find the Difference 🐛

**Pair A** — Flip the lever first. Then walk.

```
# clean
move forward
interact ahead
move forward
```

```
# buggy
move forward
move forward
interact ahead
```

**What does the buggy agent hit?**

<div class="write-space short"></div>

**Pair B** — Walk up to the lever. Flip once.

```
# clean
while no lever ahead:
    move forward
interact ahead
```

```
# buggy
while no lever ahead:
    move forward
    interact ahead
```

**How many times does the buggy agent flip?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent is in front of the lever. One line is missing.

```
____________
move forward
move forward
```

**Word bank:** `interact ahead` · `turn right`

**Write the line:**

<div class="write-space short"></div>

---

## 4 · Finish the Maze 📸

Open your homework world. Walk the agent to the lever. Flip it. Go through the door to the goal.

Send a photo or video of the agent at the end. Then write 2 sentences.

> I used `interact` to …
>
> The door opened, so the agent …

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
