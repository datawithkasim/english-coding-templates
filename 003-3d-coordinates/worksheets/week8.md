# 🧊 M003 Week 8 — English Worksheet

**Topic:** Final — Two-Faced Statue · **Course:** 3D Coordinates · **Time:** about 45 minutes

This is your final build. No new commands — just everything from this course working together. Your statue shows **one picture from the front** and a **different picture from the side**. The front face is flat along **x and y**, the side face is flat along **z and y**, and they meet at one corner edge.

---

## 1 · Predict 🔮

Read each plan. Before you imagine it happening, write what you think each **view** will show.

```
fill stone from (0, 0, 0) to (4, 4, 0)
```

**This wall stretches along x and y, and z stays 0. From the front you see a 5×5 square. What do you see from the side — the same square or something much thinner?**

<div class="write-space"></div>

```
front face: fill stone from (0, 0, 0) to (4, 4, 0)
side face:  fill stone from (0, 0, 0) to (0, 4, 4)
```

**Two faces, both 5 tall. Do they touch each other? Which blocks belong to both faces at the same time?**

<div class="write-space"></div>

```
front face: fill stone from (0, 0, 0) to (4, 4, 0)
side face:  fill stone from (0, 0, 0) to (0, 2, 4)
```

**Now the side face only goes up to height 2. Standing at the corner, do the two faces look like one statue or like a mistake? Why?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

**Bug A** — The two faces should meet only at the **corner edge** at x = 0, z = 0. Right now the side face slices through the **middle** of the front picture, so the front view is ruined.

```
fill stone from (0, 0, 0) to (4, 4, 0)
fill stone from (2, 0, 0) to (2, 4, 4)
```

**Hint:** look at the **x** numbers in the second line.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Both faces should be the **same height** — up to y = 4. Right now one face is shorter than the other.

```
fill stone from (0, 0, 0) to (4, 4, 0)
fill stone from (0, 0, 0) to (0, 2, 4)
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Both faces should sit on the **ground**, starting at y = 0. Right now one face floats one block in the air.

```
fill stone from (0, 0, 0) to (4, 4, 0)
fill stone from (0, 1, 0) to (0, 5, 4)
```

**Hint:** compare the **y** numbers where each face starts.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Tell Me What You Built 📸

Plan **before** you build. Sketch your **front view** picture as a grid (use `#` for stone, `.` for air):

<div class="write-space tall" style="min-height: 240px"></div>

Sketch your **side view** picture as a grid — same height as the front:

<div class="write-space tall" style="min-height: 240px"></div>

**List the corner coordinates of each face** — front face from ( … , … , … ) to ( … , … , … ), side face from ( … , … , … ) to ( … , … , … ):

<div class="write-space"></div>

Now switch to your homework world and build your two-faced statue. Check your build against this list:

> ☐ The front view shows one clear picture.
>
> ☐ The side view shows a **different** clear picture.
>
> ☐ Both faces are the **same height**.
>
> ☐ Both faces start at the **ground** — the bases line up.
>
> ☐ The faces meet at one corner edge, not through the middle.

Send a photo or video of **both views**, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My front picture is … and my side picture is …
>
> The two faces meet at …
>
> I made both faces the same height by …
>
> One tricky moment was when …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk around your statue. Talk through it like you are teaching someone who has never seen it. Try to use these words: **front view**, **side view**, **face**, **corner**, **height**.

> 1. Stand in front of the statue and say what the front picture shows.
> 2. Walk around to the side and say what the side picture shows.
> 3. Point at the corner edge where the two faces meet and say its coordinates.
> 4. Say in your own words how planning with coordinates made this build possible.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
