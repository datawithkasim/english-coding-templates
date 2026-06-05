# 🏆 WD001 Week 8 — English Worksheet

**Topic:** Final Project — One-Page Personal Site · **Course:** Web Design: CSS · **Time:** about 45 minutes

This is your **final build**. You will combine everything from the last seven weeks into one cohesive one-page site about you: a hero section, a menu, cards, hover effects, and a responsive layout — all sharing one colour palette so it feels like **your** site.

> Your site should include all of these:
>
> - a **hero section** (background image + heading + short intro)
> - a **navigation menu** (Flexbox)
> - **3 or more cards** (hobbies, favourites, dreams…)
> - **hover effects**
> - a **responsive** layout that works on a phone
> - a **consistent colour palette**

---

## 1 · Plan First 🔮

Before you write code, sketch your site so you know what you are building. Picture your page from top to bottom.

**List the sections of your page in order, from top to bottom.**

<div class="write-space"></div>

**Which week's idea does each section come from? (For example: hero → Week 5, menu → Week 4.)**

<div class="write-space"></div>

**Pick your colour palette: write down 2 or 3 colours you will use everywhere (you can write them as names or hex codes like `#d4380d`).**

<div class="write-space"></div>

**Which 3 things will your cards be about?**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

These bugs mix up ideas from across the whole course. Read what each is **supposed** to do, then rewrite it so it works, and explain your fix.

**Bug A** — The hero text is supposed to sit in the middle, but it is stuck in the corner.

```html
<style>
  .hero {
    background-image: url('me.jpg');
    background-size: cover;
    height: 400px;
  }
</style>
```

**Hint:** centring in the hero needs `display: flex` plus centring across and down.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — On phones the cards are supposed to stack, but they stay squished in a row.

```html
<style>
  .cards {
    display: flex;
  }
  @media (min-width: 600px) {
    .cards {
      flex-direction: column;
    }
  }
</style>
```

**Hint:** should the column rule run on **small** screens or **big** ones?

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The card is supposed to grow smoothly on hover, but it snaps and the colours clash with the rest of the page.

```html
<style>
  .card:hover {
    transform: scale(1.05);
    background-color: lime;
  }
</style>
```

**Hint:** add a `transition` for smoothness, and pick a hover colour that matches your palette.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Site 📸

In Replit, combine your work from Weeks 1–7 into **one page**. Bring in your hero, your menu, your cards, your hover effects, and your responsive media query. Then polish: make all the colours and fonts match so it feels like one site.

Work in this order so it stays manageable:

1. Start with the **hero section** at the top.
2. Add your **menu** under it.
3. Add your **row of cards**.
4. Add **hover effects** to the cards.
5. Add a **media query** so it stacks nicely on a phone.
6. Go back and make every colour fit your **palette**.

When you finish, send a **PC screenshot and a phone screenshot** of your finished site (a Replit link is welcome too), then explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> My site has these sections …
>
> I used Flexbox in …
>
> My hover effects are on …
>
> On a phone my site changes by …
>
> The hardest part was …
>
> The part I'm most proud of is …

<div class="write-space tall" style="min-height: 340px"></div>

---

## 4 · Present Your Site 🎥

This week you **present** your finished site, like a real designer showing their work. Take a video on your phone (or a parent's phone) and walk through everything you built. Try to use these words: **hero**, **flexbox**, **hover**, **responsive**, **palette**.

> 1. Show your full site, scrolling from top to bottom.
> 2. Say what each section is and which week's idea it came from.
> 3. Point out where you used Flexbox and where you used hover effects.
> 4. Make the window narrow (or show your phone) and say how the layout changes.
> 5. Finish with the hardest part and how you solved it.

**Write what you will say in your presentation.** Use the space below to plan it before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 340px"></div>

---

### Submit ✅

Send this worksheet + your PC and phone screenshots + your presentation video to teacher on KakaoTalk.
