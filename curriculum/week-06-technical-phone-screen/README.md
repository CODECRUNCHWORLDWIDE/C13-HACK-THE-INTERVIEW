# Week 6 — The Technical Phone Screen

> *The recruiter screen filtered for credibility. The hiring manager screen filtered for fit. The technical phone screen filters for one thing the first two could not test: do you actually write code? Forty-five minutes, one shared editor, one or two problems, one engineer watching your every keystroke.*

Welcome to Week 6 of **C13 · Hack the Interview**. Week 5 produced the live-delivery toolkit for the hiring manager screen — a 4-6 minute recent-project story that survives drill-down, a 12-question bank, a recorded mock with a peer playing manager. The pipeline keeps moving: candidates who landed the HM screen this cycle now have a technical phone screen scheduled, usually within 5-10 business days of the HM call.

The technical phone screen is the first call in the pipeline where you write live code while someone watches. The interviewer is an engineer (almost always not your future manager) running a 45-minute slot on a shared editor — CoderPad, HackerRank CodePair, Karat, sometimes a Google Doc, sometimes Zoom screen-share into your own editor. The problem is usually one easy LeetCode-shape question with a follow-up extension, sometimes two. The bar is not "solve the problem cleanly in silence" — the bar is "solve a problem while narrating your thinking in a way the interviewer can score."

The audience this week is the interviewer at the other end of the shared editor. The interviewer is a working engineer, usually 2-6 years into their career, asked to spend 45 minutes scoring you against a rubric they did not write. They have probably given this exact problem 20-50 times. They are not your manager, they are not the recruiter, they are not deeply invested in whether you specifically get the role — they are invested in not waving through someone who would fail the onsite, because that wastes the loop's time. The rubric phrases they write in the debrief are short: "got to brute force quickly, found the optimisation with one hint, clean code, communicated well." Or: "took 20 minutes to start coding, didn't catch the integer-overflow case, had to be walked through the optimisation."

The work in Week 6 is not deep algorithm grinding — that's Week 7. It is also not full system design — that's Week 8. The work is two things: building the muscle of **coding live on a shared editor while talking out loud**, and learning the specific tools (CoderPad, HackerRank CodePair, Karat's recorder) well enough that the tool never costs you a minute of the 45.

## Learning objectives

By the end of this week, you will be able to:

- **Describe** the structure of a technical phone screen on five axes: who's on the call, the typical problem shape, the four scoring dimensions (problem-solving, coding, communication, testing), the time budget, and the difference between an easy LeetCode in private and the same problem on a shared editor with someone watching.
- **Run** a CoderPad / HackerRank CodePair / CodeSignal session end-to-end: pick the language, configure the editor, run the test cases, paste in a function signature, handle a session that goes silent because your audio dropped — all without losing time from the 45 minutes.
- **Narrate** your problem-solving out loud in five named phases — restating the problem, walking through one or two examples by hand, sketching the brute-force approach, optimising once or twice, and writing the code — at a pace the interviewer can score against the rubric.
- **Recognise** the seven most common ways candidates fail technical phone screens: silent coding, premature optimisation, no examples-by-hand, ignoring the interviewer's hints, fighting the editor, not testing the code at the end, and badmouthing the problem.
- **Handle** the follow-up question the interviewer always has: a complexity-analysis question, an extension to the problem, a "what would you change for production?" prompt, or "did you consider this edge case?"
- **Run** a recorded mock technical phone screen with a peer playing interviewer on a real shared editor, score it against a rubric, and identify the three biggest issues to fix before the real call.

## Prerequisites

- You completed **Week 5**. You have a hiring manager screen behind you or scheduled, and the question bank / cheat sheet from that week is in your portfolio.
- You have **basic data structures and algorithms recall** at the level of C2 (CrunchTime · The Code) — arrays, hash maps, strings, two pointers, recursion. If C2 is unfinished, the easy LeetCode problems in this week's exercises will feel hard not because of the live-coding rep but because of the underlying CS — fix that lane first.
- You have **at least one technical phone screen scheduled, or you expect one in the next 2-3 weeks**. If not, work this week as a pre-load and run the pair mock as a dress rehearsal.
- You have **a peer who will play interviewer for 45 minutes** for Exercise 1 and the mini-project. C13 cohort member, C2 peer, friend who has interviewed before. Solo mode is available as a fallback with the script provided.
- You have a **CoderPad or HackerRank CodePair account** (both have free tiers). Created and tested before Tuesday — the worst time to discover the editor's quirks is during the real call.

### Bootstrap path

If you have no technical screen scheduled yet, fine — Week 6 still lands. Treat the pair mock as a dress rehearsal. The first real technical phone screen after Week 6 is the live run; the muscle either holds or it doesn't. If you have a technical screen scheduled this week, prioritise Exercises 1 and 2 (the mock with a peer, the narration drill) and treat Exercise 3 (handling follow-ups) as a one-pass draft you'll iterate on after the call.

If your data-structures and algorithms recall is weak, **do not skip ahead to Week 7's grinding**. Week 6's exercises are deliberately calibrated to easy LeetCode-shape problems — the rep is the talking-while-coding skill, not the algorithm itself. If you cannot get past the brute force on a "two sum" or "valid parentheses," put Week 6 down and spend a week on C2's array and string lanes; come back when those are fluent.

## Topics covered

- The technical phone screen vs. the HM screen and the onsite: who, what, why, and how the rubric differs from every other call in the pipeline
- The shared-editor landscape: CoderPad, HackerRank CodePair, CodeSignal, Karat, Google Doc, Zoom screen-share — what each one is, how to set up an account, the quirks that cost candidates time in the first 5 minutes
- The five-phase narration loop — restate the problem, walk through an example by hand, propose a brute force, optimise, then write the code while continuing to narrate
- Thinking out loud as a learnable skill — when to speak, when to fall silent for short coding bursts, how to recover narration after a focused 60-second coding burst
- The four scoring dimensions every technical screen uses: problem-solving, coding, communication, and testing — and how to make each visible to the scorer
- The follow-up question patterns — complexity analysis, problem extension, "what would change for production?", edge-case probes — and how to handle each in the last 5-10 minutes of the call
- The seven failure modes: silent coding, premature optimisation, no examples-by-hand, ignoring hints, fighting the editor, no testing, badmouthing the problem
- Editor hygiene — language choice, function signatures, test harnesses, where to put your scratch work, how to recover when the screen-share dies mid-call
- Note-taking during a technical screen: what to write down about the problem (what *you* learned from it for the next screen) and what to write down about the interviewer (who they were, what they emphasised)
- The post-call follow-up email — different from the recruiter and HM follow-ups, sent through the recruiter, much shorter
- Pair-mock practice with a peer playing interviewer on a real shared editor, recorded and scored against a rubric

## Weekly schedule

| Day       | Focus                                                | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|------------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | The shared-editor call, tool setup                   |    2h    |    0h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4h      |
| Tuesday   | Narration drill — easy LeetCode on CoderPad         |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     3.5h    |
| Wednesday | Thinking-out-loud lecture + narration practice       |    1.5h  |    1h     |     1h     |    0.5h   |   1h     |     0h       |    0.5h    |     5.5h    |
| Thursday  | Follow-up question drill                             |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     1h       |    0.5h    |     5h      |
| Friday    | Pair mock #1 — record and review                     |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     2h       |    0.5h    |     5.5h    |
| Saturday  | Pair mock #2 + peer feedback                         |    0h    |    0h     |     0h     |    0h     |   1h     |     3h       |    0h      |     4h      |
| Sunday    | Quiz + week reflection                               |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0h       |    0h      |     0.5h    |
| **Total** |                                                      | **3.5h** | **5.5h**  | **1h**     | **3h**    | **6h**   | **6h**       | **2.5h**   | **28h**     |

(Comparable to Week 5 in shape — voice reps, recorded mocks, one focused challenge. Use any slack for C2 problems or to seed Week 7's algorithm-grinding queue.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./README.md) | This overview |
| [resources.md](./resources.md) | Shared-editor docs, LeetCode lists, narration references, pair-mock tooling |
| [lecture-notes/01-the-shared-editor-call.md](./lecture-notes/01-the-shared-editor-call.md) | What the call is, the four scoring dimensions, CoderPad/HackerRank/CodePair tips |
| [lecture-notes/02-thinking-out-loud-on-a-call.md](./lecture-notes/02-thinking-out-loud-on-a-call.md) | The five-phase narration loop, when to speak, when to fall silent, recovery |
| [exercises/README.md](./exercises/README.md) | Three exercises |
| [exercises/exercise-01-mock-screen-with-peer.md](./exercises/exercise-01-mock-screen-with-peer.md) | Full 45-minute pair mock on a real shared editor, recorded and scored |
| [exercises/exercise-02-narrate-coderpad.md](./exercises/exercise-02-narrate-coderpad.md) | Solo narration drill — three easy LeetCode problems on CoderPad with recording |
| [exercises/exercise-03-handle-the-followup-question.md](./exercises/exercise-03-handle-the-followup-question.md) | Drill the four follow-up patterns interviewers use in the last 5-10 minutes |
| [challenges/README.md](./challenges/README.md) | One stretch challenge |
| [challenges/challenge-01-do-an-easy-leetcode-on-coderpad-narrated.md](./challenges/challenge-01-do-an-easy-leetcode-on-coderpad-narrated.md) | A single narrated easy LeetCode in a focused 30 minutes, recorded |
| [quiz.md](./quiz.md) | 10 MCQs |
| [homework.md](./homework.md) | Six problems (~6h) |
| [mini-project/README.md](./mini-project/README.md) | Recorded mock technical phone screen + self-feedback against a rubric |

## Stretch goals

- Run **a second pair mock on a different shared editor**. If Exercise 1 was on CoderPad, run the stretch mock on HackerRank CodePair, or vice-versa. The editor quirks differ enough that fluency on one does not transfer fully to the other.
- **Time five easy LeetCode problems back-to-back on CoderPad in one sitting**, narrated, recorded, no breaks. The fatigue compounds; the call quality drops measurably by problem three. Real interview cycles often have two or three technical screens in a single week, sometimes the same day. Build the stamina.
- Read **Gayle Laakmann McDowell's "Cracking the Coding Interview"** chapter 6 ("Big O") and chapter 11 ("Testing"). Most candidates lose 1-2 points on those exact dimensions in the rubric; the chapters compress what you need.
- Listen to a **single Pramp recorded mock interview** (their YouTube channel posts several). Notice the narration patterns of strong candidates: how they recover after a stuck moment, how they handle interviewer hints, when they go silent and when they resume.
- If you know a working engineer who has **run** technical phone screens (not just taken them), buy them coffee and ask: "What's the difference between a candidate who passes the screen and one who doesn't, given equal final code?" Their answer will be about narration and how the candidate handled the second-most-difficult part of the call.

## What "done" looks like by Sunday night

By the end of the week, the following should be true. If any of these aren't, stay with this week's work before moving on.

- You can run a CoderPad or HackerRank CodePair session end-to-end — log in, pick a language, configure the workspace, paste a function signature, run test cases, recover from a dropped audio connection — in under 90 seconds of overhead at the start of the call.
- You can solve an easy LeetCode-shape problem on a shared editor in **25-30 minutes while narrating in five phases**: restating the problem, walking through one example by hand, sketching the brute force, optimising once, writing the code while continuing to talk. Total spoken time covers at least 60% of the call.
- You can answer the four classic follow-up patterns — complexity analysis ("what's the time and space?"), problem extension ("what if the input were a stream?"), production framing ("how would you change this for production traffic?"), and an edge-case probe ("what if the input is empty?") — each in under 90 seconds.
- You have run a **recorded pair mock** with a peer playing interviewer (45 minutes, real shared editor), scored it against the rubric, and identified the three biggest issues to fix before the real call.
- You have updated your **screen-call cheat sheet** with a technical-screen section that fits on the same single screen — the five-phase narration cues, the four follow-up patterns compressed to one line each, the language and editor you'll use by default.
- You have written, in your own words, a **short tooling checklist** — the 5-minute pre-call routine specific to technical screens: open CoderPad/CodePair, language selected, test harness ready, audio tested, scratch paper out, the JD's role specifics open in a second tab.

This is the technical-phone-screen baseline. You will revise the narration and the tooling checklist after every real technical screen for the rest of the cycle; this week's version is v1.

## Up next

[Week 7 — Algorithms and the Onsite Loop](../week-07/) — once you can write code on a shared editor while narrating, and the follow-up questions don't catch you cold. Week 7 deepens the algorithmic surface: medium-and-hard LeetCode patterns, the two-pass and dynamic programming families, the system-design adjacent topics that show up in technical screens at senior+ levels.
