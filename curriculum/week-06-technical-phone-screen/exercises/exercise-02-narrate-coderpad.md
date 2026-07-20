# Exercise 2 — Narrate on CoderPad

**Time:** ~90 minutes. **Output:** Three recordings of you solving easy LeetCode-shape problems on CoderPad while narrating the five-phase loop, scored against a narration rubric, with one re-recording of the weakest of the three.

## Goal

Practise the narration loop solo, on a real shared editor, against three easy LeetCode-shape problems back-to-back. The point is not to solve the problems — at this difficulty you can — but to **narrate the five phases out loud** while solving them at a pace and structure an interviewer could score. The recording catches the silent stretches, filler words, and missed phases that you cannot hear in real time.

This is the cheapest exercise of the week to fix mistakes on. Do it before Exercise 1, the pair mock; you'll walk into the pair mock already-fluent on the editor and on the narration loop.

## Setup

You need:

- A **CoderPad account** (or HackerRank CodePair if you prefer). Free tier. Create the account and run a one-liner before starting the drill.
- A **recording app** — Loom, QuickTime, or OBS. Capturing your screen and your audio is the load-bearing artefact of this exercise.
- A **stopwatch** — phone is fine. Each problem is a hard 25-minute timebox; do not let yourself go over.
- A **scratch pad and pen** — for the example-by-hand work.
- A **quiet room.**
- A **markdown file**: `c13-week-06/exercise-02-narrate-coderpad.md`.

## Process

### Step 1 — Tool warm-up (10 min)

In your markdown file, write down:

```markdown
## Tool setup

- Editor: ___ (CoderPad / HackerRank CodePair / CodeSignal)
- Language: ___ (Python / JavaScript / Java / Go / C++)
- Recording app: ___ (Loom / QuickTime / OBS)
- Headset: ___ (wired / Bluetooth)
- Browser: ___ (Chrome / Firefox / Safari / Edge)
```

Then:

- Open the editor on a fresh pad.
- Switch to your chosen language. Write `print("hello")` (or the equivalent) and run it. Confirm the run pane shows the expected output.
- Open the recording app. Start a short test recording — 30 seconds of you talking — and verify the audio and screen capture both work.
- Open your prep doc in a second tab. Confirm tab-switching works without breaking the recording.

Total: under 10 minutes. If anything fails, fix it now, not during the drill.

### Step 2 — The three problems

You will solve all three back-to-back, with a 5-minute break between each, recording every problem. Pick from these six (alternates listed if you've recently done one):

**Slot 1 — Array / hash map family** (pick one)
- LeetCode 1: Two Sum
- LeetCode 217: Contains Duplicate
- LeetCode 242: Valid Anagram

**Slot 2 — String family** (pick one)
- LeetCode 125: Valid Palindrome
- LeetCode 14: Longest Common Prefix
- LeetCode 387: First Unique Character in a String

**Slot 3 — Two-pointer / sliding family** (pick one)
- LeetCode 26: Remove Duplicates from Sorted Array
- LeetCode 121: Best Time to Buy and Sell Stock
- LeetCode 283: Move Zeroes

If you have already done several of these recently, swap in any easy LeetCode you haven't seen, but **keep the difficulty at easy**. The exercise is not testing your problem-solving; it is testing your narration.

In your markdown file:

```markdown
## Selected problems

- Slot 1: ___ (Problem name + number)
- Slot 2: ___
- Slot 3: ___
```

### Step 3 — The drill (75 min total: 3 × 25-min problems + 2 × 5-min breaks)

For each problem:

#### Setup (1 min)

- Open a fresh CoderPad pad.
- Confirm language and recording.
- Note the start time.

#### The 25-minute timebox (25 min)

Hard timebox. The interviewer's clock is the real constraint; practise against it.

You will narrate the five phases out loud. Even though no one is on the call, **speak as if the interviewer is there**. The recording is the proxy.

- **Phase 1 — Restate (60-90 sec).** Read the problem aloud. Then say "let me restate" and restate it in your own words. Pretend the interviewer just gave it to you.
- **Phase 2 — Example (90-150 sec).** Walk through one example on scratch paper, out loud. Trace through what the output should be and why.
- **Phase 3 — Brute force (60-90 sec).** State the brute force out loud. Name the complexity. "The brute force is {description}, which is O({complexity})."
- **Phase 4 — Optimise (60-180 sec).** Propose an optimisation. Name the new complexity. "I can do better with {pattern}. That brings it to O({complexity})."
- **Phase 5 — Code while narrating (15-20 min).** Code the optimised solution. Narrate at the start of each coding burst and at the end. Run the code. Test on the original example, an edge case, and a stress case. Catch any bugs.

The 25 minutes is the timebox even if you finish in 18 or are still going at 25. If you finish early, narrate the testing phase more deeply. If you hit 25 with code unfinished, stop and write down where you are.

#### Wrap (2 min per problem)

In your markdown file:

```markdown
## Problem 1 — {name}

- Start time: ___
- Finish state: ___ (finished cleanly / finished with bugs / unfinished)
- Time to first line of code: ___
- Total spoken time (estimate): ___ out of 25 min
- Filler-word count (estimate, from re-watch): ___
- One specific moment you went silent for >60 seconds: ___
```

### Step 4 — The break and the next problem (5 min between problems)

Stand up, walk away from the screen for 5 minutes. Do not check messages, do not read social media, do not edit code. The break is for resetting your voice and attention, not for catching up on email.

Then back in. The second problem is harder than the first because of fatigue, even at the same difficulty rating. That is the point of doing three; the second and third are calibration for the real-cycle scenario where you have two or three screens in a week.

### Step 5 — Self-review (25 min)

Re-watch all three recordings. For each, score yourself against the narration rubric:

| Phase | Score 1-5 | What it looks like |
|-------|----------:|---------------------|
| **Phase 1 — Restate** | __ | 5: clean restatement, asked 2-3 clarifying questions. 3: read the problem, briefly summarised. 1: jumped straight to coding. |
| **Phase 2 — Example** | __ | 5: walked through one full example on paper, out loud, with output. 3: mentioned an example briefly. 1: skipped. |
| **Phase 3 — Brute force** | __ | 5: stated brute force, named complexity, said why it's insufficient. 3: mentioned brute force. 1: skipped. |
| **Phase 4 — Optimise** | __ | 5: proposed optimisation, named new complexity, sketched the approach before coding. 3: jumped to optimised approach without naming the brute force. 1: no optimisation discussion. |
| **Phase 5 — Code+narrate** | __ | 5: narrated at start and end of every coding burst, no silent stretch over 90 seconds, ran tests with narration. 3: 1-2 silent stretches over 90 seconds. 1: silent for 5+ minutes at a stretch. |

Total: __ / 25 per problem.

In the markdown file:

```markdown
## Self-review

### Problem 1 — {name}
- Phase 1: __ / 5. Notes: ___
- Phase 2: __ / 5. Notes: ___
- Phase 3: __ / 5. Notes: ___
- Phase 4: __ / 5. Notes: ___
- Phase 5: __ / 5. Notes: ___
- Total: __ / 25

### Problem 2 — {name}
(same structure)

### Problem 3 — {name}
(same structure)
```

### Step 6 — Re-record the weakest problem (15 min)

Identify the problem with the lowest total score. Re-record it on a fresh CoderPad pad, focusing on the specific phases that scored low. Goal: a measurably higher score on the same rubric.

In the markdown file:

```markdown
## Re-recording — Problem __ ({name})

- Original total: __ / 25
- Re-recording total: __ / 25
- Change: +__
- The specific fix I made: ___
- The specific thing still weak: ___
```

## Acceptance

- Three recordings exist (one per problem), each 20-25 minutes, with both audio and screen.
- All three are scored against the narration rubric.
- A re-recording of the lowest-scored problem exists, with a measurable score improvement.
- The markdown file is committed to your portfolio repo.
- A one-paragraph summary at the bottom of the file: which phase is your weakest across all three problems, and what habit you'll use to fix it.

## Common findings

Most candidates discover at least one of these in re-watch:

- **Phase 2 (Example) is skipped or compressed to 15 seconds.** This is the most-common gap; the example-by-hand is the cheapest place to find bugs, and skipping it costs the call.
- **Phase 3 (Brute force) is skipped because you already know the optimised approach.** Reads as memorised. Fix: name it anyway, even briefly.
- **Phase 5 (Code+narrate) has 2-3 silent stretches of 90+ seconds.** The most-common scoring gap. Fix: narrate at the start of each coding burst, even if just "I'm setting up the loop now."
- **Testing is compressed to 20 seconds at the end.** Fix: budget 3-5 minutes for testing. Run on three inputs out loud.

## Stretch

- **Do a fourth problem on a different shared editor.** If you did three on CoderPad, do the fourth on HackerRank CodePair. The friction reveals the muscle memory.
- **Run the recordings through Yoodli** for AI-assisted feedback on filler words and pace. Filler-word counts above 30 per 10 minutes are a flag.
- **Compare your recording to one of the public interviewing.io recordings.** Watch a 30-minute candidate recording; score it against the same rubric. Then re-score yourself. The calibration tightens.
- **Repeat once a week through the rest of the cycle.** The narration drill is the maintenance dose for technical-screen readiness. Twenty minutes a week keeps the fluency live.
