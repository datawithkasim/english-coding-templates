# 🔺 M001 Week 5 — English Worksheet

**Topic:** First Pyramid · **Course:** Pyramid Problems · **Time:** about 45 minutes

This week the agent **walks the edges** of a square and drops blocks as it moves. Stack those squares, shrink each one, and a pyramid grows.

---

## 1 · Predict 🔮

Read each set of steps. Before you imagine the agent doing it, write what you think will happen.

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

Each block of code below was meant to do something, but it is broken. Read what the code is **supposed** to do, then rewrite it so it works. After that, explain why the original was wrong and why your fix works.

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

## 3 · Tell Me What You Built 📸

Now switch to your homework world. Run your `pyra` command to build a pyramid. Then change the **starting value of `f`** (try a smaller number) and build a shorter one. If the agent ends up facing the wrong way or stuck, use your helper commands to reset it — `1` turns it left, `r` turns it right, and `r1` teleports it back to you.

Send a photo or video of your pyramid, then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I …
>
> The bottom square has sides … blocks long.
>
> Each new layer shrinks by … because …
>
> `place on move` matters because …
>
> The hardest part was …
>
> If I had more time, I would …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Record Your Walkthrough 🎥

Now take a video on your phone (or a parent's phone) while you walk the camera around your pyramid. Talk through it like you are teaching someone who has never seen it. Try to use these words: **square**, **side**, **layer**, **shrink**, **place on move**, **variable f**.

> 1. Walk around the pyramid and show all 4 sides.
> 2. Read your `repeat 4 times` loop out loud and say how it draws one square.
> 3. Say what `change f by -2` does to each layer.
> 4. Show one bug you hit and how you fixed it.

**Write what you will say in your video.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your walkthrough video to teacher on KakaoTalk.
