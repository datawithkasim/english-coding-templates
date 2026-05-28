# 🎚️ M002 Week 7 — English Worksheet

**Topic:** Multi-Lever Puzzles · **Course:** Maze Madness · **Time:** about 45 minutes

This week the maze has **multiple levers** that must be flipped in the right order. You will also wrap your "move and flip" pattern into a **function** to keep the code clean.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
function flip_next_lever:
    while no lever ahead:
        move forward
    interact ahead

flip_next_lever
flip_next_lever
flip_next_lever
```

**How many levers does the agent flip? Why use a function?**

<div class="write-space"></div>

```
function flip_next_lever:
    while no lever ahead:
        move forward
    interact ahead

flip_next_lever
turn right
flip_next_lever
```

**Between the two function calls, the agent **turns right**. Why might that matter?**

<div class="write-space"></div>

```
flip lever B
flip lever A
```

**The maze needs lever A flipped FIRST, then lever B. What happens with this order?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to flip **3 levers** in a row. The code repeats the same pattern 3 times — turn that into a function.

```
while no lever ahead:
    move forward
interact ahead

while no lever ahead:
    move forward
interact ahead

while no lever ahead:
    move forward
interact ahead
```

**Write the fixed code using a function:**

<div class="write-space"></div>

**Why is the function version better?**

<div class="write-space"></div>

**Bug B** — Lever **A must be flipped before lever B**, otherwise the door stays closed.

```
flip_next_lever   # lever B
turn right
flip_next_lever   # lever A
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The function should **only flip a lever** — not turn or move after. Right now the function does too much.

```
function flip_next_lever:
    while no lever ahead:
        move forward
    interact ahead
    turn right
    move forward
```

**Hint:** keep the function small. Move the turn and the extra move outside.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. The maze has **multiple levers** that must be flipped in the correct order. Use **at least one function** in your solution. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I planned the order of levers as …
>
> My function `…` does …
>
> I called the function … times.
>
> The order mattered because …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **lever**, **function**, **call**, **order**, **interact**.

> 1. Show all the levers in the maze and say the order to flip them.
> 2. Run your code and follow the agent through.
> 3. Read your function and the calls out loud and say what each one does.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
