# Mini-Project — Record Yourself Coding, Self-Grade Against a Rubric

**Time:** 4 hours total — 60 minutes of preparation, 45 minutes of recorded mock interview, 90 minutes of self-grading and reflection, 45 minutes of writing the one-page reflection.

**Why this mini-project:** The whole week pivots on the record-and-watch loop. The lectures, exercises, and challenges have built the structure, the failure-mode awareness, and the recovery patterns. The mini-project is the integration: a single end-to-end mock interview, recorded, graded against a structured rubric, written up. The recording is the artifact. The grading is the calibration. The one-page reflection is the personal-improvement plan you carry into the next round.

## What you will produce

By the end of the project, you will have:

1. **A 40-50 minute recording** of yourself running a full mock live coding round on a problem you have not seen before.
2. **A completed rubric** scoring the recording across 12 axes.
3. **A timestamped notes document** highlighting the moments in the recording where each rubric score was earned.
4. **A one-page written reflection** (350-500 words) covering: the three default behaviours you would change, the one tic you have already fixed in the recording, and the one situational move you want to drill next.

The four artifacts together are the mini-project deliverable. Save them in this folder; they are the most-valuable single set of artifacts the week produces.

## The four phases of the project

### Phase 1: Preparation (60 minutes)

Run the preparation in one sitting if possible. The pre-round warm-up is itself part of the project — it builds the muscle of warming up before a real round.

1. **Re-read Lecture 1** (the 45-minute structure). 15 minutes.
2. **Re-read Lecture 2** (failure modes and recovery). 15 minutes.
3. **Skim Lecture 3** (two transcripts). Pay attention to the line-by-line commentary. 10 minutes.
4. **Set up the recording environment.** OBS, QuickTime, Loom, Zoom-to-local — whichever you chose in the Resources file. Test it briefly to make sure both screen and audio are captured. 10 minutes.
5. **Pick the problem.** See "How to pick the problem" below. Do *not* read the problem statement yet. 5 minutes.
6. **Run a 5-minute breathing-and-rehearsal warm-up.** Slow breathing for 90 seconds. Rehearse your opening line aloud. Open a blank editor file with a `def ` stub. 5 minutes.

### Phase 2: The recorded mock interview (45 minutes)

Now run the round. Set the timer for 45 minutes. Start the recording.

1. **Read the problem statement aloud** when the timer starts.
2. **Run the full six-phase round.** Clarify (out loud, with at least 4 questions), examples (at least 3, including an edge case), approach (brute-force first, then optimisation, with complexity), code (with type hints and narration), test (line-by-line trace of at least one example), discuss (complexity and at least one trade-off, proactively).
3. **If you get stuck**, apply the three moves (verbalise, clarify, simplify) explicitly out loud. Do not pause the recording.
4. **At minute 20**, do the time-awareness check-in out loud: "We are about half-way through; let me make sure I leave time for testing."
5. **At minute 40**, wrap the discuss phase and stop the recording at minute 45 even if not finished. The recording is the artifact; running over is not the goal.

Do not pause the recording. Do not restart. The recording is whatever it is. Imperfection in the recording is the point — the recording captures the *real* default behaviour you bring into a round, which is the calibration baseline you need.

### Phase 3: Self-grading (90 minutes)

Watch the recording back twice.

**First pass (40-50 minutes — actual viewing time, at 1.0x speed).**

Watch the entire recording at normal speed. Take notes timestamped to specific moments. The first pass is for capturing what happened. Do not score yet.

For each phase, note:

- The minute the phase started.
- The minute the phase ended.
- The duration in minutes.
- One specific phrase or moment that stood out (positive or negative).

**Second pass (30-40 minutes — actual viewing time, at 1.5-2.0x speed).**

Watch again at faster speed, with the rubric in hand. Score each of the 12 axes.

### Phase 4: One-page reflection (45 minutes)

Write a 350-500 word reflection covering three sections:

1. **Three default behaviours I would change** (150-200 words). Be specific. "Talk less" is vague; "I default to 6 seconds of silence when I'm thinking; I want to fill that silence with the rehearsed phrase 'let me think about this for a moment'" is specific and actionable.
2. **One tic I have already fixed in this recording, compared to the bootstrap recording from Monday** (75-100 words). Pick a real improvement. If the recordings show no improvement, the reflection should acknowledge that and propose why — the week's drills did not address this particular tic, or the tic is more entrenched than expected.
3. **One situational move I want to drill next** (100-150 words). Pick a specific scenario: "the moment the interviewer says 'can you do better?' — I want to rehearse the two-step response (state factual complexity, then state optimality)." The move should be specific enough that you could practise it in 10 minutes of solo rehearsal.

Save the reflection as `REFLECTION.md` in this folder.

## How to pick the problem

The problem should be:

- **LeetCode Medium difficulty.** Easy is below the round's actual bar; Hard is above what you need for the mini-project.
- **Unseen.** You should not have solved it before. The week is about your default behaviour on a fresh problem, not about your speed on a known one.
- **Not a sliding-window variant** (you have already drilled those in exercises). Pick a problem from a different pattern: tree, graph, dynamic programming, sort, heap, two-pointer.
- **Drawn from the NeetCode 150 or LeetCode's "frequent interview questions" list.** The problem should be representative of what a real round would ask.

**Suggested problems** (pick one):

| Problem | LeetCode # | Pattern |
|---------|-----------:|---------|
| Word Break | 139 | Dynamic programming |
| Validate Binary Search Tree | 98 | Tree |
| Number of Islands | 200 | BFS/DFS |
| Course Schedule | 207 | Topological sort |
| K Closest Points to Origin | 973 | Heap |
| Reorder List | 143 | Linked list |
| Generate Parentheses | 22 | Backtracking |
| Combination Sum | 39 | Backtracking |
| Subsets | 78 | Backtracking |
| Spiral Matrix | 54 | Matrix traversal |

Pick from this list, or ask a friend to pick one for you (so you genuinely cannot prepare). Do not read the problem statement until the recording starts.

## The rubric

Score each of the 12 axes 0, 1, or 2. The full rubric is in `RUBRIC.md` in this folder.

| # | Axis | 0 | 1 | 2 |
|---|------|---|---|---|
| 1 | Clarify phase had at least 4 distinct questions | | | |
| 2 | Examples phase walked at least 3 concrete cases | | | |
| 3 | Approach phase stated brute force before optimal | | | |
| 4 | Approach phase stated complexity before coding | | | |
| 5 | Code phase had type hints on function signature | | | |
| 6 | Code phase had continuous narration (no >15s silences except deliberate pauses) | | | |
| 7 | Test phase walked at least one example line-by-line | | | |
| 8 | Discuss phase stated complexity and at least one trade-off, proactively | | | |
| 9 | Phase transitions were verbalised explicitly | | | |
| 10 | If stuck, applied at least one of the three recovery moves out loud | | | |
| 11 | If a hint was offered (or self-given), it was taken cleanly without defence | | | |
| 12 | At minute ~20, executed the time-awareness check-in | | | |

**Total possible: 24.**

| Score | Interpretation |
|------:|----------------|
| 21-24 | Strong-yes round. You can run this round in a real interview today. |
| 17-20 | Lean-yes round. The structure is mostly there; specific weak axes need targeted drilling. |
| 13-16 | Borderline round. The round would land as "weak hire" or "weak no" depending on interviewer. Multiple axes need work. |
| 9-12 | Weak round. The structure is partially formed. Repeat Week 9 before moving to Week 10. |
| Below 9 | Concerning. Restart the week. Most candidates do not score below 9; if you do, the issue is usually the lack of recording-and-review rather than a knowledge gap. |

The rubric is calibration, not a verdict. The same candidate can score 12 on the first mini-project recording and 21 on the third, six weeks later. The point is the trajectory, not the snapshot.

## After the mini-project

By Sunday evening, you should have:

1. The recording.
2. The completed rubric (with timestamped notes).
3. The one-page reflection.
4. A specific plan for the next mock interview's improvement target.

The four artifacts go in this folder. The reflection in particular is worth saving and revisiting before every subsequent interview. The same candidate reading their own reflection six months later, after a half-dozen real interviews, often finds it more accurate than they expected — the default behaviours surfaced in the mini-project tend to persist until deliberately drilled out.

## Optional: Peer review

If you have a study partner from this cohort, swap recordings on Sunday morning. Each of you scores the other's recording against the same rubric. Then compare the scores.

The gap between your self-score and your partner's score on you is a signal:

- **Partner scored you higher than you scored yourself**: you are likely under-confident, and your real performance is better than you fear.
- **Partner scored you lower than you scored yourself**: you are likely over-confident, and there are weak axes you are not seeing in your own recording. (This is more common than the first case.)
- **Scores match within 2 points**: your self-assessment is well-calibrated. The numerical score is meaningful.

The peer review is optional but high-leverage. It catches the blind spots that the self-grading misses.

## When to repeat this mini-project

Run it at the start of every active interview cycle. The artifacts compound across runs — by your third or fourth mini-project recording, you will have a longitudinal record of your default behaviour and your improvement on it.

Specific suggestion: run a fresh mini-project recording the morning of any onsite day. The 4-hour budget compresses to 60 minutes (recording + quick rubric check + 3-bullet reflection) on the day of, but the warmup effect carries cleanly into the real rounds.
