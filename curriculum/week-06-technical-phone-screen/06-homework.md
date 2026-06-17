# Week 6 — Homework

Six problems, ~6 hours total. Each commits to your portfolio.

---

## Problem 1 — Update the screen-call cheat sheet for technical screens (45 min)

Extend the cheat sheet from Weeks 4 and 5 with a technical-screen section that lives on the same single screen.

Open `c13-week-05/screen-call-cheat-sheet-v3.md` (or the version from the Week 5 mini-project). Add a technical-screen section. If you are keeping the cheat sheet per-week, start `c13-week-06/screen-call-cheat-sheet-v4.md` from the v3 version.

The new technical-screen section structure:

```markdown
## Technical-screen additions

### Pre-call tooling check (5 min before the call)
- Editor open: ___ (CoderPad / HackerRank CodePair)
- Language: ___ (Python default)
- One-liner ran: confirmed
- Audio: wired headset, tested in the call's browser
- Scratch paper + pen on desk
- JD open in a second tab; recruiter's notes open in a third

### Five-phase narration loop (one line each)
- Phase 1 — Restate: "Let me make sure I understand. We have ___. We want ___."
- Phase 2 — Example: "Let me trace through {input}. Output should be {Y}."
- Phase 3 — Brute force: "The brute force is ___. That's O(___)."
- Phase 4 — Optimise: "I can do better with ___. New complexity O(___)."
- Phase 5 — Code: open burst with sentence, close with recovery sentence.

### Four follow-up patterns (one line each)
- Complexity: time + space + amortised-vs-worst.
- Extension: what changes, what stays, new edges.
- Production: input validation + logging + metrics (pick 3, specific).
- Edge case: state behaviour, confirm code handles, note related edges.

### Banned phrases
- "Best practices, I think."
- "I've done this before."
- "This is a standard easy."
- "I'll just trust the code."

### Question bank for the technical interviewer (3 reusable)
- Q1: "What kind of work are you doing on the team currently?"
- Q2: "What's the team's stack and codebase shape?"
- Q3: "What does the rest of the loop look like from here?"
```

**Acceptance:**

- The technical-screen section is added (or v4 cheat sheet exists).
- All sub-sections populated.
- Total cheat-sheet length still fits on a single laptop screen at normal zoom — under ~450 words including all of Weeks 4 and 5's content.
- Top of file has a date stamp; the cheat sheet revises after every real call.

---

## Problem 2 — Tool fluency (60 min)

The first 90 seconds of the call should be invisible. To make them invisible, you need to be fluent on the editor.

In `c13-week-06/tool-fluency.md`:

**Part A — CoderPad fluency (30 min).** Open a fresh CoderPad pad. Run through:

- Pick your default language. Run a `print("hello")`. Confirm output.
- Switch to a different language (e.g., Python to JavaScript). Note: switching languages clears the pad.
- Open a second tab in the pad. Move code between tabs.
- Open the whiteboard / drawing tab. Sketch a simple diagram.
- Paste a sample input into the input pane. Modify your code to read from it. Run.
- Time how long it takes you to do the full sequence above end-to-end.

**Part B — HackerRank CodePair fluency (30 min).** Same drill on CodePair. Note differences:

- Language selector position?
- Test runner shape?
- Chat panel location?
- Run-output panel position?
- Any keyboard shortcuts that work differently from CoderPad?

**Acceptance:**

- Both editors used with the basic sequence completed.
- Differences noted (4-6 bullets).
- A short summary: which one you'll default to, and how you'll handle the call if you get the other.

---

## Problem 3 — Five easy LeetCode in a single sitting, narrated (75 min)

This is the stamina drill. Real interview cycles often have two or three technical screens in one week; sometimes two in one day. The narration muscle fatigues. The drill calibrates how much.

In `c13-week-06/stamina-drill.md`:

Pick five easy LeetCode problems you have not done in the last 30 days. Each is a 12-15 minute timebox (you are not aiming for 25 minutes per problem; you are aiming for fluency at speed). Record all five.

For each:

- Solve while narrating the five-phase loop.
- Stop at the 15-minute mark even if mid-line of code.
- 2-minute break between problems. No phone, no email.

After all five:

```markdown
## Stamina results

| # | Problem | Time | Finish state | Self-narration score 1-5 |
|--:|---------|-----:|--------------|------------------------:|
| 1 | ___ | __m | ___ | __ |
| 2 | ___ | __m | ___ | __ |
| 3 | ___ | __m | ___ | __ |
| 4 | ___ | __m | ___ | __ |
| 5 | ___ | __m | ___ | __ |

## Observations

- The narration score on problem 5 versus problem 1: ___
- The specific aspect of narration that degraded fastest: ___
- How you'll handle a real-cycle scenario where two screens fall on the same day: ___
```

**Acceptance:**

- Five recordings exist.
- All five are scored 1-5 on narration.
- A specific observation about how narration quality changed across the five.
- A specific habit for handling multi-screen days (typically: more sleep, more water, shorter morning warm-up, a 10-minute walk between calls).

---

## Problem 4 — Watch one full interviewing.io recording and score it (45 min)

Read: <https://interviewing.io/recordings>. Pick a recording from the public archive. The categories vary; pick one in the "medium" difficulty range that is a typical 45-minute coding interview.

In `c13-week-06/iio-recording-notes.md`:

**Part A — Score the candidate.** Use the same five-dimension rubric you used in Exercise 1: problem-solving, coding, communication, testing, follow-up. Score 1-5 on each. Total: __ / 25.

**Part B — Note the interviewer's specific phrases.** Write down the exact words the interviewer used when:

- Reading the problem statement.
- Offering a hint.
- Asking the follow-up question.
- Wrapping up the call.

The phrases are reusable — real interviewers use a small vocabulary of these.

**Part C — Identify three habits to steal.** From the candidate in the recording (if they were strong) or from the interviewer's signals about what they liked (if the candidate was weak), identify three specific habits you can adopt.

**Acceptance:**

- A recording URL is listed.
- Five-dimension rubric is scored.
- Interviewer phrases captured (at least 4 examples).
- Three habits identified.
- Total write-up: 400-600 words.

---

## Problem 5 — Pre-call routine doc (30 min)

Many candidates lose the first 5 minutes of a real call to tool setup, audio fumbling, or "wait, what was the problem again?" The fix is a 10-minute pre-call routine that you run before every technical screen.

In `c13-week-06/pre-call-routine.md`, write the routine:

```markdown
## Technical phone screen — pre-call routine (10 min)

### 10 minutes before
- [ ] Wired headset on, tested in the call's browser
- [ ] CoderPad / CodePair pad opened, language selected
- [ ] One-liner run; output confirmed
- [ ] Scratch paper + pen on desk
- [ ] Phone on Do Not Disturb
- [ ] Water on desk
- [ ] JD open in second tab
- [ ] Recruiter / HM notes open in third tab
- [ ] Cheat sheet open (or printed) but not visible on shared screen

### 5 minutes before
- [ ] Run a 5-minute warm-up: open one easy LeetCode you've done, narrate the
      first phase aloud (just Phase 1, restate). Warms up the voice.
- [ ] Re-read the cheat sheet's five-phase narration line.
- [ ] Re-read the cheat sheet's four follow-up patterns.

### 30 seconds before
- [ ] Click the call link.
- [ ] Smile. The interviewer will hear it in your voice.

### During the call (first 90 seconds)
- [ ] Greet, confirm audio.
- [ ] Confirm the editor and language match.
- [ ] Wait for the interviewer to present the problem.
- [ ] Do NOT start coding until the problem statement is complete.
```

**Acceptance:**

- The routine document exists.
- The 10-minute structure is clear and runnable.
- The 30-seconds-before and during-the-call segments are specific.
- A note at the bottom: the *one* habit you most need to remember; the most-common mistake you make in the first 5 minutes of any call.

---

## Problem 6 — Week-6 reflection (40 min)

`c13-week-06/reflection.md`, 300-400 words:

1. Before this week, what was your model of the technical phone screen? Be honest: did you think you could already do it because you can code, or did you have a clear picture of what the rubric actually measured? Where was your model wrong?
2. Of the three exercises this week, which one moved the needle most, and why? (Most candidates report Exercise 2 — the solo narration drill — because the gap between "I can solve this in silence" and "I can solve this while narrating in a way someone could score" is larger than they expected.)
3. The pair mock in Exercise 1 revealed at least one issue you didn't see in the solo Exercise 2 recordings. What was it, and what does that tell you about the limits of solo prep?
4. The technical screen is the first call in the pipeline where the *tool* itself can cost you points. What is your current relationship with CoderPad and HackerRank CodePair, and what specifically will you do differently in your real-call setup?
5. What one habit are you carrying into Week 7 — concrete, testable, not aspirational? (Example: "Before every coding session this week and next, I will narrate Phase 1 aloud even when alone, to keep the muscle live.")

---

## Time budget

| Problem | Time |
|--------:|-----:|
| 1 — Update screen-call cheat sheet for technical screens | 45 min |
| 2 — Tool fluency (CoderPad + HackerRank CodePair) | 60 min |
| 3 — Five easy LeetCode in a single sitting, narrated | 75 min |
| 4 — Watch one full interviewing.io recording and score it | 45 min |
| 5 — Pre-call routine doc | 30 min |
| 6 — Reflection | 40 min |
| **Total** | **~4h 55m** |

(Under the 6h budgeted in the README. The slack absorbs the pair-mock coordination from Exercise 1 and the recording / re-watching loop from the mini-project.)

After homework, the [mini-project](./07-mini-project/00-overview.md) records a full mock technical phone screen using a shared editor and walks the scoring rubric over the playback.
