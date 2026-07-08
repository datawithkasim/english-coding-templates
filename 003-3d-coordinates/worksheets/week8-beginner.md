# 🧊 M003 Week 8 — English Worksheet (Beginner)

**Topic:** Final — My Own Museum · **Course:** 3D Coordinates · **Level:** Beginner · **Time:** about 40 minutes

This is your big final build — no new commands, everything from this course together. Your museum has a **room** to walk into, a **flat picture** on the wall (2D, x and y), and a **solid sculpture** on a pedestal (3D, x, y, z).

---

## 1 · Predict 🔮

Read the steps. Circle your answer.

```
# a picture on the back wall — z stays 0, blocks climb with x and y
place red block at (1, 1, 0)
place red block at (2, 1, 0)
```

**These stay at z = 0 — only x and y change. A flat picture on the wall? Circle one:** yes · no

**Why? Circle one:** z never changes · z keeps growing

```
# a sculpture — all three numbers used
fill stone from (4, 0, 4) to (5, 1, 5)
place gold block at (4, 2, 4)
```

**This uses x, y, and z. Is this a solid thing you can walk all the way around? Circle one:** yes · no

---

## 2 · Find the Difference 🐛

Each pair shows clean code, then a buggy version. Circle the bug.

**Pair A** — The museum room should be **hollow** so visitors can walk in.

```
# clean
fill stone from (0, 0, 0) to (8, 4, 8)
fill air from (1, 1, 1) to (7, 3, 7)
```

```
# buggy
fill stone from (0, 0, 0) to (8, 4, 8)
```

**Can a visitor get inside the buggy museum? Circle one:** no, it is solid · yes

**Pair B** — The statue should rest **on top** of its pedestal, at height 2.

```
# clean
fill stone from (4, 0, 4) to (5, 1, 5)
place gold block at (4, 2, 4)
```

```
# buggy
fill stone from (4, 0, 4) to (5, 1, 5)
place gold block at (4, 0, 4)
```

**What is wrong? Circle one:** the statue's y should be 2, not 0 · the color is wrong

---

## 3 · Plan Your Museum 🗺️

Before you build, say your plan out loud: where your room goes, where your flat picture goes (which wall, z stays 0), and where your pedestal and sculpture go.

---

## 4 · Show Your Work 📸🎥

Switch to your homework world and build your museum from your plan. Check your build against this list:

> ☐ A **room** with a floor and walls that you can stand inside.
>
> ☐ A **doorway** to walk in through.
>
> ☐ **One flat picture** on a wall (2D — only x and y change).
>
> ☐ **One sculpture** on a pedestal (3D — x, y, and z).

Record **one video** (a phone is fine). Show two things:

**1 · Your code.** Scroll through it. Say what each part does.

**2 · Your build.** Point the camera. Name the parts.

Say these out loud, filling in the blanks:

> Today I built ______.
>
> I built it using this code: ______.
>
> In this code I used ______.
>
> The hardest part was ______.
>
> That part was hard because ______.

---

### Submit ✅

Send this worksheet + your video to teacher on KakaoTalk.
