# 🚀 RS003 Extension — Meteor Shooter Review

**Topic:** Advanced Systems Review — Weapons, Homing Missiles, Combos & Nukes · **Course:** Pygame Space Shooter · **Time:** about 45 minutes

Your finished **Meteor Shooter** is bigger than the base game: five weapons, homing missiles, combo scoring, splash damage, a nuke, and a boss health bar. This worksheet reviews how those systems work. You only **read and think** — no typing in the app.

> 🧠 Words to know: **weapon system**, **cooldown**, **homing**, **combo multiplier**, **splash damage**

---

## 1 · Predict 🔮

Read each piece of code. Write what you think it does. Do not run anything.

```python
weapon_names = {1: "Normal", 2: "Shotgun", 3: "Laser", 4: "Missile", 5: "Wave Blaster"}
current_weapon = 3
print(weapon_names[current_weapon])
```

**The weapon system stores names in a dictionary. What word gets printed?**

<div class="write-space short"></div>

```python
b = {"x": 200, "y": 100, "color": MAGENTA, "r": 3}
b["y"] -= b.get("speed", BULLET_SPEED)
```

**A normal bullet has no `"speed"` key. `BULLET_SPEED` is 12. What is the bullet's new `y`?**

<div class="write-space short"></div>

```python
combo_counter = 12
multiplier = 1 + (combo_counter // 5)
score += 2 * multiplier
```

**After a 12-hit combo, an enemy worth 2 points is hit. How much does `score` go up?**

<div class="write-space short"></div>

```python
e["y"] += 1 + (score // 10)
```

**Enemies fall faster as your score climbs. When `score` is 30, how many pixels does an enemy drop each frame?**

<div class="write-space short"></div>

---

## 2 · Spot the Bug 🐛

Each block below is broken. Write the fixed code, then explain why the original was wrong.

**Bug A** — Holding SPACE should fire at a steady rate, but the Laser fires *every single frame* and floods the screen with bullets.

```python
if is_shooting:
    bullets.append({"x": spawn_x, "y": spawn_y, "vx": 0, "color": YELLOW, "r": 2})
```

**Hint:** the real game uses a **cooldown**. It only fires when `shoot_timer == 0`, then sets `shoot_timer` back up so a few frames must pass before the next shot.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — Reading a missile's splash radius crashes the game with `KeyError: 'splash'` whenever a *normal* bullet (which has no `"splash"` key) hits an enemy.

```python
splash_radius = b["splash"]
```

**Hint:** not every bullet carries every key. Ask the dictionary for the key *with a fallback* so a missing key gives 0 instead of crashing.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — Removing dead enemies while looping over the same list skips enemies, so some survive a hit they should not.

```python
for e in enemies:
    if bullet_hit(e):
        enemies.remove(e)
```

**Hint:** the real game never deletes from the list it is walking. It builds a **new list** of survivors and keeps that instead.

**Write the fixed code (build `surviving_enemies` and reassign):**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Explain the Code 📖

This is the **homing** logic that steers a missile toward the closest target. Read it carefully, then answer the questions. Reading only — do not run it.

```python
for b in bullets:
    if b.get("homing"):
        targets = list(enemies)
        if boss is not None:
            targets.append(boss)
        if targets:
            nearest = min(targets, key=lambda t: (t["x"] - b["x"]) ** 2 + (t["y"] - b["y"]) ** 2)
            if nearest["x"] > b["x"]:
                b["vx"] = min(b["vx"] + MISSILE_HOMING_STRENGTH, 5)
            elif nearest["x"] < b["x"]:
                b["vx"] = max(b["vx"] - MISSILE_HOMING_STRENGTH, -5)
```

**Only some bullets steer. Which key on the bullet decides whether this whole block runs?**

<div class="write-space"></div>

**`min(targets, key=lambda t: ...)` returns the *closest* target. The key measures distance but never takes a square root. Why is skipping the square root safe here?**

<div class="write-space"></div>

**If `nearest["x"]` is bigger than the missile's `x`, the target is to the right. Which way does `b["vx"]` change, and which way will the missile drift?**

<div class="write-space"></div>

**`min(b["vx"] + ..., 5)` and `max(b["vx"] - ..., -5)` clamp the sideways speed to between −5 and 5. What would go wrong if there were no clamp?**

<div class="write-space"></div>

**Why does the code check `if boss is not None` before adding the boss to `targets`?**

<div class="write-space"></div>

---

## 4 · Explain Your Lesson Code 🎥

Explain the Meteor Shooter code **you** built. Record a short phone video (show the game running) and talk through it like you are teaching someone. Try to use these words: **weapon system**, **cooldown**, **homing**, **combo multiplier**, **splash damage**.

> 1. Switch weapons with the number keys and show how `weapon_names[current_weapon]` changes the HUD.
> 2. Read your **cooldown** line out loud and explain why it stops the gun firing every frame.
> 3. Fire a missile and point out the **homing** and **splash damage** parts.
> 4. Build a **combo**, then explain how the **combo multiplier** grows your score.

**Write what you will say in your video. Plan it here before you record.**

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + a video explaining your Meteor Shooter code to teacher on KakaoTalk.
