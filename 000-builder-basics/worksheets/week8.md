# 🏘️ M000 Week 8 — English Worksheet

**Topic:** Build a Village (Final Project) · **Course:** Builder Basics · **Time:** about 60 minutes

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

```
set size to 5
set height to 3

repeat height times:
    repeat 4 times:
        repeat size times:
            place block down
            move forward
        turn right
    move up by 1
```

**Which part of the village is this — house, well, or farm house?**

<div class="write-space"></div>

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

**Which part of the village is this?**

<div class="write-space"></div>

```
# Stage 1
[house walls + roof]
# Stage 2
move to next spot
[well]
# Stage 3
move to next spot
[farm house]
```

**This is the skeleton for the whole village. What does the agent need between each stage?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The village should have **a house with a roof, a well, and a farm house** — three structures, side by side.

```
# House
[house walls + roof code]
# Well
[well code]
```

**Hint:** something is missing. Rewrite the skeleton to include all three structures.

**Write the fixed skeleton:**

<div class="write-space"></div>

**What was missing? Why does the full version work?**

<div class="write-space"></div>

**Bug B** — Between each structure, the agent must **walk to a new spot** so the next structure doesn't land on top of the last one.

```
# House
[house walls + roof]
# Well
[well code]
# Farm house
[farm house code]
```

**Hint:** add the missing "move to next spot" steps. You don't need to write the full house/well/farm code — write where the agent should walk between stages.

**Write the fixed skeleton:**

<div class="write-space"></div>

**Why was the original wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The house roof should sit on top of the walls, but in this code the agent stays on the ground after the walls.

```
repeat height times:
    repeat 4 times:
        repeat size times:
            place block down
            move forward
        turn right
# now place the roof
repeat size times:
    repeat size times:
        place block down
        move forward
```

**Hint:** the agent finishes the walls on the ground. Where should it go before placing the roof?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Build your village — **a house with a roof, a well, and a farm house** at minimum. If you have time, add a standalone farm too. When you finish, come back here.

Send a photo or video of your whole village, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I built the …
>
> Then I built the …
>
> To move between structures, the agent …
>
> I used a nested loop for …
>
> The hardest part was …
>
> The thing I am most proud of is …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera through your village. Talk through it like you are teaching someone who has never seen it. Try to use these words: **village**, **house**, **roof**, **well**, **farm house**.

> 1. Walk around the village and show each building one by one.
> 2. For each building, read the loops out loud and say what stage they are.
> 3. Show one bug you hit and how you fixed it.
> 4. Say what you would add next if you had more time.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk. This is the **last week** of Builder Basics — well done!
