# 🧱 M002 Week 7 — English Worksheet (Beginner)

**Topic:** Pistons and Mazes · **Course:** Maze Madness · **Level:** Beginner · **Time:** about 30 minutes

This week the maze uses a **piston**. When your agent flips a lever, the piston opens a path across a gap. The agent crosses while the path is open.

---

## 1 · Predict 🔮

Read the steps. Before you imagine the agent doing it, circle or write your answer.

```
move forward
interact ahead
move forward
```

**The agent flips the lever and the piston opens the path. Can the agent cross now? Circle one:** yes · no

<div class="write-space short"></div>

```
if gap ahead:
    interact ahead
otherwise:
    move forward
```

**The agent is on solid ground with no gap. What does it do? Circle one:** interact · move forward

<div class="write-space short"></div>

---

## 2 · Find the Difference 🐛

Each pair shows clean steps first, then a broken version of the same idea. Circle what's different and write one short sentence about the bug.

**Pair A** — The agent should power the piston **first**, then cross.

```
# clean
interact ahead
move forward
move forward
```

```
# buggy
move forward
move forward
interact ahead
```

**What is wrong? What happens at the gap?**

<div class="write-space short"></div>

**Pair B** — The agent should `interact` only when there is a **gap** ahead.

```
# clean
if gap ahead:
    interact ahead
otherwise:
    move forward
```

```
# buggy
keep doing forever:
    interact ahead
    move forward
```

**What is wrong? How often does the buggy agent interact?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

The agent should flip the lever **only** when it sees a gap. One word is missing. Fill it in using the word bank.

```
if ____ ahead:
    interact ahead
otherwise:
    move forward
```

**Word bank:** `gap` · `grass` · `friend`

**Write the missing word:**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world. The maze has a **gap** and a **piston** that opens it. Walk the agent to the lever, flip it, cross while the path is open, and reach the goal. When you finish, come back here.

Send a photo or video of the agent reaching the end, then explain what you did. Use these sentence starters — write 2 or 3 sentences.

> I powered the piston by …
>
> Once the path opened, the agent …
>
> The hardest part was …

<div class="write-space tall" style="min-height: 240px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) while the agent runs the maze. Talk like you are teaching a friend. Try to use these words: **piston**, **lever**, **gap**, **bridge**.

> 1. Show the gap and the piston.
> 2. Run your code and show the agent crossing.
> 3. Say which line of your code opens the path.

**Write what you will say in your video.** You can read from it while filming.

<div class="write-space tall" style="min-height: 240px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
