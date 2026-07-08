# 🏠 Builder Basics — The Sloped Roof (Extension)

**Topic:** Variables · **Course:** Builder Basics · **Type:** Extension Activity · **Time:** about 45 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable building shapes and you are ready to think about how one number can do a lot of work.

---

## 1 · Predict 🔮

In the **Sloped Roof** world, typing `slope` builds a stepped roof. It does not build block by block — it stacks four square **rings** of stairs, one on the next. The bottom ring is widest; each ring above is smaller, so the roof climbs inward and up to a point — like a small pyramid of steps.

A variable called `roof_len` holds the side length of each ring. It **starts at 7** and **loses 2** each ring. So the side shrinks each layer until the roof reaches its peak.

**Write the four values of `roof_len`, from the bottom ring to the top ring.**

<div class="write-space"></div>

**Each ring has four sides. To estimate the stairs in a ring, think of about four times the side length. Add up the four sides — 7, then 5, then 3, then 1 — and write the rough total number of stairs in the whole roof. Show your adding.**

<div class="write-space"></div>

**What is the LAST value of `roof_len`, the one at the very top? What kind of shape does a ring that small make?**

<div class="write-space"></div>

Meet a second variable, `step` — it decides **how much the ring shrinks** each layer. Right now `step` is 2, so the side drops 7, 5, 3, 1.

**If `step` were 1 instead of 2, would the roof be steeper (rises fast) or gentler (rises slowly)? Would it need MORE rings or FEWER rings to reach the peak? Explain why in a sentence or two.**

<div class="write-space tall"></div>

---

## 2 · Trace Two Things 🔢

Each layer changes two things: the ring **side** gets smaller and the **height** goes up by 1. Fill in the table. Start `roof_len` at 7 and height at 1; take 2 off the side and add 1 to the height each row.

| Layer | `roof_len` (ring side) | Height |
|:-----:|:----------------------:|:------:|
| 1     | 7                      | 1      |
| 2     |                        |        |
| 3     |                        |        |
| 4     |                        |        |

**Which change makes the ring smaller each layer?**

<div class="write-space"></div>

**Which change makes the roof taller each layer?**

<div class="write-space"></div>

**Which ring becomes the peak — the top point of the roof — and why is it the peak?**

<div class="write-space"></div>

---

## 3 · Reason About Bugs 🧠

No code to rewrite — read what goes wrong and explain it in writing.

**Bug A — The shrink happens too early.** The program takes 2 off `roof_len` **before** it builds the ring, not after. So the first ring uses the shrunk number, not 7.

**What goes wrong with the roof? (Think about the bottom ring.) How would you fix the order of the steps?**

<div class="write-space tall"></div>

**Bug B — The variable never changes.** Imagine `roof_len` stays at 7 for every layer and never loses its 2.

**What shape would you get instead of a roof? Why does the roof need the variable to update each time?**

<div class="write-space tall"></div>

---

## 4 · Design Your Own Roof 🏗️

Plan a roof of your own — in numbers and words, not in a code box.

**Pick a starting `roof_len` (the widest ring) and a `step` (how much it shrinks each layer):**

<div class="write-space short"></div>

**List the ring sizes your numbers produce, layer by layer, until you reach the peak. Just write the numbers, in order.**

<div class="write-space"></div>

**How many rings does it take to reach the peak?**

<div class="write-space short"></div>

**The big idea: the whole roof is built from one variable plus one shrink rule, instead of four rings written by hand. Explain WHY that is better. If you wanted a much bigger roof, what is the smallest thing you would change?**

<div class="write-space tall"></div>

---

## 5 · Show Your Work 📸🎥

Open the **Sloped Roof** world and type `slope` in the chat to run the program and watch the roof build. Then build your **own** version by changing the numbers — try a different starting `roof_len` or a different `step` and see how the roof changes shape.

Record **one video** (a phone is fine). Show two things:

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

**Write your lines here, then say them in your video.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
