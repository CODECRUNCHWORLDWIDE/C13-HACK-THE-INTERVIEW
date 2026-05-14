# Week 7 — The Onsite: Day-of Logistics

> *The technical phone screen filtered for "can you write code on a shared editor while someone watches." The onsite filters for "can you sustain that for four to six hours, across four to five interviewers, after a bad night's sleep, in a building you have never set foot in, while a recruiter walks you between rooms and a stranger eats lunch across the table from you, and still produce signal on every round." It is not a harder version of the technical screen. It is a different test.*

Welcome to Week 7 of **C13 · Hack the Interview**. Week 6 produced the live-coding toolkit for the technical phone screen — the five-phase narration loop, the four scoring dimensions, the editor fluency, the pre-call routine, a recorded pair mock. The pipeline keeps moving: candidates who landed the technical screen this cycle now have an onsite loop scheduled, usually within 7-14 business days of the screen.

The onsite is the longest single event in the pipeline. Four to six hours, on-site or remote, with four to five interviewers across coding, system design, behavioural, and (for many companies) a lunch interview. You will be tired by hour three. You will be hungry at hour four. You will need to use the bathroom at some point and the schedule will not give you an obvious slot. You will be asked at least one hostile question, possibly more. You will be asked at least one question that the EEOC says interviewers are not allowed to ask, and you will have ninety seconds to deflect it without breaking the rapport with the interviewer asking it. None of these are the technical content. All of them affect the outcome.

The audience this week is not a single interviewer at the other end of a 45-minute call. The audience is **the loop** — four to five people who will each spend 45-60 minutes with you, then meet in a debrief room (in person or in a calibrated Slack channel) within 24-48 hours and decide collectively whether to hire. The debrief is the actual scoring event; the rounds are the data collection. The candidate who optimises only for the rounds, and not for the debrief, ships strong code and loses on the soft signal in three of the five write-ups.

The work in Week 7 is not deeper algorithm grinding — that's Week 8. It is also not negotiation — that's Week 9. The work is everything **around** the technical content: the day-of logistics that determine whether you arrive at your strongest, the conversational pacing across hours, the room-reading that tells you when an interviewer has decided and you are now optimising for their write-up rather than for the problem, the legal frame around questions interviewers are and are not allowed to ask, the deflection language for the questions that cross the line, and the bathroom break.

This week is text-heavy by design. There is almost no code in it. The skills it builds are non-substitutable; candidates with strong technical skill lose loops on these failures every month.

## Learning objectives

By the end of this week, you will be able to:

- **Describe** the shape of a typical onsite loop on six axes: total length, number of interviewers, round types and their sequence, the lunch interview, the recruiter's role across the day, and the debrief mechanism that produces the actual decision.
- **Plan** the day-of logistics for both in-person and virtual onsites: the night before (sleep, food, travel), the morning of (warm-up, breakfast, what to wear), the building (arrival buffer, security, where to wait), the room (water, restroom location, the recruiter handoff), and the recovery beats (the 5-minute gap between rounds, the lunch break, the closing).
- **Read** the room across a multi-hour loop: which interviewer is engaged, which has decided early, which is hostile by personal style and which by company-prescribed pattern, when to push back and when to defer, and how to recalibrate your performance for the next round when the previous one went badly.
- **Pace** your energy and attention across four to six hours of high-stakes conversation without burning out at hour four. The mechanical habits — water, snack, stand up, breathe — and the cognitive habits — short reset rituals between rounds, deliberate forgetting of the prior round.
- **Identify** the seven most common hostile-question patterns interviewers use as deliberate calibration tools, distinguish them from genuinely rude interviewers, and respond to each in a way that produces a positive write-up.
- **Recognise** the categories of question the EEOC and US Department of Labor identify as illegal or impermissible to base hiring decisions on — age, race, religion, national origin, sex, pregnancy, marital and family status, disability, genetic information, citizenship beyond legal-right-to-work — and deflect any such question in real time with a scripted, polite, non-confrontational redirect that preserves the interview while not answering the question.
- **Take** a break — an actual one, the bathroom or the water — in the middle of a round when you genuinely need it, without losing the round.

## Prerequisites

- You completed **Week 6**. The five-phase narration loop is on muscle memory. You can run a CoderPad or HackerRank CodePair session end-to-end in under 90 seconds of pre-problem overhead.
- You have **at least one onsite loop scheduled, or you expect one in the next 2-4 weeks**. If not, work this week as a pre-load and run the mini-project's 4-hour mock as a dress rehearsal with a peer.
- You have a **peer who will play interviewer for one full round (45-60 minutes)** for the mini-project. Ideally a peer who will commit to four rounds across two days for the full 4-hour mock; in practice, two peers each running two rounds also works.
- You have **basic comfort with both coding and behavioural rounds**. C13 Week 5 (hiring manager screen) and C13 Week 6 (technical phone screen) are the prerequisites for the round content. This week is the day-of frame around them.
- You have **read or scanned the EEOC's pre-employment-inquiries guidance**. The resources file links the source; the lecture summarises it. The legal frame in this week is US-jurisdiction; non-US candidates should consult the equivalent (UK Equality Act 2010, Canadian Human Rights Act, EU Equal Treatment Directive) and treat the US frame as a translation key, not a substitute.

### Bootstrap path

If you have no onsite scheduled yet, fine — Week 7 still lands. Run the mini-project as a 4-hour pair mock, ideally with two peers, and treat it as a dress rehearsal for the first real onsite in 2-6 weeks. The muscle is non-transferable from solo prep; you must rehearse the multi-hour-with-other-humans dynamic.

If you have an onsite scheduled this week, prioritise Exercise 1 (the hour-by-hour day-of run-of-show) and Exercise 2 (the deflection rehearsal). Exercise 3 (the debrief self-eval) is the artefact you fill out after the loop, so it does not block the loop itself. The mini-project is high-value but skippable in a crunch week if the real onsite is on Friday.

If you are interviewing at a company that has published its onsite structure publicly (Google, Meta, Amazon, Microsoft, Stripe, several others — see resources.md), read their candidate-facing guide before Tuesday. Their structure replaces the generic structure in Lecture 1 for that specific loop; the rest of the week applies unchanged.

## Topics covered

- The onsite loop as an institution: history, why companies use it, what it costs both sides, why the four-to-six-hour shape persists
- The round types: coding (usually 2-3 rounds), system design (1 round at mid-level+, 2 rounds at senior+), behavioural (1-2 rounds), lunch (1 round, often informally scored), domain-specific (data, ML, security, mobile — sometimes a dedicated round)
- The lunch interview: what it actually is, who's running it, whether it is scored, and how strong candidates handle it
- The recruiter's day-of role: greeting you, walking you between rooms, the "how's it going?" check at the midpoint, the closing and the timeline conversation
- Day-of logistics across two modes: in-person (travel, hotel, building, security, the waiting room) and virtual (multiple Zoom links, the camera setup, the timezone math, the equivalent of "between rounds")
- The night before: sleep architecture, food, alcohol, screen time, the warm-up problem question
- The morning of: breakfast, caffeine math, dressing, the 30-minute warm-up
- The bathroom break: when to take it, how to ask, why most candidates do not and lose the back half of the loop because of it
- Reading the room across hours: the engagement signals from a single interviewer, the cross-round drift in your own performance, how to recalibrate
- Conversation pacing: the difference between a 45-minute screen and a 45-minute round in a 5-hour day, the energy budget, the "I am tired and it is showing" recovery
- Hostile-question patterns: the seven common ones, what they're calibrating for, the response template
- The legal frame around interview questions: EEOC pre-employment inquiry guidance, US Department of Labor guidance, what is and is not allowed, why interviewers still ask, the deflection language
- When and how to take a break mid-round
- The closing of the loop: the last 15 minutes, the recruiter conversation about timeline and next steps
- The 2-hour post-loop debrief: while the loop is fresh, what you log for yourself and what you do not bring to the recruiter

## Weekly schedule

| Day       | Focus                                                | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|------------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Loop shape, round types, lunch interview             |    2h    |    0h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4h      |
| Tuesday   | Day-of script — hour-by-hour run-of-show             |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     3.5h    |
| Wednesday | Reading the room + pacing lecture                    |    1.5h  |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4.5h    |
| Thursday  | Hostile and illegal questions — drill                |    1.5h  |    1.5h   |     1h     |    0.5h   |   1h     |     0h       |    0.5h    |     6h      |
| Friday    | Shadow-a-loop challenge + after-action template      |    0h    |    1h     |     1h     |    0.5h   |   1h     |     1h       |    0.5h    |     5h      |
| Saturday  | Mini-project 4-hour mock with peers                  |    0h    |    0h     |     0h     |    0h     |   1h     |     3.5h     |    0h      |     4.5h    |
| Sunday    | Quiz + reflection + after-action of the mock         |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0.5h     |    0h      |     1h      |
| **Total** |                                                      | **5h**   | **5h**    | **2h**     | **3h**    | **6h**   | **5h**       | **2.5h**   | **28.5h**   |

(Comparable to Week 6 in total budget. The lecture load is higher; the exercise load is the same. The mini-project is heavier than Week 6's because the mock is a four-hour sit, not a 45-minute call.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./README.md) | This overview |
| [resources.md](./resources.md) | EEOC and US DOL guidance, Cracking the Coding Interview free-preview chapters, Glassdoor FAANG process descriptions, levels.fyi |
| [lecture-notes/01-the-shape-of-an-onsite.md](./lecture-notes/01-the-shape-of-an-onsite.md) | The loop institution, round types, lunch, recruiter day-of role, in-person vs. virtual, the night-before and morning-of logistics |
| [lecture-notes/02-reading-the-room-and-pacing.md](./lecture-notes/02-reading-the-room-and-pacing.md) | The engagement signals, the cross-round drift, conversation pacing, the energy budget, the bathroom break |
| [lecture-notes/03-handling-hostile-and-illegal-questions.md](./lecture-notes/03-handling-hostile-and-illegal-questions.md) | The seven hostile patterns, the EEOC and DOL legal frame, the deflection language, when to escalate and to whom |
| [exercises/exercise-01-mock-day-script.md](./exercises/exercise-01-mock-day-script.md) | Write your own hour-by-hour run-of-show for your real or expected onsite |
| [exercises/exercise-02-deflection-rehearsal.md](./exercises/exercise-02-deflection-rehearsal.md) | Rehearse the deflection language for hostile and illegal questions with a peer |
| [exercises/exercise-03-debrief-self-eval.md](./exercises/exercise-03-debrief-self-eval.md) | The post-loop debrief template, run on the mini-project mock or a real loop |
| [challenges/challenge-01-shadow-a-real-loop.md](./challenges/challenge-01-shadow-a-real-loop.md) | The informational request — how to script a "shadow a loop" ask to a working engineer |
| [challenges/challenge-02-after-action-template.md](./challenges/challenge-02-after-action-template.md) | Build the after-action template you'll fill out within 2 hours of every real onsite |
| [quiz.md](./quiz.md) | 10 questions on pacing signals, illegal questions, recovery from a stuck problem |
| [homework.md](./homework.md) | Six problems (~6h) |
| [mini-project/README.md](./mini-project/README.md) | The 4-hour peer mock — four rounds, scored, with a written debrief |

## Stretch goals

- Run **a second, shorter 2-hour mock** focused specifically on the lunch interview. Many candidates have never had an informal-but-scored meal conversation; the muscle is real and is rare.
- **Read the EEOC's pre-employment-inquiries guidance front to back.** It is short. The version of it you carry into a real loop should be paragraph-level, not headline-level. Source: <https://www.eeoc.gov/employers/pre-employment-inquiries>.
- **Read Cracking the Coding Interview chapter 7** ("Behavioral Questions"). McDowell's framing of the behavioural round is the canonical short reference. The free preview on Amazon or Google Books usually covers this chapter; the public library version covers the whole book.
- **Watch one full mock onsite-style loop on interviewing.io's public archive.** The system-design and behavioural rounds in particular reveal pacing patterns that are not visible in 45-minute coding clips.
- If you know a working engineer who has been **on a debrief panel** (not just been an interviewer in one round), buy them coffee and ask: "What's the difference between a 'lean hire' and a 'lean no-hire' that has the same technical content?" Their answer will be about how the candidate handled the loop as a whole, not any single round.

## What "done" looks like by Sunday night

By the end of the week, the following should be true. If any of these aren't, stay with this week's work before moving on.

- You can name the **typical shape** of an onsite loop at a representative bigtech company (4-5 rounds, 4-6 hours, 1 lunch, 2-3 coding, 1 system design, 1 behavioural, recruiter handoffs) and the variants that differ (Amazon's bar-raiser, Google's hiring-committee-not-the-interviewers, Meta's "build your network at lunch" line, Stripe's "you stay in one room" model).
- You have a written **hour-by-hour day-of run-of-show** for your next real onsite — the night before, the morning of, every gap between rounds, the lunch, the closing, the post-loop two hours — in your portfolio.
- You can identify the **seven hostile-question patterns** and reproduce, in your own words, the response template for each.
- You can identify the **eleven EEOC-protected categories** (age 40+, race, colour, religion, national origin, sex, pregnancy, disability, genetic information, citizenship beyond legal-right-to-work, retaliation for prior protected activity) and reproduce, in your own words, the deflection language for a question that crosses into any of them.
- You have run a **4-hour mini-project mock** with peers (or solo if peers were impossible), scored it against the rubric, and written a debrief that names the three biggest issues to fix before the real loop.
- You have updated your **screen-call cheat sheet** with an onsite-section that fits on the same single screen: the run-of-show outline, the seven hostile patterns compressed to one phrase each, the deflection one-liner, the energy-budget reminder.
- You have written, in your own words, the **after-action template** — the 30-minute document you will fill out within 2 hours of every real onsite, capturing the rounds, the interviewers, the questions, the read of the room, and the three things you'd do differently.

This is the onsite-day-of baseline. You will revise the run-of-show after every real onsite for the rest of the cycle; this week's version is v1.

## Up next

[Week 8 — System Design and Senior-Level Rounds](../week-08/) — once the day-of logistics, the room-reading, and the legal frame are on muscle memory. Week 8 returns to the technical surface: the system-design round at the mid-level and senior-level depth, the API-design follow-ups, the "design a URL shortener / a rate limiter / a notification system" patterns, and the senior-only rounds that test scope of decision-making at small-team and mid-team scale.
