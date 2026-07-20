# Exercise 1 — The Clarification Drill

**Time:** 30 minutes total — three 8-minute rounds plus 6 minutes of self-grading.

**Format:** Solo. You play both candidate and interviewer. You will not write any code in this exercise — the entire 30 minutes is on the first phase of the round, the clarify phase, with three different problems.

**Why this exercise:** Most candidates spend 90% of their preparation time on the code phase. The clarify phase, which Lecture 1 argued is the highest-leverage 3 minutes of the round, is rehearsed almost never. This drill is the dedicated clarification rep, run in isolation, so the muscle memory builds without the cognitive load of the code phase competing for attention.

## The setup

You will need:

- A timer (phone is fine).
- A way to record yourself talking (Loom, QuickTime, OBS, Zoom-to-local — any of the Week 9 resources will do).
- A blank document for notes.
- The three problems below, *unread* until each round starts. Cover the problem text with a sticky note or a folded piece of paper, or have a friend reveal them one at a time.

## The protocol

For each of the three rounds:

1. **Start the timer for 8 minutes.**
2. **Start the recording.**
3. **Read the problem statement aloud.** Then stop reading further detail.
4. **Run the clarify phase out loud for 2-3 minutes.** Restate the problem, ask the clarifying questions, surface ambiguity. Do this as if a real interviewer were sitting across from you.
5. **After your clarify phase ends, switch to interviewer mode** and answer your own questions in a reasonable, consistent way. Speak the answers aloud. You are now playing the interviewer.
6. **Run the examples phase out loud for 2-3 minutes.** Walk through 2-3 concrete inputs and expected outputs.
7. **Stop the timer.** Note the elapsed time. Stop the recording.
8. **Self-grade against the rubric below** before moving to the next problem. Write your scores in the notes document.

The drill is not about writing the right test cases or asking the perfect questions. It is about running the clarify-and-examples phases under time pressure, with the speech-out-loud overhead, in a way that builds the reflex.

## The three problems

### Problem 1

**Statement:** "Given a sorted array of integers, return a sorted array of their squares."

That is the entire problem statement. Run the clarify phase.

### Problem 2

**Statement:** "Design a function that returns whether two given strings are anagrams of each other."

That is the entire problem statement. Run the clarify phase.

### Problem 3

**Statement:** "Given a binary tree, return its right-side view — the values of the nodes visible from the right side of the tree, ordered from top to bottom."

That is the entire problem statement. Run the clarify phase.

## The rubric

For each round, score yourself on the four axes below. Each axis is 0, 1, or 2. Total possible per round: 8. Total possible across three rounds: 24.

| Axis                                                              | 0 | 1 | 2 |
|-------------------------------------------------------------------|---|---|---|
| **Restated the problem in your own words** (not verbatim)         |   |   |   |
| **Asked at least 3 distinct clarifying questions**                |   |   |   |
| **Walked at least 2 concrete examples with expected outputs**     |   |   |   |
| **Surfaced at least one piece of ambiguity in the problem**       |   |   |   |

Scoring rule per axis:

- **0** — Did not happen. (Skipped the restate, asked zero questions, walked zero examples, surfaced no ambiguity.)
- **1** — Partially happened. (Restated but verbatim. Asked 1-2 questions. Walked 1 example. Identified the ambiguity but did not voice it as a question.)
- **2** — Cleanly happened. (Restated in own words. Asked 3+ distinct questions. Walked 2-3 examples including an edge case. Surfaced a real ambiguity and asked it.)

**Total target: 18/24 across the three rounds.** A score below 12 means the clarify-phase muscle is not yet built; repeat the exercise next week. A score of 18-21 means the muscle is forming. A score of 22-24 means the muscle is solid; you can drop this drill from your weekly routine.

## After the three rounds: review the recording

Watch each 8-minute recording back. For each, identify:

1. **One specific phrase you said that worked.** A clean restatement, a sharp clarifying question, a well-chosen example. Note it down. This is a phrase you should re-use.
2. **One specific phrase you said that was filler.** "Um," "I guess," "I think maybe," "kind of." Note it down. These are the tics to drill out of your default speech in mock interviews this week.
3. **One question you did *not* ask but should have.** Look at the problem statement again. What is the ambiguity you missed? The most common misses are: "can the input be empty?", "are there duplicates?", "what should I return if no answer exists?", "is the input guaranteed to be valid?"

Write these three observations for each round in your notes document. The pattern across the three rounds — the same missed question, the same filler tic — is your high-leverage improvement target for the rest of the week.

## What "good" looks like for each problem

Without giving the full solutions (those are in SOLUTIONS.md), here is the *number of clarifying questions* a strong candidate would ask for each problem, as calibration:

- **Problem 1 (squares of sorted array):** 4-6 clarifying questions. The interesting ones: can the array contain negatives (changes everything), can it be empty, can it have duplicates, what is the size of the array, does the input array need to remain unchanged.
- **Problem 2 (anagrams):** 4-7 clarifying questions. The interesting ones: case-sensitive or not, whitespace counted or not, what character set (ASCII only or Unicode), what about repeated letters, what if one is empty and the other isn't, what if both are empty.
- **Problem 3 (binary tree right view):** 5-8 clarifying questions. The interesting ones: how is the tree represented (TreeNode class, array form), what does "right side view" mean exactly (visible from the right, or the rightmost at each level), what if a node has only a left child (does it count), how to handle the empty tree, what is the return type.

If your clarify phase produced fewer than 3 questions on any of these problems, you are under-investing. The strong candidate over-asks; the weak candidate under-asks. The cost of an extra question is 5 seconds; the cost of a missed question is sometimes the whole round.

## When to repeat this exercise

Run this drill once per week for the first three weeks of your active interview cycle. After that, switch to running it before any specific high-stakes round — the day before an onsite, the morning of a phone screen. The drill is short enough (30 minutes) that the cost is low and the warmup-effect is large.

The single most-common piece of feedback from candidates who have rehearsed this drill: the first 2 minutes of every real round suddenly feel calm. The clarifying questions come out without thinking. The examples come out without thinking. The candidate has already paid the cognitive cost of the first phase in advance, in rehearsal, and the real round starts at minute 3 instead of minute 0.

## Reflection prompts

After running all three rounds and the post-recording review, write one or two paragraphs in your notes document on each of these prompts:

1. **Which problem was the hardest to clarify, and why?** Was it the ambiguity, the unfamiliarity, the pressure of switching roles between candidate and interviewer? Identifying the friction point is the precondition for fixing it.
2. **What is your default tic when you run out of things to ask?** Many candidates default to "do I have to handle negative numbers?" for every problem, even when the input type makes it irrelevant. Other candidates default to silence. Identifying your default tic lets you correct it deliberately rather than randomly.
3. **What is your plan for the next mock interview's clarify phase?** Specific, actionable, written down. "Ask at least 4 clarifying questions before moving on" is better than "do the clarify phase well." The specific plan is the one you will execute under pressure.

Save these reflections. In the mini-project's self-grading rubric, you will return to them and check whether your default behaviour has shifted.
