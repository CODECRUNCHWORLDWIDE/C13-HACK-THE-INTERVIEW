# Exercise 1 — Mock screen with a peer

**Time:** ~90 minutes (15 prep + 45 mock + 30 review). **Output:** A 45-minute recorded mock technical phone screen on a real shared editor, a scored self-review against the rubric, and a list of three issues to fix before the real call.

## Goal

Run a full-length technical phone screen with a peer playing the interviewer, on a real shared editor (CoderPad or HackerRank CodePair), with audio recording. Walk through all five phases of the narration loop on at least one problem, finish testing, take a follow-up question, and ask one or two questions back. Then score yourself against the rubric and identify the three issues most worth fixing before a real call.

## Setup

You need:

- A **peer who will play interviewer for 60 minutes** (45 for the mock plus 15 for the debrief). Ideal: a C13 cohort member who has read this week's lectures, a C2 peer, or a working engineer.
- A **shared editor account** — CoderPad or HackerRank CodePair, free tier. Both you and the peer must be able to access the same pad.
- A **recording app** — Loom, QuickTime, or OBS. Capturing your screen and audio is enough; capturing the peer's video is nice-to-have.
- A **wired headset** — the audio setup you'll use on the real call. Bluetooth is acceptable for practice but discouraged for the real call.
- A **markdown file**: `c13-week-06/exercise-01-pair-mock.md`. The peer-script section is below; copy it into a doc you share with your peer.
- A **stopwatch** — phone is fine.
- A **scratch pad and pen** — for the example-by-hand work and the trace tables.
- A **quiet room.**

## Process

### Step 1 — Schedule and prep with the peer (15 min)

Send the peer:

- A link to **lecture-notes/01** and **lecture-notes/02** of this week. They do not need to read all of it; they need to know the five-phase narration loop and the four scoring dimensions.
- The **peer script** (Step 2 below). Ask them to skim it before the call. Tell them which problem they'll be running you through; do not tell yourself.
- The **scoring rubric** (Step 4 below). They should be ready to score you on it during the call.
- A **calendar invite** with the shared-editor link, the recording-app link if you're using Loom, and a 60-minute block.

Two ground rules for the peer:

- **Play the interviewer, not your friend.** They should be running the rubric, not coaching you mid-call. Coaching is the debrief.
- **Be willing to offer one hint if you genuinely look stuck for more than 2 minutes.** The hint is part of the calibration. Note in the debrief whether they had to offer it.

### Step 2 — The peer script (the peer reads this)

```markdown
# Peer script — Week 6 Exercise 1 pair mock

You are playing the interviewer in a 45-minute technical phone screen.
The candidate is preparing for a real screen in the next 1-3 weeks.

## Your job

- Run the call on the timing in Section 6 of lecture-notes/01.
- Pick **one of the three problems below** without telling the candidate which one.
- Score them against the rubric below during the call.
- Be ready to offer **one hint** if they look genuinely stuck for 2+ minutes.

## The candidate-side schedule

- Minutes 0-3: greet, audio check, brief self-intro.
- Minutes 3-8: you read the problem; they ask clarifying questions.
- Minutes 8-12: they walk through an example, sketch the brute force.
- Minutes 12-15: they propose an optimisation.
- Minutes 15-35: they code.
- Minutes 35-40: they test.
- Minutes 40-43: you ask one follow-up question (one of the four patterns
  in Exercise 3 — complexity, extension, production, edge case).
- Minutes 43-45: they ask 1-2 questions; close.

If they finish coding by minute 30, you can ask a small extension to fill
the remaining 5 minutes.

## The three candidate problems (pick one; don't tell the candidate)

### Problem A — Two Sum

> Given an array of integers `nums` and an integer `target`, return indices of
> the two numbers in `nums` that add up to `target`. You may assume that each
> input has exactly one solution; you may not use the same element twice.
>
> Examples:
>   nums = [2, 7, 11, 15], target = 9   → [0, 1]
>   nums = [3, 2, 4],     target = 6   → [1, 2]
>
> Expected progression: brute O(n²) double loop → hash-map O(n).

### Problem B — Valid Parentheses

> Given a string `s` containing only the characters `()[]{}`, return whether
> the string is a valid balanced-and-correctly-nested set of parentheses.
>
> Examples:
>   "()"     → true
>   "()[]{}" → true
>   "(]"     → false
>   "([)]"   → false
>
> Expected progression: stack-based single pass O(n). The candidate should
> arrive at the stack approach quickly; the test is whether they handle the
> edge cases (empty string, single open, mismatched close) cleanly.

### Problem C — Best Time to Buy and Sell Stock

> Given an array `prices` where `prices[i]` is the price of a stock on day i,
> find the maximum profit from one buy-sell pair (sell must be after buy). If
> no profit possible, return 0.
>
> Examples:
>   prices = [7, 1, 5, 3, 6, 4] → 5    (buy at 1, sell at 6)
>   prices = [7, 6, 4, 3, 1]    → 0
>
> Expected progression: brute O(n²) all-pairs → single-pass O(n) tracking the
> minimum seen so far.

## Scoring rubric (you fill this out during the call)

| Dimension | Score 1-5 | Notes |
|-----------|----------:|-------|
| Problem-solving (clarification, example, brute force, optimisation) | __ | |
| Coding (cleanness, idiomaticness, correctness) | __ | |
| Communication (narration in beats, recovery, hint handling) | __ | |
| Testing (ran on original, edge case, stress case) | __ | |
| Follow-up answer (the 1 question you asked them) | __ | |

Total: __ / 25. Anchor: 18+ is screen-ready; 14-17 needs another mock;
under 14 needs the lectures re-read and a second drill.

## Hint policy

If the candidate is stuck for 2+ minutes on the optimisation, offer:

- For Problem A: "What if you only made one pass through the array?"
- For Problem B: "Is there a data structure that's good for matching opens
  and closes in order?"
- For Problem C: "What information do you need from the past prices?"

Note in the debrief whether the hint was needed and how the candidate
responded to it.
```

### Step 3 — Run the mock (45 min)

You and the peer join the shared-editor pad and the recording starts. Run the call on the timing above. The peer manages the clock; you manage the editor and the narration.

Things to remind yourself, internally, during the call:

- **The first 90 seconds are tooling.** Greet, confirm audio, confirm editor, confirm language. Then wait.
- **Restate the problem after they read it.** Phase 1 of the narration loop. Even if it feels obvious; do it anyway.
- **Walk through an example before coding.** Phase 2. Out loud, on scratch paper or the whiteboard tab.
- **Name the brute force.** Phase 3. Even if you immediately know the optimisation. Say the words "the brute force is" and name the complexity.
- **Optimise once.** Phase 4. Name the new complexity.
- **Narrate in beats while coding.** Phase 5. Open the coding burst with a sentence; close with a recovery sentence.
- **Test for 3-5 minutes at the end.** Original example, edge case, stress case.
- **Take the follow-up question seriously.** Section 10 of lecture-notes/02. Do not rush.
- **Ask 1-2 questions at the close.** Section 11 of lecture-notes/02.

### Step 4 — Self-review against the rubric (30 min)

After the call, before the peer debrief, re-watch the recording (you should have one — the recording is non-negotiable for this exercise). Score yourself against the same rubric the peer filled out, on the same five dimensions plus the follow-up answer.

In `c13-week-06/exercise-01-pair-mock.md`, fill in:

```markdown
## Self-review

| Dimension | Self-score 1-5 | Peer-score 1-5 | Notes |
|-----------|---------------:|---------------:|-------|
| Problem-solving | __ | __ | |
| Coding | __ | __ | |
| Communication | __ | __ | |
| Testing | __ | __ | |
| Follow-up answer | __ | __ | |

**Self-total:** __ / 25. **Peer-total:** __ / 25.

## Top 3 issues to fix

For each issue: name it, give a timestamp from the recording, name the
specific fix you'll make before the real call.

1. **Issue:** ___ . **Timestamp:** ___ . **Fix:** ___ .
2. **Issue:** ___ . **Timestamp:** ___ . **Fix:** ___ .
3. **Issue:** ___ . **Timestamp:** ___ . **Fix:** ___ .

## Where the self-score and the peer-score diverged

If any dimension has a 2+ point gap between self-score and peer-score,
explain why. The gap is usually informative — most candidates over-score
themselves on Communication and under-score themselves on Coding.
```

### Step 5 — Peer debrief (15 min, after Step 4)

You and the peer compare scores. Two specific things to ask the peer:

1. **"What was the single moment in the call where you most wanted to give me feedback?"** This surfaces the highest-leverage fix — often something you didn't notice in self-review.
2. **"What's the one habit a stronger candidate would have done differently?"** This re-anchors against the rubric, not against you.

Write the peer's answers into the same file. Do not argue with the peer's read; record it. You will agree or disagree on your own time.

## Acceptance

- 45-minute recording exists, captures audio and screen, is reviewable.
- All five phases of the narration loop are present in the recording (even if one was weak).
- Self-review is filled in with all five dimensions scored and 3 issues named with timestamps.
- Peer-review is filled in.
- Self-score and peer-score gaps over 2 points are noted with a one-sentence explanation.
- One specific habit identified to bring to Exercise 2 or the mini-project.

## Solo fallback

If you cannot find a peer:

- **You read the peer script aloud yourself, then answer it as the candidate.** Less fidelity than a real peer; more fidelity than no rep.
- **Record the same recording.** Score against the rubric. The "peer" column stays empty.
- **Send the recording to one C13 cohort member** asking for asynchronous feedback against the rubric. They can score in 30 minutes; you've now bought 80% of the live-peer signal at higher async cost.

The pair mock is the highest-leverage exercise of the week. Solo mode is acceptable but second-best. Try for a peer first.

## Stretch

- **Run two mocks back-to-back with the same peer**, different problems. The fatigue between the two reveals the pacing weaknesses. The second mock usually scores 1-2 points lower than the first; that is the signal to budget energy on a real screen.
- **Switch peer roles after one mock.** You play interviewer for the peer on Problem B (if they did Problem A). Running an interview is the fastest way to internalise what an interviewer is scoring on.
- **Repeat on the other shared editor.** If Exercise 1 was on CoderPad, do the stretch on HackerRank CodePair. The 5-10 minutes of editor learning is itself a useful rep.
- **Run the mock on the audio setup you'll have at the real-call location.** Coffee shop, home office, the desk you'll be at — practise where you'll perform.
