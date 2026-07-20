# Challenge 1 — Handle the trick question

**Time:** ~60 minutes (10 prep + 30 drill + 20 review). **Difficulty:** Easy/Medium. **Materials:** A recording app, a stopwatch, this file open as the prompt list.

## Problem

Four hiring-manager questions account for the majority of "I froze" moments in HM screens: the conflict question, the weakness question, the why-you-over-others question, and the first-90-days question. Each is fully scriptable in advance. The candidates who freeze on them are not the ones who can't think of an answer; they are the ones who haven't drilled the structure cold.

The challenge is to record yourself answering each of the four, score them, fix the weakest one, and re-record it until it lands.

## The four questions

Recap from Lecture 1, §10:

1. **The conflict question:** "Tell me about a time you disagreed with a teammate or your manager."
2. **The weakness question:** "What's your biggest weakness?"
3. **The why-you-over-others question:** "Why should we hire you over the other candidates?"
4. **The first-90-days question:** "What would you do in your first 90 days in this role?"

For each, the structure that works is in Lecture 1 §10. Re-read that section before starting.

## Protocol

### Part A — Prep (10 min)

In `c13-week-05/challenge-01-stress-questions.md`, draft 3-5 bullet points per question that capture the answer structure:

```markdown
## Stress question prep

### Q1 — Conflict
- Situation: [Specific recent disagreement; person + topic.]
- Substance: [The crux, fairly characterised.]
- Process: [What you did to resolve.]
- Outcome + lesson: [Where it landed; what you took from it.]

### Q2 — Weakness
- Real but bounded weakness: [Specific, not humblebrag.]
- Concrete cost: [What it actually costs you.]
- What you've done about it: [Active remediation, not aspiration.]
- Recent evidence: [Last 6 months; specific instance.]

### Q3 — Why you over others
- Two specific requirement-to-experience mappings.
- Honest acknowledgement: you don't know the other candidates.
- Concrete contribution sentence: [What you'd specifically bring.]

### Q4 — First 90 days
- Days 0-30 — listen: [2-3 specific intake activities.]
- Days 30-60 — small contribution: [What kind of first PR.]
- Days 60-90 — first ownership: [What you'd want to own, framed as a question to the HM.]
```

Constraints on the prep:

- Each answer should land in **60-90 seconds spoken** (~150-225 words).
- Each contains at least one **specific named example** (a recent disagreement, a specific remediation, a specific requirement from a JD, a specific component to own).
- Zero banned phrases from Lecture 1 (`passionate`, `team player`, `best practices`, `lifelong learner`, `work too hard`).

### Part B — The drill (30 min)

Open your recording app. For each of the four questions:

1. **Read the question aloud** (yes, out loud — pretend the HM just asked it).
2. **Pause for 2 seconds** to gather your thoughts. (Most candidates skip this; the pause makes the answer better.)
3. **Answer from the bullets**, on the stopwatch. Aim for 60-90 seconds.
4. **Stop the recording. Note the length.**
5. **Re-record once more.** Most second takes are 15-20% better.

Save four pairs of recordings: `q1-conflict-take1`, `q1-conflict-take2`, `q2-weakness-take1`, etc.

This is the drill loop. Eight recordings total in 30 minutes is right.

### Part C — Score and pick the weakest (10 min)

Play all eight recordings back. For each question's better take, score it against the 5-point rubric below.

| Score | What it looks like |
|------:|---------------------|
| 5 | Under 90 sec; specific named example; structured (4-part for conflict, 4-part for weakness, 3-part for why-you, 3-part for 90-days); landed cleanly; no banned phrases; no hand-waving. |
| 4 | All of the above with one minor miss (slight over-length, one hedge phrase, one slightly generic clause). |
| 3 | Two or three misses. Length might be 100s or the structure was partially missing. |
| 2 | Substantive structural problem (missed the remediation step, missed the example, ended without a forward sentence). |
| 1 | Failed structurally — the HM would write "couldn't answer cleanly." |

In your draft file:

```markdown
## Scores

- Q1 (conflict): __ / 5. Length: __ sec. Issues: __
- Q2 (weakness): __ / 5. Length: __ sec. Issues: __
- Q3 (why-you): __ / 5. Length: __ sec. Issues: __
- Q4 (90-days): __ / 5. Length: __ sec. Issues: __

**Weakest of the four:** Q__
```

### Part D — Fix the weakest, re-record (10 min)

For the lowest-scored question:

1. **Identify the structural miss.** Was the example missing? Was the structure off? Was the length over?
2. **Rewrite the bullets** to fix the specific miss.
3. **Re-record.** Score the new take against the same rubric.

If the new take scores 4+, you're done. If it doesn't, you have one more re-record budgeted (10 minutes is enough for two more takes). If after three takes it's still under 4, note the question for further work and move on; some answers take multiple sessions to land.

## Acceptance criteria

- [ ] `c13-week-05/challenge-01-stress-questions.md` exists.
- [ ] Prep bullets for all four questions populated.
- [ ] Eight recordings exist (two takes per question) in `c13-week-05/recordings/` or linked.
- [ ] Scores for the best take of each question recorded.
- [ ] The weakest question identified and re-recorded; new score noted.
- [ ] Total time budget held to ~60 minutes (or noted if it ran over and why).

## Common findings

- **Conflict answer leaked frustration.** The recording catches what the page hides. Rewrite to centre on the process, not the disagreement.
- **Weakness was a humblebrag.** "I work too hard" / "I'm too detail-oriented." Pick something real and bounded; HMs see the humblebrag immediately.
- **Why-you-over-others ran 30 seconds.** Too short reads as no answer prepared. The minimum is naming two specific requirement-to-experience mappings; aim for the full 60-90 seconds.
- **90-days was generic.** "I'd meet people and read the codebase." The fix is naming *specific* intake activities (which 1:1s, which docs, which on-call) and ending with a question to the HM about expectations.
- **Length over by 20+ seconds across all four.** Common; the fix is to cut the second example or the meta-commentary. Stress-question answers tighten significantly between Take 1 and Take 2.

## Stretch

- **Add a fifth question.** "Tell me about a time you handled an unexpected production issue" is a common HM behavioural that follows the same structure. Drill it.
- **Reverse pair.** If you have a peer for this challenge, run the four questions on each other in a 30-minute slot. Hearing someone else stumble through Q3 specifically will sharpen your own answer.
- **Cold-test the next day.** Sleep on it; the next morning, record one cold take of each of the four (no warm-up, no re-reading the prep). The cold take is closer to what'll happen on a live call.

## Why this matters

The four stress questions are not actually hard. They are scriptable, structured, and answerable in 60-90 seconds with the right prep. The reason they catch candidates is that candidates do not drill them in advance — they think "I'll figure it out in the moment" — and then in the moment, with someone watching, they freeze or hedge.

The 60-minute investment in this challenge converts "freeze" into "fluent" for the four questions that show up in roughly 80% of HM screens. The challenge is high-leverage specifically because the prep is bounded (four questions, four structures) and the rep value is immediate (the next HM screen will probably ask at least two of them).

The mini-project will catch any remaining looseness on these answers under the rubric. This challenge is the focused-drill version that gets you most of the way there in an hour.

## Submission

Commit `c13-week-05/challenge-01-stress-questions.md` and the recordings to your portfolio repo. The four answers will be referenced from your screen-call cheat sheet for the rest of the cycle.
