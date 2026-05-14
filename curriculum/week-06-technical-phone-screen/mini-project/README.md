# Mini-Project — Recorded Mock Technical Phone Screen Using a Shared Editor

> By the end of this week, the artefacts you'll lean on in every real technical phone screen — the five-phase narration loop, the four-follow-up patterns, the editor fluency, the pre-call routine — exist on paper or in your muscle memory. The mini-project is the operational test: do they hold up when you deliver them under live conditions, on the clock, on a real shared editor, with the recording running?

**Estimated time:** 5-7 hours, spread Friday-Saturday. The recording is non-negotiable; the self-review against the rubric is where the value lives.

## What you ship

A **recorded mock technical phone screen using a shared editor with self-feedback**, delivered as five artefacts:

1. **A recorded mock screen** — 45 minutes of you running the full technical screen against a script or with a peer, on a real shared editor (CoderPad or HackerRank CodePair). Video preferred; audio + screen-capture acceptable.
2. **A self-review document** — you re-watch the recording and score yourself against the rubric in §3 of this file. Specific timestamps for each issue.
3. **A revised pre-call routine and cheat-sheet** (v2 of each) — the version after self-review, with the top 3 issues addressed.
4. **A second short recording (10-15 min)** — the highest-leverage beat (typically the narration of one of the five phases, or the follow-up question) redone after revising the cheat sheet, demonstrating the fix.
5. **A peer-feedback record** (if Exercise 1 done with a peer) — peer's scored feedback from the live pair mock, plus the changes you applied.

All artefacts committed to `c13-week-06/mini-project/`. The recordings can be stored outside the repo and linked if they're large; the markdown files and the cheat-sheet text live in the repo.

## How to run the recording

Two valid recording modes. Choose one (or do both, if you can).

### Mode A — Solo recording, self-scripted

You play both sides. Time-box at 45 minutes. Use the peer script from Exercise 1 (Part B of that file) as your prompt list — read each beat's interviewer line aloud, pause, then answer it as the candidate. The recording captures your candidate-side audio, your screen, and the editor state; the interviewer-side is implied.

Easier to schedule. The cost: you don't get the live-interruption rep, the surprise hint, or the actual problem-not-known-in-advance dynamic. The benefit: you control the pacing and can deliberately push yourself on weaker phases.

The trick to making solo mode work: **roll a die for the problem** the same way the challenge does. You pick from the bank of three (Two Sum / Valid Parentheses / Best Time to Buy and Sell Stock) but the choice is random. The randomness simulates not-knowing.

### Mode B — Peer-played recording (the Exercise-1 mock)

If you did Exercise 1 with a peer, the recording from that session **is** the mini-project's primary recording artefact. Use it directly. The peer-feedback form goes into the artefact pack.

Mode B is strictly higher-fidelity. Use it if at all possible; fall back to Mode A if not.

### Mode A+B — Both

The strongest version of the mini-project: do Mode B on Friday (the pair mock from Exercise 1), then a focused Mode A run on Saturday (35-40 minutes solo, re-doing the segments where the pair mock revealed issues). The Saturday solo run typically scores 4-6 points higher because the Friday review surfaced the specific fixes.

## The self-review rubric

After the recording (within 24 hours, while it's fresh), re-watch with this rubric. Score each beat 1-5; for each score under 4, note a timestamp.

### Beat 1 — Tooling and intro (first 5 minutes)

| Score | What it looks like |
|------:|---------------------|
| 5 | Under 90 sec of greeting and audio check; editor and language confirmed; smooth pivot to short self-intro under 90 sec; total tooling overhead under 3 minutes. |
| 4 | Slightly long greeting (2 min) or one minor tool fumble. |
| 3 | 3-4 minutes of tooling before the problem statement begins. |
| 2 | 5+ minutes of overhead; visible struggle with the editor. |
| 1 | Failed to set up cleanly — interviewer (real or implied) had to wait. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 2 — Problem clarification and example (3-5 minutes)

| Score | What it looks like |
|------:|---------------------|
| 5 | Restated the problem in own words; asked 2-3 clarifying questions; walked through one example on scratch paper out loud; named the expected output. |
| 4 | Restated and asked clarifying questions but compressed the example. |
| 3 | One of restate / clarify / example skipped or shallow. |
| 2 | Jumped to coding after 60 seconds. |
| 1 | No restate, no example. Pure jump-to-code. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 3 — Brute force discussion (1-2 minutes)

| Score | What it looks like |
|------:|---------------------|
| 5 | Named the brute force explicitly, named the complexity, named why it's not the final answer. |
| 4 | Named the brute force; named complexity; didn't justify moving past it. |
| 3 | Mentioned a brute force briefly. |
| 2 | Skipped to the optimisation. |
| 1 | No brute-force phase at all. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 4 — Optimisation discussion (1-3 minutes)

| Score | What it looks like |
|------:|---------------------|
| 5 | Named the optimisation; named the new complexity; sketched the approach in plain English before coding; confirmed with the interviewer. |
| 4 | Two of the four (named optimisation, named complexity, sketched, confirmed). |
| 3 | One of the four. |
| 2 | Jumped to code without naming. |
| 1 | No optimisation discussion. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 5 — Coding while narrating (15-25 minutes)

This is the load-bearing beat. Score carefully.

| Score | What it looks like |
|------:|---------------------|
| 5 | Narrated at the start and end of every coding burst; no silent stretch over 90 seconds; clean idiomatic code; ran on first or second try; handled any hint gracefully. |
| 4 | One silent stretch over 90 seconds; otherwise clean. |
| 3 | Two or three silent stretches; one minor coding issue (off-by-one, wrong variable name fixed mid-call). |
| 2 | Long silent stretches (3+ minutes); code did not run on first try and required visible struggle. |
| 1 | Silent throughout; code did not work; interviewer (real or implied) had to guide. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 6 — Testing (3-5 minutes)

| Score | What it looks like |
|------:|---------------------|
| 5 | Ran on the original example with stated expected output; ran on one edge case; ran on one stress case; narrated each; caught any bugs visibly. |
| 4 | Two of the three test cases narrated. |
| 3 | One test case run. |
| 2 | Said "I think this works" and ran nothing. |
| 1 | Skipped testing entirely. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 7 — Follow-up question (60-90 seconds)

| Score | What it looks like |
|------:|---------------------|
| 5 | Recognised which of the four patterns (complexity / extension / production / edge case) the question was; deployed the right structure; answered in 60-90 seconds with specifics. |
| 4 | Got the structure right but slightly long or short. |
| 3 | Recognised the pattern but the answer was generic. |
| 2 | Didn't recognise the pattern; gave a confused or generic answer. |
| 1 | Stumbled; gave a non-answer. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Beat 8 — Your questions back and close (2-3 minutes)

| Score | What it looks like |
|------:|---------------------|
| 5 | Asked 1-2 substantive questions appropriate to the technical interviewer (their role, the team's stack, the rest of the loop); confirmed next steps; professional close. |
| 4 | 1 substantive question; close present but slightly soft. |
| 3 | Asked one generic question. |
| 2 | "Nope, I'm good." |
| 1 | Awkward or rushed close. |

**My score:** ____ **Timestamp(s) of issues:** ____

### Overall

**Total possible:** 40 (8 beats × 5). **Your total:** ___ / 40.

**Interpretation:**

- **32-40:** Strong. You're ready for a real technical phone screen. Watch once more, fix the timestamped issues, book the call.
- **24-31:** Mid. The structure is there, but specific beats need work. Identify the lowest-scored beat (often Beat 5 or Beat 7) and run a focused drill (one beat, 15 min, two takes) before the real call.
- **16-23:** Needs work. The mock revealed multiple structural issues. Schedule a second full mock — ideally with a peer (Exercise 1) — before booking real technical screens.
- **Below 16:** Stop. The recording is telling you something. Re-read Lectures 1 and 2, redo Exercise 2 from scratch, run a second pair mock the next day.

## Acceptance criteria

### Recording (the load-bearing artefact)

- [ ] One recording (Mode A, Mode B, or both) exists, 40-45 minutes long, capturing all 8 beats of the screen.
- [ ] All 8 beats are present (none skipped).
- [ ] Recording is reviewable: audio is clear, screen is captured, you're audible.
- [ ] Recording is timestamped or trivially navigable.

### Self-review

- [ ] `c13-week-06/mini-project/self-review.md` exists.
- [ ] All 8 rubric beats are scored 1-5 with at least one timestamped note per beat scored under 5.
- [ ] Total score is computed.
- [ ] An "Overall interpretation" sentence is written.

### Cheat-sheet v4 and pre-call routine v2

- [ ] `c13-week-06/mini-project/screen-call-cheat-sheet-v4.md` exists.
- [ ] `c13-week-06/mini-project/pre-call-routine-v2.md` exists.
- [ ] The top 3 issues from self-review are addressed via cheat-sheet edits, each annotated ("Fixing issue #1 from review: narration-recovery cue added after the coding burst").
- [ ] v4 is not longer than v3 from Week 5 plus the Homework-1 additions. Cheat sheets bloat without discipline.

### Second short recording

- [ ] A 10-15 minute follow-up recording redoes the **lowest-scored beat** from the rubric (most often Beat 5 narration or Beat 7 follow-up).
- [ ] In `self-review.md`, a comparison: what improved, what didn't, what remains as the next focus.

### Peer-feedback (if Exercise 1 done with a peer)

- [ ] Peer feedback form attached.
- [ ] At least 2 pieces of peer feedback applied to cheat-sheet v4 (or rejected with a one-line justification).

## Rubric (mini-project itself)

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Recording completeness | 20% | All 8 beats captured; 40-45 min; reviewable |
| Self-review specificity | 25% | Timestamps for every scored-under-5 beat; honest scoring |
| Issue identification | 20% | The top 3 issues are correctly the highest-leverage ones, not the most-comfortable ones to fix |
| Cheat-sheet v4 quality | 15% | Top 3 issues addressed; v4 not bloated; still fits one screen |
| Second-recording improvement | 15% | The lowest-scored beat measurably improved between recording 1 and recording 2 |
| Peer feedback integration | 5% | (Bonus if Exercise 1 done with peer; ignored otherwise) |

## How to actually re-watch yourself

A few practical notes specific to the technical-screen recording:

- **Watch alone first.** Don't show anyone else. The first watch is for diagnosis, not performance.
- **Note before you react.** Pen in hand. When something makes you wince, write down the timestamp and the specific thing. Don't fix in your head; just record.
- **Watch the coding-and-narration segment (Beat 5) at 1x first, then 1.5x for a second pass.** Beat 5 is where most candidates discover silent stretches they didn't notice in real time. The 1.5x pass surfaces the pacing.
- **Watch Beat 7 (follow-up) twice.** This is the segment most candidates underrate in self-review. Listen for: did you recognise the pattern? Did you deploy the right structure? Did the answer fit in 60-90 seconds?
- **Separate "code quality" from "narration quality."** The rubric scores both, separately. Even if the code was right, the narration may have been weak. Score them independently.
- **Specifically time the silent stretches.** Use the recording's scrub bar. Any stretch over 90 seconds is a Beat 5 deduction. Many candidates discover, on re-watch, that what felt like a 30-second silent stretch was actually 2 minutes.

## How the cheat sheet evolves

After every real technical phone screen, spend 10-15 minutes updating:

1. What problem did the interviewer give you, exactly? Add it to your problem-tracking notebook. Phone-screen problems repeat across companies; the same problem may appear in three loops.
2. What follow-up question did the interviewer ask? Which of the four patterns was it? Add the variant to your follow-up-patterns file.
3. What hint did the interviewer offer (if any)? What was the trigger? Add a note for future screens.
4. What part of your narration did you trip on? Add a one-line cue to the cheat sheet.
5. What did the interviewer say about the rest of the loop? Capture verbatim for the next call.

By Week 8, your cheat sheet and your problem-tracking notebook will be the most-revised documents in your portfolio. That's the intent. v4 from this week is one stop on the path; v6 by Week 12 is what passes a senior-level technical screen at a tier-A company.

## Stretch

- **Run the mini-project twice this week.** Friday Mode A, Saturday Mode B with a peer. The Saturday version usually scores 4-6 points higher because the Friday review surfaced the specific fixes.
- **Pair-review with a cohort peer.** Trade recordings: you self-review yours, then watch theirs and give scored feedback against the same rubric. Two passes over the rubric catches issues each individually misses.
- **Run a second problem.** Many real technical screens have a second problem if the first finishes early. After the mini-project recording, run a 15-minute focused drill on a second easy problem with the same five-phase loop.
- **Build the "next-screen prep checklist."** A 10-minute pre-call routine specific to technical screens (from Homework 5). Commit the checklist next to the cheat sheet.
- **Repeat the mini-project on a different shared editor.** If the primary was CoderPad, the stretch is HackerRank CodePair. The 5-10 minutes of editor learning is itself a useful rep.

## Why this matters

The technical phone screen is the first call in the pipeline where you cannot bluff. Every prior call had wiggle room — a meandering self-intro could be reframed, a thin project description could be patched. The shared editor is binary. The code runs or it does not. The interviewer watches you find the optimisation or they do not. The rubric is more mechanical than the HM screen's qualitative paragraph.

The mini-project's recording is the diagnostic that surfaces the gap between "I can solve easy LeetCodes" and "I can solve them on a shared editor, narrating in five phases, in 25 minutes, while a stranger evaluates me on four dimensions." Most candidates discover, the first time they watch the recording, that the narration is the loose hinge: the code lands fine, but the 4-minute silent stretch in the middle of Beat 5 produces a Communication score of 3 instead of 5, and the call gets a "lean no" because of it.

This week's artefacts also carry forward. The five-phase narration is the foundation of every coding round of every onsite (Week 7+). The follow-up patterns recur in every senior+ technical interview. The editor fluency persists. Week 6 produced the live-coding toolkit for the *third* stage of the pipeline; the same toolkit, with refinement, carries through the rest of the cycle.

## Submission

Commit `c13-week-06/mini-project/` to your portfolio repo. The folder should contain:

- `self-review.md` — the rubric, scored, with timestamps and an overall interpretation.
- `screen-call-cheat-sheet-v4.md` — the revised cheat sheet, top-3-issues addressed.
- `pre-call-routine-v2.md` — the updated pre-call routine.
- `peer-feedback.md` (if Exercise 1 done with peer) — the peer's form + the changes you applied.
- `recordings/` — links to or paths to the two recordings (`mock-tech-screen-full.{mp4|m4a}` and `redo-lowest-beat.{mp4|m4a}`). If files are large, store outside the repo and link.
- `README.md` — a short index pointing to each file, plus a one-paragraph summary of what the mini-project surfaced about your technical-screen readiness.

---

When done: open [Week 7 — Algorithms and the Onsite Loop](../../week-07/). The first onsite — usually a 4-5 round technical loop — is the next major filter in the pipeline. You've prepped the *write-code-on-a-shared-editor* surface; next, the deeper algorithm surface, system design at scale, and the multi-round endurance of a full onsite.
