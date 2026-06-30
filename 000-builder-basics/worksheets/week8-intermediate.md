# 🏘️ M000 Week 8 — English Worksheet (Intermediate)

**Topic:** Build a Village (Final Project) · **Course:** Builder Basics · **Level:** Intermediate · **Time:** about 38 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think it builds and why.

```
repeat 4 times:
    repeat 3 times:
        place block down
        move forward
    turn right
repeat 3 times:
    destroy block down
    move down by 1
```

**Which part of the village is this — a house, a well, or a farm? How do you know?**

<div class="write-space"></div>

```
# Stage 1
[house]
# Stage 2
move to next spot
[well]
# Stage 3
move to next spot
[farm]
```

**This is the skeleton for the whole village. What does the agent do between each stage, and why does it matter?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block below was meant to do something, but it is broken. Read the goal, then write a fixed version and explain the bug in one or two sentences.

**Bug A** — The village should have a **house and a well**, side by side.

*Goal: the agent should end up with two structures, not one.*

```
# buggy
[house]
move to next spot
```

**Write the fixed skeleton:**

<div class="write-space short"></div>

**What was missing, and why does your fix work?**

<div class="write-space short"></div>

**Bug B** — The well must **not** land on top of the house.

*Hint: look at what is between the two structures.*

```
# buggy
[house]
[well]
```

**Write the fixed skeleton:**

<div class="write-space short"></div>

**Why was the original wrong, and why does your fix work?**

<div class="write-space short"></div>

**Bug C** — The roof should sit **on top** of the walls, but here the agent stays on the ground after building the walls.

*Hint: after the walls finish, the agent is still at ground level. Where does it need to be?*

```
repeat 3 times:
    repeat 4 times:
        place block down
        move forward
    turn right
# now place the roof
repeat 3 times:
    place block down
    move forward
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong, and why does your fix work?**

<div class="write-space short"></div>

---

## 3 · Fill the Gap ✏️

Here is the skeleton of a three-part village. One stage is missing. Fill it in so all three structures end up in a row.

```
# Stage 1
[house]
move to next spot
# Stage 2
[well]
# Stage 3
move to next spot
____________
```

**Write the missing stage, and explain why the agent needs the "move to next spot" line above it.**

<div class="write-space short"></div>

---

## 4 · Tell Me What You Built 📸

Now switch to your homework world and build your **final project**: a village with a **house and one more structure** — a well or a farm, your choice. Add a third structure if you have time. When you finish, come back here.

Send a photo or video of your village, then explain what you did. Use these sentence starters — write 3 or 4 sentences.

> First, I built the …
>
> Then I built the …
>
> To move between structures, the agent …
>
> The thing I am most proud of is …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 5 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and walk the camera through your village. Talk like you are teaching a friend who has never seen it. Try to use these words: **village**, **house**, **roof**, **well**, **farm**.

> 1. Walk around the village and show each building one by one.
> 2. Say which building you made first and which came next.
> 3. Show one bug you hit and how you fixed it.
> 4. Say what you would add next if you had more time.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk. This is the **last week** of Builder Basics — well done!
