# Challenge 1 — The Senior-Drift Drill

**Time:** ~1 hour. **Format:** A simulated mid-round event with a structured recovery script. **Prerequisite:** Lectures 1-3.

## What this challenge is for

The single most-common round-derailing event for a new-grad or L4 candidate in a design round is what we call "senior drift" — the interviewer asks a question that pushes the design above the candidate's level. Common forms:

- "What happens when the entire region goes down?"
- "How do you handle the case where two writers commit conflicting updates at exactly the same time?"
- "Walk me through your capacity planning model for the third quarter after a major product launch."
- "What's the consistency guarantee you're offering, in terms of the CAP theorem?"
- "If you had to operate this for the next five years across three new regulatory jurisdictions, what changes?"

Each of these is a senior-level question. None of them is a fair question to a new-grad candidate cold. But interviewers ask them — sometimes by accident (they have not internalised that the candidate is at the new-grad bar), sometimes by design (they want to see how the candidate handles being above their depth), and sometimes by promotion (the company is hiring you at a level above what they advertised and is informally probing your ceiling).

The strong move when this happens is **not** to bluff your way through. The strong move is to surface the level shift audibly and either (a) say what you know honestly and admit the gap, or (b) propose a partial answer at your level and offer to take the senior question as a follow-up. Both protect the round. Both score positively in the debrief. Bluffing — pretending to know the answer to a CAP-theorem trade-off you have not internalised — is the failure mode this challenge inoculates you against.

## The challenge

Run the following script with a peer, or alone if no peer is available. The peer plays the interviewer. You are mid-design-round, ~20 minutes in, on the URL shortener prompt.

### Round 1 — The interviewer asks a senior question

Peer (interviewer): pick one of these to ask, mid-deep-dive:

1. "Walk me through what happens if the entire us-east region goes down for an hour. How does the service degrade, and how does it recover?"
2. "You said you'd use Postgres. Walk me through how the write throughput holds up at 10x scale — say, 1 billion URLs per day — including the replication topology and the failover behaviour during a primary outage."
3. "Tell me about the CAP-theorem trade-off you've made. Specifically: under a network partition, would you prefer to remain available and accept stale data, or remain consistent and reject writes?"
4. "How would you instrument this service to detect a 5% drop in cache hit rate within 90 seconds, and what would your runbook be when that alert fires?"
5. "Imagine a regulatory requirement appears that says every URL must be tied to a verified human identity and the verification record must be auditable for seven years. What changes in the design?"

You (candidate): you have 4 minutes to respond. Run the response on one of the four templates below.

### The four response templates

**Template A: I know the answer at my level; here it is.**

> "That's a good question. At the level I've designed for so far, the answer is [partial answer at the L3/L4 depth]. There's a deeper version — [name what the deeper version is] — but I'd be more careful answering it than I have time for here. Should we save it for the trade-offs phase, or do you want me to take a shot now?"

The interviewer almost always says "your call" or "save it for trade-offs." Either way you have surfaced the level shift, given an honest partial answer, and protected the round.

**Template B: I have heard of the concept but cannot articulate the trade-off in depth.**

> "I know the concept — [name it: 'cross-region failover', 'CAP', 'observability', 'compliance retention'] — but I've not designed at the depth where the trade-offs feel concrete to me. The high-level shape of the answer would be [10-15 second sketch of what you'd do, defensibly]. I'd want to be more careful about [the specific thing that gets hard] than I can be in 4 minutes. Happy to take it as a follow-up after the round."

This is the honesty move. The interviewer's debrief writeup will note "candidate calibrated their own depth correctly under pressure; surfaced an honest gap without losing composure." That is a positive signal.

**Template C: I have not heard of the specific concept the question depends on.**

> "I'm not sure I follow the specific question — could you walk me through what you mean by [the term that confused you]? I want to make sure I'm responding to what you actually asked rather than guessing."

The interviewer either rephrases or backs off. Either is fine. Asking for a re-explanation is not weakness; bluffing through a question you didn't understand is.

**Template D: The question is above my level, full stop.**

> "That's a senior-level question — multi-region failure handling at scale is a real specialisation. At my level, I haven't designed for that. I can tell you what the high-level shape of a senior answer would include — [3 bullet points] — but I'd be guessing at the depth. Should we move on?"

Saying "that is a senior question" directly is occasionally the right move, especially if the interviewer is genuinely drifting and didn't realise they had drifted. Most interviewers will calibrate down and return to a level-appropriate question.

### Run all five questions

Run all five senior-drift questions in succession. Pick a different response template for each (do not use the same one twice). The goal is to have all four templates rehearsed; the fifth question lets you pick whichever fits.

After each, the peer (interviewer) gives 30 seconds of feedback:

- Did you surface the level shift, or did you bluff?
- Did the honest partial answer protect the round, or did it collapse the round?
- Did the response template feel natural, or scripted?
- Was the proposed follow-up ("save it for trade-offs") appropriate?

Score yourself: 5 questions × the four template options means you should be able to handle any of them on Friday. If two or more questions trapped you into bluffing, rerun the next day before the round.

### Solo variant

No peer? Run the same exercise with a timer and a written response. Set a 4-minute timer; type the response. After the timer, read it back and ask:

- Did I bluff?
- Did I surface the level shift?
- Would I be comfortable saying this out loud in a real round?
- Would a senior engineer reading this respect the calibration?

The solo variant is weaker than the peer variant because the social pressure of saying it out loud is the variable being trained. If you can find a peer for even 30 minutes, do.

## Why this matters

The debrief writeup after a real round will sometimes contain a line like: "Candidate was pushed above their level on the region-failure question; handled it honestly and produced a clear partial answer; calibrated well." This line is a positive signal even when the question itself was not answered well. Hiring panels weight calibration heavily; the candidate who knows the limit of their own knowledge is, paradoxically, more valuable than the candidate who claims to know everything.

The opposite line in the writeup is: "Candidate bluffed on the CAP-theorem question; said things that don't quite hang together; appeared to be reasoning live rather than from preparation." This is a lean-no-hire signal even when the rest of the round was strong.

The first language ("Candidate calibrated well") is what this challenge produces. The four response templates are the muscle.

## Acceptance criteria

- You ran all five senior-drift questions with a peer (or wrote five typed responses solo).
- For each, you produced a response that did not bluff.
- You used at least three of the four response templates across the five questions.
- The peer feedback (or your own self-eval) noted "did not bluff" for at least four of the five.
- You can now recite the four templates from memory.

## Common failure modes

1. **Bluffed on the CAP-theorem question.** Said something that sounded technical but did not hang together. The peer caught it. Fix: Template B for any concept you have heard of but cannot articulate fully.
2. **Collapsed and said "I don't know" without proposing anything.** This is too defensive; you have *something* to say at your level. Fix: Template A with the partial answer.
3. **Used Template C on a question you understood but didn't want to answer.** The interviewer will see through this. Fix: only use Template C when you genuinely don't understand the terms.
4. **Surfaced the level shift but in a self-deprecating way.** "Oh, I'm just a new grad, I haven't done that" is not the calibrated move; it lowers your evaluation. Fix: matter-of-fact, not apologetic. "That's a senior question; at my level, here's what I can answer."

## What to carry forward

The four templates fit on a small notecard. Carry it into the next real round. When a senior question lands, glance at the card, pick the template, run the response. The 4-minute response is enough; the rest of the round continues.

After the round (in the after-action template from Week 7, Challenge 2), log:

- Did the interviewer ask a senior-drift question?
- Which template did I use?
- How did I think the response landed?

Over several rounds, the template-usage data tells you which kind of senior-drift question you handle worst. That is the gap to close in your next prep cycle.
