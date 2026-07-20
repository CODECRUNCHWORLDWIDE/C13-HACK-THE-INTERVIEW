# Challenge 2 — Build the Rubric, Score Yourself

**Time:** ~1 hour. **Format:** Write the new-grad-passing rubric in your own words; score one of your exercise write-ups against it. **Prerequisite:** Lectures 1-3; Exercises 1-3.

## What this challenge is for

Interviewers use rubrics. The rubric is the document the interviewer fills out within an hour of the round and ships to the hiring panel. The rubric is what is averaged in the debrief; the rubric is what the calibrator reads when there is disagreement; the rubric is the artefact that produces the hire/no-hire decision.

If you do not know what the rubric looks like, you are designing against a target you cannot see. If you do know, you can practice against it directly.

Real rubrics vary by company, but most FAANG-tier rubrics for system design have a similar shape. This challenge has two parts: (1) build the rubric in your own words, in the format real interviewers use, and (2) score one of your three exercises against it. The scoring is the calibration; the writing the rubric is what forces the calibration to be specific.

## Part 1 — Write the rubric

A real system-design rubric has 5-7 scoring dimensions. Each dimension has 3-5 levels (commonly: Strong No-Hire, No-Hire, Lean No-Hire, Lean Hire, Hire, Strong Hire). For each dimension at each level, the rubric has a one-sentence behaviour anchor describing what the candidate did.

Build your version. The dimensions you should include (matching what most FAANG rubrics actually score):

1. **Requirements clarification and scoping**
2. **High-level system structure**
3. **API and data model**
4. **Depth on the deep-dive component**
5. **Quantitative reasoning (estimation, latency, capacity)**
6. **Trade-offs and scale**
7. **Communication and pacing**

For each, write the behaviour anchor at three levels: No-Hire, Lean Hire (the new-grad-passing bar), Hire (the L4 passing bar). You do not need to write Strong Hire or Strong No-Hire; the middle three are where 90% of new-grad candidates land.

### Example: dimension 1, behaviour anchors

| Level | Behaviour anchor |
|-------|------------------|
| No-Hire | Did not clarify requirements; dove straight into the design. Did not ask about scale. Could not commit to a non-functional priority. |
| Lean Hire (new-grad bar) | Confirmed the core feature in one sentence. Asked for or committed to a scale anchor. Listed two non-functional priorities. Bounded the scope. Took ~5 minutes. |
| Hire (L4 bar) | Same as Lean Hire, plus: identified at least one non-obvious requirement that the prompt did not state explicitly. Made the scope boundary explicit in a way that the interviewer noted as thoughtful. |

Write all seven dimensions with the same three-level structure. Spend ~30 minutes; the rubric should be ~1-2 pages.

### What to copy from real sources, what to make your own

Look at the public rubric language from:

- Google's "Search Quality Rater Guidelines" (not system design, but the rubric-format pattern is canonical and public).
- Amazon's "Leadership Principles" rubric for behavioural rounds (the format, not the content).
- Pramp's free system-design scoring rubric (visible to anyone who runs a mock; if you have not run one, the format is published in their help docs).

The dimensions are universal. The behaviour anchors are yours to write — and they have to be in your own words, because in a real round you are not reading a rubric, you are reproducing one from internal model.

## Part 2 — Score yourself

Pick one of your three exercise write-ups (URL shortener, rate limiter, or news feed). Read it carefully. For each of the seven dimensions on your rubric, place yourself on the No-Hire / Lean Hire / Hire scale. Write a one-sentence justification for the score.

### Example self-score

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Requirements clarification | Lean Hire | Confirmed the URL shortener prompt; committed to 100M URLs/day; listed two non-functional priorities (low-latency reads, high availability); bounded scope. Took 6 minutes (slightly over the 5-min budget, but acceptable). |
| High-level system structure | Lean Hire | Five boxes, all labelled. Defaulted to Postgres, Redis, ticket server, app servers. Missed the queue (no analytics, but the prompt didn't require one — borderline). |
| API and data model | Hire | Three endpoints with full HTTP semantics; two-table schema with typed fields and indexes. Indexed short_code correctly. Caught the expires_at and is_active fields, which are not strictly required but are common follow-ups. |
| Deep-dive depth | Lean Hire | Three approaches for short-code generation; committed to counter+base62 with the ticket-server pattern; drew a second diagram. Did not get into the failover behaviour of the ticket server in detail. |
| Quantitative reasoning | No-Hire | Stated DAU but did not compute QPS or storage. The estimation phase was implicit, not visible to the interviewer. This is the biggest gap. |
| Trade-offs and scale | Lean Hire | Named two trade-offs (Postgres choice, strong consistency on ID generation). Named one thing that changes at 10x. Did not name a failure mode I didn't handle. |
| Communication and pacing | Lean Hire | Ran the six phases. Transitions were audible. The deep dive ran ~3 minutes long, which compressed the trade-offs phase. |

**Overall:** Six Lean Hire, one Hire, one No-Hire. The No-Hire is on quantitative reasoning — that is the gap to close before the real round. Targeted drill: redo the estimation phase three times solo with a timer.

### What to do with the self-score

The self-score produces a list of dimensions and the level you scored on each. The plan:

- **Any No-Hire dimensions:** drill specifically before the real round. Each No-Hire is a real gap. Two No-Hires means the round itself is likely to be a no-hire; close at least one.
- **All Lean Hire:** you are passing. The work for the rest of the week is to drill the weakest Lean Hire toward Hire.
- **Any Hire dimensions:** you can lean on these in the round. They are your strengths. The strong candidate plays to strengths in the deep-dive selection and the trade-offs phase.

## Part 3 — Compare against a peer

If you have a peer in C13 who is also doing the exercises, swap rubrics and self-scores. Each scores the other's exercise write-up against the other's rubric. The cross-score is more honest than self-score; the peer will catch the No-Hires you rationalised into Lean Hires.

The peer comparison takes ~20 minutes. It is high-leverage. The candidates who go to the real round having been scored by a peer outperform candidates who only self-scored, in the same way that Pramp peer mocks outperform solo prep.

## Acceptance criteria

- You produced a written rubric with all seven dimensions, each at three levels, with behaviour anchors.
- You self-scored one of your three exercise write-ups against your rubric, with a one-sentence justification for each score.
- You identified at least one dimension to drill before the real round.
- (Optional, high-leverage) You swapped scores with a peer.

## Common failure modes

1. **The rubric was too soft.** Every dimension's behaviour anchors looked like things you already did. The rubric is not for self-flattery; it is for honest calibration. Fix: write the No-Hire anchor first; it should describe a specific, observable failure mode.
2. **The self-score was uniformly Lean Hire.** No dimensions called out as weak. This is statistically suspicious; almost every candidate has at least one No-Hire or one Hire dimension. Fix: be honest about quantitative reasoning specifically; it is the single most-skipped phase.
3. **The rubric and the self-score did not produce an action.** "I scored a Lean Hire on average" is not actionable. The action is "I scored No-Hire on dimension X; I will drill X." Fix: every rubric-and-score exercise must produce one drill item.
4. **The rubric only had Lean Hire and Hire.** Without a No-Hire level, the rubric cannot distinguish "passed the bar" from "stood out." Fix: write all three levels even if you score yourself only at the middle two.

## Why the rubric belongs to you

The rubric is yours — not the company's — because the company's actual rubric is confidential and you will never see it. The exercise is to internalise what a rubric looks like so that, in the real round, you can hold your own performance against an implicit version of it. The candidate who has a rubric in their head and is silently scoring themselves at each phase boundary produces a different round than the candidate who is just doing what feels right.

The rubric you build this week will evolve. After your first real onsite with a design round, revise it. The dimensions that turn out to matter more than you weighted go up; the dimensions that matter less go down. By your fourth or fifth real round, the rubric is internal vocabulary and the explicit document is no longer necessary.

## What to carry forward

The rubric, the self-score, and the drill list. Specifically:

- One page of rubric, on your notes folder, that you re-read the morning of the real round.
- One self-score, dated, showing the dimensions you most need to drill.
- One drill scheduled before the round — a redo of one exercise with the targeted dimension in focus.

The rubric is a tool, not an artefact. The rubric is good when the round goes better because you used it. Track that; treat the rubric the way you treat the run-of-show from Week 7 — a living document, revised after every real round.
