# 🕹️ M002 Week 6 — English Worksheet (Beginner)

**Topic:** Redstone Levers and Mazes · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 30 minutes

This week the maze has a **lever**. Your agent **flips the lever** (`interact`) to open a closed redstone door, then walks through.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
move forward
interact ahead
move forward
```

**The agent walks up to a lever and flips it. What happens to the door? Circle one:** it opens · it closes · nothing

<div class="write-space short"></div>

```
interact ahead
```

**There is no lever in front of the agent. What happens? Circle one:** the door opens anyway · nothing happens

**Why?**

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should flip the lever **first**, then walk through the open door.

```
# clean
move forward
interact ahead
move forward
move forward
```

```
# buggy
move forward
move forward
move forward
interact ahead
```

**What is wrong? What does the buggy agent walk into?**

<div class="write-space short"></div>

**Pair B** — The agent should walk **up to** the lever, then flip it once.

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

**What is wrong? How many times does the buggy agent interact?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent stands right in front of the lever. It must flip it, then walk through the door. One line is missing. Fill it in using the word bank.

```
____________
move forward
move forward
```

**Word bank:** `interact ahead` · `place block down` · `turn right`

**Write the missing line:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. The maze has a **lever** that opens a **closed door**. Walk the agent to the lever, flip it with `interact`, and go through the door to the goal. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I used `interact` to …
>
> Once the door opened, the agent …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent runs the maze. Talk like you are teaching a friend. Try to use these words: **lever**, **interact**, **door**, **open**.

> 1. Show the closed door and the lever.
> 2. Run your code and show the agent flipping the lever.
> 3. Say which line of your code opens the door.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
