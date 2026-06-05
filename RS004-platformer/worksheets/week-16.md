# 🏆 RS004 Week 16 — English Worksheet

**Topic:** Title · Level Select · Sound · Showcase (Final) · **Course:** Platformer Game · **Time:** about 45 minutes

This is the final week. You polish 15 weeks of work into a finished game: a **title screen**, a **level select** menu, and **sound** for jumps and coins. The whole thing runs on a **game state machine** that moves between title → level select → playing → game over / victory. Then you **present** it.

> Keep these words handy: **state machine**, **title screen**, **level select**, **sound**, **showcase**.

---

## 1 · Predict 🔮

Read each snippet. Before you run it, write what you think will happen.

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

Draw arrows (write them out) showing which state leads to which. Fill in the blanks.

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

Each snippet is broken. Rewrite it so it works, then explain why the original was wrong.

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

## 4 · Polish Pass 🛠️

Start from your working state machine. Add polish one piece at a time.

1. Add your own title text and a "press space to start" line. What does your title say?

<div class="write-space"></div>

2. Add a jump sound *and* a coin sound. When does each play?

<div class="write-space"></div>

3. **Stretch:** add a creator screen with your name, or a death sound, or a screen shake on Game Over. What did you add?

<div class="write-space"></div>

---

## 5 · Finish & Showcase 📸

Bring it all together into your finished game: title → level select → at least three of your own levels → victory, with sound.

Send a **photo or video** of a full play-through (title to victory), then write your **showcase notes** below. Write 4 to 6 sentences.

> The part of my game I am most proud of is …
>
> My favourite function or class is ___, and it works by …
>
> My game state machine moves from … to … to …
>
> The hardest bug I solved this term was …
>
> If I kept building, I would add …
>
> One thing I can do now that I couldn't 16 weeks ago is …

<div class="write-space tall" style="min-height: 360px"></div>

---

## 6 · Showcase Walkthrough 🎥

Record your final showcase video — this is the one you present. Teach your game to someone who has never seen it. Try to use these words: **state machine**, **title**, **level select**, **sound**, **function**.

> 1. Show the title screen, then level select.
> 2. Play through a full level with sound.
> 3. Show one function or class you are proud of and explain it.
> 4. Reach the victory screen.
> 5. Say the hardest bug you fixed and how.

**Write what you will say in your showcase.** Plan it here first.

<div class="write-space tall" style="min-height: 360px"></div>

---

### Submit ✅

Send this worksheet + your finished game video + your showcase notes to teacher on KakaoTalk.
