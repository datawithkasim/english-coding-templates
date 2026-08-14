# 🏗️ Builder Basics · One Variable, Any Size — English Worksheet

**Topic:** Building Structures From One Input · **Course:** Builder Basics · **Time:** about 45 minutes

One number at the top of your code decides the whole build. Change that one number, run again, and the same code builds a different size.

---

## 1 · Predict 🔮

Read each set of steps. Write what you think will happen.

```
size = 4
place on move ON
repeat 4 times:
    move forward by size
    turn left
```

**What shape does the agent draw? How long is each side?**

<div class="write-space"></div>

**Now the first line says `size = 7` instead. How many lines did you edit, and how long is each side now?**

<div class="write-space"></div>

```
size = 5
place on move ON
repeat size times:
    repeat 4 times:
        move forward by size
        turn left
    place on move OFF
    move up by 1
    place on move ON
```

**How wide is the build? How tall is it? Which line decides both?**

<div class="write-space"></div>

```
size = 8
repeat 4 times:
    [draw one square, size blocks per side]
    move up by 1
    size = size - 2
```

**Write the side length of every layer, bottom to top.**

<div class="write-space short"></div>

**Change the first line to `size = 10`. Write the new layers, bottom to top. What happens to the number of layers?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each code block is broken. Read what it should do, rewrite it, then explain why the original was wrong.

**Bug A** — Every side of the square should follow `size`. Right now one side ignores it.

```
size = 9
place on move ON
move forward by size
turn left
move forward by size
turn left
move forward by 6
turn left
move forward by size
turn left
```

**Write the fixed code:**

<div class="write-space"></div>

**What shape do you get instead of a square? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — The tower should be exactly as tall as the wall beside it. The wall is 10 blocks tall.

```
size = 11
place on move ON
repeat size times:
    repeat 4 times:
        move forward by 5
        turn left
    place on move OFF
    move up by 1
    place on move ON
```

**Count the layers this code builds. Write the number, then write the fixed first line.**

<div class="write-space short"></div>

**How can you check the height before you run the code, instead of after?**

<div class="write-space"></div>

**Bug C** — One input should change the whole house. Here, changing `size` only changes the floor.

```
size = 6
place on move ON
repeat 4 times:
    move forward by size
    turn left
place on move OFF
move up by 1
place on move ON
repeat 4 times:
    move forward by 4
    turn left
```

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Show Your Work 📸🎥

Switch to your homework world. Build a structure — a tower, a hut, a pyramid, your choice — where **one variable at the top decides the size**. Inside the build, use the variable name, not a number.

Run it three times. Between runs, edit **only** the first line: a small size, a medium size, a big size. Leave every other line alone.

Record **one video** — one take, no stopping (a phone is fine). Show these in order:

**1 · Your code.** Scroll through it. Say what each part does. Point at the one line you edit between runs.

**2 · Your build.** Point the camera. Show all three sizes.

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
