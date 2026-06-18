# 🏗️ M002 Extension 3 — Build Your Own Maze (Beginner)

**Topic:** Make a Maze + Write the Solution · **Course:** Maze Madness · **Level:** Extension (Beginner) · **Time:** about 45 minutes

This time **you** are the maze maker! You will build one long maze that goes through **6 parts**, add some pistons and doors, and then write code to get the agent to the end.

Open the **M002 EXT 3 — Cube World** and build inside it. Drive the agent with chat: `l` turns left, `r` turns right, `run` starts your code, `rl` sends the agent back to start.

**Your maze needs at least:**

- **2 pistons** (open a wall when powered)
- **2 doors** (the agent opens them)
- **4 AND** checks in your code (`... and ...`)
- **1 OR** check in your code (`... or ...`)

---

## 1 · Plan Your 6 Parts 🗺️

Your maze has **6 parts** in a row. The agent finishes one part and walks into the next.

**Draw or write what each part has.** Easy idea: part = one room with one turn, one door, or one piston.

> Part 1: …
>
> Part 2: …
>
> Part 3: …
>
> Part 4: …
>
> Part 5: …
>
> Part 6: …

<div class="write-space tall" style="min-height: 200px"></div>

**Which 2 parts will have a piston? Which 2 will have a door?**

<div class="write-space"></div>

---

## 2 · Build It 🧱

Build your maze in the world. Walk it yourself first to make sure you can reach the end. Check off each part as you build it.

> ☐ Part 1   ☐ Part 2   ☐ Part 3   ☐ Part 4   ☐ Part 5   ☐ Part 6
>
> ☐ Piston #1   ☐ Piston #2
>
> ☐ Door #1   ☐ Door #2
>
> ☐ A START block and a GOAL block

---

## 3 · AND means BOTH · OR means EITHER 🔍

**AND** is true only when **both** things are true. **OR** is true when **at least one** is true.

```
if block on left AND redstone ahead:
    turn left
```

**There is a block on the left, but NOT redstone ahead. Does it turn? Circle one:** yes · no

<div class="write-space short"></div>

```
if block ahead OR redstone on right:
    open it
```

**There is a block ahead, but NO redstone on the right. Does it open it? Circle one:** yes · no

<div class="write-space short"></div>

---

## 4 · Write the Solution 💻

Fill in the code to get the agent through your maze. Use a loop so it checks every step. You need **4 AND** checks and **1 OR** check in total.

```
while True:
    agent.move(FORWARD, 1)

    # turn only when BOTH are true  (AND)
    if agent.detect(BLOCK, LEFT) and agent.detect(REDSTONE, AHEAD):
        agent.turn(LEFT_TURN)

    # a door OR a piston gate  (OR)
    elif agent.detect(BLOCK, AHEAD) or agent.detect(REDSTONE, RIGHT):
        agent.interact(AHEAD)
        agent.move(FORWARD, 1)
```

**Write your own checks for your maze here.** Put `# AND` or `# OR` next to each one.

<div class="write-space tall" style="min-height: 240px"></div>

**How many AND checks did you write? How many OR checks?**

<div class="write-space short"></div>

---

## 5 · Test It and Finish 📸

Type `run` and watch the agent. If it gets stuck, fix it and run again. Use `rl` to send it back to start. Keep going until the agent reaches the **GOAL** on its own.

When it finishes, send a photo or video of the agent at the goal and explain. Use these sentence starters — write 2 or 3 sentences.

> My maze has 6 parts. The hardest part to build was …
>
> I put my pistons in … and my doors in …
>
> I used AND to make the agent … and OR to …

<div class="write-space tall" style="min-height: 200px"></div>

---

## 6 · Present Your Maze 🎥

Take a video on your phone (or a parent's phone) and show off **your** maze like a game designer. Try to use these words: **part**, **piston**, **door**, **AND**, **OR**.

> 1. Show the whole maze and point out the 6 parts.
> 2. Show each piston and each door.
> 3. Type `run` and let the agent reach the goal.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 200px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
