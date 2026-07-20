# Challenge 2 — Funnel projection

**Time:** ~75 minutes. **Difficulty:** Easy/Medium.

## Problem

Build a **funnel model** for your specific cycle. Predict how many offers you should expect from your 30-company list, with **explicit assumptions** you can revisit at the end.

## Output

`challenge-02-funnel-model.md` containing:

1. A table of your 30 companies grouped by tier.
2. For each tier, your estimated conversion rates at each stage:

| | Outreach → recruiter | Recruiter → HM | HM → tech | Tech → onsite | Onsite → offer |
|--|:-:|:-:|:-:|:-:|:-:|
| Tier A | ? | ? | ? | ? | ? |
| Tier B | ? | ? | ? | ? | ? |
| Tier C | ? | ? | ? | ? | ? |

3. The expected offers in each tier, computed.
4. The total expected offers.
5. A 100-word reflection on the most likely *bias* in your estimates.

## How to estimate conversion rates

The numbers in Lecture 1 are averages. Your numbers should reflect:

- **Your level + experience.** Senior candidates convert higher at every stage.
- **Your prep level.** If you're not solid on C2's patterns by Week 4, your tech-screen conversion will be lower than average.
- **Your network.** More referrals = higher early-stage conversion.
- **Industry effects.** A hot market boosts outreach-to-call; a cool market lowers it.

Don't try to be precise. Use round numbers (5%, 10%, 20%, 40%). The point is the *shape*, not the decimal.

## The math

For each company, your expected offer is:

```
P(offer | this company) = P(recruiter | outreach) × P(HM | recruiter) × P(tech | HM)
                                              × P(onsite | tech) × P(offer | onsite)
```

Sum across all 30 companies. That's your expected-offer count.

If your math gives you <2 expected offers, you need either more companies (expand list to 40-50) or better prep (so each stage converts higher).

If your math gives you >10, you're overconfident or your list is unbalanced.

## Acceptance criteria

- [ ] `challenge-02-funnel-model.md` has the table, per-tier conversion estimates, and the computed expected offers.
- [ ] You sanity-check the result against the rough rule from Lecture 2 (10/15/5 list should yield ~5-6 offers at average prep).
- [ ] You identify at least 2 places where you're guessing vs. drawing on data.
- [ ] You commit to **updating this document at Weeks 4, 8, and end-of-cycle** with actual numbers.

## Stretch

- Compute the same numbers assuming 50% better prep (each conversion rate × 1.5, capped at 95%). How many offers do you get?
- Compute the same numbers assuming you do NO outreach beyond cold ATS applications (kill the warm + recruiter-initiated rows). How does the answer change?
- Find someone in the field who's been through a similar cycle. Show them your numbers. Ask which are off.

## Why this matters

Funnel modeling makes the search **legible** to yourself. Without it, you can't tell whether a slow week is "the funnel is on track and I'm impatient" or "the funnel is broken and I should change something." With it, you have receipts.

This document is the single most-useful artifact for the Week-4 retrospective when we revisit how the cycle is actually going.

## Submission

Commit to your portfolio under `c13-week-01/challenge-02/`.
