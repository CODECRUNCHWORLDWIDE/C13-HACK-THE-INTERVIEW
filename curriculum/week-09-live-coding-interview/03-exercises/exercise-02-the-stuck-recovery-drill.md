# Exercise 2 — The Stuck-Recovery Drill

**Time:** 45 minutes total — 40 minutes for the mock interview, 5 minutes for self-grading.

**Format:** Solo, with a recording. The problem is deliberately chosen to be one notch above your comfort level so that the stuck-recovery moves are exercised. You will hit a wall in this drill. That is the point. The drill is the rehearsal of the recovery, not of the solve.

**Why this exercise:** Failure mode 3 — getting stuck silently — is the failure mode most candidates have *no rehearsed response to* because their LeetCode practice avoids it. When the candidate is alone on the couch, hitting a wall, they look at the hint button or open the editorial; there is no externally-visible stuck-state, so there is no rehearsal of the recovery. This drill removes the hint button. You hit the wall; you stay there; you exercise the three moves (verbalise, clarify, simplify) until the wall comes down.

## The setup

You will need:

- A 45-minute uninterrupted block of time.
- A recording setup (screen + audio).
- A blank Python file (or your preferred language) and a timer.
- The problem below, *unread* until the timer starts.
- The Lecture 2 stuck-recovery moves in your head: verbalise the stuck-point, ask a clarifying question, simplify the problem. Re-read them once before starting.

You will **not** use:

- LeetCode, Google, Stack Overflow, an LLM assistant, or any external reference. The drill is closed-book.
- A hint button, an editorial, or any reveal of the solution. If you get stuck, you stay stuck until the three moves get you out.

## The protocol

1. **Set the timer for 40 minutes.** Start recording.
2. **Read the problem statement aloud.** Run the clarify phase out loud, playing both candidate and interviewer. Give yourself reasonable, consistent answers.
3. **Run the full six-phase round.** Clarify, examples, approach, code, test, discuss. Out loud. Type as you go.
4. **When you get stuck — and you will — apply the three moves, in order, out loud:**
   - **Move 1:** Verbalise the stuck-point. "I am stuck because X."
   - **Move 2:** Ask a clarifying question (to yourself, as the interviewer). "Just to double-check, can the input have X?"
   - **Move 3:** Simplify the problem. "Let me solve a simpler version of this first — imagine X were Y."
5. **Do not stop the recording until either the timer hits 40 minutes or you have a working solution that passes your test cases.** The recording captures the stuck moments and the recovery moments; the recording is the artifact you grade against.
6. **After the timer ends, take 5 minutes** for self-grading using the rubric below.

## The problem

**Statement:**

> Given a list of meeting time intervals as `[start, end]` pairs, find the minimum number of conference rooms required to schedule all the meetings.

**Constraints to assume (you should still ask them out loud as part of the clarify phase):**

- The list has between 0 and 10,000 intervals.
- `start` and `end` are non-negative integers, `start < end`.
- A meeting that starts at time `T` and another that ends at time `T` can use the same room (shared endpoint is fine).

**Why this problem:**

This is one notch harder than the "can a person attend all meetings" problem from Lecture 3. The naive approach is recognisable but the optimal approach requires either a sweep-line algorithm (using a sorted list of events) or a min-heap of end times. Both approaches involve a non-obvious data-structure choice and are the kind of problem where most candidates hit a wall around minute 10-15.

If you have already seen this problem and remember the solution clearly, skip ahead to the **alternate problem** below. The drill only works if you genuinely hit a wall.

### Alternate problem (if you have already seen Meeting Rooms II)

**Statement:**

> Given a non-empty array of strings `words` and an integer `k`, return the `k` most frequent words in the array. The result should be sorted by frequency from highest to lowest. If two words have the same frequency, the word with the lower alphabetical order comes first.

**Constraints to assume:**

- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, number of unique words]`.

This is a variant of "top K frequent" that requires a custom comparator for the heap (frequency descending, alphabetical ascending for ties). The custom-comparator move is where most candidates trip.

## The rubric

After the 40-minute round, score yourself on the six axes below. Each axis is 0, 1, or 2. Total possible: 12.

| Axis                                                                                      | 0 | 1 | 2 |
|-------------------------------------------------------------------------------------------|---|---|---|
| **Ran the clarify phase before coding (out loud, with at least 3 questions)**             |   |   |   |
| **Walked at least 2 concrete examples before coding**                                     |   |   |   |
| **Stated the brute force complexity before proposing the optimisation**                   |   |   |   |
| **When stuck, applied at least one of the three moves explicitly out loud**               |   |   |   |
| **Tested your code with at least one example traced line-by-line**                        |   |   |   |
| **Stated final complexity (time and space) at the end of the round**                      |   |   |   |

Scoring per axis:

- **0** — Did not happen.
- **1** — Happened partially or in the wrong phase order.
- **2** — Happened cleanly and at the right time.

**Target: 9/12.** A score below 6 means the structure is not yet on muscle memory; rerun this drill next week with a different problem. A score of 9-10 means the structure is forming but recovery is slow. A score of 11-12 means the structure and the recovery are both solid; you are ready for live mocks with humans.

## After the round: review the recording

Watch the recording back at 1.5x or 2x speed. Note the timestamps of:

1. **The first time you went silent for more than 15 seconds.** Note what was happening just before the silence and what was happening just after. This is your stuck-point pattern.
2. **Every time you applied one of the three moves.** Was it verbalise, clarify, or simplify? Did the move actually unstick you, or did you remain stuck?
3. **Every "um," "I guess," "maybe," or "I think" filler word in the first 5 minutes.** Count them. The Week 9 goal is to have under 5 fillers in the first 5 minutes; most candidates start at 20+.
4. **The moment you committed to the final approach.** What time was it? How did you arrive at the commitment? Was it after a clean approach phase, after a struggle, after a moment of insight?

Write these timestamps and observations in your notes document.

## What "stuck" should look like

If you executed the drill correctly, the recording should contain at least one stuck moment lasting 60-180 seconds. The stuck moment should feature:

- You verbalising the stuck-point out loud.
- You either asking yourself a clarifying question, or attempting to simplify, or both.
- A recovery — the moment where you said "okay, I see it now" or equivalent — within 3 minutes of the start of the stuck-spiral.

If your recording contains zero stuck moments, one of two things happened:

1. **The problem was too easy for you.** Pick a harder one from LeetCode Medium and rerun. The drill only works at the edge of your competence.
2. **You skipped past the stuck moments without acknowledging them.** This is more common. Watch the recording again with the question "where did I almost go silent?" in mind. Those near-misses are where the recovery rehearsal would have happened if you had let yourself slow down. Next time, slow down.

If your recording contains a 5+ minute stuck moment with no recovery, the drill is still useful — it surfaces that your recovery moves are not yet reflex. Re-read Lecture 2's three moves, rehearse the exact phrases out loud (without a problem), and rerun this drill next week. The recovery is a skill; it gets better with deliberate practice.

## Reflection prompts

After grading and reviewing, write one or two paragraphs on each of these:

1. **Which of the three moves did you actually use?** Most candidates default to "simplify" (because it feels productive) and skip "verbalise" (because it feels like admitting weakness). The verbalise move is the cheapest and the highest-leverage; if you skipped it, that is your improvement target.
2. **What did the stuck moment feel like from inside?** Panic? Frustration? Calm? The emotional state during the stuck moment is half the round; calm-during-stuck is a rehearsable skill, and identifying your default emotional response is the precondition.
3. **What is your specific plan for the next time you get stuck?** "I will verbalise within 15 seconds and try simplifying within 60 seconds." Specific, time-bounded, written down. The specific plan is the one you execute under pressure.

## When to repeat this exercise

Run this drill once before any high-stakes round. Pick a problem one notch above your comfort level each time — the comfort zone moves as you practise, so the drill stays at the edge. The drill is short enough (45 minutes total) that the warmup effect carries cleanly into the same-day real round if scheduled correctly.

A specific suggestion: the morning of an onsite day, run this drill on a problem you have not seen before, 6-8 hours before the first round. The morning-of warm-up is the single highest-leverage pre-round move most candidates do not make.
