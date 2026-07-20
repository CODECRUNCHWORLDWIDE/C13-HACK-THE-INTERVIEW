# Exercise 3 — Handle the follow-up question

**Time:** ~60 minutes (15 prep + 30 drill + 15 review). **Output:** A drafted answer template for each of the four follow-up patterns, three recordings of you answering each pattern under 90 seconds, and a marked-up version showing the specific fixes you'll apply.

## Goal

The last 5-10 minutes of a technical phone screen always include a follow-up question. Most candidates underprep this beat, because they assume the call ends when the coding ends. It does not. The follow-up question is its own scored beat, and a strong follow-up answer raises the rubric one notch even on a screen where the coding was rough.

This exercise drills the **four patterns** the follow-up question always falls into: complexity analysis, problem extension, production framing, and edge-case probe. By the end, each has a default structure you can deploy under 90 seconds on any easy or mid problem.

## Setup

You need:

- A **recording app** — Loom, QuickTime, or OBS. Audio is the minimum.
- A **stopwatch** — phone is fine. The 90-second target is the load-bearing constraint.
- A **scratch pad and pen** — for sketching the extensions and complexity arguments.
- A **markdown file**: `c13-week-06/exercise-03-followup-question.md`.
- A **completed Exercise 2** — you'll use the problems from Exercise 2 as the substrate for the follow-up answers.

## The four follow-up patterns

Recap from Lecture 1 §11 and Lecture 2 §10. Each has a known structure and known failure mode.

### Pattern 1 — Complexity analysis

> "What's the time and space complexity of your solution?"

Sometimes phrased as: "Can you walk me through the Big-O?" or "What's the bound here?" or "How does this scale?"

**The structure:**

1. **Time complexity, named and justified.** "Time is O(n) because we iterate through the input once; each operation inside the loop is constant time (hash-map insert and lookup are O(1) amortised)."
2. **Space complexity, named and justified.** "Space is O(n) because the hash map can hold up to n entries in the worst case."
3. **Acknowledge the worst case if it differs from amortised.** "In the absolute worst case, hash-map operations are O(n) due to collisions, which would make the overall time O(n²); in practice with a good hash function it's O(n)."

60-90 seconds spoken. Do not over-explain; do not skip the worst-case acknowledgement at senior+ levels.

**The failure modes:**

- "I think it's O(n)." Reads as not sure.
- Naming only time, not space.
- Confusing amortised and worst-case.
- Using "constant" when you mean O(1), or "linear" when you mean O(n), without naming the formal complexity. (Acceptable at junior level; flagged at senior.)

### Pattern 2 — Problem extension

> "What if the input were a stream instead of an array?"

Variants:
- "What if the input were too large to fit in memory?"
- "What if the input were sorted?"
- "What if we needed to handle k pairs instead of one?"
- "What if we wanted to return all solutions, not just one?"
- "What if the input came in two parts?"

**The structure:**

1. **Name what changes.** "If the input is a stream, we can't iterate twice. The hash-map approach still works because it processes each element once, but we can no longer go back to look up earlier elements."
2. **Name what stays.** "The per-element work is still O(1) — hash-map insert and lookup. So the per-element complexity is the same."
3. **Name any new edge cases or constraints.** "We'd need to think about memory if the stream is unbounded — the hash map grows without bound. In production we'd add a sliding-window constraint or an eviction policy."
4. **Optionally: sketch the change to the code.** "Concretely, the function signature changes from `solve(arr: List[int])` to `solve(stream: Iterator[int])`. The main loop is the same; we just consume the iterator."

60-90 seconds spoken. The structure is name-what-changes / name-what-stays / name-new-edges. The "sketch the change" is optional at junior level, expected at senior.

**The failure modes:**

- "It would be harder." Reads as not having thought about it.
- "I'd just rewrite it." Reads as not understanding the structure.
- Conflating an extension with a totally different problem.
- Ignoring that the original solution might still work with minor changes.

### Pattern 3 — Production framing

> "How would you change this for production traffic?"

Variants:
- "What would you add before shipping this?"
- "Imagine this is going into a real service. What's missing?"
- "How would you make this robust?"

**The structure:**

1. **Pick three concrete things, prioritised.** From: input validation, error handling, logging, monitoring, metrics, concurrency, caching, rate limiting, observability. Pick the three most-relevant to *this specific problem*.
2. **Name what each does.** "First, input validation — currently the function assumes the input is well-formed; in production we'd validate that the array is non-null, the integers are within bounds, and the target is a valid integer. Second, logging — we'd log the function entry with the input size and the output; that goes into the structured-log pipeline. Third, metrics — we'd emit a histogram of execution time, because if this scales to O(n²) on a degenerate input we want to see it in monitoring."
3. **Acknowledge what you're *not* covering.** "I'm not covering concurrency here because the function is pure and stateless; if it shared state we'd need synchronisation."

60-90 seconds spoken. Three things, named, with a sentence on each. Do not list eight things shallowly.

**The failure modes:**

- "I'd add error handling and logging." (Two-word answer; no specifics.)
- "I'd test it." (Test the production version, sure — but that's separate from the change.)
- Over-engineering for a simple function. (Reads as not having calibrated to the actual production context.)
- Mentioning Kubernetes / microservices / event sourcing on a stateless utility function. (Reads as memorised.)

### Pattern 4 — Edge-case probe

> "What if the input is empty?"

Variants:
- "What if the array has only one element?"
- "What if there are duplicates?"
- "What if there's no valid answer?"
- "What if the input is malformed?"
- "What's the largest input this can handle?"

**The structure:**

1. **State the behaviour for this case.** "If the input is empty, the function returns an empty list — there are no pairs to find."
2. **Confirm the code handles it.** "My code handles this because the loop body never executes on empty input; the empty result is the default."
3. **Name any other related edges.** "Related edges: single-element input also returns empty for the same reason. The other edge worth checking is all-duplicates — my hash-map approach handles that because the lookup-and-insert pattern naturally deduplicates."
4. **Optionally: add a guard if you didn't have one.** "Actually, I didn't add an explicit guard for null input — let me add that. {Edit code.} Now it returns empty for both null and empty."

30-90 seconds spoken. Shorter than the other three patterns because the answer is usually "the code already handles it" or "let me add a one-line guard."

**The failure modes:**

- "Oh, I didn't think about that." (Reads as not having tested.)
- Adding the guard without re-running the tests. (Reads as not respecting the test phase.)
- Long discussions of how to handle malformed input when the original problem assumed well-formed input. (Reads as scope creep.)

## Process

### Step 1 — Pick the substrate problems (5 min)

In your markdown file, pick three of the problems you solved in Exercise 2. You'll do one follow-up pattern on each.

```markdown
## Substrate problems

- Problem A (will drill complexity + edge case on this one): ___
- Problem B (will drill extension on this one): ___
- Problem C (will drill production framing on this one): ___
```

### Step 2 — Draft the answer for each (15 min, 5 per pattern)

In your markdown file, draft the answer using the four-pattern structures above. Aim for 90 seconds spoken (~150-225 words) per answer.

```markdown
## Drafted answers

### Pattern 1 (Complexity) on Problem A

[Draft, 100-200 words.]

### Pattern 2 (Extension) on Problem B — "what if input were a stream?"

[Draft.]

### Pattern 3 (Production) on Problem C

[Draft.]

### Pattern 4 (Edge case) on Problem A — "what if input is empty?"

[Draft.]
```

### Step 3 — Record (15 min)

For each of the four answers, start the recording, give yourself 5 seconds of pause, then deliver the answer from memory (not reading the draft). Time each one. Stop the recording after each.

Four short recordings, each 60-90 seconds. Save them named:

- `followup-01-complexity.{m4a|mp4}`
- `followup-02-extension.{m4a|mp4}`
- `followup-03-production.{m4a|mp4}`
- `followup-04-edge-case.{m4a|mp4}`

### Step 4 — Score (10 min)

Re-listen to each recording. Score yourself on three things per answer:

| Criterion | 1-5 |
|-----------|----:|
| Length (90 seconds or under) | __ |
| Structure (followed the named structure for the pattern) | __ |
| Specificity (named concrete things, not generic phrases) | __ |

Total per answer: __ / 15.

In your markdown file:

```markdown
## Scoring

| Answer | Length | Structure | Specificity | Total |
|--------|-------:|----------:|------------:|------:|
| Complexity | __ | __ | __ | __/15 |
| Extension | __ | __ | __ | __/15 |
| Production | __ | __ | __ | __/15 |
| Edge case | __ | __ | __ | __/15 |
```

The minimum bar is 11/15 per answer. Anything under needs a re-record with the specific issue fixed.

### Step 5 — Re-record any answer under 11/15 (15 min)

Same protocol as Step 3 for any answer that scored under 11. Note the change:

```markdown
## Re-recordings

### Pattern N — {original score → new score}
- Fix made: ___
- Specific thing improved: ___
```

## Acceptance

- All four drafted answers exist in the markdown file.
- All four recordings exist (length 60-90 seconds each).
- All four are scored against the rubric.
- Any answer under 11/15 has a re-recording with a measurable score improvement.
- A one-paragraph summary at the bottom: which of the four patterns is hardest for you, and why.

## Common findings

- **Pattern 3 (production) is the most-skipped prep area.** Most candidates can name "error handling, logging, monitoring" but cannot fluently sketch each on a 30-second budget. Fix: keep three specific phrases ready for each ("structured log on function entry with input size and execution time").
- **Pattern 1 (complexity) is the most-rushed.** Candidates assume "O(n)" answers the question. Senior+ levels expect time AND space AND a worst-case acknowledgement.
- **Pattern 2 (extension) catches candidates who memorised the original solution.** If you cannot articulate what your solution actually depends on, you cannot articulate what changes when the input changes.
- **Pattern 4 (edge case) most-often surfaces an actual bug** — the candidate realises mid-answer that their code did *not* handle the case they're describing. That's fine in practice; in a real call, surface the bug honestly and fix it.

## Stretch

- **Record yourself answering all four patterns on a single problem.** "Two Sum" works well. The integrated 4-minute follow-up sequence is closer to the real-call shape than four separate answers.
- **Have a peer ask you the follow-up questions cold.** If you can pair with someone from Exercise 1, swap roles: you answer four follow-ups on each of two problems. Mutual drill, 30 minutes, very high signal.
- **Repeat once a week.** The follow-up patterns degrade faster than the narration loop because they are less practised. Fifteen minutes weekly through the rest of the cycle keeps them sharp.
