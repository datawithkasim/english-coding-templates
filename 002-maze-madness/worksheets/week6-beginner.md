# 🔴 M002 Week 6 — Redstone & Levers

**Topic:** Redstone Levers · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 25 minutes

The maze has a **lever**. Flip it and the door opens.

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

**What does the buggy agent hit? Circle one:** the closed door · the lever · the goal

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

**How many times does the buggy agent flip? Circle one:** once · many times · never

---

## 3 · Fill the Gap ✏️

The agent is in front of the lever. One line is missing.

```
____________
move forward
move forward
```

**Missing line? Circle one:** interact ahead · turn right

---

## 4 · Show Your Work 📸🎥

Open your homework world. Walk the agent to the lever. Flip it. Go through the door to the goal.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

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
>
> The most fun part was ______.
>
> Something new I learned was ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
