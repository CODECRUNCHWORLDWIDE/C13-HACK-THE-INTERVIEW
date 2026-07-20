# Week 6 — Quiz

Ten questions. Lectures closed.

---

**Q1.** The technical phone screen differs from the HM screen on several axes. Which of the following is the **most** structurally important difference?

- A) The technical screen is recorded; the HM screen is not.
- B) The technical screen is 45 minutes; the HM screen is 30-45 minutes.
- C) The technical screen is the first call in the pipeline where you write live code on a shared editor, evaluated against a four-dimension rubric (problem-solving, coding, communication, testing).
- D) The HM screen is conducted by a recruiter and the technical screen is conducted by an engineer.

---

**Q2.** The four scoring dimensions in a typical technical-screen rubric are:

- A) Speed, language, syntax, style.
- B) Problem-solving, coding, communication, testing.
- C) Algorithm depth, system design, comp expectations, fit.
- D) Brute force, optimisation, refactoring, deployment.

---

**Q3.** A candidate skips the brute force and goes straight to a hash-map optimisation. The interviewer's most likely read is:

- A) Strong candidate; they know the pattern.
- B) Memorised; reads as not having genuinely problem-solved on the call. Costs at least half a point on the problem-solving dimension.
- C) Neutral; the optimisation is what matters.
- D) The candidate is too senior for this problem.

---

**Q4.** The interviewer says "what if the input were sorted?" mid-coding. The right candidate response is:

- A) Continue with the original approach; the hint is just background colour.
- B) Acknowledge the hint, restate it to yourself, update your approach visibly, and confirm with the interviewer before going back to code.
- C) Apologise and offer to start over from scratch.
- D) Defend the original approach until the interviewer concedes.

---

**Q5.** Which of the following is the **strongest** version of the testing phase?

- A) "I think this works." (Stop.)
- B) "Let me run it. {Run.} Yep, works." (Stop.)
- C) "Let me run on the original example — {run} — got expected output. Now empty input — {run} — returns empty as expected. Now a larger one — {run} — looks right. Any other edges? Duplicates — {run} — matches. I think it's solid."
- D) "I'll trust the code." (Stop.)

---

**Q6.** A candidate codes in silence for 4 minutes, then says "I think it works." The interviewer's debrief on Communication is most likely:

- A) Strong — focused work, did not interrupt their own thinking.
- B) Weak — 4 minutes of unscored time; the interviewer cannot reconstruct what the candidate was doing. The rubric drops at least half a point.
- C) Neutral — silence is fine if the code is right.
- D) Bonus — efficient candidate.

---

**Q7.** The five-phase narration loop is, in order:

- A) Restate, brute force, code, test, optimise.
- B) Restate, example-by-hand, brute force, optimise, code-while-narrating.
- C) Greet, intro, code, test, ask questions.
- D) Optimise, code, test, complexity, extension.

---

**Q8.** The interviewer asks the production-framing follow-up: "How would you change this for production traffic?" The strongest answer:

- A) "I'd add error handling and logging." (Generic two-word answer.)
- B) "I'd test it." (Conflates testing with production hardening.)
- C) Three concrete things, each named with a sentence — e.g., "input validation for null and out-of-bounds integers, structured logging on function entry with input size and execution time, and a metric histogram of execution time to catch a degenerate input that would push us into O(n²)" — and an acknowledgement of what you're not covering.
- D) A full microservices and Kubernetes architecture.

---

**Q9.** The first 90 seconds of a technical phone screen should produce which observable outcome?

- A) The candidate has solved the brute force.
- B) The candidate has greeted, confirmed audio, confirmed the editor and language, and is waiting for the interviewer to present the problem. The tooling is invisible.
- C) The candidate has started coding.
- D) The candidate has named their target compensation.

---

**Q10.** A Karat technical screen differs from a typical in-house technical screen on which two axes?

- A) Karat is harder.
- B) The Karat interviewer is a Karat-employed engineer (not from the hiring company), and the session is recorded by default for the hiring company to review.
- C) Karat doesn't follow a rubric.
- D) Karat sessions are 90 minutes.

---

## Answer key

<details>
<summary>Reveal after attempting</summary>

1. **C** — The structural shift is that the technical screen is the first call where you write live code on a shared editor against a four-dimension rubric. Recording (A) is sometimes true; length (B) is similar to HM; (D) is wrong — recruiter does not run the technical screen.
2. **B** — Problem-solving, coding, communication, testing. The four-axis rubric is the synthesised public standard across most companies.
3. **B** — Skipping the brute force reads as memorised; the interviewer is watching for the process of optimisation, not just the optimised answer.
4. **B** — Acknowledge, process visibly, update, confirm. The four-step pattern. Ignoring (A) costs the call; over-deference (C) and defending (D) both lose points.
5. **C** — Three test cases narrated out loud (original, edge, stress, plus an extra), with expected outputs named before running, is the load-bearing testing phase. (A) and (D) skip; (B) is the minimum, not strong.
6. **B** — 4 minutes of silent coding produces unscored time. The rubric drops on Communication; the interviewer cannot reconstruct what you did.
7. **B** — Restate, example, brute force, optimise, code-while-narrating. The structure of the 35-40 minute coding block.
8. **C** — Three specific things with sentences each, plus an acknowledgement of scope. (A) is generic; (B) conflates testing with production; (D) is over-engineered and reads as memorised.
9. **B** — Tooling invisible; problem statement begins. (A) and (C) are too far ahead; (D) is wrong category (comp belongs to the recruiter screen).
10. **B** — Karat-employed interviewer (not the hiring company) and recorded by default. Karat is calibrated against itself across multiple sessions and is more rubric-strict than typical in-house screens.

</details>

If under 7, re-read the lecture you missed. If 9+, you're ready for the homework.
