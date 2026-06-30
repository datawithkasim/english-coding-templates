# 🧩 M002 Extension 4 — Complete the Maze

**Topic:** Add Two AND Conditions · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 60 minutes

This is an **extension challenge** for students who have finished the weekly mazes. The agent already knows **four rules** for following a redstone trail through a 3D maze. But the solver is **not finished** — at two junctions the agent gets stuck because one redstone signal is not enough. Your job is to **add two more rules**, and both of them must be **AND** conditions (two things true at the same time). **You** decide which two signals each junction needs — go look at the maze and figure it out. Then run the solver and get the agent all the way to the goal.

You drive it with **chat commands**: type `l` to turn left, `r` to turn right, `run` to start the solver, and `rl` to teleport the agent back to you.

---

## 1 · Read the Four Rules the Agent Already Knows 🎛️

The solver already has these four rules. Each one checks **one** redstone signal and does **one** action.

```
if agent.detect(REDSTONE, LEFT):
    agent.turn(RIGHT_TURN)
elif agent.detect(REDSTONE, RIGHT):
    agent.turn(LEFT_TURN)
elif agent.detect(REDSTONE, DOWN):
    agent.move(UP, 1)
elif agent.detect(REDSTONE, UP):
    agent.move(DOWN, 1)
```

**Fill in this table from the code above. You will reuse these actions in your own rules later.**

| When the agent sees… | the agent will… |
|---|---|
| redstone on the **left** | |
| redstone on the **right** | |
| redstone **below** (down) | |
| redstone **above** (up) | |

**Notice the trick: redstone on the _left_ makes the agent turn _right_, and redstone _below_ makes it move _up_. In your own words, why might the maze be built this way (signal on one side, action to the other)?**

<div class="write-space"></div>

---

## 2 · Find the Two Stuck Junctions 🔍

At most junctions only **one** redstone signal is on, so one of the four rules fires. But the maze has **two special junctions** where **two** signals are on **at the same time**. There the four rules are not enough — only the first matching one fires, and the agent stops.

**Run the solver with `run`. Watch where it stops. Walk over to that spot and look around the agent. Which redstone signals are on there? Tick all you see, then do the same for the second stuck spot.**

| | left | right | below | above |
|---|---|---|---|---|
| **Junction 1** (first place it stops) | | | | |
| **Junction 2** (second place it stops) | | | | |

**At each stuck junction, only the _first_ matching rule fires and the agent freezes. Look at the words `if` and `elif` — how many of those branches can run on one pass? Why does that leave the second signal unused?**

<div class="write-space"></div>

---

## 3 · AND means BOTH at once 🧠

An **AND** condition is true **only when both** halves are true.

```
if agent.detect(REDSTONE, LEFT) and agent.detect(REDSTONE, DOWN):
    ...
```

**(This is just an example pair — yours may be different.) There is redstone on the left but NOT below. Is this whole condition true? What about redstone below but not on the left?**

<div class="write-space short"></div>

**Look at your table from section 2. For Junction 1, which two signals are both on? Write the AND condition that is true only at that spot.**

<div class="write-space short"></div>

**At that junction the agent must do the action for _each_ signal (use your table from section 1). Write those action lines in the order you think they should happen.**

<div class="write-space"></div>

---

## 4 · Add the Two New Rules 🛠️

Open the **M002 Complete the Maze** world. Find the four rules from section 1 in the code. You will add **two more `elif` branches**, one for each stuck junction, using the signals **you** found.

**Rule for Junction 1** — write the whole branch: the AND condition for the two signals on at that spot, then the action for each signal (from your table in section 1).

```
elif agent.detect(REDSTONE, ______) and agent.detect(REDSTONE, ______):
    agent.________(__________)
    agent.________(__________)
```

<div class="write-space"></div>

**Rule for Junction 2** — write the whole branch yourself, from scratch:

<div class="write-space"></div>

**Both new rules must be checked _before_ the four single-signal rules. Why? What would happen at a stuck junction if one of the plain single-signal rules was checked first?**

<div class="write-space"></div>

---

## 5 · Spot the Bug 🐛

Each block is broken. Read what it should do, rewrite it so it works, then explain the fix. (The signals here are just examples — the idea is the same for whatever pair you chose.)

**Bug A** — This junction rule should fire **only when both** signals are on. Right now it fires when **either** one is there, so it triggers at the wrong spots too.

```
elif agent.detect(REDSTONE, LEFT) or agent.detect(REDSTONE, DOWN):
    agent.turn(RIGHT_TURN)
    agent.move(UP, 1)
```

**Hint:** "this signal **and** that signal" — both must be true together.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — A junction needs **two** actions, but this rule only does one, so the agent solves half the junction and gets stuck again.

```
elif agent.detect(REDSTONE, RIGHT) and agent.detect(REDSTONE, UP):
    agent.turn(LEFT_TURN)
```

**Hint:** each signal in the AND has its own action. How many actions should this branch have?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 6 · Finish the Whole Maze 📸

The goal is to get the agent from the **start to the very end** — past both stuck junctions and every plain turn. Type `run`, watch where it stops, fix your two new rules, and run again until it reaches the goal.

When the agent finishes, come back here. Send a photo or video of the agent at the goal, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The four rules the agent already had each checked …
>
> The agent got stuck at a junction because one redstone signal was not …
>
> The two signals I found at the first stuck junction were … and …
>
> My AND rule was true only when both of those were …
>
> I put my two new rules before the old rules because …
>
> The hardest part of finishing the whole maze was …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 7 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent solves the whole maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **detect**, **redstone**, **AND**, **both**, **condition**, **turn**, **move up**, **move down**.

> 1. Show the maze and point out the redstone signals.
> 2. Type `run` and show the agent following the trail.
> 3. Read one of your AND rules out loud and say which two signals must be true.
> 4. Show the agent passing one of the two stuck junctions.
> 5. Show it reaching the goal at the end.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
