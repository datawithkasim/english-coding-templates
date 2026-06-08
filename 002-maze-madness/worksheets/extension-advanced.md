# 🧩 M002 Extension — Advanced Worksheet

**Topic:** Redstone Trail Solver (3D Cube Maze) · **Course:** Maze Madness · **Level:** Extension (Advanced) · **Time:** about 60 minutes

This is an **extension challenge** for students who have finished the weekly mazes and want something harder. The agent solves a **3D cube maze** on its own by following a **redstone trail** — reading redstone above, below, left, right and ahead, then deciding what to do at every step.

You drive it with **chat commands**: type `l` to turn left, `r` to turn right, `run` to start the solver, and `rl` to teleport the agent back to you.

---

## 1 · Read the Chat Commands 🎛️

Each block of code binds a **chat word** to an action. When you type that word in chat, the agent runs the code.

```
def on_on_chat():
    agent.turn(LEFT_TURN)
player.on_chat("l", on_on_chat)
```

**What does the agent do when you type `l` in chat?**

<div class="write-space short"></div>

```
def on_on_chat4():
    agent.teleport_to_player()
player.on_chat("rl", on_on_chat4)
```

**You typed `rl`. Where does the agent go? When would that be useful?**

<div class="write-space"></div>

**Why is it handy to bind small helpers like `l`, `r` and `rl` to chat _before_ you write the big `run` solver?**

<div class="write-space"></div>

---

## 2 · Trace the Solver 🔍

This is the loop that runs when you type `run`. It checks redstone in different directions and reacts.

```
while True:
    agent.move(FORWARD, 1)
    if agent.detect(REDSTONE, DOWN) and agent.detect(REDSTONE, RIGHT):
        agent.move(FORWARD, 1)
        agent.interact(LEFT)
    elif agent.detect(BLOCK, RIGHT) and agent.detect(REDSTONE, LEFT):
        agent.move(FORWARD, 1)
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, 1)
    elif agent.detect(REDSTONE, DOWN):
        agent.move(UP, 1)
    elif agent.detect(REDSTONE, UP):
        agent.move(DOWN, 4)
```

**The loop starts with `while True`. When does it stop on its own?**

<div class="write-space short"></div>

**The redstone is a _trail_ the agent follows. In your own words, what does `detect(REDSTONE, DOWN)` tell the agent?**

<div class="write-space"></div>

**This maze is 3D — the agent goes up and down, not just flat. Which two lines move it between floors? What does each one do?**

<div class="write-space"></div>

**Why does the order of the `if` / `elif` checks matter? What would change if the `elif agent.detect(REDSTONE, DOWN)` check came _first_, before the others?**

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each block below is broken. Read what it is **supposed** to do, rewrite it so it works, then explain the fix.

**Bug A** — The solver should keep going until the maze is done, checking the trail on every step.

```
agent.move(FORWARD, 1)
if agent.detect(REDSTONE, DOWN):
    agent.move(UP, 1)
```

**Hint:** this only checks _once_. What wraps a block so it repeats?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — When there is redstone **down and to the right**, the agent should step forward then flip a lever on its **left**.

```
if agent.detect(REDSTONE, DOWN) or agent.detect(REDSTONE, RIGHT):
    agent.interact(LEFT)
```

**Hint:** "down **and** right" — both must be true. And it should move forward before it interacts.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Make It Your Own 🛠️

Open the extension world and run the solver with `run`. Now **change one thing** and predict what happens before you test it.

Pick **one** idea (or your own):

- Add a new chat command, like `back`, that turns the agent around (two right turns).
- Change `agent.move(DOWN, 4)` to a different number and watch where the agent lands.
- Add an `elif` that does something when there is redstone straight **ahead**.

**Which change did you pick? Write the code for it.**

<div class="write-space tall" style="min-height: 200px"></div>

**Predict first:** what do you think will happen when you run it?

<div class="write-space short"></div>

**Then test it.** What actually happened? If it surprised you, why?

<div class="write-space"></div>

---

## 5 · Tell Me What You Built 📸

When the agent finishes the cube maze, come back here. Send a photo or video of the agent reaching the goal, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> The maze was 3D, so the agent had to …
>
> The redstone trail told the agent to …
>
> I used `detect` to …
>
> The change I made in section 4 was …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent solves the maze. Talk through it like you are teaching someone who has never seen it. Try to use these words: **detect**, **redstone**, **trail**, **loop**, **3D**, **elif**.

> 1. Show the cube maze and the redstone trail before you start.
> 2. Type `run` and show the agent following the trail.
> 3. Read one `if` / `elif` line out loud and say what decision it makes.
> 4. Show the change you made in section 4 and what it did.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
