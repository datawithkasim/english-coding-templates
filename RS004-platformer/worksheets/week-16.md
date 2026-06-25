# 🏆 RS004 Week 16 — English Worksheet

**Topic:** Title · Level Select · Sound · Showcase (Final) · **Course:** Platformer Game · **Time:** about 45 minutes

This is the final week. You built a finished game over 16 weeks: a **title screen**, a **level select** menu, and **sound** for jumps and coins, all running on a **game state machine** that moves between title → level select → playing → game over / victory. This worksheet is about reading and explaining that code in plain English, then presenting your finished game.

> Keep these words handy: **state machine**, **title screen**, **level select**, **sound**, **showcase**.

---

## 1 · Predict 🔮

Read each snippet. Write what you think it does.

```python
current_state = "title"
# "title" → "level_select" → "playing" → "gameover" / "victory" → "title"
```

**The game starts in `"title"`. List one path it can take through the states to a win.**

<div class="write-space"></div>

```python
if current_state == "title":
    if event.key == pygame.K_SPACE:
        current_state = "playing"
    elif event.key == pygame.K_l:
        current_state = "level_select"
```

**On the title screen the player presses L. What screen comes next?**

<div class="write-space"></div>

```python
if event.key == pygame.K_SPACE and on_ground:
    velocity_y = JUMP_STRENGTH
    jump_sound.play()
```

**When does the jump sound play? Could it play in the air? Why or why not?**

<div class="write-space"></div>

---

## 2 · Map the States 🗺️

Write out the arrows showing which state leads to which. Fill in the blanks.

```
title  --space-->  ________
title  --L------>  ________
level_select  --Enter-->  ________
playing  --hit enemy-->  ________
playing  --clear last level-->  ________
gameover  --R-->  ________
```

<div class="write-space"></div>

---

## 3 · Spot the Bug 🐛

Each snippet is broken. On paper, rewrite it so it works, then explain why the original was wrong.

**Bug A** — Pressing space on the title should start the game. Right now space does nothing because the key is only checked while playing.

```python
if current_state == "playing":
    if event.key == pygame.K_SPACE:
        velocity_y = JUMP_STRENGTH
```

**Hint:** the title screen also needs to react to space. Handle each state's keys.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — In the level select menu, ↑/↓ should move the highlight and wrap around the ends. Right now going past the last item crashes with an index error.

```python
if event.key == pygame.K_DOWN:
    selected_level = selected_level + 1
```

**Hint:** use `% len(LEVELS)` so the choice wraps back to the start.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — A coin pickup should play a sound, but the game is silent even though `coin_sound` exists.

```python
for coin in coins[:]:
    if player.colliderect(coin):
        coins.remove(coin)
        score += 1
```

**Hint:** the sound is created but never played on pickup.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 4 · Explain the Code 📖

This is the heart of your finished game — the state machine that decides what screen the player sees and what each key does.

```python
current_state = "title"

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if current_state == "title":
                if event.key == pygame.K_SPACE:
                    current_state = "playing"
                elif event.key == pygame.K_l:
                    current_state = "level_select"
            elif current_state == "level_select":
                if event.key == pygame.K_RETURN:
                    current_state = "playing"
            elif current_state == "gameover":
                if event.key == pygame.K_r:
                    current_state = "title"

    if current_state == "title":
        draw_title()
    elif current_state == "level_select":
        draw_level_select()
    elif current_state == "playing":
        update_player()
        if player_died:
            current_state = "gameover"
    elif current_state == "gameover":
        draw_gameover()
```

**What value does `current_state` start as, and what screen does the player see first?**

<div class="write-space"></div>

**On the title screen, what do the SPACE key and the L key each do?**

<div class="write-space"></div>

**Inside the `"playing"` state, what makes the game switch to `"gameover"`?**

<div class="write-space"></div>

**From `"gameover"`, which key sends the player back, and back to which state?**

<div class="write-space"></div>

**Why does the code check `current_state` both in the event loop and again lower down when drawing?**

<div class="write-space"></div>

---

## 5 · Explain Your Lesson Code 🎥

This is your final presentation. Record a phone video of the **finished platformer YOU built across the course**. Show it running from title to victory, then explain the key parts of your own code. Try to use these words: **state machine**, **title**, **level select**, **sound**, **function**.

> 1. Show the title screen, then level select, then play through a level with sound.
> 2. Open your code and point to your state machine — explain how it moves between screens.
> 3. Show one function or class you are proud of and explain what it does.
> 4. Reach the victory screen, and say the hardest bug you fixed and how.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your finished-game presentation video to teacher on KakaoTalk.
