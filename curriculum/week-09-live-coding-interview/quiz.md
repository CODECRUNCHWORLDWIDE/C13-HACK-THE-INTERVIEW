# Week 9 Quiz — The Live Coding Interview

Ten questions on phase structure, failure modes, recovery patterns, test-driven thinking, complexity, and the two worked transcripts. Time yourself — target 15 minutes, max 25 minutes. Answers and rubric at the bottom.

Each question is worth 2 points. Total: 20 points. **Passing: 14/20.**

---

## Question 1

The six phases of the live coding round, in order, are:

A) Clarify, code, examples, test, approach, discuss
B) Clarify, examples, approach, code, test, discuss
C) Examples, clarify, approach, code, discuss, test
D) Approach, clarify, examples, code, test, discuss

---

## Question 2

The candidate has spent 4 minutes on the clarify phase of a 45-minute round and is still asking clarifying questions. The interviewer has answered five questions and is starting to look impatient. What is the strong-candidate next move?

A) Keep asking until you have a complete picture of the problem.
B) Apologise for taking so long and rush through the examples phase.
C) Acknowledge that you have enough to proceed and transition to examples out loud: "I think I have enough to start — let me walk through a couple of examples to confirm."
D) Stay silent and start coding to make up for lost time.

---

## Question 3

The four common failure modes covered in Lecture 2 are:

A) Slow typing, weak typing, no comments, no tests
B) Over-engineering, premature optimisation, getting stuck silently, ignoring the hint
C) Wrong algorithm, wrong data structure, wrong language, wrong complexity
D) Talking too much, talking too little, asking too many questions, asking too few questions

---

## Question 4

You are 15 minutes into a 45-minute round. You have finished the code phase. The code compiles. You think it works. The interviewer has not asked for testing. What is the strong-candidate next move?

A) Wait for the interviewer to ask for testing.
B) Move directly to the discuss phase to save time.
C) Transition to the test phase yourself: "Let me walk through a test case line-by-line to make sure it works."
D) Optimise the code further while you have time.

---

## Question 5

The three moves for getting unstuck during the round, in the order Lecture 2 recommends trying them:

A) Simplify, clarify, verbalise
B) Verbalise, clarify, simplify
C) Verbalise, simplify, clarify
D) Clarify, simplify, verbalise

---

## Question 6

The interviewer asks "is your solution O(n) or O(n log n)?" What are the two sub-questions hidden inside this prompt?

A) "Is the time complexity correct?" and "Is the space complexity correct?"
B) "Is your stated complexity factually correct?" and "Is this the optimal complexity for the problem?"
C) "Did you sort the input?" and "Did you use a hash map?"
D) "Can you prove a lower bound?" and "Can you handle the worst case?"

---

## Question 7

Test-driven thinking during the interview means:

A) Writing unit tests in pytest before the function body.
B) Writing the test cases out loud *before* writing the code, naming at least three categories (happy path, edge cases, failure-mode input).
C) Running the code through a test framework at the end of the round.
D) Asking the interviewer for the expected output before writing any code.

---

## Question 8

In Transcript 1 of Lecture 3 (the round that went well), what specific move did the candidate make at minute 3:30 that earned signal in the approach phase?

A) Started typing the function signature.
B) Asked the interviewer for a hint.
C) Stated the brute force solution and its complexity before proposing the optimised approach.
D) Drew a diagram of the algorithm on a separate sheet.

---

## Question 9

The candidate in Transcript 2 (the round that went badly and recovered) had three failure moments and three recovery moments. Which failure mode did they exhibit at minute 6:15?

A) Over-engineering
B) Premature optimisation
C) Getting stuck silently
D) Ignoring the hint

---

## Question 10

The interviewer says, mid-round, "have you thought about what happens if the input is sorted?" Your current approach assumes unsorted input. What is the strong-candidate response?

A) "Yes, my approach handles both cases."
B) Pause, acknowledge the hint, explicitly consider what changes if the input is sorted, and pivot if it improves the solution.
C) Continue executing the original plan; the interviewer's question was just a clarification.
D) Restart the round with the sorted-input assumption.

---

## Answers

1. **B** — Clarify, examples, approach, code, test, discuss. (Lecture 1)
2. **C** — The strong move is to *explicitly* signal the phase transition. The clarify phase has a 2-3 minute budget; running long is fine *if you signal the transition rather than running silently long*.
3. **B** — The four failure modes from Lecture 2: over-engineering, premature optimisation, getting stuck silently, ignoring the hint.
4. **C** — Self-initiate the test phase. A candidate who waits to be asked is signalling that testing is not their default; the strong candidate tests without prompting.
5. **B** — Verbalise (cheapest), clarify (collaborative), simplify (most-aggressive intervention). The order matters because verbalising often reveals the answer without needing the other two moves.
6. **B** — Lecture 2's complexity-push framing. The factual question is separate from the optimisation question; the strong candidate answers each cleanly.
7. **B** — Lecture 2's test-driven-thinking framing. Three categories minimum: happy, edge, failure-mode. Written out *before* the code, not after.
8. **C** — Lecture 3 Transcript 1, minute 3:30. The candidate stated the O(n²) brute force, identified the bottleneck, proposed the O(n log n) optimisation. This is the canonical strong-approach phase.
9. **C** — Lecture 3 Transcript 2, minute 6:15. The candidate had been typing and deleting silently for 90 seconds. The keyboard was moving but the narration had stopped. Classic failure mode 3.
10. **B** — Take the hint cleanly. The take-the-hint pattern: pause, acknowledge, integrate, pivot if needed. The interviewer's question is almost certainly a redirect, not a casual probe.

---

## Scoring

| Score | Interpretation |
|------:|----------------|
| 18-20 | Excellent. You have internalised the Week 9 structure and can recognise the patterns under time pressure. Ready for live mocks with humans. |
| 14-17 | Good. The framework is mostly there. Re-read the lecture sections corresponding to your missed questions and run the exercises this week. |
| 10-13 | Developing. The structure is partially internalised. Re-read all three lectures and run all three exercises before the mini-project. |
| Below 10 | Concerning. The framework has not landed. Restart the week from Lecture 1 and run each exercise twice. The live coding round is too important to leave at this level of preparation. |

---

## After the quiz

For each question you got wrong, write down:

1. The question number.
2. The correct answer.
3. The specific lecture section that covers it.
4. One sentence on why you got it wrong (forgot, misread, confused with another concept).

Save this list. The patterns in your misses are the high-leverage targets for the rest of the week. If you missed multiple questions on failure modes, drill Lecture 2 again. If you missed multiple on the transcripts, re-read Lecture 3 with the rubric in hand. If you missed multiple on phase structure, re-read Lecture 1.

The quiz is not a gatekeeper. It is a calibration. The candidate who scores 14 and reflects on the four wrong answers learns more from the quiz than the candidate who scores 20 and moves on.
