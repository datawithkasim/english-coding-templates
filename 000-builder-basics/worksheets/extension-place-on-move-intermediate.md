# 🧱 Builder Basics — The Trail Maker (Extension · Intermediate)

**Topic:** Place On Move · **Course:** Builder Basics · **Type:** Extension Activity · **Level:** Intermediate · **Time:** about 38 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable placing blocks and you want the agent to place a whole line for you.

In Week 2 you placed blocks one at a time. This world has a faster way. When you type `run` in the chat, the agent flips a switch called **place on move** and then walks forward. Your job in this worksheet is to understand the **idea** behind it, not to type any code.

Here is the idea. When **place on move** is **ON**, the agent drops a block on every step it walks — it leaves a **trail** behind it. When the switch is **OFF**, the agent walks the same steps but places nothing, so you get a **gap**. The program turns the switch ON, walks a bit, turns it OFF, walks a bit, then turns it ON again — so the trail comes out with a gap in the middle.

---

## 1 · Predict 🔮

Here is the order the program runs:

```
place on move ON
move forward by 4
place on move OFF
move forward by 2
place on move ON
move forward by 4
```

**Each move places one block per step while the switch is ON. How many blocks come from the first `move forward 4`? How many from the `move forward 2` while OFF? How many from the last `move forward 4`? Write all three numbers.**

<div class="write-space tall"></div>

**Add them up. How many blocks are placed in total, and how wide is the gap in the middle? Show your working.**

<div class="write-space"></div>

---

## 2 · Trace the Switch 🔢

Walk through the program one move at a time. For each move command, write the switch state and how many blocks that stretch places. Show the count, not just a guess.

| Move command | Switch (ON / OFF) | Blocks placed |
|--------------|-------------------|---------------|
| move forward 4 |                 |               |
| move forward 2 |                 |               |
| move forward 4 |                 |               |

<div class="write-space"></div>

**The agent walked 10 steps but placed fewer than 10 blocks. Why? Which stretch is the reason?**

<div class="write-space"></div>

---

## 3 · Reason About the Switch 🧠

No code here — just think it through.

**The trail comes out as one solid line with NO gap. The switch must have been left in the wrong state somewhere. Which line of the program went wrong for that to happen? Explain in one or two sentences.**

<div class="write-space tall"></div>

**Now imagine the very first `place on move ON` was missing, so the switch stayed OFF the whole time. What would be on the ground after the agent finished walking? Explain why.**

<div class="write-space tall"></div>

---

## 4 · Make It Yours ✏️

The switch decides WHEN the agent places, and the move numbers decide HOW MANY blocks and how wide the gap is.

**Design a trail that places exactly **10 blocks** with a **3-wide gap** in the middle. Write your ON / OFF / move sequence, line by line.**

<div class="write-space tall"></div>

**One sentence: how did you pick your move numbers to get 10 blocks?**

<div class="write-space"></div>

---

## 5 · Build It 📸

Open the **Trail Maker** world. Type `run` in the chat to watch the agent lay a trail with a gap. Then try your own version from Section 4 — change the move numbers and the ON / OFF switches, and run it again.

When it looks right, send a photo or video to teacher on KakaoTalk. Then explain what you did. Use these starters — write 4 to 6 sentences total.

> When **place on move** was **ON**, the agent …
>
> When it was **OFF**, the agent …
>
> My gap is … wide because …
>
> This was faster than Week 2 because …

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a photo or video of your trail to teacher on KakaoTalk.
