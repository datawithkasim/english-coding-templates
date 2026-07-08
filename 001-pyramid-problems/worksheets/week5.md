# 🔺 M001 Week 5 — English Worksheet

**Topic:** First Pyramid · **Course:** Pyramid Problems · **Time:** about 45 minutes

The agent **walks the edges** of a square, dropping blocks as it moves. Stack the squares, shrink each one, and a pyramid grows.

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
set f to 6
place on move ON
repeat 4 times:
    move forward by f
    turn left
```

**What shape does the agent draw? How many blocks long is each side?**

<div class="write-space"></div>

**Why is it `repeat 4 times` and `turn left`? What would `repeat 3 times` draw instead?**

<div class="write-space"></div>

```
set f to 6
repeat 3 times:
    [draw one f × f square]
    move up by 1
    change f by -2
```

**List the side length of each layer from bottom to top. Looking from the side, what shape do the stacked squares make?**

<div class="write-space"></div>

```
place on move ON
move forward by 4
place on move OFF
move forward by 4
```

**Where do the blocks end up? Why does turning `place on move` OFF matter when the agent moves up to start the next layer?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block below is broken. Read what it should do, rewrite it so it works, then explain why the original was wrong and why your fix works.

**Bug A** — The agent is supposed to draw a closed **square** outline.

```
set f to 6
place on move ON
repeat 4 times:
    move forward by f
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Each new layer must be **2 blocks smaller** than the one below, so the tower narrows into a pyramid.

```
set f to 8
repeat 4 times:
    [draw one f × f square]
    move up by 1
    change f by 2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Each square must sit one block **higher** than the last.

```
set f to 8
repeat 4 times:
    [draw one f × f square]
    change f by -2
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Now switch to your homework world. Run your `pyra` command to build a pyramid. Then change the **starting value of `f`** (try a smaller number) and build a shorter one. If the agent ends up facing the wrong way or stuck, use your helper commands to reset it — `1` turns it left, `r` turns it right, and `r1` teleports it back to you.

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
