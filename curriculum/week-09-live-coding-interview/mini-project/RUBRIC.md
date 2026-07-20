# Mini-Project Rubric — The 12-Axis Self-Grading Sheet

This is the rubric you apply to your recorded mock interview. Print it, or open it in a second window, and fill it in as you watch the recording back.

Each axis is scored 0, 1, or 2. The scoring conventions are described in detail below. Total possible: 24.

---

## Axis 1 — Clarify phase had at least 4 distinct questions

- **0** — Asked zero or one clarifying question. Started coding before the problem was clarified.
- **1** — Asked 2-3 clarifying questions. The questions were correct but the phase ended too soon.
- **2** — Asked 4 or more distinct clarifying questions, including at least one about edge cases (empty input, single element, duplicates, negatives) and at least one about ambiguity in the problem statement.

**Timestamp where this happened:** _____________

**Notes:**

---

## Axis 2 — Examples phase walked at least 3 concrete cases

- **0** — Did not walk any examples; jumped from clarify to code.
- **1** — Walked 1-2 examples. The examples covered the happy path but not the edges.
- **2** — Walked 3 or more examples, including a happy path, an edge case (empty, single, duplicates, negatives, very large), and either a failure-mode input or an explicit confirmation of a clarification answer.

**Timestamp where this happened:** _____________

**Notes:**

---

## Axis 3 — Approach phase stated brute force before optimal

- **0** — Skipped the brute force entirely. Jumped to the optimal solution.
- **1** — Mentioned the brute force in passing without stating its complexity, or stated complexity but did not connect it to the optimisation.
- **2** — Stated the brute force, named its complexity, identified the bottleneck, proposed the optimisation, named the new complexity. All before coding.

**Timestamp where this happened:** _____________

**Notes:**

---

## Axis 4 — Approach phase stated complexity before coding

- **0** — Did not state the expected complexity of the chosen approach before coding.
- **1** — Stated complexity but vaguely ("this should be fast" / "linear-ish").
- **2** — Stated the precise expected time and space complexity, with a brief justification, before writing the first line of code.

**Timestamp where this happened:** _____________

**Notes:**

---

## Axis 5 — Code phase had type hints on function signature

- **0** — No type hints anywhere.
- **1** — Type hints on the function signature but not on intermediate variables, or partial type hints (return type missing).
- **2** — Type hints on the function signature (including return type) and on at least one intermediate variable. Python-style preferred; equivalent for other languages.

**Snippet of your function signature:** _____________

**Notes:**

---

## Axis 6 — Code phase had continuous narration

- **0** — Multiple silences of 30+ seconds during the code phase. Long stretches of typing without speaking.
- **1** — Narration was present but uneven. Some silences of 15-30 seconds. The interviewer would occasionally lose track of the candidate's reasoning.
- **2** — Continuous narration. Silences of more than 15 seconds were rare and deliberate (e.g., the explicit "let me think for a moment" pause). The narration was specific (not vague filler) and tracked the actual reasoning.

**Longest silence in the code phase (seconds):** _____________

**Notes:**

---

## Axis 7 — Test phase walked at least one example line-by-line

- **0** — No test phase. Said "I think it works" and stopped.
- **1** — Ran one example through the code but at a high level, not line-by-line. Skipped the variable-state walkthrough.
- **2** — Walked at least one example through the code line-by-line, naming each variable's value at each step, and explicitly checking the return value matches the expected output.

**Timestamp where this happened:** _____________

**Notes:**

---

## Axis 8 — Discuss phase stated complexity and at least one trade-off, proactively

- **0** — No discuss phase; round ended with the code working.
- **1** — Discuss phase happened but was triggered by the interviewer asking. Stated complexity but did not surface trade-offs unprompted.
- **2** — Discuss phase happened proactively. Stated time and space complexity, surfaced at least one trade-off (memory vs speed, readability vs cleverness, etc.) without being asked, and named at least one follow-up direction.

**Timestamp where this happened:** _____________

**Notes:**

---

## Axis 9 — Phase transitions were verbalised explicitly

- **0** — Phases blurred together. No transition phrases. The recording would be hard to segment into the six phases.
- **1** — Some phase transitions were verbalised but not all. Specifically, the transitions out of clarify and into discuss were silent.
- **2** — All five phase transitions were verbalised with explicit language ("let me walk through some examples now", "let me think about the approach", "let me start coding", "let me test this", "let me talk about trade-offs"). The recording is easy to segment.

**Notes (list the transition phrases you used):**

---

## Axis 10 — Applied at least one recovery move when stuck

- **0** — Got stuck and went silent. Did not apply any of the three moves (verbalise, clarify, simplify).
- **1** — Got stuck and applied one of the three moves, but only after a prolonged silence (>60 seconds).
- **2** — Got stuck and applied one of the three moves within 15-30 seconds. Or: did not get stuck at any point, in which case the axis is not applicable and you score 2 by default.

**If applicable, timestamp of the stuck moment and the move applied:** _____________

**Notes:**

---

## Axis 11 — Hint was taken cleanly without defence

- **0** — Was offered a hint (or gave yourself one through self-questioning) and either ignored it or defended the original plan. Phrases like "yes I already considered that" appear in the recording.
- **1** — Took the hint but with visible reluctance, or took it without acknowledging it explicitly.
- **2** — Took the hint cleanly: paused, acknowledged ("good question"), integrated explicitly out loud, pivoted if needed. Or: no hint was offered, in which case the axis is not applicable and you score 2 by default.

**If applicable, timestamp of the hint and your response:** _____________

**Notes:**

---

## Axis 12 — Executed the time-awareness check-in at minute ~20

- **0** — No time-awareness signal at any point in the round. Time was not visibly tracked.
- **1** — Time-awareness signal happened but late (after minute 30) or implicitly ("oh, we're running long").
- **2** — Explicit time-awareness check-in at minute 15-25, signalling the half-way point and the budget allocation for the remaining phases.

**Timestamp where this happened:** _____________

**Notes:**

---

## Total score

Add the 12 axis scores. Maximum: 24.

**Your total: _____ / 24**

**Interpretation:**

| Score | Tier | What this means |
|------:|------|-----------------|
| 21-24 | Strong-yes | Real-round-ready today. The structure is on muscle memory. |
| 17-20 | Lean-yes | Mostly there. Identify the 1-2 weak axes and drill them in the next week. |
| 13-16 | Borderline | Round would land as "weak hire" or "weak no" depending on the interviewer. Multiple axes need targeted work; rerun the mini-project in 1-2 weeks. |
| 9-12 | Weak | Structure is partially formed. Repeat Week 9 before moving forward. |
| Below 9 | Concerning | Restart the week. The issue is usually pacing or recording-skipping, not knowledge. |

## Which axes to prioritise

If your total is in the 13-20 range, identify the **two lowest-scoring axes** and treat them as your improvement targets for the next 1-2 weeks. The pattern of common low-scoring axes:

- **Axes 1-2 low** → Your clarify-and-examples discipline needs work. Re-run Exercise 1 daily for a week.
- **Axes 3-4 low** → Your approach-phase narration needs work. Re-read Lecture 1's approach-phase section; on the next mock, deliberately over-narrate the brute-force-then-optimal arc.
- **Axes 5-6 low** → Your code-phase mechanics need work. Add type hints to every variable on the next mock; consciously fill any silence longer than 10 seconds with the rehearsed phrases from Week 6.
- **Axes 7-8 low** → Your test-and-discuss phase is being skipped or rushed. The most-common cause is over-running earlier phases; the fix is the minute-20 check-in.
- **Axes 9** low → You're treating the phases as internal rather than visible. The fix is the explicit phrase rehearsal — pick five transition phrases and use them on every round.
- **Axes 10-11 low** → Recovery and hint-taking are weak. Run Challenge 1 with a partner before the next mock.
- **Axis 12** low → Time-awareness needs work. Set an actual phone alarm for minute 20 of your next solo mock; the alarm is the external trigger that builds the internal one.

## Save the rubric

When you have completed the rubric, save it as `RUBRIC-FILLED.md` in this folder. Do not overwrite this template. The filled version is your artifact for the week; the template is the reusable scoring sheet for future rounds.

Date the filled rubric. When you run a future mini-project (likely 2-4 weeks later), save the next filled rubric with the new date. Comparing two filled rubrics across time is the longitudinal record of your improvement.
