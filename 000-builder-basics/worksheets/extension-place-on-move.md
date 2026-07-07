# 🧱 Builder Basics — The Trail Maker (Extension)

**Topic:** Place On Move · **Course:** Builder Basics · **Type:** Extension Activity · **Time:** about 45 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable placing blocks by hand and you are ready to let the agent place them for you.

---

## 1 · Predict 🔮

In the **Trail Maker** world, typing `run` in the chat starts the agent walking forward in a straight line. But first it flips a switch called **place on move**.

When **place on move** is **ON**, the agent drops a block on every single step it takes — it leaves a **trail** behind it as it walks. When the switch is **OFF**, the agent still walks the same steps, but it places nothing, so the ground stays empty and a **gap** appears.

Here is the exact order the program runs:

```
place on move ON
set block to purple concrete
move forward by 4
place on move OFF
move forward by 2
place on move ON
move forward by 4
```

**The switch starts ON and the agent moves forward 4. How many blocks does it drop in this first stretch?**

<div class="write-space"></div>

**Then the switch turns OFF and the agent moves forward 2. How many blocks does it drop while the switch is OFF?**

<div class="write-space"></div>

**The switch turns ON again and the agent moves forward 4. Add up every block from the whole program. How many blocks in total? Show your adding.**

<div class="write-space"></div>

**Describe the finished trail. Where is the gap, and how wide is it? Draw or describe the shape.**

<div class="write-space tall"></div>

---

## 2 · Trace the Switch 🔢

Walk through the program one line at a time. For each move command, write whether the switch is **ON** or **OFF**, how many steps the agent takes, how many blocks that stretch places, and the running total so far.

| Move command | Switch (ON / OFF) | Steps | Blocks this stretch | Total so far |
|:------------:|:-----------------:|:-----:|:-------------------:|:------------:|
| move forward 4 |                 |       |                     |              |
| move forward 2 |                 |       |                     |              |
| move forward 4 |                 |       |                     |              |

**Which move command placed NO blocks, and why?**

<div class="write-space"></div>

**The agent walked forward 10 steps in total but did not place 10 blocks. Explain why the number of blocks is smaller than the number of steps.**

<div class="write-space"></div>

---

## 3 · Reason About Bugs 🧠

No code to rewrite here — just read what goes wrong and explain it in writing.

**Bug A — The switch never turns OFF.** Imagine the program leaves **place on move** ON the whole time and never flips it OFF in the middle. The agent still walks the same 10 steps forward.

**What does the trail look like now? What happened to the gap? Explain why.**

<div class="write-space tall"></div>

**Bug B — The switch never turns ON.** Imagine the program forgets the very first `place on move ON`, so the switch stays OFF from start to finish. The agent still walks all 10 steps.

**How many blocks get placed? What do you see on the ground when it finishes? Why?**

<div class="write-space tall"></div>

---

## 4 · Design Your Own Trail 🏗️

Plan a trail of your own — in words and numbers, not in a code box.

**Choose your block, and decide your ON and OFF pattern. Fill in the blanks:**

> My block is …
>
> Switch ON, move forward … (places … blocks)
>
> Switch OFF, move forward … (a gap … wide)
>
> Switch ON, move forward … (places … blocks)

<div class="write-space tall"></div>

**How many blocks does your pattern place in total? How many empty steps are in your gap?**

<div class="write-space"></div>

**Now the big idea. In Week 2 you placed each block by hand — one `place` command for every block. With **place on move** you write one `move` command and the agent places a whole line for you. In writing, explain WHY that is easier. To help you think: if you wanted a trail 50 blocks long, which way would you rather build it, and why?**

<div class="write-space tall"></div>

---

## 5 · Build It 📸

Open the **Trail Maker** world and type `run` in the chat to watch the agent lay its trail. Then build your **own** version by changing the program — try a longer trail, a wider gap, more than one gap, or a different block.

Send a photo or video of your trail, then explain what you did. Use these starters — write 4 to 6 sentences total.

> First, I ran `run` and saw the agent …
>
> When **place on move** was **ON**, the agent …
>
> When I turned it **OFF**, the agent …
>
> The change I made was …
>
> My trail has a **gap** because …
>
> Building this way was easier than placing by hand because …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 6 · Record Your Walkthrough 🎥

Take a video on your phone (or a parent's phone) and teach someone how the Trail Maker works. You are narrating and explaining — not presenting to a class. Try to use these words: **place on move**, **switch**, **ON**, **OFF**, **trail**, **gap**.

> 1. Point to the trail and the gap, and say which part was built with the switch **ON**.
> 2. Explain what **place on move** does when it is **ON**.
> 3. Explain what happens to the ground when it is **OFF**, and why that made the **gap**.
> 4. Show the change you made and what it did to the trail.
> 5. Say one reason this is easier than placing every block by hand.

**Write what you will say in your video.** Plan it here first — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
