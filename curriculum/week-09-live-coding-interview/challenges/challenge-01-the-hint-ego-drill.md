# Challenge 1 — The Hint-Ego Drill

**Time:** 45 minutes. One full mock interview with another human.

**Format:** Pair drill. Find a partner (a study buddy, a friend, a Pramp pairing, an interviewing.io session). One person plays interviewer, one plays candidate. After 45 minutes, switch roles and run a second round on a different problem.

**Why this challenge:** Failure mode 4 — ignoring the hint — is the failure mode that is hardest to rehearse alone. Solo drills cannot simulate the human-delivered hint, the awkward beat after a redirect, the social pressure of conceding a wrong approach. This drill manufactures those moments deliberately. The interviewer's job is to *insert hints into the round whether or not they are needed*, and the candidate's job is to take each hint cleanly without defending, without ego, and without losing their composure.

## The setup

You will need:

- A partner.
- A 45-minute uninterrupted slot, plus 15 minutes for the role swap and a second round.
- A shared coding environment — CoderPad, HackerRank, a Google Doc, a shared VS Code Live Share, whatever you have.
- A recording (audio at minimum). Both rounds get recorded.
- The interviewer's hint script below.
- The candidate has not seen the problem before. The interviewer has, and has read the hint script.

## The interviewer's job

You are not a normal interviewer. You are the **hint-injector**. Your specific job for this drill is to inject hints into the candidate's round whether or not the candidate needs them, and observe how the candidate receives each hint.

You will inject **at least three hints** during the round. They do not have to be at fixed minutes — but space them roughly 10-15 minutes apart. The three hints, in order:

1. **The course-correction hint** (at approximately minute 8-12, during the candidate's approach phase). "Have you considered [a different approach]?" — substitute a real alternative for the candidate's stated approach. If the candidate is reaching for a hash map, suggest a two-pointer approach. If the candidate is reaching for a sort, suggest a heap. Even if the candidate's chosen approach is correct, propose the alternative.

2. **The clarification-disguised-as-hint** (at approximately minute 20-25, during the candidate's code phase). "Just to double-check — have you thought about what happens if [edge case]?" Pick a real edge case that the candidate's code handles, and ask anyway. The hint is whether the candidate goes back and verifies, or whether they wave it off.

3. **The complexity push** (at approximately minute 30-35, after the candidate's code is mostly working). "Is this O(n) or O(n log n)? And — can you do better?" Run the full complexity-push sequence even if the candidate has already volunteered the answer.

The hints are graded artifacts. You are watching the candidate's response to each one. The grading rubric is below.

## The candidate's job

You are running a normal live coding round. The problem is whatever the interviewer chooses (suggestions below). You execute the six-phase structure from Lecture 1. When the interviewer says something — and they will say things at minute 10, 22, and 32 — you treat each utterance as a hint, even if it sounds like a casual question.

Your specific goal is to demonstrate the **take-the-hint pattern** from Lecture 2:

1. **Pause.** Stop typing for a beat.
2. **Acknowledge the hint explicitly.** "Good question — let me think about that."
3. **Integrate the hint into your plan, out loud.** Even if you do not change course, articulate *why* you are or are not changing course in response to the hint.
4. **Pivot if needed.** If the hint reveals a real flaw, pivot. Do not defend.

The challenge is that **you do not know which hints are real flaws and which are bait**. The interviewer is going to inject all three regardless. Your job is to evaluate each on its merits, take it seriously, and respond cleanly.

## Suggested problems for the round

Pick one. The interviewer should pick a problem the candidate has not seen, ideally LeetCode Medium difficulty.

| Problem | LeetCode # | Pattern |
|---------|-----------:|---------|
| Group Anagrams | 49 | Hash map |
| Longest Substring Without Repeating Characters | 3 | Sliding window |
| Word Break | 139 | Dynamic programming |
| Coin Change | 322 | Dynamic programming |
| Number of Islands | 200 | BFS/DFS on a grid |
| Merge Intervals | 56 | Sort + merge |
| Top K Frequent Elements | 347 | Heap |
| Course Schedule | 207 | Topological sort |

The interviewer should rotate between problems on different drill runs; the candidate gets a fresh problem each time.

## The rubric

After the 45-minute round, both the interviewer and the candidate score the candidate independently, then compare.

| Axis                                                                                                          | 0 | 1 | 2 |
|---------------------------------------------------------------------------------------------------------------|---|---|---|
| **Paused before responding to each hint (no immediate "yes I did that")**                                     |   |   |   |
| **Acknowledged the hint explicitly with a phrase like "good question" or "let me think about that"**          |   |   |   |
| **Articulated why the hint did or did not change the plan**                                                   |   |   |   |
| **Pivoted cleanly when a hint revealed a real flaw (or stayed cleanly when the hint was bait)**               |   |   |   |
| **Did not defend the original plan with ego (no "I already considered that" or "no, that doesn't work")**     |   |   |   |
| **Resumed the round smoothly after each hint (no lingering frustration or re-litigation)**                    |   |   |   |

Score each of the six axes 0-2. Total possible: 12.

**Target: 9/12.** A score below 6 means the take-the-hint pattern is not yet a reflex. A score of 9-10 means the pattern is forming. A score of 11-12 means the pattern is on muscle memory.

Both the interviewer and the candidate score independently, then compare the scores. The gap between the two scores is itself a signal — if you scored yourself higher than the interviewer scored you, your default is probably defensive, and you should drill the take-the-hint pattern more. If the interviewer scored you higher, you are probably under-confident; the defensive instinct is not actually showing as much as you fear.

## The interviewer's grading sheet

For each hint, the interviewer should record:

- The time the hint was delivered.
- The candidate's first verbal response (verbatim, if possible).
- Whether the candidate paused (yes/no/partial).
- Whether the candidate's pivot decision matched the hint's intent (correct/incorrect/unclear).
- Whether the candidate showed defensive language (yes/no/partial).

These are useful artifacts for the post-mortem and for the candidate's improvement plan.

## The post-mortem

After both rounds (with the role swap), spend 15 minutes debriefing:

1. **Which hint was the hardest to receive?** The course-correction at minute 10, the edge-case-disguised-as-clarification at minute 22, or the complexity push at minute 32? Different candidates struggle with different hints. The course-correction hint is the hardest for most candidates because it lands while the approach is still mutable, and pivoting means admitting the first approach was wrong.

2. **What was your first instinct when the hint landed?** Defensive? Curious? Anxious? The instinct is rehearseable. Most candidates default to defensive; the take-the-hint pattern shifts the default to curious.

3. **What specific phrase did you use to acknowledge each hint?** "Good question" is fine. "I appreciate the push" is fine. "Hmm, let me think" is fine. "No, I already considered that" is *not* fine — even when it's true. Identify the phrase that comes naturally; if no natural phrase exists, pick one and rehearse it.

4. **Did you change your final approach based on any of the hints?** If yes, was the change improvement? If no, did you articulate why?

5. **What would you do differently next time?** Specific. Written down.

## Variations

- **The silent-treatment variant.** The interviewer says nothing for the entire round — no hints, no encouragement, no clarifications. The candidate's job is to run the round entirely under their own steam. This is the inverse drill; it builds the muscle of running the round without an external prompt.
- **The aggressive-disagree variant.** The interviewer pushes back on every approach the candidate proposes. "No, that won't work — try something else." The candidate's job is to defend, pivot, or commit, depending on whether each pushback is real or theatrical. This is the senior-level drill; it builds the muscle of distinguishing real pushback from rhetorical pushback.
- **The non-native-speaker variant.** The interviewer speaks in halting English, hesitates often, and asks the candidate to clarify their own statements. The candidate's job is to remain patient, repeat themselves clearly, and not lose composure. This is the cross-cultural-interview drill; it builds the muscle of handling interviewers whose first language is different from the candidate's.

Run the standard version first. The variations are for the candidate who has scored 11-12 on the standard rubric and is looking for the next layer of difficulty.

## When to repeat this drill

Run it twice per week during your active interview cycle. The pairing requirement makes it the most-expensive single drill of the week, but it is also the highest-leverage. The candidates who have run this drill three or four times before the real round handle interviewer pushback without flinching; the candidates who have never run it freeze at the first redirect.

Pramp and interviewing.io's free tiers are sufficient for the pairing. If neither is available, swap with another C13 candidate in the same cohort. The pairing quality matters less than the practice itself; even a clumsy partner produces a useful drill.
