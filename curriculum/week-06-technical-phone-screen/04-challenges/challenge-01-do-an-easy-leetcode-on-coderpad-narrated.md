# Challenge 1 — Do an easy LeetCode on CoderPad, narrated

**Time:** ~30-45 minutes (5 prep + 25 drill + 10 review). **Difficulty:** Easy/Medium. **Materials:** CoderPad (or HackerRank CodePair), a recording app, a stopwatch, scratch paper, this file open as the prompt list.

## Problem

The single load-bearing skill of Week 6 is the ability to **solve one easy LeetCode-shape problem on a real shared editor while narrating in the five-phase loop, in 25 minutes, recorded**. Exercise 2 builds this skill across three problems. Exercise 1 pressure-tests it under a live partner. This challenge isolates the single rep.

Why a challenge and not just another Exercise-2 slot: the challenge adds three constraints that the exercises do not:

- **You do not pick the problem.** Pick from the bank below by rolling a die, drawing randomly, or asking a friend to pick one for you. The friction of an unpicked-by-you problem is closer to a real call.
- **The 25-minute timebox is hard.** No going over. If you hit 25 with code unfinished, stop. The recording captures the unfinished state; the review is about *why* you ran out of time.
- **The post-call review is mandatory and structured.** A 10-minute re-watch with the rubric, not a vibes-based "I think that went okay."

## Protocol

### Part A — Prep (5 min)

In `c13-week-06/challenge-01-coderpad-narrated.md`:

```markdown
## Tool setup

- Editor: ___
- Language: ___
- Recording app: ___
- Browser: ___

## Problem selection

Roll a six-sided die (or use a random.org pick). The number selects the problem:

1. LeetCode 1 — Two Sum
2. LeetCode 217 — Contains Duplicate
3. LeetCode 125 — Valid Palindrome
4. LeetCode 26 — Remove Duplicates from Sorted Array
5. LeetCode 283 — Move Zeroes
6. LeetCode 121 — Best Time to Buy and Sell Stock

If you've solved the picked problem in the last 30 days, re-roll.

- Selected problem: ___
- Why this picked: rolled __ on the die.
```

Open the CoderPad pad, switch to your language, run a one-liner, confirm the recording is on. Total: under 5 minutes.

### Part B — The drill (25 min)

Set the stopwatch for 25 minutes. Start the recording. Open the LeetCode page for the picked problem in a tab; read the problem statement aloud (this simulates the interviewer reading it to you), then close that tab and work only in the CoderPad pad.

Run the five-phase loop:

- Phase 1 — Restate (60-90 sec).
- Phase 2 — Example by hand (90-150 sec). On scratch paper, out loud.
- Phase 3 — Brute force (60-90 sec). Name it and the complexity, even if you immediately see the optimisation.
- Phase 4 — Optimise (60-180 sec). Name the new complexity. Sketch the approach.
- Phase 5 — Code and test (15-20 min). Narrate in beats. Test on the original, an edge, and a stress case.

When the stopwatch hits 25, stop. Even mid-line of code. Note the state.

In your markdown file:

```markdown
## Drill execution

- Stopwatch start: ___
- Stopwatch end: ___
- Finish state: ___ (finished cleanly / finished with bugs / unfinished — what stage)
- Time to first line of code: ___ minutes
- Total spoken time (estimate after re-watch): ___
- Longest silent stretch: ___ seconds
- Number of times you said "um" / "uh" / "like" (estimate after re-watch): ___
```

### Part C — Review (10 min)

Re-watch the recording. Score against the same five-phase rubric from Exercise 2:

| Phase | Score 1-5 | Notes (timestamp) |
|-------|----------:|-------------------|
| Phase 1 — Restate | __ | |
| Phase 2 — Example | __ | |
| Phase 3 — Brute force | __ | |
| Phase 4 — Optimise | __ | |
| Phase 5 — Code+narrate | __ | |

Total: __ / 25.

Then: identify the **single highest-leverage fix**. Not three; one. Write it as a habit:

```markdown
## Single highest-leverage fix

The one habit I'll bring to the next narrated drill: ___

Specifically, when I notice ___, I will ___.
```

## Acceptance

- Recording exists, 20-25 minutes, with audio and screen.
- Markdown file completed: tool setup, problem selection, drill execution, scored review.
- One specific habit identified.
- Recording is committed (or linked) to the portfolio.

## When to use this challenge

- **Between Exercise 2 and Exercise 1.** Exercise 2 builds the muscle; the challenge tests it under pressure; Exercise 1 puts it in front of a live partner.
- **The morning of a real technical phone screen.** A 30-minute warm-up rep keeps the muscle live. Many candidates report measurably better real-call performance after a morning-of warm-up.
- **As a weekly maintenance dose.** Once you have done Week 6, the narration muscle degrades unless used. Twenty to thirty minutes weekly through Week 7 and beyond keeps it ready.

## Stretch

- **Roll twice, do both problems back-to-back.** The fatigue across two 25-minute drills is closer to the cycle reality of two-screens-in-a-week. The second drill usually scores 1-3 points lower; that is the calibration.
- **Pick the language you do not usually pick.** If you always do Python, run the challenge in JavaScript or Go. The friction reveals language-fluency gaps you would not see in your default language.
- **Run on a different editor.** CoderPad → HackerRank CodePair, or vice-versa. Same drill, different tool. The first time on the second editor will be measurably slower; that gap is the cost of single-editor practice.
