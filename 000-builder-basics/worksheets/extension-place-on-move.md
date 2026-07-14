# 🧱 Builder Basics — The Trail Maker (Extension)

**Topic:** Place On Move · **Course:** Builder Basics · **Type:** Extension Activity · **Time:** about 45 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable placing blocks by hand and you are ready to let the agent place them for you.

---

## 1 · Predict 🔮

In the **Trail Maker** world, typing `run` starts the agent walking forward in a straight line. First it flips a switch called **place on move**.

When **place on move** is **ON**, the agent drops a block on every step — it leaves a **trail**. When it is **OFF**, the agent walks the same steps but places nothing, so a **gap** appears.

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

Walk through the program one line at a time. For each move command, write the switch state, the steps, the blocks placed, and the running total.

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

No code to rewrite — read what goes wrong and explain it in writing.

**Bug A — The switch never turns OFF.** The program leaves **place on move** ON the whole time. The agent still walks the same 10 steps.

**What does the trail look like now? What happened to the gap? Explain why.**

<div class="write-space tall"></div>

**Bug B — The switch never turns ON.** The program forgets the first `place on move ON`, so the switch stays OFF the whole time. The agent still walks all 10 steps.

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

**The big idea: in Week 2 you placed each block by hand — one `place` per block. With place on move you write one `move` and the agent places a whole line. Explain WHY that is easier. If you wanted a trail 50 blocks long, which way would you rather build it, and why?**

<div class="write-space tall"></div>

---

## 5 · Show Your Work 📸🎥

Open the **Trail Maker** world and type `run` in the chat to watch the agent lay its trail. Then build your **own** version by changing the program — try a longer trail, a wider gap, more than one gap, or a different block.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Fill the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.
>
> The most fun part was ______.
>
> Something new I learned was ______.

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
