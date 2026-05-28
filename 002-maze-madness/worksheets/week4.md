# 🧱 M002 Week 4 — English Worksheet

**Topic:** Midpoint Check — Build a Maze & Solve It · **Course:** Maze Madness · **Time:** about 45 minutes

This is your **midpoint check**. You design a maze yourself, then solve it with the code you learned in Weeks 1–3.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**This is a classic "right-hand wall follower". On an L-shaped maze, does the agent reach the goal? Why or why not?**

<div class="write-space"></div>

```
keep doing forever:
    if no wall ahead:
        move forward
    otherwise if no wall on right:
        turn right
    otherwise:
        turn left
```

**Two things can go wrong with this agent on your own maze. Name one of them.**

<div class="write-space"></div>

```
A maze with:
- 3 corners
- 1 dead end
- 1 path to the goal
```

**Sketch a quick floor plan of how this maze could look. (Draw boxes for walls.)**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — At a dead end (walls on the front AND right AND left), the agent should **turn around** (turn right twice).

```
if wall ahead AND wall on right AND wall on left:
    turn right
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — At a fork, the agent should **prefer going forward** if it can, then right, then left.

```
if no wall on left:
    turn left
otherwise if no wall on right:
    turn right
otherwise:
    move forward
```

**Hint:** the priorities are upside-down.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The agent's loop never stops, even after reaching the goal.

```
keep doing forever:
    if wall ahead:
        turn right
    otherwise:
        move forward
```

**Hint:** swap "keep doing forever" for a while loop that stops at the goal.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. **Design and build your own 2D maze**. It must include:

- at least **3 corners**
- at least **1 dead end**
- a clear **start** and **goal**

Then solve it with your own agent code (while loop + conditions). When you finish, come back here.

Send a photo or video of the agent solving your maze, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I sketched the maze with …
>
> My maze has … corners and … dead ends.
>
> My agent's strategy was …
>
> The agent got stuck when …
>
> I fixed it by …
>
> If I had more time, I would add …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while the agent runs your maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **maze**, **corner**, **dead end**, **strategy**, **stuck**.

> 1. Show the maze from above and point out the start, the goal, and the dead end.
> 2. Run your code and follow the agent through.
> 3. Show one bug you hit and how you fixed it.
> 4. Say what your agent's strategy is in one sentence.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
