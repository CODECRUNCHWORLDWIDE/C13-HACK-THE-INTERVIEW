# Exercise 2 — Rewrite five bullets

**Time:** ~90 minutes. **Output:** Five bullets rewritten from duties-shape into STAR+R, with the before / after / what-changed annotated.

## Goal

Take the five **weakest** bullets from your current resume and rewrite each into a STAR+R bullet with a quantified result. The before/after comparison teaches the pattern; once you can do five, you can do twenty.

## Process

### Step 1 — Inventory all your bullets (10 min)

In `c13-week-02/exercise-02-bullet-rewrites.md`, paste every bullet from your `resume-v1.pdf`. Number them. (Roughly 12-20 total.)

Count them. Note the total at the top of the file.

### Step 2 — Score the number-density of v1 (5 min)

For each bullet, mark whether it contains **at least one quantified result that represents a real measurement** (a number with a unit or a comparable baseline; not "many" or "several" or "a lot").

Compute: `(bullets-with-numbers / total-bullets) * 100`. Write the percentage at the top of the file.

If you're at <40%, that's your gap to close. If you're already at 60%+, this exercise will be a polish pass; pick the five weakest anyway.

### Step 3 — Identify the five weakest (10 min)

Mark each bullet with a tag from Lecture 2, §2:

- **A**: starts with "Responsible for"
- **B**: starts with "Worked on"
- **C**: starts with "Helped"
- **D**: starts with "Participated in"
- **E**: job-description paste (buzzwords, no specifics)
- **F**: any other weak verb or no quantified result

The five with the most antipattern signal are your rewrite targets. If you have more than five duties bullets, pick the five whose underlying achievements you remember most clearly — easier to rewrite when you remember the work.

### Step 4 — Rewrite each one (60 min — ~12 min per bullet)

For each of the five, in your file write:

```
## Bullet 1

**Before:**
> Responsible for the company's data ingestion pipeline.

**Antipattern tag:** A (Responsible for)

**What I actually did (free-form notes):**
- It was ingesting ~3M events/day from Kinesis into Snowflake.
- I rewrote the dedup logic; we'd had ~2% duplicate row rate.
- After my rewrite, dupe rate went to ~0.02%.
- Also cut the per-event cost from $0.0008 to $0.0003.

**After:**
> Rewrote the deduplication layer of the data ingestion pipeline (3M events/day from Kinesis to Snowflake), reducing the duplicate-row rate from 2% to 0.02% and per-event cost from $0.0008 to $0.0003.

**What changed:**
- Verb: "Responsible for" → "Rewrote" (specific, past-tense, active).
- Specifics: named the source (Kinesis), destination (Snowflake), magnitude (3M/day).
- Quantified result, twice: dupe rate AND cost.
- One bullet, one sentence, two numbers.
```

Repeat for all five.

### Step 5 — Score the v2 number-density (5 min)

Of your five new bullets, count how many have at least one real quantified result. Five out of five is the goal. If any are weak (no honest number available), the bullet may not be worth rewriting — go back to Step 3 and pick a different one.

Then *project*: if you applied this rewrite pattern across your whole resume, what would your overall number-density be? Write the projection.

## Acceptance criteria

- [ ] `c13-week-02/exercise-02-bullet-rewrites.md` exists.
- [ ] Total bullet count and v1 number-density percentage at the top.
- [ ] Five bullets, each with Before / Antipattern tag / Notes / After / What-changed sections.
- [ ] Every "After" bullet:
  - Past tense (unless the action is genuinely ongoing in your current role).
  - Active voice.
  - Starts with a strong verb (not Responsible / Worked / Helped / Participated / Assisted).
  - Contains at least one quantified result.
  - Fits in 1-2 lines (~12-22 words).
- [ ] A "Projected v2 number-density" line at the bottom.

## Common mistakes

- **Invented numbers.** "Improved performance by 1000%." If you don't remember the actual magnitude, ask your old manager or use a defensible range ("roughly 3x"). Inventing is worse than not quantifying.
- **Credit-stealing.** "Led the platform migration" when you owned 1 of 5 services. Be precise about your slice.
- **"We" hiding inside a bullet.** "Migrated to Kubernetes" with no mention of what you specifically did → rewrite to name your contribution.
- **The 30-word bullet.** If your rewrite is 3 lines long, you're stuffing two bullets into one. Split.
- **Vague magnitudes.** "Significantly improved latency" → no. Be exact or pick a different bullet.

## Stretch

- Rewrite **all** your duties bullets, not just five. Most candidates have 8-12; the full pass takes ~3 hours.
- Have a peer review your five. Ask them: "what number in each bullet do you doubt, and why?" Replace the doubtful numbers with ones you can defend.
- Read three resumes from senior engineers at your Tier-A companies (LinkedIn profiles, public portfolios). Note which bullets stand out and why.

## Why this matters

The bullets are the load-bearing content of the resume. The header, the section structure, the font choices — all of those determine whether the document gets *parsed*. The bullets determine whether you get *interviewed*. A clean-parsing duties-heavy resume still gets passed over; a clean-parsing outcome-heavy resume converts.

## Submission

Commit `c13-week-02/exercise-02-bullet-rewrites.md` to your portfolio repo.
