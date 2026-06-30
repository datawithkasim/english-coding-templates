# 🏠 Builder Basics — The Sloped Roof (Extension · Intermediate)

**Topic:** Variables · **Course:** Builder Basics · **Type:** Extension Activity · **Level:** Intermediate · **Time:** about 38 minutes

> 🧩 This is a bonus challenge, not a weekly lesson. Try it once you are comfortable building square rings with loops and you want to make a roof that steps up to a point.

A real roof is not one flat row — it is a stack of **square rings** that get smaller as they go up. The Sloped Roof world already has the working program inside it: when you type `slope` in the chat, it builds the whole roof for you. Your job in this worksheet is to understand the **idea** behind it, not to type any code.

Here is the idea. The program stores the side length of a ring in a **variable** called `roof_len`. It starts at **7**, so the bottom ring is a square 7 stairs long on each side. After each ring is finished, the program steps **up and inward**, then shrinks the variable by 2. So the next ring is shorter, the one after that shorter still, until the roof reaches a tiny peak. Four rings get built in total, with side lengths of **7, 5, 3, and 1**. Change the starting number and the whole roof changes shape.

---

## 1 · Predict 🔮

The variable `roof_len` starts at **7**. Each layer the agent walks a square ring with 4 sides, each side `roof_len` stairs long, then shrinks `roof_len` by 2 before stepping up to the next ring. The four rings have sides of **7, 5, 3, 1**.

**What shape do the rings make as they stack up? Describe it in one sentence.**

<div class="write-space"></div>

**About how many stairs are placed in total across all four rings? Each ring's edge is about 4 × its side length, and the side lengths are 7, 5, 3, 1. Write the four numbers you got, then add them for the total. Show your working — do not just guess.**

<div class="write-space tall"></div>

---

## 2 · Trace the Variable 🔢

Walk through the build one ring at a time. For each layer, write the value of `roof_len` **for that ring** (the side length the agent uses), then the value **after** the variable loses 2 and gets ready for the next ring. Show the subtraction, not just the answer.

| Layer | `roof_len` for this ring | `roof_len` after it loses 2 |
|-------|--------------------------|------------------------------|
| 1     |                          |                              |
| 2     |                          |                              |
| 3     |                          |                              |
| 4     |                          |                              |

<div class="write-space"></div>

**After the 4th ring, what is the value of `roof_len`? Why does the roof stop here instead of building one more ring?**

<div class="write-space"></div>

---

## 3 · Reason About the Variable 🧠

No code here — just think it through.

**The roof comes out FLAT, like a box, instead of sloped. Every ring ended up the same size. Which part of the rule about the variable must have gone wrong for that to happen? Explain in one or two sentences.**

<div class="write-space tall"></div>

**Now imagine the variable lost **1** each ring instead of **2**. How would the roof look different — would the sides be steeper or gentler? Would there be more rings or fewer before it reached the peak? Explain why.**

<div class="write-space tall"></div>

---

## 4 · Make It Yours ✏️

The starting value of `roof_len` decides how wide the bottom ring is. Because the variable drops by 2 each ring, a bigger starting number takes more rings to shrink all the way down to 1.

**Choose a starting `roof_len` so the roof has exactly **5 rings** and still shrinks neatly to a peak of 1. What starting value works? List the 5 ring sizes in order, from the widest bottom ring up to the peak.**

<div class="write-space tall"></div>

**One sentence: how did you pick that starting value?**

<div class="write-space"></div>

---

## 5 · Build It 📸

Open the **Sloped Roof** world. Type `slope` in the chat to run the build and watch the rings shrink and step up to the peak. Then try the wider **5-ring** version by changing the starting number to the value you chose in Section 4, and run it again.

When it looks right, send a photo or video to teacher on KakaoTalk. Then explain what you did. Use these starters — write 4 to 6 sentences total.

> I used a **variable** called roof_len to …
>
> Its starting **value** was … and each ring it …
>
> The variable had to **update** so that …
>
> My roof has a **slope** because …

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a photo or video of your sloped roof to teacher on KakaoTalk.
