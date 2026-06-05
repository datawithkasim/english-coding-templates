# ⚡ WD002 Week 8 — English Worksheet

**Topic:** Final Project — Interactive Quiz App · **Course:** Web Dev Basics: JavaScript · **Time:** about 45 minutes

This is the big one. You will combine **everything** from the last 8 weeks — variables, the DOM, events, input, conditionals, arrays, loops, and functions — into your own **interactive quiz app**. You already have all the pieces. This week you put them together and present.

---

## 1 · Recall 🧠

Before you build, prove to yourself that the pieces are ready. Answer from memory — peek at earlier weeks only if you are stuck.

**Write an array of 3 of your own quiz questions, as objects. (Look at the shape: each has a question, choices, and the answer index.)**

```
let questions = [
  { q: "______", choices: ["___", "___", "___"], answer: __ },
  ...
];
```

<div class="write-space"></div>

**Which line below shows a question on screen, and which one checks the answer? Label each.**

```
document.querySelector("#question").textContent = questions[current].q;
if (chosen === questions[current].answer) { score = score + 1; }
```

<div class="write-space"></div>

**How do you move to the next question and know when the quiz is over? Write it in plain English.**

<div class="write-space"></div>

---

## 2 · Spot the Bug 🐛

Each block is part of a quiz app, but it is broken. Read what it is **supposed** to do, then rewrite it so it works. Explain why the original was wrong and why your fix works.

**Bug A** — A correct answer should add 1 to the score. Right now the score goes up **every** time, even on wrong answers.

```
function checkAnswer(chosen) {
  score = score + 1;
  current = current + 1;
}
```

**Hint:** the score should only rise when `chosen` matches the correct answer. Add an `if`.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug B** — After the last question, the quiz should stop and show the final score. Right now it crashes with `undefined` because it tries to show a question that does not exist.

```
function checkAnswer(chosen) {
  current = current + 1;
  showQuestion();
}
```

**Hint:** check whether `current` is still less than `questions.length` before showing another question.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

**Bug C** — The restart button should set everything back to the start. Right now it resets the score but the quiz stays on the last question.

```
function restart() {
  score = 0;
  showQuestion();
}
```

**Hint:** one more variable needs to go back to 0 before the first question can show.

**Write the fixed code:**

<div class="write-space"></div>

**Why was it wrong? Why does your fix work?**

<div class="write-space"></div>

---

## 3 · Build Your Quiz App 📸

Now build the real thing. Your quiz app must have:

1. **At least 5 questions** stored in an array (each one an object with a question, choices, and the correct answer).
2. One question shown at a time, with its answer choices on buttons.
3. A correct answer adds 1 to the score; a wrong answer adds 0.
4. The **final score** shown after the last question.
5. A **restart** button that begins the quiz again from question 1.

Make your questions about something you love — games, K-pop, animals, your favorite show. It is your app.

**Stretch:** show which questions you got wrong, add a timer, or make the page celebrate a perfect score.

When you finish, send a **photo or video** of a full play-through (answering questions, then the final score, then a restart), and explain what you did. Use these sentence starters — write 4 to 6 sentences total.

> First, I designed my questions as …
>
> To show one question at a time, I …
>
> The score goes up only when …
>
> My restart button works by …
>
> The hardest part was …
>
> The part I am most proud of is …

<div class="write-space tall" style="min-height: 360px"></div>

---

## 4 · Final Presentation 🎤

Record a video where you **present** your finished quiz app, like you are showing it to someone for the first time. Try to use these words: **array**, **object**, **score**, **function**, **condition**.

> 1. Play through your quiz from start to final score, then restart it.
> 2. Show how your quiz questions are stored (array + objects).
> 3. Point to where the answer-checking logic lives.
> 4. Explain how the score is saved and shown on screen.
> 5. Say what was hardest and how you solved it.

**Write what you will say in your presentation.** Plan it here before you record — you can read from it while filming.

<div class="write-space tall" style="min-height: 360px"></div>

---

### Submit ✅

Send this worksheet + your finished quiz app (video of it running, and a photo of the full code or a Replit link) to teacher on KakaoTalk.
