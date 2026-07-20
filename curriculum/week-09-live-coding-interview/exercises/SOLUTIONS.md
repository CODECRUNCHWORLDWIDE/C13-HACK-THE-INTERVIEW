# Week 9 Exercises — Sample Strong Responses

This file contains sample strong responses to the three exercises in this folder. The samples are not "the only correct answer." They are calibration baselines — the kind of response that, run inside a real interview round, would earn a passing-or-better signal on the rubric.

The samples are written as transcripts — the candidate speaking, in their own voice, with the inner-monologue narration that produces a strong-yes round. Use them to grade your own recordings, not to memorise verbatim. Memorising the wording fails in the round; internalising the structure works.

## Exercise 1 — The Clarification Drill: Sample Strong Responses

### Problem 1: Squares of a sorted array

**Strong clarification phase (~2 minutes 30 seconds):**

"Okay, let me restate to make sure I have this right. The input is a sorted array of integers. The output is an array of the same length containing the squares of the input, in sorted order. A few questions:

— First, can the array contain negative numbers? This matters because negative numbers, when squared, can produce a value larger than the original positive numbers in the array. So if I have `[-7, -3, 2, 5]`, the squares are `[49, 9, 4, 25]`, and the sorted output is `[4, 9, 25, 49]`. The position of the largest squared value depends on whether the most-negative or the most-positive number has the larger absolute value.

— Second, can the array be empty? If so, I assume I return an empty array.

— Third, can it contain a single element?

— Fourth, can it contain duplicates? For example `[-3, -3, 2]` — that gives squares `[9, 9, 4]`, sorted `[4, 9, 9]`.

— Fifth, is the input always non-decreasing (sorted ascending), or could it be non-increasing? I assume non-decreasing, but want to confirm.

— Sixth, what is the size of the array? This affects whether I should worry about O(n²) being too slow versus O(n) — for an input of size up to 10⁴, both fit; for an input of size 10⁷, only O(n) fits."

**Strong examples phase (~90 seconds):**

"Let me walk through a few examples to lock in the shape.

— Happy path: `[-7, -3, 2, 5]` → squares `[49, 9, 4, 25]` → sorted `[4, 9, 25, 49]`.

— All-positive: `[1, 2, 3]` → squares `[1, 4, 9]`. Already sorted because squaring preserves order when all inputs are positive.

— All-negative: `[-5, -3, -1]` → squares `[25, 9, 1]` → sorted `[1, 9, 25]`. The order reverses because the most-negative has the largest square.

— Edge case: empty array → `[]`.

— Edge case: single element `[-2]` → `[4]`.

These examples are enough to confirm the contract. The interesting structural insight is that the output requires merging two reverse-of-sorted halves: the squares of the negatives (in reverse) and the squares of the positives (in order). That suggests a two-pointer approach, but I'm not going to commit to the approach until I've stated the brute force."

**What this earns:**

| Rubric axis | Score | Why |
|-------------|-------|-----|
| Restated in own words | 2 | Restatement is not verbatim, surfaces the key structural insight about negatives |
| 3+ clarifying questions | 2 | Six distinct questions, each with a reason |
| 2 concrete examples | 2 | Five examples covering happy, all-positive, all-negative, empty, single |
| Surfaced ambiguity | 2 | The negative-numbers question, the sort-order question, the size question — all are real ambiguity points |

**Total: 8/8.**

### Problem 2: Anagram check

**Strong clarification phase (~2 minutes):**

"Okay, anagrams. The input is two strings; the output is a boolean indicating whether the first is an anagram of the second. An anagram means same characters with same counts, in any order. A few questions:

— Is this case-sensitive? Is 'Listen' an anagram of 'silent'? In English usage, anagrams are usually case-insensitive, but in a programming context I'd want to confirm.

— Is whitespace counted as a character? 'a b' versus 'ab' — same characters but different lengths if we count whitespace.

— What character set are we working with? ASCII only, or Unicode? Unicode anagrams are tricky because of combining characters and normalisation forms.

— What about punctuation? 'rail safety' vs 'fairy tales' — those are the canonical anagram pair, but only if we strip punctuation and whitespace.

— What if one or both strings are empty? Two empty strings — are they anagrams of each other? I'd argue yes (vacuously).

— What's the maximum string length? This affects whether I should care about constant-factor optimisations or just write the cleanest version.

— Is the input guaranteed to be a valid string, or could it be None or a non-string type?"

**Strong examples phase (~90 seconds):**

"Examples:

— Happy path: `'listen'`, `'silent'` → True.

— Different lengths: `'abc'`, `'abcd'` → False, because the lengths differ.

— Same letters different counts: `'aab'`, `'abb'` → False, because the counts of 'a' and 'b' differ.

— Both empty: `''`, `''` → True, vacuously.

— Case difference (assuming case-sensitive per clarification): `'Listen'`, `'silent'` → False, because 'L' ≠ 'l'.

The structural insight: this reduces to comparing character-frequency dictionaries. The optimal approach is O(n) using a hash map of character counts, or O(n log n) using sorted strings. The lengths-don't-match early-exit is a free optimisation."

**Total: 8/8.**

### Problem 3: Binary tree right-side view

**Strong clarification phase (~2 minutes 30 seconds):**

"Okay, right-side view of a binary tree. The output is a list of node values, one per level of the tree, representing what is visible from the right side. A few questions:

— First, how is the tree represented? Is it a `TreeNode` class with `.val`, `.left`, `.right` attributes, or is it given as an array in level-order (the LeetCode-style serialisation)?

— Second, what does 'visible from the right' mean exactly? My reading is: at each level, the rightmost node at that level. So for a tree where level 0 is the root and levels increase downward, I return one node per level, the rightmost one.

— Third, what if a node has only a left child at a level where higher levels had right children? For example, a root with a right child that itself has only a left child. The right-side view at the leaf level should be the left child (because there is no right sibling). Is that right?

— Fourth, what if the tree is empty? I assume return an empty list.

— Fifth, what if the tree has only a root? The right-side view is `[root.val]`.

— Sixth, are the node values integers? Strings? Generic?

— Seventh, what is the expected return type? A `list[int]`, a generator, a string representation?"

**Strong examples phase (~2 minutes):**

"Let me draw a few trees:

```
Tree 1:
    1
   / \
  2   3
       \
        4

Right-side view: [1, 3, 4]
```

The root (level 0) is 1. At level 1, the rightmost is 3. At level 2, the only node is 4 (under the 3).

```
Tree 2:
    1
   / \
  2   3
 /
4

Right-side view: [1, 3, 4]
```

This is the tricky case. At level 2, the only node is 4, and it's under the left subtree. But from the right, looking down, you still see 4 — there's nothing blocking it. So the answer is [1, 3, 4].

```
Tree 3:
    1
   /
  2
 /
3

Right-side view: [1, 2, 3]
```

All left children, but each is the rightmost at its level (the only node at its level).

The structural insight: this is a level-order traversal where, at each level, you record the last node visited. BFS with a queue, or DFS with right-first recursion."

**Total: 8/8.**

### Self-grading on the three rounds (sample)

If your clarify-and-examples phase across the three rounds scored:

- **22-24/24** — Excellent. Drop this drill from your weekly routine; rotate to the harder drills.
- **18-21/24** — Good. Run the drill once more this week with three different problems (any LeetCode Easy will do).
- **12-17/24** — Developing. Repeat this exercise on Tuesday and again on Saturday. The clarify-phase muscle is not yet built.
- **Below 12/24** — Concerning. Re-read Lecture 1's clarify-phase section. The most common reason for a sub-12 score is treating the clarify phase as a formality; if that's the case, the lecture's "even when you know the answer, ask anyway" discipline is the fix.

## Exercise 2 — The Stuck-Recovery Drill: Sample Strong Response

This is a partial transcript of a strong run on the **Meeting Rooms II** problem. The transcript shows the full clarify-and-approach phases, the moment the candidate hits a wall, and the application of the three recovery moves.

### Clarify phase

"Okay, minimum number of conference rooms to schedule all meetings. The input is a list of intervals; the output is an integer. A few questions:

— Can the list be empty? Returns 0 if so, presumably.

— Can it contain a single meeting? Returns 1.

— Can two meetings share an endpoint? I.e., one ends at time 10 and another starts at time 10 — same room or different?

— Are the times integers or floats?

— What's the size of the input? Up to 10⁴? 10⁶?

— Are the meetings guaranteed to have `start < end`, or could `start == end`?

— What about negative times?"

### Examples phase

"Let me try a couple of examples.

`[[0, 30], [5, 10], [15, 20]]`. Meeting 1 from 0-30. Meeting 2 from 5-10 — overlaps with 1, so we need 2 rooms. Meeting 3 from 15-20 — overlaps with 1 (since 1 runs to 30), but does it overlap with 2 (which ends at 10)? No. So at any moment, the maximum concurrent meetings is 2 (during 5-10 and during 15-20, since meeting 1 is still going). Answer: 2.

`[[7, 10], [2, 4]]`. Meeting 1 ends at 4, meeting 2 starts at 7. No overlap. 1 room.

`[[1, 5], [5, 10]]`. Shared endpoint — assuming same room is allowed, 1 room. Otherwise 2.

The structural insight: at each point in time, count how many meetings are 'active.' The answer is the maximum of that count over all times. That suggests a sweep-line algorithm."

### Approach phase

"The brute force: for each pair of meetings, check overlap, build a conflict graph, find the maximum clique. That's exponential — wrong direction.

Better brute force: for each minute of the time range, count how many meetings are active. That's O(T × n) where T is the time range and n is the number of meetings. Bad if T is large.

Smarter approach: sweep line. Sort the events — each meeting produces two events, a 'start' event and an 'end' event. Sort all events by time. Walk through them in order, maintaining a counter: increment on a start event, decrement on an end event. The maximum value of the counter during the walk is the answer.

That's O(n log n) for the sort, O(n) for the walk, O(n) extra space for the events list.

There's also a heap-based approach: sort intervals by start time, then use a min-heap of end times. For each new interval, if the top of the heap is `<=` the new start, pop it (a room has freed up). Push the new end. The size of the heap at the end is the answer. Also O(n log n), also O(n) space.

I'll go with the sweep-line approach. Let me code it up."

### Code phase — and the stuck moment

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    events: list[tuple[int, int]] = []
    for start, end in intervals:
        events.append((start, 1))   # 1 for start
        events.append((end, -1))    # -1 for end
    events.sort()
    # ...
```

"Hmm, wait. I need to be careful about the sort key. If a meeting ends at time 10 and another starts at time 10, and shared endpoints don't count as overlap, then the 'end' event needs to come *before* the 'start' event at the same time. Otherwise we'd count them as overlapping.

But my current sort is on `(time, delta)` where delta is `+1` for start and `-1` for end. Since `-1 < +1`, the end event sorts before the start event automatically. That's correct... I think. Let me trace through.

Actually wait. If two events have the same time but different deltas, my tuple sort puts the `-1` first. That means at time 10, the 'end' is processed before the 'start.' Good. But what if two meetings both *end* at the same time, or both *start* at the same time? Doesn't matter for correctness — the count moves by the right amount either way.

Okay let me continue.

```python
    max_rooms: int = 0
    current_rooms: int = 0
    for time, delta in events:
        current_rooms += delta
        if current_rooms > max_rooms:
            max_rooms = current_rooms
    return max_rooms
```

Wait. Hmm. Let me think. If I process the end event first when times are tied, the count decrements before it increments. So for `[[1, 10], [10, 20]]`, the events sorted are `[(1, 1), (10, -1), (10, 1), (20, -1)]`. Walk: 1, 0, 1, 0. Max is 1. Correct — they share an endpoint, one room.

For `[[1, 10], [5, 15]]`: events `[(1, 1), (5, 1), (10, -1), (15, -1)]`. Walk: 1, 2, 1, 0. Max is 2. Correct — overlapping in [5, 10], two rooms."

### The stuck moment (it does not appear in this run)

The above run was clean. But to illustrate the recovery pattern, here is the same problem with a stuck moment inserted at the point where the candidate is uncertain about the tie-breaking rule:

**Hypothetical stuck moment:**

"Wait. I'm not sure about the tie-breaking. Let me think... [silence for 20 seconds]...

[Move 1 — verbalise:] Okay, I'm stuck because I'm not sure whether `(10, -1)` should sort before `(10, +1)` or after. My instinct says before — end the meeting first, then start the new one — but I want to verify.

[Move 2 — clarify:] Let me ask myself the clarifying question: if a meeting ends at 10 and another starts at 10, is that one room or two? I clarified earlier that shared endpoints are okay, so it should be one room.

[Move 3 — simplify:] Let me trace through the simplest case. `[[1, 10], [10, 20]]`. If end comes first: events at time 10 are `(10, -1), (10, 1)`. Walk: 1, 0, 1, 0. Max is 1. That's correct — one room. If start comes first: events at time 10 are `(10, 1), (10, -1)`. Walk: 1, 2, 1, 0. Max is 2. That's wrong — should be one room. So end-first is correct.

Tuple sort with `-1 < +1` puts end-first automatically. Good. I'll proceed."

The hypothetical version is what the strong-recovery pattern looks like applied to a real stuck moment. The actual transcript above did not include a stuck moment because the candidate's preparation already covered the edge case; the hypothetical is what the rehearsed-recovery would look like in the moment.

### Test phase

"Let me test. `[[0, 30], [5, 10], [15, 20]]`. Events sorted: `[(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)]`. Walk: 1, 2, 1, 2, 1, 0. Max is 2. Correct.

Edge case empty: returns 0 at the early-exit. Correct.

Edge case single: `[[1, 5]]` → events `[(1, 1), (5, -1)]` → walk 1, 0 → max 1. Correct."

### Discuss phase

"Complexity: O(n log n) time from the sort. O(n) extra space for the events list. Optimal? Sorting is the lower bound here for the general case, so yes, O(n log n) is optimal for a comparison-based approach.

Trade-off: I chose the sweep-line approach over the heap-based one because the sweep-line is conceptually simpler — one pass through events with a counter. The heap-based is also O(n log n) but the constants are slightly larger (heap operations have higher overhead than the linear walk).

If we wanted to handle a streaming input, the sweep-line doesn't generalise — we can't sort what we haven't seen. The heap-based, with online sorting of intervals by start time, would generalise."

### Self-grading

Score against the rubric in Exercise 2:

| Axis | Score |
|------|-------|
| Clarify phase with 3+ questions | 2 |
| 2 concrete examples before coding | 2 |
| Brute force complexity stated | 2 |
| Stuck-recovery move applied | 1 (no real stuck moment in the actual run, would be 2 with the hypothetical applied) |
| Tested with line-by-line trace | 2 |
| Final complexity stated | 2 |

**Total: 11/12.**

## Exercise 3 — Complexity-Defence Drill: Sample Strong Responses

For each snippet, the strong-response shape is the same: state time, state space, state optimality, surface one trade-off. The answers below are the correct ones; the verbal delivery is what you should rehearse.

### Snippet 1: find_duplicate with a set

"Time complexity: O(n). Single pass through the array; set lookup and insertion are O(1) average. Space complexity: O(n) for the set in the worst case (when no duplicate is found until the last element). Optimal: yes, O(n) is the lower bound — you have to look at each element at least once. Trade-off: space-for-time. The set buys O(n) extra memory to get O(n) time; without it, the brute force is O(n²)."

### Snippet 2: find_duplicate with sort

"Time complexity: O(n log n) from the sort; the linear scan after is O(n) but dominated. Space complexity: O(n) for `sorted()` returning a new list, or O(log n) for an in-place sort's recursion stack. Optimal: no — Snippet 1's O(n) is better. Trade-off: avoids the O(n) extra memory of Snippet 1's set, but pays O(n log n) instead of O(n) in time. Useful only if memory is the primary constraint."

### Snippet 3: has_path with DFS

"Time complexity: O(V + E) — each vertex is visited at most once (due to the visited set check), and each edge is examined at most once. Space complexity: O(V) for the visited set and the stack in the worst case (a linear chain graph). Optimal: yes for unweighted reachability. Trade-off: DFS vs BFS — DFS uses a stack (LIFO), BFS uses a queue (FIFO). Same asymptotic, but BFS finds the shortest path in addition to reachability, at no asymptotic cost. If shortest path is needed, swap to BFS."

### Snippet 4: longest_common_prefix

"Time complexity: O(n × m) where n is the number of strings and m is the length of the shortest. The inner `while` loop can shrink the prefix by one character per iteration, and each iteration's `startswith` call is O(m). Space complexity: O(m) for the prefix variable (in Python, string slicing creates a new string). Optimal: this is fine asymptotically. The alternative — vertical scan, comparing the i-th character of all strings — is also O(n × m) but with potentially better early-exit if the strings diverge quickly. Trade-off: horizontal (current code) vs vertical scan; horizontal is simpler to read but vertical has better early-exit on diverse inputs."

### Snippet 5: kth_smallest with heapq.nsmallest

"Time complexity: O(n log k) — `heapq.nsmallest` maintains a max-heap of size k and processes n elements. Space complexity: O(k) for the heap. Optimal: no for the average case — Quickselect achieves O(n) average. But Quickselect is O(n²) worst case; heap is O(n log k) deterministically. Trade-off: simplicity and worst-case bound (heap wins) vs average-case speed (Quickselect wins). For interview-level code, heap is almost always the right answer."

### Snippet 6: fibonacci with memoisation

"Time complexity: O(n) — each value from 0 to n is computed exactly once. Space complexity: O(n) for the memo dict plus O(n) for the recursion stack. Optimal: yes, O(n) is tight (you have to compute each Fibonacci number from 0 to n at least once). Trade-off: this code has a *real bug* — the mutable default argument `memo: dict[int, int] = {}` is shared across all calls to `fibonacci`. This is actually a feature for memoisation purposes (the cache persists) but it's a famous Python gotcha because it can cause unexpected behaviour. The Pythonic fix is `memo: Optional[dict[int, int]] = None` with `memo = memo if memo is not None else {}` inside the function. Or use `@functools.lru_cache`. I'd flag this in code review."

### Self-grading

Score each snippet on the four axes. Across six snippets:

- **45-48/48** — Strong. You can defend complexity in any round.
- **36-44/48** — Good. One or two specific gaps to drill (likely space complexity, or specific data-structure complexities).
- **24-35/48** — Developing. Spend an hour on a complexity-cheat-sheet and rerun.
- **Below 24** — Major gap. Complexity is a baseline expectation in any technical round; this is the first thing to fix before more mocks.

The complexity-defence muscle is the cheapest single muscle to build — it's all in the head, no environment needed, no other person needed. An hour a week of complexity-quiz on random LeetCode solutions builds it permanently.
