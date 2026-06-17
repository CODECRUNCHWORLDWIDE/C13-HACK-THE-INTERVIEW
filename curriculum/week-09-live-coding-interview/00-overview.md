# Week 9 — The Live Coding Interview: 45 Minutes, One Screen, One Interviewer

> *The live coding interview is the single round most candidates have practised the wrong skill for. They have spent six months solving LeetCode in silence on their couch with a hint button half a centimetre away, and then they walk into a 45-minute one-on-one in which silence is read as freezing, the hint button is now a human who is keeping score, and the "answer" includes not just the working code but the running narration of how the working code came to exist. The skill of solving the problem and the skill of performing the solve are not the same skill. Most candidates who fail this round did not fail because they could not solve the problem. They failed because they could solve the problem in silence on their couch and could not solve it out loud in front of a stranger on a forty-minute clock.*

Welcome to Week 9 of **C13 · Hack the Interview**. Week 8 produced the design-round structure, the four building blocks, the back-of-envelope estimation, and the canonical six 101-level problems. The full onsite loop is now within reach: the technical screen has already happened (Week 6), the system design round has a method (Week 8), the behavioural depth is the round still ahead (Week 10). Week 9 closes the loop on the round that occupies the largest fraction of the onsite day — the live coding interview — and that, more than any other round in the loop, decides the outcome of the entire interview.

Most candidates have done some version of live coding before. The recruiter phone screen (Week 4) sometimes included a five-minute warm-up. The technical phone screen (Week 6) was a 45-minute live coding round in a shared editor. The onsite typically includes two or three more. Week 9 is not a substitute for Week 6 — Week 6 covered the medium of the phone screen, the shared editor, the narration loop. Week 9 is the round itself: what to say in the first 90 seconds, what to do when the interviewer goes silent, how to take a hint without losing your composure, what the four common failure modes look like from inside the candidate's head, and how the strong candidates recover from a stuck moment that, from the outside, looks indistinguishable from the failed candidate's stuck moment.

The week deliberately leans on three free corpora. Gayle Laakmann McDowell's *Cracking the Coding Interview* book is the canonical reference but is paid; her free conference talks and podcast appearances cover almost the same ground with extra commentary on the interviewer's side of the table, and Week 9 cites those. Hello Interview's free YouTube channel has the best public archive of recorded mock interviews at the live coding level, with running commentary on what the candidate did well and where the round started to slip. Carl Tashian's free essays on the "interview-coding mindset" cover the under-discussed psychological layer — the inner monologue of the stuck candidate, the calm-under-pressure rehearsal, the framing of the interviewer as a collaborator rather than an adversary — that the LeetCode-grinding corpus uniformly ignores.

## Learning objectives

By the end of this week, you will be able to:

- **Run** the live coding interview on the six-phase structure: clarify (2-3 min) → examples (2-3 min) → approach (5-8 min) → code (15-20 min) → test (5-8 min) → discuss (3-5 min). Hit each transition out loud; recognise which phase you are in at any moment; recognise when one phase has eaten more time than its budget and recover.
- **Read** the interviewer's signals: silence is a request to keep thinking aloud, not an invitation to go quiet; pushback on your approach is a hint to pivot, not a hint to defend; a direct hint should be taken inside ten seconds without ego; a "what would you do differently" at the end is a chance to surface trade-offs, not an attack on the code.
- **Identify** the four common failure modes — over-engineering (building the abstraction layer the problem does not need), premature optimisation (jumping to the O(n log n) before the O(n²) is on the board), getting stuck silently (the inner-monologue spiral with the keyboard frozen), and ignoring the hint (the candidate who heard the hint but kept executing the original wrong plan) — and the recovery pattern for each from inside the round.
- **Apply** test-driven thinking during the interview: write the test cases out loud *before* the code, not after. Three input categories minimum — happy path, edge cases (empty, single element, duplicates, negatives), and the failure mode (input that breaks the naive approach). Naming the cases before coding catches half the bugs that would otherwise surface during the test phase.
- **Handle** the complexity push — the "is this O(n) or O(n log n)" question — by separating the two sub-questions inside it: is your stated complexity correct (a factual question, answerable), and is this the optimal complexity for the problem (a different question, sometimes "yes" and sometimes "I do not know, here is the trade-off I am making").
- **Recover** from being stuck without losing the round: verbalise the stuck-point ("I am stuck because I need to track X but my current data structure does not let me look it up in O(1)"), ask a clarifying question ("does the input have duplicates?"), or simplify the problem ("let me solve it for the case where the list is sorted first, then generalise").
- **Walk** through the two worked transcripts in this week's lectures — one round that went well, one round that went badly and recovered — and identify, line by line, the moments where the candidate's choice of phrase moved the score up or down.

## Prerequisites

- You completed **Week 6 — the technical phone screen**. The shared-editor mechanics, the narration loop, the "I am thinking about X" filler are on muscle memory. Week 9 layers the in-person and onsite-specific behaviour on top of that base; if Week 6 has not landed, run the Week 6 mini-project first.
- You completed **Week 7 — the onsite day-of logistics**. The room-reading, the legal frame, the multi-round endurance are the surface on which Week 9 sits. The live coding round is one of three to five rounds on the day; the standalone-round skill alone is not sufficient.
- You completed **Week 8 — system design 101**. The design-round phase structure mirrors the coding-round phase structure (clarify → high-level → deep dive → trade-offs); the two weeks share the "say the phase boundary out loud" muscle.
- You have **solved at least 50 LeetCode-style problems**, of which at least 15 were "medium" difficulty. The live coding round draws from the medium-difficulty pool at most companies; the easy-only candidate will be over-stretched, the hard-only candidate will be over-engineering everything. The 50-problem floor is the C13 baseline; if you are below it, run the C13 LeetCode-warmup track (planned for a future C13 expansion) in parallel with Week 9.
- You have **a working webcam, microphone, and a quiet 45-minute window** for the mini-project's record-yourself drill. The whole week pivots on the record-and-watch loop; without recording capability the self-grading rubric is just opinion.
- You can **type without looking at the keyboard**. The live coding round is read on the surface as a coding round, but the meta-skill is divided attention: the typing happens with one part of the brain while the narration happens with another, while the interviewer's reactions are being read with a third. Hunt-and-peck typing is a forcing function that collapses the divided attention to one stream — usually the typing wins and the narration goes silent. If your typing is slow, drill the typing first; the round will not feel manageable until it is automatic.

### Bootstrap path

If you are entering Week 9 with light prep, run the bootstrap before Tuesday:

1. Solve a LeetCode Easy ("Two Sum", "Valid Parentheses", or "Reverse Linked List") out loud, with no IDE help, in under 20 minutes, while recording yourself on Zoom or Loom. Watch the recording. Count the seconds of silence. Count the number of times you said "um." This is your baseline.
2. Solve the same problem a second time, narrating differently, trying to halve the silence. Re-record. Compare.
3. Read Lecture 1 of this week before continuing the rest of the curriculum.

The bootstrap is uncomfortable. The first time most candidates watch themselves coding, the experience is mortifying. That mortification is the precondition for improvement — the candidate who has watched themselves three times has resolved more of the unconscious tics than the candidate who has solved fifty problems in silence.

## Topics covered

- The six-phase structure of the live coding interview: clarify, examples, approach, code, test, discuss — and the rough time budget for each
- Reading the interviewer's signals: silence (a request, not an attack), pushback (a hint to pivot), direct hints (take them inside 10 seconds, no ego), trade-off prompts ("what would you do differently")
- The four common failure modes — over-engineering, premature optimisation, getting stuck silently, ignoring the hint — with the recovery pattern for each
- Test-driven thinking during the interview: writing the test cases out loud *before* the code; the three categories (happy, edge, failure-mode); how this catches bugs at the cheapest possible time
- The complexity push: separating "is my stated complexity correct" from "is this the optimal complexity for this problem"; what to do when you do not know the optimal
- Recovery from a stuck moment: the three moves (verbalise, clarify, simplify) and the order to try them in
- Two worked transcripts: a 38-minute round that went well, and a 42-minute round that went badly and recovered into a passable signal
- The mindset framing: the interviewer is a future colleague evaluating whether they want to work with you, not an adversary evaluating whether you are smart enough; the candidate who internalises this performs visibly better
- The pre-round 5-minute warm-up: what to think about in the elevator, what to type in the editor before the interviewer arrives, what to say in the first 30 seconds
- The post-round 5-minute decompression: what to write down before you forget, what *not* to share on Blind or in your group chat until the loop is done

## Weekly schedule

| Day       | Focus                                                | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|------------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | The six-phase structure + reading the interviewer    |    2h    |    0h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4h      |
| Tuesday   | The four failure modes + test-driven thinking        |    1.5h  |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4.5h    |
| Wednesday | Worked transcripts (lecture 3) + complexity push     |    2h    |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Thursday  | Mock-interview drills (exercises 1 and 2)            |    0h    |    2h     |     1h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Friday    | Mock-interview drill 3 + recovery challenge          |    0h    |    1.5h   |     1h     |    0.5h   |   1h     |     1h       |    0.5h    |     5.5h    |
| Saturday  | Mini-project — record yourself coding, self-grade    |    0h    |    0h     |     0h     |    0h     |   1h     |     3.5h     |    0h      |     4.5h    |
| Sunday    | Quiz + reflection + peer review of the recording     |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0.5h     |    0.5h    |     1.5h    |
| **Total** |                                                      | **5.5h** | **5.5h**  | **2h**     | **3h**    | **6h**   | **5h**       | **3h**     | **30h**     |

(Comparable to Week 8 in total budget. The exercise load is slightly lower because each mock-interview drill is a 30-50 minute solo run rather than a 60-90 minute design write-up. The mini-project load is the same; the recording-and-grading loop is where the week's hours actually compound.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./00-overview.md) | This overview |
| [resources.md](./01-resources.md) | Gayle Laakmann McDowell's free conference talks and podcast appearances, Hello Interview's free YouTube archive, Carl Tashian's free essays, the canonical free LeetCode and NeetCode resources for problem sourcing |
| [lecture-notes/01-the-45-minute-structure.md](./02-lecture-notes/01-the-45-minute-structure.md) | The six-phase structure, the time budget for each phase, the transitions out loud, the recovery moves when one phase eats another |
| [lecture-notes/02-failure-modes-and-recovery.md](./02-lecture-notes/02-failure-modes-and-recovery.md) | The four failure modes, test-driven thinking during the interview, the complexity push, the three moves for getting unstuck |
| [lecture-notes/03-two-worked-transcripts.md](./02-lecture-notes/03-two-worked-transcripts.md) | A 38-minute round that went well, a 42-minute round that went badly and recovered, with line-by-line commentary |
| [exercises/exercise-01-the-clarification-drill.md](./03-exercises/exercise-01-the-clarification-drill.md) | A 30-minute solo drill on the first phase only — ask the questions before writing the code |
| [exercises/exercise-02-the-stuck-recovery-drill.md](./03-exercises/exercise-02-the-stuck-recovery-drill.md) | A 45-minute mock interview on a problem deliberately chosen to be one notch above your comfort level — the goal is to practise the recovery moves |
| [exercises/exercise-03-the-complexity-defence-drill.md](./03-exercises/exercise-03-the-complexity-defence-drill.md) | A 30-minute drill on the complexity-push moment — defending the stated complexity, recognising the implicit "can you do better" prompt |
| [exercises/SOLUTIONS.md](./03-exercises/SOLUTIONS.md) | Sample strong responses for each of the three exercises, with the inner-monologue narration that produces a passing-signal round |
| [challenges/challenge-01-the-hint-ego-drill.md](./04-challenges/challenge-01-the-hint-ego-drill.md) | The "interviewer just gave you a hint" drill — receive it, integrate it, do not defend |
| [challenges/challenge-02-the-over-engineering-trap.md](./04-challenges/challenge-02-the-over-engineering-trap.md) | The "is this code too clever for the problem" drill — identify your over-engineering tells and write the simpler version first |
| [quiz.md](./05-quiz.md) | 10 questions on phase structure, failure modes, recovery, complexity, the transcripts |
| [homework.md](./06-homework.md) | Six live-coding drills (~6h), with rubric and time estimates |
| [mini-project/README.md](./07-mini-project/00-overview.md) | Record yourself coding a medium-difficulty problem end-to-end; grade the recording against a self-grading rubric; produce a written one-page reflection |

## Stretch goals

- Watch **Gayle Laakmann McDowell's free conference talks on YouTube**, in particular her "How to Interview at Top Tech Companies" Google Tech Talk and her appearances on the *CoRecursive* and *Software Engineering Daily* podcasts. The book is paid; the talks cover most of the same material plus the inside-the-interviewer perspective that the book under-weights. Pick two talks, watch on 1.25x.
- Watch **three full Hello Interview live coding mock interviews** on their free YouTube channel. Pick mocks labelled "senior" or "L4-L5" — the new-grad mocks tend to skip the trade-offs phase, which is where the round's signal-density is highest. Pause the video at the moment the candidate starts coding; predict what they will do; resume; compare. The predictive-pause loop builds the read-ahead skill that the live coding round implicitly tests.
- Read **all of Carl Tashian's interview-coding essays**, free on his personal blog. The total reading time is under an hour. The essays are the most-quoted free reference on the psychological side of the round — the inner-monologue moves, the "future colleague" framing, the calm-under-pressure rehearsal. The essays are not a substitute for the practice; they are the framing the practice sits inside.
- Run **at least one full mock interview with another human** — a study partner, a roommate, a friend from your CS cohort, a stranger from Pramp or interviewing.io's free tier. The simulated pressure of a real human watching is qualitatively different from solving with yourself in the room; the gap between the two is the gap Week 9 is trying to close.
- If you are interviewing at a company that uses CoderPad, HackerRank, or CodeSignal as the shared editor: spend 20 minutes in the platform's free practice environment before Friday. The keybindings, the auto-complete behaviour, the run-code button — all are platform-specific and all can absorb 30 seconds of the interview if encountered for the first time during the round.
- Read **at least one Blind or Glassdoor "interview experience" post** for each company on your shortlist, filtered to the live coding round only. The format of the question, the kind of follow-up the interviewer tends to ask, and the typical time pressure are visible from the postings. Pattern-match across at least three posts before drawing conclusions; single posts are noisy.

## What "done" looks like by Sunday night

By the end of the week, the following should be true. If any of these aren't, stay with this week's work before moving on.

- You can talk through the **six phases of a 45-minute live coding round** by name, the time budget for each, the transition phrase you say out loud at each phase boundary, and one recovery move for when one phase eats into the next.
- You can name the **four common failure modes** (over-engineering, premature optimisation, getting stuck silently, ignoring the hint), describe what each looks like from inside the candidate's head, and describe the recovery pattern that brings the round back.
- You can write **test cases out loud before the code** for any medium-difficulty LeetCode problem — three categories minimum (happy path, edge cases, failure-mode input) — and you can do this in under three minutes.
- You can handle the **complexity push** — "is this O(n) or O(n log n)?" — by separating the factual question (what is my code's complexity) from the optimisation question (is this the best you can do) and answering each cleanly.
- You can run the **three moves for getting unstuck** in the right order (verbalise the stuck-point, ask a clarifying question, simplify the problem) and you have practised each on at least one live mock.
- You have **recorded yourself coding** a medium-difficulty problem end-to-end at least once and watched the full recording back. You have a list of at least three of your own tics — silence-stretches, "um" filler, premature typing — and a plan for fixing one of them.
- You have **read the two worked transcripts** in Lecture 3 line-by-line and can articulate why each specific phrase moved the score up or down. The transcripts are not a substitute for your own recording; they are the calibration baseline.
- You have **a written one-page reflection** from the mini-project: the three things you would change about your default round behaviour, the one tic you have already fixed, and the one situational move you want to drill next.

This is the live-coding-round baseline at the new-grad-to-L4 level. The senior-level depth — the staff-engineer behavioural overlay, the explicit-architecture push inside the coding round, the multi-problem stamina across a 4-hour onsite — is in the C13 senior-track companion week (planned for a future C13 expansion). The new-grad-to-L4 baseline is what Week 9 ships.

## Up next

[Week 10 — Behavioural Depth and the Hiring-Manager Round](../week-10/) — once the live coding structure, the failure modes, the recovery moves, and the recorded self-grading are on muscle memory. Week 10 returns to the behavioural surface from Week 5, this time at the depth required for the full onsite behavioural round, the bar-raiser round at Amazon, and the hiring-manager final conversation: the STAR-format deep dive, the conflict question, the leadership-principle prep at Amazon, the "tell me about a time you failed" recovery, and the questions you ask back.
