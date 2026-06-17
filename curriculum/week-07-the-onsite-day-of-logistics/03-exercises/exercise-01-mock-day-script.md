# Exercise 1 — Mock Day Script

**Time:** ~90 minutes. **Output:** A written hour-by-hour run-of-show for your real or expected onsite — from the night before, through the morning of, every gap between rounds, the lunch, the closing, and the post-loop two hours. Lives in your portfolio as `c13-week-07/run-of-show.md`.

## Goal

Convert the generic shape of an onsite (Lecture 1) into a specific, named, dated, named-interviewer-where-known, run-of-show document for your next real onsite. The document is the artefact you read the night before and the morning of; it is the substitute for trying to plan against the loop in real time when you are tired, nervous, and short on cognitive bandwidth.

The document should be specific enough that someone else could follow it and produce a credible mock of your day. If yours reads "Drink coffee. Be on time. Do my best," it is not yet the artefact.

## Setup

You need:

- **A specific loop to plan against.** Real (one you have scheduled) is best. Expected (one you anticipate scheduling in the next 2-4 weeks) works. Hypothetical (one you would imagine for your target company) is the fallback; if you go this route, pick a real target company and use its published candidate guide.
- **The company's published candidate guide**, if it exists. Section 2 of the resources file lists the published guides for the bigtech companies. Smaller companies may not have one; in that case, use the Glassdoor "Interviews" surface for the company plus the role.
- **Your cheat sheet from Weeks 4-6.** You will be adding an onsite section to it as part of the homework; this exercise produces the run-of-show, the cheat-sheet update is separate.
- **A markdown file**: `c13-week-07/run-of-show.md`. Template below.
- **A specific calendar slot for the loop** (real or rehearsed). The run-of-show is dated.

## Process

### Step 1 — Capture the known facts (15 min)

Open the file. Fill in the header:

```markdown
# Onsite run-of-show — {company}, {date}

## Known facts

- **Company:** ___
- **Role and level:** ___
- **Date:** ___
- **Mode:** in-person / virtual / hybrid
- **Location:** ___ (in-person) OR Zoom / Google Meet / other (virtual)
- **Total length:** ___ hours
- **Number of rounds:** ___
- **Recruiter:** ___ (name, email, phone if known)
- **Hiring manager:** ___ (if known; from Week 5)
- **Round types and order (if known):** ___
- **Lunch:** included / not included / virtual
- **Source for the structure above:** ___ (the recruiter's email; the company's candidate guide; Glassdoor reports)
```

If you do not know something, write "unknown — will ask recruiter by {date}." The point is to surface gaps now, not to leave them latent.

### Step 2 — The night before (10 min)

Write the night-before plan as a checklist. Lecture 1 Section 4 has the framework; convert it into items you will actually execute. Be specific:

```markdown
## The night before — {date - 1}

### Evening (17:00-22:30)

- [ ] 17:00 — Light exercise: 30-min walk in the neighbourhood
- [ ] 18:00 — Dinner: {specific meal you've eaten before}, no alcohol
- [ ] 19:00 — Re-read cheat sheet (the onsite section, twice; the screen-call sections, once)
- [ ] 19:30 — Lay out clothes for the morning: {specific outfit}
- [ ] 20:00 — Pack the bag: laptop, charger, ID, water bottle, snacks, scratch paper, pen, printed cheat sheet
- [ ] 20:30 — Confirm transportation: {hotel-to-office walk, or rideshare app open, or transit route}
- [ ] 21:00 — Last work email reply if needed
- [ ] 21:30 — Screens off; book or quiet activity until bed
- [ ] 22:30 — Asleep

### Sleep target

- Lights out: 22:30
- Wake: 07:00
- Total: 8.5 hours
- Backup alarm: phone in another room, second alarm on watch
```

### Step 3 — The morning of (15 min)

Same structure, more granular because the morning of has more moving parts:

```markdown
## The morning of — {date}

### Wake to leave (07:00-08:30)

- [ ] 07:00 — Wake; water 500ml before anything else
- [ ] 07:15 — Shower, dress
- [ ] 07:45 — Breakfast: {specific protein-heavy meal}, plus fruit, plus coffee (just my usual amount)
- [ ] 08:15 — Warm-up: 30 min, one easy LeetCode I've done before, narrate Phase 1 only; then read the cheat sheet twice
- [ ] 08:45 — Bathroom; pack final items (water bottle filled, snacks zipped into bag)
- [ ] 09:00 — Leave home / hotel

### Travel (09:00-09:40)

- [ ] Walking / rideshare / transit — buffer for traffic
- [ ] 09:30 — Arrive in lobby (15-20 min before start time)
- [ ] 09:35 — Bathroom in the lobby (or as soon as the building has one)
- [ ] 09:40 — Identify myself at the front desk; ask for {recruiter's name}
- [ ] 09:50 — Greet recruiter; settled in waiting area

### Virtual variant — wake to start (07:00-09:55)

- [ ] 07:00-08:45 — Same as in-person above
- [ ] 08:45 — Final setup check: camera, audio, all Zoom links open in tabs, second monitor showing cheat sheet, water bottle on desk
- [ ] 09:00 — Bathroom; quiet sit
- [ ] 09:30 — Read the cheat sheet again; warm-up the voice (Phase 1 of one easy problem)
- [ ] 09:55 — Click the first Zoom link
```

### Step 4 — The loop itself (25 min)

This is the hour-by-hour structured time. For each round, write the start time, the end time, the round type, the interviewer (where known), the round-specific notes, and the recovery beat in the gap before the next round.

```markdown
## The loop — {date}

### Round 1 — Coding — 10:00-11:00

- **Interviewer:** {name}, {title}, {team}
- **Notes from recruiter:** {anything they shared about the round structure or the interviewer's style}
- **My notes:** Lean Python; brute force first; over-narrate the first phase to set the day's tone.
- **Energy: 8-9.** Risk: speaking too fast. Reminder: slow down.

### Gap 1 — 11:00-11:10

- [ ] Water (half a bottle)
- [ ] Bathroom if needed (yes — ask recruiter)
- [ ] Walk with recruiter; do not relitigate round 1
- [ ] Slow breath x 2 before round 2

### Round 2 — Coding — 11:10-12:10

- **Interviewer:** {name}, {title}, {team}
- **Notes from recruiter:** {…}
- **My notes:** Watch for the round-2 overconfidence trap. Test cleanly at the end.
- **Energy: 8.** Risk: sloppy testing. Reminder: at least three test cases narrated aloud.

### Gap 2 — 12:10-12:20

- [ ] Snack (small)
- [ ] Water (refill)
- [ ] Bathroom
- [ ] Walk to lunch with the peer engineer

### Lunch interview — 12:20-13:20

- **Peer engineer:** {name, if known}
- **My notes:** Treat as scored. One specific question about the team's recent work — ready to ask: "I noticed the team published {blog post}; could you tell me more about how {decision} was made?"
- **Conversation lanes:** the team's work, my interest in the company, light personal context if invited. Banned: complaining about the morning; deep technical opinions; grilling for inside info.
- **Eating:** sandwich or wrap; small portion; no messy food.
- **Energy: 6-7.** Risk: hunger; sloppy small talk; over-eating. Reminder: eat enough not to be hungry, not to satiation.

### Gap 3 — 13:20-13:30

- [ ] Bathroom
- [ ] Water
- [ ] Stand and stretch
- [ ] Slow breath x 2; "Round 3 starts now"

### Round 3 — System design — 13:30-14:30

- **Interviewer:** {name}
- **My notes:** This is the round I'm weakest on. Start with the clarifying questions; sketch the high-level boxes before going deep on any one. Diagram on the whiteboard or shared doc.
- **Energy: 5-6.** Risk: post-lunch dip; jumping into details before establishing the system shape. Reminder: 5 min on requirements; 5 min on high-level design; only then dive.

### Gap 4 — 14:30-14:40

- [ ] Water
- [ ] Walk hallway; reset
- [ ] Slow breath x 2

### Round 4 — Behavioural — 14:40-15:30

- **Interviewer:** {name}; bar raiser (if Amazon) or behavioural specialist
- **My notes:** The story bank from Week 5 is the source material. Prepared stories: {project A}, {project B}, {project C}, {project D}. Hostile-pattern prep: pushback (Pattern 1), failure question (Pattern 3), what would you do differently (Pattern 4).
- **Illegal-question prep:** Lecture 3's deflections. Most-likely category for an informal moment: family / kids.
- **Energy: 5.** Risk: cognitive depth shrinking; first-thing-that-comes-to-mind answers. Reminder: deliberate pause before each answer.

### Closing with recruiter — 15:30-15:50

- **My notes:** Composed, specific answer to "how was your day?" — pre-write: "Really good — Sam's coding round was a great problem; Priya's behavioural let me talk about {project}. I enjoyed the team."
- **Questions back:** Timeline. Process from here. Compensation range if not yet covered.
- **Closing line:** "Thanks — really enjoyed the day. Looking forward to hearing."
```

### Step 5 — The post-loop two hours (10 min)

The post-loop window is where the after-action document gets filled out (see Challenge 2). The run-of-show names the slot:

```markdown
## Post-loop — {date}, 15:50-19:00

### 15:50-16:30 — Decompression

- [ ] Walk; do not check phone
- [ ] Light food if hungry (real meal at 18:00)
- [ ] No relitigating; the loop is done

### 16:30-17:30 — After-action

- [ ] Open `c13-week-07/after-action-template.md`
- [ ] Fill out: rounds, interviewers, questions, read of the room, three things to do differently
- [ ] Specific timestamps for any illegal or hostile moments
- [ ] Save to portfolio

### 17:30-19:00 — Recovery

- [ ] Real meal: {specific dinner plan}
- [ ] Quiet evening; no work; no LeetCode
- [ ] One-line follow-up email to the recruiter: "Thanks for organising today; enjoyed meeting the team. Looking forward to the next step."

### Sleep target

- Lights out: 22:30
- The recovery is the day after, not this evening.
```

### Step 6 — Final sanity check (15 min)

Read the whole document through. Check:

- **Every time is dated and bounded.** No "around 10am"; "10:00-11:00."
- **Every gap has a specific recovery action.** Not "rest"; "water, bathroom, slow breath x 2."
- **Every round has a specific risk and a reminder.** Not "do well"; "speak slower" or "test three cases aloud."
- **The night-before, morning-of, and post-loop are not skipped.** Most candidates draft the loop itself and skip these; the loop itself is the part that is most rehearsed and the surrounding hours are the part that produces the most variance in performance.
- **You have named all four illegal-question categories you most expect to hear** based on your demographic and the company context. The deflections live in your cheat sheet; the run-of-show just flags them.

## Acceptance criteria

- The document `c13-week-07/run-of-show.md` exists and is committed.
- The header (known facts) is complete or has named gaps.
- The night-before, morning-of, loop-itself, and post-loop sections are populated.
- Every gap between rounds has at least three specific actions.
- The lunch interview has its own section with banned and ready conversation lanes.
- The closing-with-recruiter section has a pre-written answer to "how was your day?"
- The post-loop section names the after-action slot specifically.
- The run-of-show is dated, even if for a hypothetical near-future date.
- A short note at the bottom: the *one* thing you most need to remember from this run-of-show; the most-common mistake you make in long high-stakes events.

## Stretch — version the run-of-show

If you have more than one loop scheduled (or expected), version the document per-company. `c13-week-07/run-of-show-google.md`, `c13-week-07/run-of-show-stripe.md`. Each company's variant in Lecture 1 Section 9 (hiring committee, bar raiser, one-room model, etc.) belongs in the company-specific version.

## Why this exercise matters

The night before the real loop, you will be too anxious to plan. The morning of, you will be too rushed. Between rounds, you will be too tired. The run-of-show is what carries you through those windows. It is the deliberate offload of decisions to a moment when you had bandwidth, so that the live loop has none of those decisions left to make.

The candidates who do this well report two things: the loop felt shorter than they expected, and the early-rounds energy held later than they expected. Both are the same effect: the cognitive load of in-the-moment planning is what burns the candidate out; the run-of-show absorbs that load.
