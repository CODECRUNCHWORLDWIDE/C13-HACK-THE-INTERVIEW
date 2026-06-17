# Lecture 3 — Two Worked Transcripts: One That Went Well, One That Went Badly and Recovered

> *The structure and the failure modes are abstractions. The way they actually appear in a round is through specific phrases at specific minutes, said by specific candidates in specific tones, in response to specific interviewer reactions. The abstractions land only when you can see them at the line level. This lecture provides two complete transcripts — one of a 38-minute round that earned a "strong yes," one of a 42-minute round that started failing and recovered into a "lean yes" — with running commentary on what each phrase did to the score.*

The transcripts are composite. They are stitched together from patterns observed across many actual rounds, anonymised, sequenced for pedagogical clarity. The technical problems are real — both are problems that appear regularly in new-grad and L4 live coding rounds. The candidate behaviours are real — they appear, in roughly this distribution, in roughly this proportion of rounds. The transcripts are not screenplays; they are calibration artifacts.

## Transcript 1: The round that went well

**Problem:** Given a list of meeting time intervals as `[start, end]` pairs, determine whether a single person could attend all of the meetings (i.e., return `True` if and only if no two meetings overlap).

**Setting:** 45-minute scheduled round. Shared editor. Both parties are in their respective home offices on video. Camera on for both.

**Total round length:** 38 minutes. The candidate finished early, used the remaining 7 minutes for follow-up discussion.

---

**Minute 0:00 — Interviewer:** *Hi, thanks for joining today. I'm going to share a problem with you — I'll paste it in the editor. Take a minute to read it, and feel free to ask me any clarifying questions.*

*[Interviewer pastes the problem statement.]*

**Minute 0:30 — Candidate:** "Thanks. Let me read this through, and then I'll ask a couple of questions to make sure I understand."

> **Commentary.** First move is to set expectations: the candidate is going to read, then ask questions, then engage. No premature dive into the problem. The "let me read and then ask" framing is a 5-second move that calibrates the interviewer for the next 90 seconds of silence.

**Minute 1:15 — Candidate:** "Okay, I think I have the shape. Let me restate it to make sure. The input is a list of intervals where each interval is a `[start, end]` pair. The output is a boolean — `True` if a single person can attend all meetings, which means none of them overlap, and `False` otherwise. A few questions: can the list be empty? Can it contain a single interval? Are the intervals guaranteed to have `start < end`, or could we have a degenerate interval where `start == end`? And — when two meetings share an endpoint, for example `[1, 5]` and `[5, 10]`, do those count as overlapping or as adjacent?"

> **Commentary.** Five clarifying questions in 30 seconds. The empty-list and single-interval questions are edge-case probes. The `start < end` question is a contract question. The shared-endpoint question is the one that actually changes the algorithm — depending on the answer, the comparison is `<` or `<=`. The strong-candidate move is identifying this *before* coding, not discovering it in the test phase.

**Minute 1:45 — Interviewer:** *Good questions. Empty list returns True trivially — vacuously, no meetings to conflict. Single interval returns True. You can assume `start < end` always. And shared endpoints do not count as overlapping — `[1, 5]` and `[5, 10]` are fine.*

**Minute 2:00 — Candidate:** "Got it — shared endpoints are okay. So `[1, 5]` and `[5, 10]` is fine, but `[1, 5]` and `[4, 10]` overlaps. Let me walk through a couple of examples to confirm I have the shape."

*[Candidate writes in the scratch area of the editor:]*

```
Example 1: [[0, 30], [5, 10], [15, 20]]
  Meeting 1: 0-30, Meeting 2: 5-10. These overlap (5 is inside 0-30).
  Expected: False.

Example 2: [[7, 10], [2, 4]]
  Meeting 1: 7-10, Meeting 2: 2-4. These do not overlap.
  Expected: True.

Example 3: [[1, 5], [5, 10]]
  Shared endpoint, per clarification, not an overlap.
  Expected: True.
```

> **Commentary.** Three examples, each exercising a different case. The first is the canonical "overlapping" case. The second is the canonical "non-overlapping" case. The third is the clarification-driven case — the one the candidate explicitly probed in the clarify phase. Writing this third case out is what differentiates the strong candidate; it locks in the contract.

**Minute 3:30 — Candidate:** "Good, I think I understand the problem. Let me think out loud about the approach. The brute force is: for every pair of meetings, check if they overlap. That is O(n²) — for each meeting we compare to every other meeting. The overlap-check for two intervals is constant time. So the brute force is O(n²) time, O(1) extra space."

"Can we do better? The bottleneck is the pairwise comparison. If the meetings were sorted by start time, we could do a single pass — compare each meeting's start to the previous meeting's end. If any meeting's start is less than the previous meeting's end, we have overlap. That is O(n log n) for the sort plus O(n) for the scan, so O(n log n) total time and O(1) extra space if we sort in place, or O(n) if we sort a copy."

"I think the O(n log n) is the right answer here. Do you want me to code that up, or do you want me to keep thinking about whether there is an O(n) solution?"

> **Commentary.** Full approach narration in 90 seconds. The candidate stated the brute force, named its complexity, identified the bottleneck, proposed the optimisation, named its complexity, and asked the interviewer to drive. This is a complete strong-approach phase. Note the deliberate brute-force-first move: the candidate did not skip it. The fact that the brute force is named, with its complexity, is a positive signal even though the candidate will not write it.

**Minute 5:00 — Interviewer:** *O(n log n) is fine, go ahead and code that up.*

**Minute 5:15 — Candidate:** "Okay, coding it up. Let me start with the function signature."

```python
def can_attend_all_meetings(intervals: list[list[int]]) -> bool:
    # Sort intervals by start time.
    intervals_sorted: list[list[int]] = sorted(intervals, key=lambda x: x[0])
    # Walk the sorted list; check for overlap.
    for i in range(1, len(intervals_sorted)):
        prev_end: int = intervals_sorted[i - 1][1]
        curr_start: int = intervals_sorted[i][0]
        if curr_start < prev_end:
            return False
    return True
```

> **Commentary.** The candidate narrated as they typed. Type hints on the signature, type hints on the intermediate variables. The `intervals_sorted` variable is a deliberate copy rather than an in-place sort — this avoids mutating the input, which is the production-engineering instinct. The comparison is `<` rather than `<=`, matching the clarification that shared endpoints are fine.

**Minute 9:30 — Candidate:** "Okay, I think that is the implementation. Let me walk through the test cases I wrote earlier."

"Example 1: `[[0, 30], [5, 10], [15, 20]]`. After sorting by start time: `[[0, 30], [5, 10], [15, 20]]` — same order, already sorted by start. Iteration i=1: `prev_end = 30`, `curr_start = 5`. Is `5 < 30`? Yes. Return False. Correct."

"Example 2: `[[7, 10], [2, 4]]`. After sorting: `[[2, 4], [7, 10]]`. Iteration i=1: `prev_end = 4`, `curr_start = 7`. Is `7 < 4`? No. Loop ends. Return True. Correct."

"Example 3: `[[1, 5], [5, 10]]`. After sorting: same order. Iteration i=1: `prev_end = 5`, `curr_start = 5`. Is `5 < 5`? No. Loop ends. Return True. Correct — the shared endpoint case passes because of the strict less-than."

"Let me check the edge cases too. Empty list: `range(1, 0)` is empty, so the loop does not execute, returns True. Correct. Single interval: `range(1, 1)` is empty, returns True. Correct."

> **Commentary.** Three trace-throughs of the canonical examples, plus the two edge cases. Each trace is 15-20 seconds, line-by-line, with the candidate verifying the comparison at each step. The shared-endpoint case is explicitly tested — the candidate proves to themselves and the interviewer that their `<` versus `<=` choice was correct. This is the strong test-phase signal.

**Minute 12:30 — Candidate:** "I think the implementation is correct. Let me talk about trade-offs and complexity."

"The time complexity is O(n log n), dominated by the sort. The scan is O(n) and the per-iteration work is O(1), so the loop is O(n). Total is O(n log n)."

"The space complexity is O(n) if we count the sorted copy, or O(1) if we sort in place. I chose the copy because I did not want to mutate the input — but if the problem allowed it, sorting in place would drop the space to O(log n) for the sort's recursion stack, which is essentially constant for most practical inputs."

"Is the O(n log n) optimal? I think so for the general case — sorting has a lower bound of Ω(n log n) for comparison-based algorithms, and I do not see a way to determine the answer without effectively sorting. There might be a clever approach using a sweep-line algorithm or a bucket-based approach if the input range is bounded, but for arbitrary integer ranges I think this is the bound."

"In a production setting, I might add: validation of the input (do all intervals have `start < end`?), a more explicit error type if validation fails, and possibly a streaming variant if the input is too large to fit in memory all at once. The streaming variant would need a different algorithm — probably a priority queue keyed by end time."

> **Commentary.** This is a complete discuss phase, run unprompted. Time complexity stated and justified. Space complexity stated, with the trade-off articulated. Optimality discussed honestly. Production extensions named. The whole phase is 2 minutes. The candidate has, without being asked, surfaced four pieces of signal: mechanical complexity analysis, trade-off awareness, theoretical lower-bound thinking, and production-engineering instincts. Each one moves the rubric score up.

**Minute 14:30 — Interviewer:** *That is excellent. Let me push on one thing — you mentioned a streaming variant. Can you sketch how that would work, at the high level? You do not need to code it.*

**Minute 14:45 — Candidate:** "Sure. In the streaming case, intervals arrive one at a time, and we cannot see the full input up front. The question becomes: at any point, given the meetings we have seen so far, is there a conflict?"

"The naive streaming approach would be to maintain a sorted list of all meetings seen so far, and on each new meeting, binary-search for the insertion point and check against the neighbours. That is O(log n) per arrival for the search plus O(n) for the insertion, so O(n) amortised per arrival, O(n²) total."

"A better streaming approach would use an interval tree or a segment tree, which supports interval-overlap queries in O(log n) per arrival, total O(n log n). The implementation is more complex but the asymptotic is better."

"If the meetings are guaranteed to arrive in order of start time, we can simplify — just keep track of the maximum end time seen so far, and check the new meeting's start against it. That is O(1) per arrival, O(n) total."

> **Commentary.** Three streaming variants, increasing in algorithmic sophistication, decreasing in assumption strength. The candidate has demonstrated awareness of the data-structure repertoire (sorted list, interval tree, segment tree) and the algorithmic principle (when can we exploit input order to drop complexity). This is the senior-bar follow-up answer at a new-grad-level question. The interviewer's rubric for the discuss phase just maxed out.

**Minute 18:00 — Interviewer:** *Great. We have about 25 minutes left — I could ask a follow-up problem, or we can use the remaining time for your questions. What would you prefer?*

**Minute 18:15 — Candidate:** "I'd love to try a follow-up if we have time — and if there's a few minutes left for my questions at the end."

*[The interviewer poses a follow-up: "find the minimum number of conference rooms needed to schedule all the meetings." The candidate runs the same six-phase structure, takes ~15 minutes for the full round, and ends at minute 38 with 7 minutes left for the candidate-questions phase.]*

---

### What this transcript gets right

A line-level inventory of the strong moves:

| Minute | Move                                                            | Phase     |
|-------:|-----------------------------------------------------------------|-----------|
|   0:30 | "Let me read and then ask questions" — set expectations         | Pre-clarify |
|   1:15 | Restate the problem in own words                                 | Clarify   |
|   1:15 | Five clarifying questions, including the contract-changing one  | Clarify   |
|   2:00 | Three example inputs covering happy, non-overlap, shared-endpoint | Examples |
|   3:30 | Brute force stated first, with complexity                       | Approach  |
|   3:30 | Bottleneck identified, optimisation proposed                    | Approach  |
|   3:30 | Optimisation complexity stated                                  | Approach  |
|   3:30 | Confirmed with interviewer before coding                        | Approach  |
|   5:15 | Function signature with type hints                              | Code      |
|   5:15 | Narrated as typing                                              | Code      |
|   5:15 | Deliberate non-mutation of input                                | Code      |
|   9:30 | Walked test cases line-by-line                                  | Test      |
|   9:30 | Walked edge cases unprompted                                    | Test      |
|  12:30 | Time complexity stated and justified                            | Discuss   |
|  12:30 | Space complexity trade-off articulated                          | Discuss   |
|  12:30 | Optimality discussed honestly                                   | Discuss   |
|  12:30 | Production extensions named                                     | Discuss   |
|  14:45 | Three streaming variants with increasing sophistication         | Follow-up |

Every move is small. None is impressive in isolation. The package, run for 38 minutes, is the strong-yes round.

## Transcript 2: The round that went badly and recovered

**Problem:** Given a string `s`, find the length of the longest substring without repeating characters.

**Setting:** 45-minute scheduled round. Shared editor. Both parties are on video.

**Total round length:** 42 minutes. The candidate stumbled at minute 6, was visibly stuck at minute 14, took a hint at minute 19, and recovered into a working solution by minute 35. The final rubric was "lean yes" — passable, but with notes about the slow recovery.

---

**Minute 0:00 — Interviewer:** *Hi, thanks for joining. I have a problem for you — let me share the prompt.*

*[Pastes: "Given a string `s`, find the length of the longest substring without repeating characters."]*

**Minute 0:15 — Candidate:** "Okay, longest substring without repeating characters. I think I have seen this one. Let me start coding."

> **Commentary.** **Failure mode 2 — premature optimisation, plus a skipped clarify phase.** The candidate has recognised the problem and is about to dive directly into the known optimal solution without confirming the inputs, the output, the edge cases, or even what "longest" means in the edge case of an empty string. This is the canonical round-opening that produces a struggle 5 minutes later.

**Minute 0:45 — Candidate types:**

```python
def length_of_longest_substring(s: str) -> int:
    # Sliding window with a hash set.
    seen = set()
    left = 0
    longest = 0
    for right in range(len(s)):
        # ...
```

**Minute 2:30 — Candidate:** "Hmm, wait. I need to think about this. If I see a repeated character, I need to advance the left pointer past the previous occurrence. But just removing it from the set is not enough — I need to remove all characters between the old position and the new one."

*[Candidate stares at the code for 30 seconds.]*

**Minute 3:15 — Candidate:** "Let me try a different approach."

*[Candidate deletes the code and starts over.]*

```python
def length_of_longest_substring(s: str) -> int:
    char_index: dict[str, int] = {}
    # ...
```

> **Commentary.** The candidate has now restarted twice, has not asked a single clarifying question, has not written a single test case, and is 3 minutes into the round with no visible progress. The premature-optimisation failure mode is in full effect.

**Minute 4:00 — Candidate:** "Okay, the idea is to use a hash map of character to its last index. When I see a repeat, I move left to one past the last index..."

*[Candidate types another half-implementation, types out a partial loop body, deletes it, types again.]*

**Minute 6:15 — Candidate:** *[silently typing and deleting for 90 seconds. No narration.]*

> **Commentary.** **Failure mode 3 — getting stuck silently.** The keyboard is moving but the narration has stopped. The interviewer cannot see what the candidate is thinking. The round is now actively failing.

**Minute 7:45 — Interviewer:** *Take your time. What are you thinking about?*

**Minute 7:50 — Candidate:** "Just trying to get the indexing right."

> **Commentary.** This response is bad. "Just trying to get the indexing right" is a non-answer; it gives the interviewer nothing to engage with. The correct response would have been to verbalise the specific stuck-point. The candidate is in failure mode 3 and has not registered it.

**Minute 8:30 — Candidate:** *[continues typing, then deletes, then types again]*

**Minute 11:00 — Interviewer:** *Let me jump in for a second. Can you tell me what you have so far at the high level — what is the approach you are trying to implement?*

**Minute 11:15 — Candidate:** "I'm trying to use a hash map of character to its last seen index, and a sliding window with a left pointer. When I see a character that is already in the map and its index is at or above the left pointer, I move left to one past that index."

**Minute 11:35 — Interviewer:** *Okay — and have you walked through any concrete examples to test the logic?*

**Minute 11:40 — Candidate:** "No, I have not. Let me do that."

> **Commentary.** **The interviewer just gave a hint.** The hint is not a question; it is a redirect. The interviewer has registered that the candidate skipped the examples phase and is suggesting the candidate go back to it. The candidate, to their credit, takes the hint. The recovery starts here.

**Minute 11:45 — Candidate:** "Let me restart from the examples. I'll pick `s = 'abcabcbb'`. The longest substring without repeats is `'abc'`, length 3. The next substring `'bca'` is also length 3. The substring `'cab'` is also length 3. So the answer is 3."

"Let me try `s = 'bbbbb'`. Every character is the same, so the longest is just `'b'`, length 1."

"Let me try the empty string `s = ''`. Length 0."

"And — I should ask, but I assume — `s = 'a'` gives length 1."

> **Commentary.** Four examples in 60 seconds. The candidate has belatedly executed the examples phase. This is recoverable, but the candidate has now spent 12 minutes on a round and has only a partial implementation and a fresh set of examples. The remaining 33 minutes need to produce the complete solution.

**Minute 13:00 — Candidate:** "Okay, let me also confirm — does the string contain only ASCII characters, or could it have Unicode? And is whitespace counted as a character?"

**Minute 13:15 — Interviewer:** *Good questions, let's say ASCII for now, and whitespace is just another character.*

**Minute 13:30 — Candidate:** "Got it. Let me think about the approach more carefully now."

*[Candidate stops typing. Stares at the screen for 60 seconds without speaking.]*

> **Commentary.** **Failure mode 3 — getting stuck silently — again.** The candidate has done the examples but is now stuck on the algorithm. The keyboard is not moving. The narration is not happening. This is the death state.

**Minute 14:30 — Interviewer:** *What are you thinking about right now?*

**Minute 14:35 — Candidate:** "I'm trying to figure out the right way to track the start of the window."

> **Commentary.** Better answer than the previous one — it names the specific stuck-point. But still not great; the candidate is two minutes into the second stuck-spiral and the interviewer is now actively coaching them through the round. The interviewer's rubric for "did the candidate need significant prompting" just got a negative tick.

**Minute 14:50 — Interviewer:** *Let me give you a hint. Try walking through `'abcabcbb'` one character at a time, by hand, and track what the window should look like at each step. Do not worry about code yet.*

**Minute 15:00 — Candidate:** "Okay, let me do that on the side."

*[Candidate types in the scratch area:]*

```
s = 'abcabcbb', indexes 0-7

i=0, c='a': window = 'a',     left=0, length=1, longest=1
i=1, c='b': window = 'ab',    left=0, length=2, longest=2
i=2, c='c': window = 'abc',   left=0, length=3, longest=3
i=3, c='a': 'a' was at index 0, move left to 1. window = 'bca', left=1, length=3, longest=3
i=4, c='b': 'b' was at index 1, move left to 2. window = 'cab', left=2, length=3, longest=3
i=5, c='c': 'c' was at index 2, move left to 3. window = 'abc', left=3, length=3, longest=3
i=6, c='b': 'b' was at index 4, move left to 5. window = 'cb',  left=5, length=2, longest=3
i=7, c='b': 'b' was at index 6, move left to 7. window = 'b',   left=7, length=1, longest=3

Final: 3
```

**Minute 18:30 — Candidate:** "Okay, I see it now. The key insight is: when I see a repeated character, I move left to `max(left, last_index_of_char + 1)`. The `max` is important — if the last-seen index is before the current left pointer, I should not move left backwards."

> **Commentary.** **The candidate has now taken the hint cleanly and recovered.** The walk-through-by-hand surfaced the `max(left, last_index + 1)` insight that the candidate had been failing to derive in their head. This is the recovery moment. From here, the round is back on track.

**Minute 19:00 — Candidate:** "Let me code this up now."

```python
def length_of_longest_substring(s: str) -> int:
    char_last_index: dict[str, int] = {}
    left: int = 0
    longest: int = 0
    for right in range(len(s)):
        c: str = s[right]
        if c in char_last_index and char_last_index[c] >= left:
            left = char_last_index[c] + 1
        char_last_index[c] = right
        current_length: int = right - left + 1
        if current_length > longest:
            longest = current_length
    return longest
```

**Minute 24:00 — Candidate:** "Okay, let me test this with the example I walked through."

*[Candidate traces through `'abcabcbb'` line by line, confirms each step matches the by-hand trace.]*

**Minute 30:00 — Candidate:** "Looks good. Let me also test `'bbbbb'`. i=0, c='b', not in map, left=0, length=1, longest=1. i=1, c='b', in map at index 0, 0 >= 0, so left becomes 1. length = 1-1+1=1. longest stays 1. And so on. Final: 1. Correct."

"Empty string: loop does not execute, return 0. Correct. Single character 'a': i=0, c='a', not in map, length=1, longest=1. Return 1. Correct."

**Minute 33:00 — Candidate:** "I think that is the implementation. Let me talk about complexity. The time complexity is O(n) — each character is visited once by the right pointer; the left pointer only moves forward. The space complexity is O(min(n, k)) where k is the size of the character set. For ASCII, k=128, so effectively O(1). For Unicode, k could be much larger, but bounded."

**Minute 34:30 — Interviewer:** *Good. Any trade-offs you would highlight, or things you would do differently?*

**Minute 34:45 — Candidate:** "One thing I would mention — I struggled at the start of the round to get the sliding-window mechanics right. Looking back, I should have done the walk-through-by-hand at the start, before any coding. The walk-through surfaced the `max(left, last_index + 1)` detail that I was struggling to derive abstractly. In a production code review, I would also add input validation, possibly a type-hint constraint for ASCII-only strings if that is a documented assumption, and maybe a test suite covering the edge cases I just walked."

> **Commentary.** **The candidate has acknowledged their own struggle.** This is a meaningful signal. The interviewer was about to write the rubric note "candidate needed significant prompting to recover" — and the candidate has pre-empted by saying it themselves. The self-awareness shifts the rubric note from "this is a concern" to "candidate is aware of their default and is working on it." The shift is small but real, and it bumps the rubric from "weak hire" to "lean hire."

**Minute 35:30 — Interviewer:** *Fair. We have about 10 minutes left. Let me ask one follow-up: what if the question were 'find the longest substring with at most K distinct characters'? Just sketch the approach.*

**Minute 35:45 — Candidate:** "That generalises the problem — instead of forbidding any repeat, we allow up to K distinct characters. The sliding-window template still works, but the move-left condition changes. We track the count of each character in the current window in a hash map, and when the number of distinct characters (the size of the map's non-zero entries) exceeds K, we move left until it does not. Time is still O(n), space is O(K)."

*[The candidate runs the follow-up with the rest of the time. The interviewer wraps the round at minute 42 with 3 minutes for the candidate-questions phase.]*

---

### What this transcript shows about recovery

A line-level inventory of the failure-and-recovery moves:

| Minute | Move                                                       | Failure or Recovery? |
|-------:|------------------------------------------------------------|----------------------|
|   0:15 | Dives into code without clarifying                         | Failure (FM 2)       |
|   2:30 | Restarts the implementation                                | Failure (FM 2)       |
|   6:15 | Goes silent for 90 seconds                                 | Failure (FM 3)       |
|   7:50 | "Just trying to get the indexing right" — vague answer      | Failure (FM 3)       |
|  11:15 | Takes the interviewer's redirect to high-level approach    | Recovery start       |
|  11:45 | Belatedly does the examples phase                          | Recovery             |
|  13:00 | Asks clarifying questions about ASCII vs Unicode           | Recovery             |
|  14:30 | Goes silent again                                          | Failure (FM 3)       |
|  15:00 | Takes the interviewer's hint to walk through by hand       | Recovery (took hint) |
|  18:30 | Surfaces the `max(left, last_index + 1)` insight            | Recovery complete    |
|  19:00 | Codes the solution with type hints and narration            | Recovery             |
|  34:45 | Self-acknowledges the slow start                            | Recovery (signal-up) |

The round had three failure moments and three corresponding recovery moments. The fact that the candidate eventually recovered — and that they self-acknowledged the recovery in the discuss phase — is what turned the round from a failure into a "lean yes." A candidate who failed the same three moments and did not recover would have produced the canonical losing round.

## What the two transcripts together teach

The strong-candidate version and the recovering-candidate version of the same 45-minute round differ in three specific axes:

1. **The pre-coding investment.** Transcript 1's candidate spent 5 minutes on clarify-examples-approach before writing a line of code. Transcript 2's candidate spent 30 seconds. The 4.5-minute difference produced the entire rest of the divergence.
2. **The response to a stuck moment.** Transcript 1's candidate was never stuck. Transcript 2's candidate was stuck twice and recovered twice. The recoveries were not automatic — they required interviewer prompting. A candidate who can rehearse the recovery moves *without* needing the interviewer to prompt is one rubric tier above the candidate who needs the prompt.
3. **The reception of a hint.** Transcript 1's candidate received no hints because none were needed. Transcript 2's candidate received two hints — one at minute 11, one at minute 15 — and took both cleanly. Taking the hint cleanly is itself a positive signal; ignoring the hint would have produced a clear "no hire" result on the same round.

The candidates in both transcripts had the same underlying technical ability. The difference between "strong yes" and "lean yes" was entirely in the method. The exercises and the mini-project for this week are the rehearsal loop that closes the method gap.

In the exercises that follow, you will run drills targeted at each failure mode and each recovery pattern. In the mini-project, you will record yourself running a full mock round and grade the recording against a rubric derived from these two transcripts. By Sunday night, your default method should resemble Transcript 1 more than Transcript 2 — not because Transcript 2 is a failure, but because the strong-yes round is what you are aiming for, and the lean-yes round is the floor below which a single bad moment can drop you back.
