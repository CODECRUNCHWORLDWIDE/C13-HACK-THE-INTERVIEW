# Exercise 2 — Deflection Rehearsal

**Time:** ~90 minutes (15 prep + 60 rehearsal + 15 review). **Output:** A rehearsed, recorded session covering the seven hostile-question patterns and the eleven EEOC-protected categories, with a written debrief naming which categories you handled fluently, which felt clumsy, and the specific revision to each deflection you will carry into a real loop. Lives in your portfolio as `c13-week-07/deflection-rehearsal.md`.

## Goal

Convert the deflection scripts in Lecture 3 from text on a page into language that you can produce, in the middle of a real round, while tired, when the question lands cold. The only reliable path is rehearsal with a peer who is willing to ask the questions out loud, in roleplay, in the middle of a behavioural-round mock.

## Setup

You need:

- **A peer who will play the interviewer for 60 minutes**. The peer needs to be comfortable asking the illegal questions in roleplay; some people find this uncomfortable. Confirm before the session. Ideal: a C13 cohort member who has also read Lecture 3.
- **A recording app** — Loom, QuickTime, or OBS. Audio is sufficient; video is nice-to-have.
- **A markdown file**: `c13-week-07/deflection-rehearsal.md`. Template below.
- **The script card** in Section 2 below. The peer reads from it.
- **A stopwatch.** Each question gets 90 seconds of response time, max.
- **A quiet room.**

## Process

### Step 1 — Prep with the peer (15 min)

Send the peer:

- A link to **Lecture 3** of this week. They should skim Sections 5-7 (the legal frame and the deflection scripts) before the session.
- The **script card** in Section 2. They will read from it; do not memorise.
- The **ground rules** below.

The ground rules:

- **Play the interviewer, not your friend.** Ask the questions in the framing they would be asked in a real loop — warm, conversational, often as small talk. Do not signal the question is coming with a knowing pause.
- **Mix the questions.** The script card alternates hostile-pattern questions with illegal-category questions and with normal behavioural prompts. The point is to ask them in a stream so the candidate cannot predict which is coming next.
- **No coaching mid-session.** Coaching is the debrief. During the session, ask the question; let the candidate respond; ask the next question. Do not say "good answer" or "I'd have said it differently" between questions.
- **The 90-second clock.** The candidate has 90 seconds to respond to each question. If they go over, the peer says "let me ask the next one" and moves on. This simulates the time pressure of a real round.
- **The "are you sure?" probe** (Pattern 7 from Lecture 3) is on the script card with explicit instructions to ask up to three times.

### Step 2 — The script card (the peer reads from this)

```markdown
# Peer script — Week 7 Exercise 2 deflection rehearsal

You are the interviewer in a behavioural round. The candidate is rehearsing
the hostile-question and illegal-question patterns. Stick to the script;
mix the questions; do not signal which category is coming next.

## The questions (read in order; pause for the candidate's response; move on)

### Block 1 — Warm-up (3 questions)

1. "Tell me about a recent project you're proud of."
2. "What's the most interesting technical challenge you've faced in the past year?"
3. "How did you decide to apply for this role?"

### Block 2 — Mixed (alternating hostile and illegal; ~15 questions)

4. (Pattern 1, pushback) "Your design doesn't handle the case where the
   queue backs up. What would you do?"
5. (Illegal, age) "When did you graduate from college?"
6. (Pattern 2, why this choice) "Why did you choose Postgres for the user
   table instead of a document store?"
7. (Illegal, national origin, soft) "Where are you from originally?"
8. (Pattern 3, failure) "Tell me about a project that failed."
9. (Illegal, family) "Do you have kids?"
10. (Pattern 4, what would you do differently) "Walk me through your design
    again. What would you change?"
11. (Illegal, religion) "Will you need time off for religious observances?"
12. (Pattern 5, interrupt) Start asking about the candidate's most recent
    project; let them get 30 seconds in; then cut in: "Wait, slow down. What
    did you just say about the index?"
13. (Illegal, marital) "Are you married?"
14. (Pattern 6, hypothetical) "Imagine your tech lead has shipped code you
    think is wrong and is refusing to revert it. What do you do?"
15. (Illegal, citizenship) "Are you a US citizen?"
16. (Pattern 7, are you sure) Ask: "What's the time complexity of the
    optimised version of two sum?" Whatever they say, ask "are you sure?"
    Whatever they say, ask "are you sure?" once more. (Three probes total.)
17. (Illegal, disability) "How is your health?"
18. (Illegal, salary history) "What were you making at your last job?"

### Block 3 — Cool-down (2 questions)

19. "Do you have any questions for me about the team or the role?"
20. "Is there anything else you'd like me to know about you that we
    haven't covered?"

## After the session

- Do not coach during the session.
- After the last question, give the candidate a 60-second silent break.
- Then run the debrief in Section 4 of this exercise file.
```

### Step 3 — Run the session (60 min)

Set up the recording. Confirm the peer has the script. Start the recording.

The session runs for 50-60 minutes (the script has 20 questions; with 90 seconds each plus transitions, that is 35-40 minutes of question time plus 10-15 minutes of buffer for any longer answers and the closing).

During the session:

- **Treat each question as if it were the real round.** Do not break character; do not laugh at the illegal questions; do not signal "I know this is a drill."
- **Use the four-move deflection** for illegal questions: pause one beat, bridge, pivot, continue.
- **Use the response template** for hostile questions: acknowledge, reconsider visibly, land cleanly.
- **Keep within 90 seconds.** If you find yourself going long, you are over-explaining; the script will move on without you.
- **Notice your own discomfort.** Which categories made your stomach drop? Which felt smooth? Note mentally; you'll write it after.

### Step 4 — The debrief (15 min)

After the session, run a structured debrief with the peer. Recording continues during the debrief.

The peer's job in the debrief:

1. **Name two deflections that landed cleanly.** Specific: which question, what the candidate said, why it worked.
2. **Name two deflections that did not land.** Specific: which question, what went wrong (over-explained, visibly uncomfortable, broke rapport, answered the question, lectured).
3. **Name one hostile pattern the candidate handled well.**
4. **Name one hostile pattern the candidate handled poorly.**
5. **One overall comment.**

The candidate's job in the debrief:

1. **Name the question(s) that surprised you most.** Some illegal questions land cold even after Lecture 3; identify yours.
2. **Name the category of deflection you need the most rehearsal on.** From your own felt experience, not just the peer's read.
3. **Name one revision you will make to your deflection scripts** before the next rehearsal.

### Step 5 — The write-up (in the deflection-rehearsal.md file)

Within 24 hours of the session, fill out:

```markdown
# Deflection rehearsal — {date}

## Session info

- **Peer:** {name}
- **Duration:** {actual time}
- **Recording:** {Loom / Drive / etc. link}

## What the peer flagged

### Cleanly landed deflections (the peer's two)

1. Question: ___. My response: ___. Why it worked: ___.
2. Question: ___. My response: ___. Why it worked: ___.

### Deflections that did not land

1. Question: ___. My response: ___. What went wrong: ___. Revised script:
   ___ (the actual revised words).
2. Question: ___. My response: ___. What went wrong: ___. Revised script:
   ___ (the actual revised words).

### Hostile-pattern handling

- Pattern handled well: ___
- Pattern handled poorly: ___ — revised approach: ___

## What I noticed (the candidate's side)

### The question that surprised me most

___ (specifically, what I felt, and why I think it surprised me — was I tired
toward the end? Did the warmth of the framing throw me off? Did I expect the
category but not the specific phrasing?)

### The category I need the most rehearsal on

___ (one of: age, race/national origin, religion, sex/pregnancy/family,
disability, genetic, citizenship, salary history, or one of the seven
hostile patterns)

### One revision I'm making

The specific deflection I'm rewriting. Old script: ___. New script: ___.
Why the new one is better: ___.

## My fluency scores (1-5, self-assessed after re-watching the recording)

| Category | Fluency | Notes |
|----------|--------:|-------|
| Age (graduation / "when did you graduate") | __ | ___ |
| National origin ("where are you from") | __ | ___ |
| Religion (holidays / time off) | __ | ___ |
| Sex / marital status | __ | ___ |
| Family / kids | __ | ___ |
| Disability ("how is your health") | __ | ___ |
| Citizenship (beyond legal-right-to-work) | __ | ___ |
| Salary history | __ | ___ |
| Pattern 1 — pushback | __ | ___ |
| Pattern 2 — why this choice | __ | ___ |
| Pattern 3 — failure question | __ | ___ |
| Pattern 4 — what would you do differently | __ | ___ |
| Pattern 5 — interrupting interviewer | __ | ___ |
| Pattern 6 — hypothetical hostile | __ | ___ |
| Pattern 7 — "are you sure?" repeated probe | __ | ___ |

Score 1: I had no response or I answered the question.
Score 2: I deflected but visibly uncomfortable; rapport dropped.
Score 3: I deflected with one clumsy beat; recovered.
Score 4: I deflected smoothly, in one sentence, rapport held.
Score 5: I deflected smoothly with a clean pivot to a legitimate topic.

## Action items

- [ ] Update cheat sheet with the revised deflection scripts (Problem 1 of homework)
- [ ] Schedule a second rehearsal in 7-10 days, focusing on the categories scored 1-3
- [ ] Re-read EEOC pre-employment-inquiries guidance once more before the next real loop
```

## Acceptance criteria

- The session happened with a peer, was recorded, and was at least 45 minutes long.
- The write-up file exists and is committed.
- The peer's two-cleanly-landed and two-not-landed sections are filled in with specifics.
- The fluency table is filled with self-assessed scores after re-watching the recording.
- At least one deflection script has been revised, with old and new versions named.
- The action items list has the second-rehearsal scheduled.

## Solo mode (fallback)

If you genuinely cannot find a peer, the exercise still has value run solo, but at a meaningful cost.

Solo procedure:

- Record yourself reading the script-card questions aloud, one at a time, with 90 seconds of silence after each.
- After the recording, listen back; pause after each question; respond out loud as if to an interviewer; record your response.
- This produces two recordings: the questions and the responses, interleaved on playback.
- Run the same self-scored fluency table.

The cost of solo mode: you do not get the live-eye-contact pressure, the warmth of the framing, or the surprise of having a real person ask "do you have kids" while making eye contact. The deflection muscle does build; it builds less than with a peer. Use solo as a fallback if and only if a peer is not available.

## Stretch — the lunch-interview variant

A separate 30-minute mock specifically simulating the lunch interview, with the peer playing a friendly peer engineer and slipping in 1-2 illegal questions in casual small-talk framing. The category that lands most often at lunch is family-status; rehearse that specifically.

## Stretch — the bar-raiser variant

If you are interviewing at Amazon (or anywhere with a hostile-by-design behavioural round), run a 45-minute mock where the peer plays the bar raiser: consistently hostile pattern across all questions, no warmth, dry tone. The questions are all hostile-pattern (patterns 1-7) rather than illegal. The drill is composure-under-sustained-pressure; the muscle is distinct from the deflection muscle.

## Why this exercise matters

Illegal questions land in real onsites. Not in every loop; not even in most loops; but in enough of them that every working engineer who has done a year of interviewing has at least one to recount. The candidates who handle them well share one habit: they had rehearsed the deflection before the question landed.

The cost of the rehearsal is 90 minutes and one peer favour. The cost of fumbling a deflection in a real loop is a round you cannot recover and a write-up that goes to the debrief carrying your worst minute of the day. The economics are obvious; only the discomfort of asking a peer to ask "are you married" in roleplay is real, and that discomfort is the entire point of doing it now instead of in front of a hiring committee.
