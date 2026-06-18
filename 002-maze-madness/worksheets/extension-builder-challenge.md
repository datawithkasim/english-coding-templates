# 🏗️ M002 Extension 3 — Build Your Own 6-Maze Challenge

**Topic:** Design a Maze + Write the Solution · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 75 minutes

This is the big **builder challenge** for students who have finished the weekly mazes. This time you are not solving someone else's maze — **you are the maze maker.** You will design one long maze that **stretches through 6 different sections**, wire it with pistons and doors, and then write the **solution code** that drives the agent all the way to the end.

Open the **M002 EXT 3 — Cube World** and build inside it. You drive the agent with **chat commands** just like before: `l` turns left, `r` turns right, `run` starts your solver, and `rl` teleports the agent back to you.

**Your maze must include at least:**

- **2 pistons** (each opens a wall or path when powered)
- **2 doors** (the agent opens them with `agent.interact(...)`)
- **4 AND conditions** in your solution code (`... and ...`)
- **1 OR condition** in your solution code (`... or ...`)

Keep this page beside you while you build — you will check off each part as you go.

---

## 1 · Plan Your 6 Mazes 🗺️

A great maze is **planned before it is built.** Your maze runs through **6 sections** in a row — the agent finishes one and walks straight into the next. Give each section one job.

**Sketch your 6 sections.** For each one, write the section number and what makes it tricky (a turn, a piston, a door, a junction where the agent must check two things).

<div class="write-space tall" style="min-height: 260px"></div>

**Where will your 2 pistons go? Which sections, and what does each piston open?**

<div class="write-space"></div>

**Where will your 2 doors go? What is behind each one?**

<div class="write-space"></div>

---

## 2 · Build the Maze 🧱

Now build it in the world. Walk the path yourself first (no code) and make sure a person can get from start to end. **Check off each part as you place it.**

> ☐ Section 1 built
>
> ☐ Section 2 built
>
> ☐ Section 3 built
>
> ☐ Section 4 built
>
> ☐ Section 5 built
>
> ☐ Section 6 built
>
> ☐ Piston #1 placed and tested
>
> ☐ Piston #2 placed and tested
>
> ☐ Door #1 placed
>
> ☐ Door #2 placed
>
> ☐ A clear START block and a clear GOAL block

**Did anything break while you built it? What did you have to change?**

<div class="write-space"></div>

---

## 3 · Write the Solution 💻

Now write the **solver** — the code that gets the agent through your whole maze. Use a `while True` loop so it checks on every step.

Here is the shape to start from. Fill it in for **your** maze. Remember the rule: your solution needs **at least 4 AND conditions and 1 OR condition.**

```
while True:
    agent.move(FORWARD, 1)

    # a junction — turn only when BOTH things are true (AND)
    if agent.detect(BLOCK, LEFT) and agent.detect(REDSTONE, AHEAD):
        agent.turn(LEFT_TURN)

    # a door OR a piston gate — handle either one (OR)
    elif agent.detect(BLOCK, AHEAD) or agent.detect(REDSTONE, RIGHT):
        agent.interact(AHEAD)
        agent.move(FORWARD, 1)
```

**Write your full solution here.** Add more `if` / `elif` checks until it covers all 6 sections. Mark each AND with `# AND` and your OR with `# OR` in a comment so you can count them.

<div class="write-space tall" style="min-height: 360px"></div>

---

## 4 · Count Your Logic ✅

Go back through the solution you just wrote and **count.** Write the number, then copy out one real line from your code as proof.

**How many AND conditions did you use? (need at least 4)**

<div class="write-space short"></div>

**Copy one of your AND lines here:**

<div class="write-space short"></div>

**How many OR conditions did you use? (need at least 1)**

<div class="write-space short"></div>

**Copy your OR line here:**

<div class="write-space short"></div>

**Why did that one spot need an OR instead of an AND? What two different things is it checking for?**

<div class="write-space"></div>

---

## 5 · Test It and Finish 📸

Type `run` and watch the agent. It will get stuck somewhere — that is normal. Find where it stops, fix that part of your code or your maze, and run it again. Keep going until the agent reaches the **GOAL** all by itself. Use `rl` to send it back to the start between tries.

When the agent finishes your maze on its own, come back here. Send a photo or video of the agent at the goal, then explain what you did. Use these sentence starters — write 5 to 7 sentences total.

> My maze runs through 6 sections. The trickiest section was …
>
> I put my 2 pistons in … because …
>
> The agent opens my doors with `agent.interact(...)`, which works because …
>
> I used an AND condition at … to make the agent …
>
> I needed an OR condition at … because …
>
> The agent kept getting stuck at … until I …
>
> If I built a version 2, I would add …

<div class="write-space tall" style="min-height: 360px"></div>

---

## 6 · Present Your Maze 🎥

You built this maze, so you are the expert. Take a video on your phone (or a parent's phone) and **present your maze like a designer showing off their game.** Try to use these words: **section**, **piston**, **door**, **detect**, **AND**, **OR**, **loop**.

> 1. Show the whole maze from the start and point out the 6 sections.
> 2. Show each piston and each door, and say what it does.
> 3. Read one AND check from your code out loud and say what decision it makes.
> 4. Read your OR check and say why it needed OR.
> 5. Type `run` and let the agent solve your maze to the goal.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 360px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
