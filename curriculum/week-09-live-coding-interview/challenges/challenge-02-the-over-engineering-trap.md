# Challenge 2 — The Over-Engineering Trap

**Time:** 60 minutes total. Two 25-minute rounds plus 10 minutes of self-grading and comparison.

**Format:** Solo, with recording. You will solve the same problem twice — once with the deliberate instruction to over-engineer (write the "production-quality" version), and once with the deliberate instruction to write the simplest possible solution. The comparison is the lesson.

**Why this challenge:** Failure mode 1 — over-engineering — is the failure mode that candidates with software-engineering instincts struggle with most. The candidate who has been told for two years that they should write clean, abstract, well-tested, well-documented code finds it counter-intuitive that the interview round penalises exactly that behaviour. This drill makes the cost of over-engineering visible by running both versions side by side; the comparison itself is the calibration.

## The setup

You will need:

- A timer.
- A recording setup.
- A blank file (Python recommended for type-hint clarity).
- The problem below.
- 60 minutes of uninterrupted time.

## The problem

**Statement:**

> Given a non-empty array of integers, every element appears twice except for one. Find that single element.

**Constraints:**

- The array has length between 1 and 30,000.
- Every element appears exactly twice, except for one element which appears exactly once.
- Your algorithm should have O(n) time complexity and ideally O(1) extra space.

This is LeetCode 136 — "Single Number." It is deliberately chosen because:

1. The optimal solution is famously short (a single XOR fold over the array). The pull to write more code than necessary is enormous.
2. The brute force is easy to write (count occurrences with a hash map), but the optimal is *shorter*. This is the rare case where the optimal solution is also the most-readable.
3. The candidate's instinct to add error handling, input validation, type-checking, edge-case branching is the trap. The trap is unusually visible here.

## The protocol

### Round 1: The over-engineered version (25 minutes)

For the first 25 minutes, your instruction is: **write the production-quality version of this code**. Treat it as if you were submitting a pull request to a critical codebase. Include:

- A full clarification phase.
- Input validation (what if the input is null? what if it has the wrong shape? what if the constraint is violated?).
- A docstring with type hints, parameter descriptions, return value, raises clauses.
- Error handling for invalid inputs.
- Logging or telemetry hooks (commented out is fine, but include them).
- A unit-test sketch at the bottom of the file showing how you would test it.
- Comments explaining the algorithm.

Record yourself. Run the full clarify-and-code phase out loud. Treat it as if you were going to ship this code.

**Target file length: 40-60 lines.**

### Round 2: The simplest version (25 minutes)

For the second 25 minutes, your instruction is: **write the simplest possible interview-round version of this code**. Treat it as if you were in a 45-minute live coding round with a strict time budget. Include:

- A short clarification phase (1-2 minutes).
- The simplest correct algorithm.
- Type hints on the function signature.
- No input validation beyond what the problem explicitly requires.
- No docstring; the function name and signature should be self-explanatory.
- No error handling for invalid inputs (per problem constraint, they don't occur).
- No logging, no telemetry, no extras.

Record yourself. Run the full clarify-and-code phase out loud.

**Target file length: 5-10 lines.**

### The comparison (10 minutes)

After both rounds, put the two files side by side. Watch both recordings back at 1.5x.

For each version, answer:

1. **How long did you spend on each phase?** Clarify, examples, approach, code, test, discuss. Was the time distribution appropriate for the version's instructions?
2. **What does each version optimise for?** The over-engineered version optimises for production-readiness. The simple version optimises for interview-round signal. Both are legitimate; they answer different questions.
3. **Which version would you submit in a real interview?** The answer is the simple version. The instinct to submit the over-engineered version is the failure-mode trigger.
4. **Which parts of the over-engineered version are valuable in a real interview, and which are not?** Generally: type hints on the signature are valuable. A two-line docstring is valuable. Input validation for problem-specified constraints is *not* valuable (the interviewer already gave you the constraint). Error handling is *not* valuable in a 45-minute round. A test sketch is valuable if you have time and the interviewer expects it; in most rounds, you do not have time.

## What the simple version should look like

The strong simple-version response to this problem:

```python
def single_number(nums: list[int]) -> int:
    """Return the only element that appears once when every other appears twice."""
    result: int = 0
    for num in nums:
        result ^= num
    return result
```

Five lines of logic. Type hint on the input, type hint on the return, type hint on the accumulator. One-line docstring (optional — many strong candidates omit it for an interview-round artifact). The algorithm: XOR everything together; duplicates cancel; the single survivor is the answer.

The trade-off discussion in the discuss phase:

> "The complexity is O(n) time, O(1) space. The XOR trick works because XOR is associative, commutative, and self-inverting — `a ^ a = 0` and `a ^ 0 = a`. So XOR-ing every element together cancels out all the duplicates and leaves the single. The trade-off is readability: the XOR approach is concise but requires the reader to know the algebraic properties of XOR. The alternative with a hash map of counts is more discoverable for readers unfamiliar with the trick, but pays O(n) extra space. For a production codebase where the team may not include XOR-fluent readers, I'd write a one-line comment explaining the trick rather than refactoring to the hash map."

That is the strong-candidate discuss phase. Five lines of code, two minutes of discussion, the whole round runs in 15 minutes total. The remaining 30 minutes are typically used for a follow-up problem.

## What the over-engineered version should look like

For comparison, the over-engineered version (do not submit this in a real round):

```python
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class SingleNumberFinder:
    """Find the element that appears exactly once in an array where all others appear twice."""

    def __init__(self, validate: bool = True) -> None:
        """Initialise the finder.

        Args:
            validate: If True, validate the input matches the expected shape.
                      If False, skip validation for performance-critical paths.
        """
        self.validate: bool = validate

    def find(self, nums: List[int]) -> int:
        """Find the single element using XOR aggregation.

        Args:
            nums: A non-empty list of integers where every element appears
                  exactly twice except for one element which appears once.

        Returns:
            The integer that appears exactly once.

        Raises:
            ValueError: If `nums` is empty or `validate=True` and the input
                        does not match the expected shape.
        """
        if not nums:
            raise ValueError("Input list must be non-empty.")

        if self.validate:
            self._validate_input(nums)

        result: int = 0
        for num in nums:
            result ^= num

        logger.debug("Found single number %d from input of length %d", result, len(nums))
        return result

    def _validate_input(self, nums: List[int]) -> None:
        """Verify that the input matches the constraint: every element appears
        twice except for exactly one element which appears once.
        """
        counts: dict[int, int] = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        ones: int = sum(1 for c in counts.values() if c == 1)
        twos: int = sum(1 for c in counts.values() if c == 2)
        others: int = sum(1 for c in counts.values() if c not in (1, 2))

        if others > 0:
            raise ValueError(f"Found {others} elements with unexpected count.")
        if ones != 1:
            raise ValueError(f"Expected exactly 1 element appearing once, found {ones}.")
```

Fifty-plus lines. Logging hook. Validation method that itself runs O(n) — which means the validation undoes the O(1) space win of the XOR algorithm. The class wrapper adds nothing. The docstrings are well-written but consume 15 of the 50 lines.

In a real interview, the candidate who produces this in 35 minutes has:

- Spent 15 minutes longer than necessary on infrastructure.
- Demonstrated awareness of the *concept* of validation, logging, and class design, but burned the interview-round budget that should have been spent on follow-up problems or trade-off discussion.
- Signalled "I conflate production code with interview code," which is a maturity concern from the interviewer's perspective.

The over-engineered version is *not* bad code in a vacuum. It is bad code *for the interview context*. The challenge is recognising that the context drives the choice.

## The rubric

After running both versions, score yourself:

| Axis                                                                                                | 0 | 1 | 2 |
|-----------------------------------------------------------------------------------------------------|---|---|---|
| **Simple version is genuinely 5-15 lines (no hidden cleverness inflating the line count)**         |   |   |   |
| **Simple version has type hints on the function signature**                                          |   |   |   |
| **Over-engineered version is genuinely production-quality (validation, docstring, logging, etc.)**  |   |   |   |
| **You can articulate which parts of the over-engineered version are valuable in a real round**       |   |   |   |
| **You can articulate which parts are anti-signals in a real round**                                  |   |   |   |
| **Your default instinct, on reflection, is the over-engineered version (be honest)**                |   |   |   |

For the last axis, scoring is reversed:

- **0** — Yes, my default is to over-engineer. (This is the honest answer for most candidates with software-engineering instincts.)
- **1** — Mixed; I sometimes over-engineer and sometimes write the simple version.
- **2** — My default is the simple version; I have to consciously work to write the over-engineered one for this drill.

A high score on the last axis is rare and means you have already internalised the interview-versus-production distinction. Most candidates score 0 or 1; that is fine, and the drill is the cure.

**Target across the other five axes: 8/10.**

## The big lesson

The big lesson of this challenge is that **the live coding round is a context, not a permanent identity**. The candidate who writes the over-engineered version in the interview is not a bad engineer; they are a good engineer who has not read the context correctly. The same candidate, in a code review at work, writing the same over-engineered version, would be celebrated.

The interview context optimises for *signal density per minute*. The 45-minute round gives the interviewer roughly 60 individual signal-moments. Each line of unnecessary infrastructure costs the candidate one signal-moment that could have been used for a trade-off discussion, a follow-up problem, a clarifying question. The interviewer's rubric is filled with signal-moments; the candidate who burns their signal-moments on infrastructure rather than insight scores lower regardless of code quality.

The production context optimises for *robustness under sustained operation*. The 50-line over-engineered version is the right answer there. Both contexts are real; both deserve respect; conflating them is the failure.

## Reflection prompts

After the drill:

1. **Did the simple version feel uncomfortable to write?** Many candidates report that the simple version felt "lazy" or "unprofessional." That feeling is the calibration error; the simple version is the correct context-aware response, and the discomfort is the signal that your default is over-engineering.
2. **Which parts of the over-engineered version would you actually include in a real interview?** Type hints on the signature: always. One-line docstring: usually skip. Input validation: skip unless the interviewer asks. Logging: skip. Class wrapper: skip unless the problem genuinely requires state. Two-sentence trade-off discussion at the end: always.
3. **Is there a context — a specific company, a specific kind of round — where the over-engineered version would actually be the right answer?** Some senior staff-level rounds at some companies (notably Amazon's bar-raiser, sometimes Google's L5+ rounds) do reward production-thinking signals. But even there, the round-time-budget constraint applies; the over-engineering must be *visible signal*, not just *visible scaffolding*. The bar-raiser's rubric line is "demonstrates ownership and operational excellence" — which means the right move is to *mention* the production concerns, not necessarily to *code* them.

## When to repeat this drill

Once is usually enough for this specific drill. The lesson is calibration; once calibrated, it sticks. If you find yourself over-engineering in subsequent mock interviews, rerun this drill with a different problem (any LeetCode Easy will do). The repeated comparison is what fixes the default.

A specific suggestion: keep the simple-version file from this drill on hand during your real interview week. Re-read it the morning of any onsite. The 5-line file is the visual reminder that the interview-round optimum is shorter than your instinct will produce; the reminder is enough to calibrate the day's rounds.
