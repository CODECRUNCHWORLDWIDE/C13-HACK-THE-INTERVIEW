# Exercise 3 — The Complexity-Defence Drill

**Time:** 30 minutes total — six 4-minute rounds, plus 6 minutes of self-grading.

**Format:** Solo. You will not write new code in this exercise. You will be given six small code snippets, one at a time. For each, you have 4 minutes to (a) state the time complexity, (b) state the space complexity, (c) state whether this is optimal for the underlying problem, and (d) state one trade-off you would surface if asked.

**Why this exercise:** The complexity-push moment — "is this O(n) or O(n log n)?" — is one of the most-evaluated moments in any live coding round and one of the most under-rehearsed. Most candidates have memorised the complexity of canonical algorithms but freeze when given an unfamiliar snippet and asked to analyse it on the spot. This drill is the focused rep on the unfamiliar-snippet analysis, with the same speech-out-loud overhead as the real round.

## The setup

You will need:

- A timer.
- A recording setup (audio is sufficient; video is optional).
- The six snippets below, *unread* until each round starts.
- A blank document for notes.

## The protocol

For each of the six snippets:

1. **Set the timer for 4 minutes.** Start recording.
2. **Read the snippet aloud.** Do not start analysis until the read-aloud is complete.
3. **Run the analysis out loud:**
   - State the time complexity. Justify it line-by-line.
   - State the space complexity. Justify it.
   - State whether you think this is optimal for the problem the code is solving. If yes, briefly say why. If no, sketch the better approach.
   - State one trade-off you would surface in the discuss phase. (Memory vs speed, code clarity vs constant factor, etc.)
4. **Stop the timer.** Note the elapsed time.
5. **Move to the next snippet.**

The 4-minute budget is tight on purpose. The real-round complexity question lands inside 60-90 seconds; the 4-minute drill budget gives you room to think but still applies time pressure.

## The six snippets

### Snippet 1

```python
def find_duplicate(nums: list[int]) -> int:
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1
```

**Problem context:** Given a list of integers where exactly one integer appears twice and all others appear once, find the duplicate.

Analyse: time, space, optimality, trade-off.

### Snippet 2

```python
def find_duplicate_v2(nums: list[int]) -> int:
    nums_sorted: list[int] = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            return nums_sorted[i]
    return -1
```

**Problem context:** Same problem as Snippet 1, different approach.

Analyse: time, space, optimality, trade-off. Note this is an explicit comparison case — compare your analysis of Snippet 1 vs Snippet 2.

### Snippet 3

```python
def has_path(graph: dict[int, list[int]], start: int, end: int) -> bool:
    visited: set[int] = set()
    stack: list[int] = [start]
    while stack:
        node: int = stack.pop()
        if node == end:
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                stack.append(neighbour)
    return False
```

**Problem context:** Given a directed graph as an adjacency list and two nodes, return whether a path exists from start to end.

Analyse: time, space, optimality, trade-off. Be careful — the time complexity here is not obviously O(V) or O(V + E).

### Snippet 4

```python
def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix: str = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

**Problem context:** Given a list of strings, find the longest common prefix.

Analyse: time, space, optimality, trade-off. Pay attention to the `while not s.startswith(prefix)` loop — it has a hidden cost.

### Snippet 5

```python
def kth_smallest(nums: list[int], k: int) -> int:
    import heapq
    return heapq.nsmallest(k, nums)[-1]
```

**Problem context:** Given a list of integers and a positive integer k, return the kth smallest element.

Analyse: time, space, optimality, trade-off. The standard library is doing the work; you need to know what its complexity is.

### Snippet 6

```python
def fibonacci(n: int, memo: dict[int, int] = {}) -> int:
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

**Problem context:** Return the nth Fibonacci number.

Analyse: time, space, optimality, trade-off. Pay attention to the *mutable default argument* — this is a real Python gotcha.

## The rubric

For each snippet, score yourself on the four axes:

| Axis                                                            | 0 | 1 | 2 |
|-----------------------------------------------------------------|---|---|---|
| **Stated time complexity correctly with justification**         |   |   |   |
| **Stated space complexity correctly**                           |   |   |   |
| **Made a defensible claim about optimality**                    |   |   |   |
| **Surfaced one real trade-off**                                 |   |   |   |

Scoring per axis:

- **0** — Got it wrong or did not address it.
- **1** — Got the answer but not the justification, or the justification was hand-wavy.
- **2** — Got the answer and could justify it line-by-line.

**Total possible per snippet: 8. Total possible across six snippets: 48.**

**Target: 36/48.** A score below 24 means complexity-analysis is not yet a reflex; spend an hour with NeetCode or CS50 videos on complexity and rerun. A score of 36-44 means the muscle is forming. A score of 45+ means you can defend complexity confidently in a real round.

## After the six rounds: targeted review

Identify the snippet where you scored lowest. For that snippet:

1. **Look up the correct analysis.** Use any free source — NeetCode YouTube, LeetCode discussion, a standard algorithms textbook reference. Spend up to 10 minutes.
2. **Re-record yourself doing the analysis** for that snippet alone, 4 minutes max, now that you know the correct answer.
3. **Compare the two recordings.** What was the specific gap? Did you misread the loop? Did you forget that `sorted()` is O(n log n)? Did you miss the recursion-stack space contribution?

The gap-identification step is the high-leverage part. Most candidates do this drill, get most snippets right, and move on. The candidates who go back to the snippet they got wrong and re-record after learning are the candidates who close the complexity-defence gap permanently.

## What "good" looks like for each snippet

The answer key, condensed:

- **Snippet 1.** Time O(n), space O(n), optimal for the unsorted-input case, trade-off is space-for-time (the set costs O(n) memory to buy O(n) time).
- **Snippet 2.** Time O(n log n) due to sort, space O(n) for the sorted copy (or O(log n) for in-place sort), not optimal compared to Snippet 1 if extra space is acceptable. Trade-off: if you cannot mutate the input but also cannot use O(n) extra space, this is the right answer; otherwise Snippet 1 wins.
- **Snippet 3.** Time O(V + E) where V is the number of vertices and E the number of edges. Space O(V) for the visited set and the stack. Optimal for the general case. Trade-off: depth-first using a stack vs breadth-first using a queue — same complexity, different memory patterns; BFS is better if you also want the shortest path.
- **Snippet 4.** Time O(n × m) in the worst case, where n is the number of strings and m is the length of the shortest. Space O(m) for the prefix. Optimal in the asymptotic sense; trade-off is the early-exit when the prefix becomes empty — the worst case happens only when all strings share a long prefix.
- **Snippet 5.** Time O(n log k) using `heapq.nsmallest`, space O(k). Not optimal for "kth smallest" — Quickselect is O(n) average, O(n²) worst-case. Trade-off: simpler code with `nsmallest` vs more complex code with Quickselect; pick `nsmallest` if k is small relative to n, Quickselect if you need the average-case linear time.
- **Snippet 6.** Time O(n) due to memoisation, space O(n) for the memo plus O(n) for the recursion stack. The mutable default argument `memo: dict[int, int] = {}` is a real bug — the dict is shared across calls to `fibonacci`, which means the memo is correct for repeated calls but is also a memory leak across the program's lifetime. The fix is `memo: Optional[dict[int, int]] = None` with `memo = memo if memo is not None else {}` inside the function. Trade-off: explicit memo parameter vs functools.lru_cache.

If your analysis missed the mutable-default-argument bug in Snippet 6, that is a Python-specific gotcha worth burning into memory. Some interviewers will ask follow-up questions specifically about this pattern.

## Reflection prompts

After the six rounds:

1. **Which complexity-class did you get wrong most often?** Time, space, or optimality? Each has a different remediation — for time, drill more loop-counting examples; for space, drill recursion-stack and aux-data-structure examples; for optimality, drill more "what is the lower bound" reasoning.
2. **Which snippet's trade-off surprised you?** The trade-off discussion is the highest-leverage signal in the discuss phase of a real round. Knowing the canonical trade-off for each algorithm family — sort vs hash, BFS vs DFS, heap vs Quickselect, iterative vs recursive — is the calibration you carry into every round.
3. **Are you fluent in Python's standard-library complexity?** `sorted` is O(n log n). `list.append` is amortised O(1), `list.insert(0, x)` is O(n). `dict.__contains__` is O(1) average, O(n) worst case. `set.__contains__` is O(1) average. If any of these are uncertain, spend 30 minutes on the CPython documentation page for time-complexity-of-built-ins. The page is free and is the canonical reference.

## When to repeat this exercise

Run this drill once a month if you are actively interviewing. The snippets above are the starter set; you can generate fresh snippets by picking any LeetCode Medium and analysing the canonical solution. The drill itself is the rep; the snippets are interchangeable.
