# Exercise 1 — Your recent-project story

**Time:** ~90 minutes. **Output:** A bulleted draft of your 4-6 minute recent-project story, a prepared drill-down sheet covering 3-5 key decisions with their alternatives and inflection points, and three recordings showing measurable improvement across iterations.

## Goal

Produce a recent-project answer that lands in the 4-6 minute spoken range, uses the six-segment structure from Lecture 1, leads with the problem, demonstrates ownership through correctly placed "I" pronouns, includes one technical trade-off you actually owned, lands on a concrete outcome with at least one number, and **survives two layers of drill-down follow-ups** on at least three of the project's key decisions.

## Setup

You need:

- Your **current v2 resume** (from Week 2 mini-project). The project story must agree with what's listed.
- A **shortlist of candidate projects** — write down 2-4 projects from the last 6-18 months you could plausibly tell this story about. You'll pick one.
- A **stopwatch** — your phone is fine.
- A **recording app** — phone voice memo, Loom, QuickTime, OBS, or Yoodli. Audio is enough; video is better because you'll catch pacing and eye-contact issues.
- A **markdown file to draft in**: `c13-week-05/exercise-01-recent-project.md`. Draft in writing; do not draft in your head.
- A **quiet room** for the recording.

## Process

### Step 1 — Pick the project (10 min)

In your draft file, list 2-4 candidate projects:

```markdown
## Candidate projects

1. **{Project name 1}** — {one-line summary}, {when, dates}, {your role}.
2. **{Project name 2}** — ...
3. **{Project name 3}** — ...
```

For each, run the three-criteria filter from Lecture 1 §3:

- **Recent?** Was it in the last 6-18 months? (12-18 months is the sweet spot; older risks the "your best work is dated" read.)
- **Owned?** Did you make non-trivial decisions, or did you implement someone else's design? (You need decisions you can speak to.)
- **Drill-downable?** Can you name 3-5 key decisions, the alternatives for each, and the conditions under which you'd have chosen differently?

For each, score recency / ownership / drill-downability as low / mid / high. Pick the project that is **mid-or-high on all three**. If only one project clears the bar, pick it. If multiple, pick the one with the deepest drill-downability, even if not the flashiest.

```markdown
## Selected project: {Project name}

**Why this one:** [One sentence: most-recent / strongest ownership / deepest follow-up survivability.]
```

### Step 2 — Pull the raw material (15 min)

In your draft file, capture the inputs that feed the six-segment structure. Don't write the story yet; just gather the parts.

```markdown
## Raw material

**Problem (Segment 1):**
- The system or surface: [What was the system, in 1 sentence?]
- The problem statement: [What was wrong? Include a number — latency, dollars, error rate, throughput, customer count.]
- The cost of the problem: [What was the concrete consequence — pages, lost revenue, broken SLO, customer complaints?]

**Your role (Segment 2):**
- Your specific role: [Owned / co-owned with N others / led team of N.]
- Your scope: [Which of: design, implementation, rollout, operations, all?]

**Decisions and trade-offs (Segment 3) — the key list:**
1. **Decision 1:** [What was it? What was the alternative? Why did you choose this way?]
2. **Decision 2:** [Same.]
3. **Decision 3:** [Same.]
4. **Decision 4 (optional):** [Same.]
5. **Decision 5 (optional):** [Same.]

**Implementation specifics (Segment 4):**
- 2-3 specific technologies, design patterns, or architectural details.
- The hardest part: [One specific challenge.]
- How you handled it: [Specific approach.]

**Outcome (Segment 5):**
- One or two metrics: [Latency drop, throughput gain, customer impact, dollar number, incident count.]
- Any surprises: [Incidents, rollbacks, things that went unexpectedly well or poorly.]

**What you'd change (Segment 6):**
- One specific thing you'd do differently.
- The lesson, in one sentence.
```

This is the corpus. The script is built from these inputs and nothing else.

### Step 3 — Build the drill-down sheet (15 min)

Before writing the spoken script, write the prep for the follow-ups. This is the most-skipped and highest-leverage part of the exercise.

For each of the 3-5 decisions you listed in Segment 3, write:

```markdown
## Drill-down prep

### Decision 1: {one-line description}

- **What you chose:** [One sentence.]
- **What you didn't choose:** [The actual alternative, in one sentence.]
- **Why you didn't choose it:** [One or two sentences. Specific reasoning, not "best practice."]
- **What would have changed your mind:** [The inflection point. "If {condition X}, we'd have chosen {alternative} instead."]
- **What did the other engineer / team / stakeholder think:** [If relevant — who agreed, who pushed back, how it was resolved.]

### Decision 2: ...

[Same five sub-points.]
```

This sheet does not appear in your spoken story. It is your prep for the drill-down questions that follow the story. **In a real call, an HM will probe two or three of these decisions for at least two layers.** You should be able to answer fluently because you've already thought through the inflection points.

### Step 4 — Draft v1 of the spoken script (15 min)

Using the six-segment structure from Lecture 1 §4, write a spoken-style draft:

```markdown
## Draft v1 — the spoken script

**Segment 1 — The problem (30-45 sec):**
> [Lead with the problem statement and the cost.]

**Segment 2 — Your role and team shape (30 sec):**
> [Who you were on the team and what your scope was.]

**Segment 3 — The decisions and trade-offs (90-120 sec):**
> [The key decisions — 2-3 named, with the non-obvious one explained and the trade-off stated.]

**Segment 4 — Implementation specifics (45-60 sec):**
> [The 2-3 technologies; the hardest part; how you handled it.]

**Segment 5 — Outcome (30-45 sec):**
> [The metrics, with numbers; any surprises.]

**Segment 6 — What you'd change (20-30 sec):**
> [The one thing; the one lesson.]
```

Constraints on the draft:

- Total word count: **500-700** (corresponds to 4-6 spoken minutes at normal pace).
- At least **one "I" pronoun per segment** for segments 2-6. If you've only written "we" anywhere, audit: was it genuinely the team, or are you hiding individual contribution?
- At least **two specific quantified outcomes** somewhere in the answer — one in the problem statement, one in the result.
- At least **one named trade-off** in Segment 3 — "we chose A over B because X; the cost was Y."
- Zero banned phrases (`passionate`, `team player`, `wear many hats`, `lifelong learner`, `best practices`, `move the needle`, `it was a great learning experience`).

### Step 5 — First recording, untimed (5 min)

Open your recording app. Record yourself delivering Draft v1 from bullets (not from prose).

**Important: read from bullets, not from prose.** The prose is for structure-checking and word-counting; the delivery is from bullets so you sound conversational, not read-aloud.

Save as `recording-01-untimed.{m4a|mp4}`. Note the length in your draft file.

### Step 6 — Review the first recording (10 min)

Play it back. Note in your draft file:

```markdown
## Recording 1 review

**Length:** [seconds]

**Structural issues:**
- [ ] Did not lead with the problem (opened with the solution or with team context)
- [ ] Decisions and trade-offs were buried at the end instead of in the middle
- [ ] No "what I'd change" segment (or it was generic)
- [ ] No specific numbers in problem statement or outcome
- [ ] Used a banned phrase

**Ownership language:**
- [ ] Five or more "we"s with no "I"s in the same segment
- [ ] Switched from "I" to "we" specifically when describing a technical decision
- [ ] Hid a decision behind "the team decided" — was it actually the team, or was it you?

**Delivery:**
- [ ] Pace too fast (under 4 minutes total)
- [ ] Pace too slow (over 6 minutes total)
- [ ] Filler ("um," "uh," "like") at a count of: ___
- [ ] Hedge words ("kind of," "sort of," "I guess," "I think we maybe")
- [ ] Trailing "yeah" or "so" at sentence ends
```

Most candidates' first recordings have 3-6 of these issues. The point is to *see* them, not to be defensive about them.

### Step 7 — Revise to v2 (10 min)

Edit the bullets to fix the structural issues first, then the ownership issues, then the delivery issues. Specifically:

- If you didn't lead with the problem, rewrite Segment 1 so the first sentence is the problem statement with a number.
- If decisions were buried, restructure so Segment 3 is the longest, centred segment.
- If "we" hid individual contribution, replace specific "we"s with "I"s. Where you used "the team decided," rewrite as "I proposed X, the team ratified it" or "we decided X" if it was genuinely collective.
- If you used a banned phrase, replace with a specific noun (a technology, a metric, a decision).

### Step 8 — Drill-down rehearsal (10 min)

Before re-recording the spoken script, rehearse the drill-down. Read the questions below aloud, and answer each, timing yourself. Aim for 30-60 seconds per answer.

For *each* of the 3-5 decisions in your drill-down sheet, practice:

- "Why did you choose {your choice} over {the alternative}?"
- "What would have changed your mind?"
- "Did you consider {a third option}?"

If any answer takes more than 90 seconds, it's too long. If any answer comes out as "I'm not sure" or "we just thought it was right," that decision is not drill-down-survivable; either prep more, or pick a different decision for the spoken script.

### Step 9 — Second recording, timed (5 min)

Re-record Draft v2 from the revised bullets. Use the stopwatch. Aim for 4-6 minutes.

If under 4 minutes: you're skipping or rushing a segment. Re-record more deliberately, especially Segment 3 (decisions and trade-offs).

If over 6 minutes: you're describing rather than narrating. Trim Segment 4 (implementation specifics) first; that's usually the most-trimmable.

Save as `recording-02-timed.{m4a|mp4}`. Note the length.

### Step 10 — Review and revise to v3 (10 min)

Play recording 2 back. Update the issues checklist. Specifically attack:

- **Pace.** If you're at 4:30-5:00, you're in the sweet spot. If you're at 5:30-6:00, you're at the high end; any nervous talking on a real call will push you over.
- **Filler words.** Above 5 per minute is high. The fix is silent pauses, not "removing fillers."
- **The opening sentence.** Replay just the first 15 seconds. Does it state the problem with a number? If not, rewrite Segment 1's first bullet.
- **Segment 3's centre of gravity.** Replay the middle minute. Are decisions and trade-offs clearly the centre? If you can't tell from listening, the structure didn't land.

### Step 11 — Third recording, final (5 min)

Re-record v3. Save as `recording-03-final.{m4a|mp4}`.

This is the version you'll use as your baseline. Future revisions (after each real HM screen) will build on this.

## Acceptance criteria

- [ ] `c13-week-05/exercise-01-recent-project.md` exists.
- [ ] Candidate-projects shortlist is documented with the selection rationale.
- [ ] Raw-material section is filled in completely (problem, role, 3-5 decisions, implementation, outcome, what you'd change).
- [ ] Drill-down sheet exists with 3-5 decisions, each with what-you-chose, what-you-didn't, why, what-would-have-flipped-it.
- [ ] Draft v1 is 500-700 words across the six segments.
- [ ] Draft v1 contains zero banned phrases, at least one "I" per segment 2-6, and two quantified outcomes.
- [ ] Three recordings exist: untimed, timed, final.
- [ ] Recording 3 is **between 4 and 6 minutes**.
- [ ] Recording 3 has fewer than 5 filler words per minute.
- [ ] Recording 3 leads with the problem in the first 15 seconds.
- [ ] Recording 3 names at least one explicit trade-off ("we chose X over Y because...").
- [ ] An issues-checklist comparison across the three recordings, showing what improved.

## Common mistakes

- **Picking the flashiest project, not the most drill-downable one.** Your highest-profile project may have been one where someone else made the key decisions. Pick the project where *you* owned the decisions, even if it's smaller.
- **Skipping the drill-down sheet.** "I'll just answer the follow-ups when they come up." On a live call, "when they come up" is when you stumble. The 15 minutes spent on the sheet is the single most-valuable part of this exercise.
- **The all-we answer.** Every "we" is a place an HM cannot find your individual contribution. After Draft v1, do a pass specifically on pronouns — if a segment has zero "I"s, audit every "we" in it.
- **Over-rehearsing into woodenness.** The fifth time you say the script, it starts sounding rehearsed. Stop at three recordings; refresh by re-reading the bullets cold before the live call.
- **The 7-minute version.** Your answer is too long. You think it's because there's "so much to cover." It's actually because you're not selecting — every detail is in there. Cut Segment 4 first; that's almost always the bloat zone.
- **No "what I'd change" segment.** Most candidates skip this in their first draft and never go back. An HM specifically listens for self-critique; absence of it reads as defensiveness or as someone who hasn't reflected on their own work.

## Stretch

- **Build a second project story.** Some HMs ask for two projects, or steer you off your first answer to test breadth. Draft a second 4-6 minute story for a second project, with its own drill-down sheet. (Half the time of this exercise; the structure transfers.)
- **The 90-second variant.** Some HMs preface their probe with "give me a 90-second version of a project, then I'll pick where to drill in." Draft a 90-second compression that names the problem, the role, the central decision, and the outcome — designed to be re-expanded under follow-up.
- **The "what would you do differently if you had to start over today" variant.** A common HM follow-up. Draft a 60-second answer specifically to that question for your project, separate from Segment 6.
- **Yoodli analysis.** Run recording 3 through Yoodli's free tier. Compare the AI's filler-word density and pace numbers against your self-assessment.
- **The peer-read.** Send recording 3 to a peer with the rubric from the mini-project. Have them score the recent-project beat blind, then compare their score with your self-assessment.

## Why this matters

The recent-project answer is the single most-asked question of the HM screen and the load-bearing artifact for the *rest of the call*. The HM's drill-down decides how the next 20 minutes go: a strong answer earns substantive follow-ups (which is the conversation you want); a weak answer earns either a softer set of questions (the HM has already decided) or a probe-until-it-cracks pattern.

The 90 minutes you spend on this exercise pay back the first time an HM drills into your project for ten minutes and you answer every layer fluently. The HM's debrief then writes itself: "owned the project, articulated the trade-offs under follow-up, would be strong on the team." That's the move-forward.

The drill-down sheet is the part most candidates skip and the part that separates the candidates who pass HM screens from the ones who don't. The script gets you started; the sheet keeps you on your feet.

## Submission

Commit `c13-week-05/exercise-01-recent-project.md` and the three recordings to your portfolio repo. (If audio files are large, store outside the repo and link.)
