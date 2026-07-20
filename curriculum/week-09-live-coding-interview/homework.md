# Week 9 Homework

Six drills spread across the week, totalling approximately 6 hours of focused practice plus 1 hour of review. Each drill targets a specific Week 9 muscle. Run them in the order listed; later drills assume earlier drills have built the corresponding muscle.

Record yourself on every drill. The recordings are not for sharing; they are for self-review. The cumulative recordings across the week, plus the mini-project's full recording on Saturday, are your improvement-tracking artifact.

## Drill 1 — Watch Three Hello Interview Mocks (Monday, 60 minutes)

**Why:** Calibration. Most candidates have never seen a recorded live coding mock at the L4-L5 level. The Hello Interview free archive is the closest free analogue to "watching what passing the round actually looks like." Pattern-matching across three mocks calibrates your sense of pace, phrase choice, and structure.

**What to do:**

1. Go to the Hello Interview YouTube channel.
2. Pick three full mocks. Suggested filter: search for "L4 mock," "L5 mock," "Google live coding," or "Meta live coding" — pick variety.
3. Watch each mock at 1.25x or 1.5x. Total real-time: ~60 minutes for three mocks at 1.5x.
4. For each mock, write down:
   - The candidate's clarify-phase length (in minutes).
   - One specific phrase the candidate said that you would steal.
   - One moment where you would have done something differently, and what.
5. After all three mocks, write one paragraph on the pattern across the three candidates. What did all three do? What did only one do?

**Time:** ~1 hour total.

**Output:** Three sets of notes, one summary paragraph. Save in your Week 9 working folder.

## Drill 2 — The Solo Mock Round on a Familiar Problem (Tuesday, 45 minutes)

**Why:** Baseline. Before drilling the new patterns, establish your default behaviour on a problem you already know.

**What to do:**

1. Pick a LeetCode Medium that you have already solved at least once before (any of the canonical patterns: Two Sum, Group Anagrams, Longest Substring, Number of Islands, Coin Change).
2. Set the timer for 45 minutes. Start recording.
3. Run the full six-phase round out loud. Treat yourself as if it were a real interview — clarify even though you know the problem, examples even though you know the answer, brute-force narration before the optimal, etc.
4. After the round, watch the recording at 1.5x.
5. Apply the Lecture 1 phase rubric: did you hit each phase? Did you signal each transition? Did you run the full clarify-and-examples phases even though you "knew" the problem?

**Time:** 45 minutes for the round + 30 minutes for review = ~75 minutes.

**Output:** Recording + a 6-axis self-grade (one row per phase: did you do it cleanly, partially, or not at all).

## Drill 3 — The Solo Mock Round on an Unfamiliar Problem (Wednesday, 50 minutes)

**Why:** The real round. The Tuesday drill measured your default behaviour on a known problem; the Wednesday drill measures it on an unknown one. The gap between the two is your "under-pressure" delta.

**What to do:**

1. Pick a LeetCode Medium you have **not** seen before. Use the NeetCode 150's randomiser or LeetCode's daily challenge.
2. Set the timer for 45 minutes. Start recording.
3. Run the full six-phase round out loud. If you get stuck, apply the three moves from Lecture 2 explicitly out loud.
4. After the round, watch the recording at 1.5x.
5. Compare your default behaviour on this unfamiliar problem to Tuesday's drill on the familiar problem. Where did the structure hold? Where did it break under pressure?

**Time:** 50 minutes for the round (5 extra minutes for unfamiliarity) + 30 minutes for review = ~80 minutes.

**Output:** Recording + a comparison note ("Compared to Tuesday's drill, my clarify phase was [shorter/longer] and my approach phase [broke down at minute X / held cleanly].")

## Drill 4 — The Two-Pointer/Hash-Map Pattern Drill (Thursday, 60 minutes)

**Why:** Pattern fluency. The two most-asked patterns in live coding rounds are the two-pointer pattern and the hash-map pattern. Both are simple individually; both are the answer to at least 40% of all Medium problems. Building fluent muscle memory for "is this a two-pointer problem or a hash-map problem?" speeds up the approach phase by 2-3 minutes.

**What to do:**

1. Solve three problems from NeetCode's two-pointer or hash-map list. Suggested:
   - Two Sum (hash map)
   - Valid Palindrome (two pointers)
   - Longest Substring Without Repeating Characters (sliding window, related to two pointers)
2. For each problem, you have 20 minutes maximum: 5 minutes clarify-and-approach, 10 minutes code, 5 minutes test-and-discuss. Recording is optional but recommended.
3. At the end of all three, write down: for each problem, what was the *signal* that told you "this is a two-pointer / this is a hash-map" within 60 seconds of reading the prompt? Be specific. The signals are pattern-recognition handles you carry into future rounds.

**Time:** 60 minutes for three problems + 15 minutes for the signal-reflection = ~75 minutes.

**Output:** Three solved problems + a pattern-recognition cheat-sheet.

## Drill 5 — The "Test Cases Before Code" Drill (Friday, 45 minutes)

**Why:** Test-driven thinking, from Lecture 2. The single highest-leverage discipline of the week. This drill is the focused rep on writing the test cases out loud *before* any code, on a problem you have not seen.

**What to do:**

1. Pick a LeetCode Medium you have not seen.
2. Set the timer for 45 minutes. Start recording.
3. Run the clarify and examples phases as normal.
4. **Before writing any code**, write out at least four test cases:
   - One happy-path case.
   - One empty/single-element edge case.
   - One "tricky" edge case (duplicates, negatives, very large, etc.).
   - One failure-mode input (an input that breaks the naive approach).
5. Only after writing the four test cases, start coding.
6. After coding, walk the four test cases through the code line-by-line.
7. Watch the recording back. Did the act of writing the test cases first surface any bugs you would otherwise have discovered later? Most candidates report: yes, at least one.

**Time:** 45 minutes for the round + 30 minutes for review = ~75 minutes.

**Output:** Recording + a written reflection on whether the test-cases-first discipline shifted the bug-discovery point in the round.

## Drill 6 — The Pramp or interviewing.io Mock (Saturday, 60-90 minutes)

**Why:** The human-in-the-loop drill. All previous drills were solo. This drill is the closest free analogue to a real round — another human, real-time, mutual evaluation, no rewinding.

**What to do:**

1. Schedule a Pramp session for Saturday morning or afternoon. If Pramp is unavailable, use interviewing.io's free tier or a study-partner.
2. Run the session as the candidate first if you can choose (most platforms alternate roles).
3. Treat the session as a real round: run all six phases, take the hints if offered, apply the recovery moves if you get stuck.
4. After the session, ask your partner for one specific piece of feedback ("what is the single thing you would change about my round?"). The single-specific-thing constraint forces useful feedback rather than vague encouragement.
5. Write down their feedback verbatim. Write your own assessment of the round (one paragraph). Compare.

**Time:** 60-90 minutes for the session + 15 minutes for reflection.

**Output:** Your partner's feedback + your own self-assessment. Save both.

## Total time budget

| Drill | Day | Time |
|-------|-----|-----:|
| Drill 1 — Watch three Hello Interview mocks | Monday | 60 min |
| Drill 2 — Solo mock on familiar problem | Tuesday | 75 min |
| Drill 3 — Solo mock on unfamiliar problem | Wednesday | 80 min |
| Drill 4 — Two-pointer/hash-map pattern drill | Thursday | 75 min |
| Drill 5 — Test-cases-before-code drill | Friday | 75 min |
| Drill 6 — Pramp or interviewing.io mock | Saturday | 90 min |
| **Total** | | **~7.5 hours** |

The 7.5-hour budget is slightly above the 6-hour target stated in the README, accounting for the review time after each drill. If you are time-constrained, you can compress by skipping the watch-recording-back step on Drill 4 (the pattern-fluency drill has lower marginal review value than the structure-rehearsal drills).

If you are *truly* time-constrained and have to skip one drill, skip Drill 4. Drills 1, 2, 3, 5, and 6 cover the highest-leverage muscles. Drill 4 is the pattern-recognition booster; useful but not load-bearing.

## The cumulative recording

By Sunday morning, you should have:

- Three Hello Interview mock notes from Monday.
- A recording of yourself on a familiar problem from Tuesday.
- A recording of yourself on an unfamiliar problem from Wednesday.
- Three solved problems from Thursday with a pattern-recognition cheat-sheet.
- A recording of yourself with test-cases-first discipline from Friday.
- A Pramp or interviewing.io session feedback from Saturday.

That is six artifacts spread across the week, each ~30-90 minutes of work. The artifacts together are the input to the mini-project, which is Saturday-afternoon's record-and-grade exercise.

## Rubric for the week

A simple binary check:

| Drill | Did you complete it? |
|-------|----------------------|
| Drill 1 | yes / no |
| Drill 2 | yes / no |
| Drill 3 | yes / no |
| Drill 4 | yes / no |
| Drill 5 | yes / no |
| Drill 6 | yes / no |

**Target: 5/6.** Skipping one drill is acceptable if it is Drill 4. Skipping more is the signal that the week did not get the attention it needs; consider repeating Week 9 before moving to Week 10.

The cumulative effect across six drills is more important than perfection on any single drill. The candidate who did all six drills at 70% quality is in a stronger position than the candidate who did three drills at 95% quality.
