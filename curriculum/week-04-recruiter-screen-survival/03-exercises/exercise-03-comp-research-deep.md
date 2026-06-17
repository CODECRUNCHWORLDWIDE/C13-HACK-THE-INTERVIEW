# Exercise 3 — Comp research deep-dive

**Time:** ~90 minutes. **Output:** A defensible compensation band for each of your top 5 target companies, sourced from levels.fyi and cross-checked against at least one secondary reference, with a high anchor, base case, and walkaway minimum for each.

## Goal

Replace any guesswork in your comp answer with public-data-backed numbers. For each of your five Tier-A targets, produce a band you can defend on a recruiter screen with one sentence of justification. The output is a per-company comp-band table that drops directly into your screen-call cheat sheet.

## Setup

You need:

- Your **five Tier-A targets** from Exercise 2 (same companies, for prep coherence).
- A **target level** for each company. You may target the same nominal level across all five (e.g., "Senior") or different ones if companies use different levelling. levels.fyi's level-mapping page helps when in doubt.
- A **target location** for each company. If you're applying for remote roles, use the recruiter-likely-anchor city (often the company's HQ or a major hub).
- **Browser tabs open** to:
  - <https://www.levels.fyi/> (primary)
  - The relevant company's posted job descriptions on their careers page (for any pay-transparency-required salary ranges).
  - <https://h1bdata.info/> (secondary base-salary cross-check).
  - One of: Glassdoor, salary.com, or the company's Pragmatic Engineer / Blind profile (tertiary cross-check).
- A **markdown file**: `c13-week-04/exercise-03-comp-research.md`.

## Process

### Step 1 — Set the column headers (5 min)

In your draft file, create the comp-band table template. Each row is one company; columns capture the components and the anchors you'll use on the call.

```markdown
## Comp band table — Week 4

| Company | Level | Location | levels.fyi 50th TC | 75th TC | Base 50th | Base 75th | Equity / yr (75th) | Signing (typical) | **High anchor TC** | **Base case TC** | **Walkaway TC** | Source notes |
|---------|-------|----------|---------------------|---------|-----------|-----------|--------------------|-------------------|---------------------|-------------------|------------------|--------------|
| Company 1 | | | | | | | | | | | | |
| Company 2 | | | | | | | | | | | | |
| Company 3 | | | | | | | | | | | | |
| Company 4 | | | | | | | | | | | | |
| Company 5 | | | | | | | | | | | | |
```

(In your editor this will be a wide table; markdown rendering will wrap it. The columns matter; how it renders doesn't.)

### Step 2 — Per-company research (15 min × 5 = 75 min)

For each company, run the following lookups and fill the row.

#### 2a — levels.fyi (8 min per company)

1. Navigate to `levels.fyi/companies/{company-slug}`.
2. Filter by **target level** (use levels.fyi's level mapper if the company uses internal level names you don't know).
3. Filter by **target location**.
4. Note the **median (50th percentile) and 75th percentile** for: Total Comp, Base, Equity (per year), Bonus.
5. If the percentile breakdown isn't shown, scroll to the "All Offers" table and look at the actual data points. Compute the 75th yourself if there are 10+ offers in the filter.
6. Note the **number of data points** in the filter. Fewer than 5 = thin data; flag it and rely more on secondary sources.

Capture in the row:

```
| Company X | Senior (L5 equiv) | San Francisco | $390k | $440k | $200k | $215k | $200k | $40k typical | TBD | TBD | TBD | levels.fyi N=72 in filter, March 2025 |
```

#### 2b — Job posting salary range (4 min per company)

1. Go to the company's careers page.
2. Find an open posting at your target level (or one level adjacent if your exact level isn't posted).
3. **Note any posted salary range.** Many US-state jobs and EU postings now require it. The range may include a wide spread (e.g., $180k-$280k base across multiple levels); narrow to your level if possible.
4. Compare the posted range to levels.fyi's data. They should overlap; if they disagree by more than 20%, dig in (the posted range may include geo / level spread; the levels.fyi may be stale).

Update the row's source notes:

```
... | levels.fyi N=72 in filter, March 2025; JD posted $180-$240 base for Senior in SF
```

#### 2c — Secondary cross-checks (3 min per company)

For *base salary only* — equity is harder to cross-check:

- **h1bdata.info.** Search the company name. The site shows USCIS-disclosed base salaries from H-1B filings. Filter by year and role. Note the typical Senior base.
- **Glassdoor / salary.com.** Spot-check; expect 10-20% downward bias vs. levels.fyi.
- **A Blind thread or Reddit r/cscareerquestions post** if you can find one specific to the company. Anecdotal but useful for sanity-checking.

If the cross-checks agree within ~15% of levels.fyi, your number is well-grounded. If they disagree by more, note the disagreement and use the median of all sources, not levels.fyi alone.

### Step 3 — Set anchors (10 min, after all 5 rows are populated)

For each company, set three numbers:

**High anchor TC.** The number you name on the screen call if asked. Set at the **75th percentile** of your defensible band. This is the number you anchor with. It is *not* the maximum you'd accept; it is the *target* you anchor the negotiation around.

**Base case TC.** The number you'd realistically expect to land at without exceptional leverage. The **60th-65th percentile** range. This is your private estimate of where the offer is likely to come in.

**Walkaway TC.** The number below which you would decline the offer. The **40th-50th percentile**, adjusted for your personal situation (cost of living, current comp, savings runway). Below the 40th and you're being paid less than half of comparable candidates.

Capture in the row:

```
| Company X | ... | **High anchor: $440k** | **Base case: $400k** | **Walkaway: $360k** | ... |
```

### Step 4 — Identify the negotiation lever per company (5 min)

Using Lecture 2, §8's lever table, write a one-line note per company on which lever is most-flexible:

```markdown
## Lever notes

- **Company 1 (FAANG-tier, public):** Equity (RSU grant) is the most-flexible lever. Anchor TC by quoting the grant value, not just base. Base is band-constrained.
- **Company 2 (Series-B startup):** Equity percentage is negotiable; cash often capped. Frame the ask as % equity + base, not pure TC.
- **Company 3 (mid-stage scaleup):** Signing bonus and base are most-flexible. Equity is standard for the level.
- **Company 4 (mature private):** Base + signing. Equity grants are standard, hard to move.
- **Company 5 (FAANG-tier, public, same as Company 1):** Same as Company 1.
```

This shapes *what specifically you ask for* on the call, even when the headline TC is the same.

### Step 5 — Draft the one-sentence justification per company (5 min)

For each company, write the one sentence you'd say on a screen call when asked "what's that number based on?":

```markdown
## Justifications

- **Company 1:** "Based on levels.fyi data for L5 in SF — median TC is around $390k, 75th percentile around $440k; I'm anchoring around the 75th given my five years in payments."
- **Company 2:** "Based on the posted range on the JD, levels.fyi reports for Senior at peer Series-B fintechs, and h1bdata for base — that puts me around ${X} TC."
- ...
```

This is the sentence that converts a number into a *defensible* number. Memorise the structure; you'll vary it per company.

## Acceptance criteria

- [ ] `c13-week-04/exercise-03-comp-research.md` exists.
- [ ] Comp band table contains a row per company, with at least these columns populated: company, level, location, levels.fyi 50th TC, levels.fyi 75th TC, base 50th, base 75th, equity/yr at 75th, signing typical, high anchor, base case, walkaway, source notes.
- [ ] Each row's source notes name at least one cross-check (JD posted range, h1bdata, Glassdoor, or other).
- [ ] Each row has high anchor, base case, and walkaway numbers — three distinct values, with high > base > walkaway.
- [ ] Lever notes section names the most-flexible negotiation lever per company.
- [ ] One-sentence justification per company is drafted and would be deliverable in under 15 seconds on a real call.
- [ ] At least one company in the table has thin data (fewer than 5 levels.fyi data points or wide cross-source disagreement); the row is flagged and the justification accounts for the uncertainty.

## Common mistakes

- **Using the median as the anchor.** You looked up the 50th, named it on the call, and now your maximum is the typical case. Anchor at the 75th.
- **Confusing TC with base.** A recruiter quotes "$300k for this role." Is that base or TC? Always confirm. The screen-call standard is to ask "is that base or total?" when in doubt.
- **Using stale levels.fyi data.** levels.fyi shows the date range of the data points. Comp at most tech companies has shifted meaningfully since 2022. Filter to the last 12-18 months.
- **Trusting Glassdoor as primary.** Glassdoor's self-reporting skews lower than levels.fyi and lower still than reality at FAANG-tier. Use as cross-check, not as primary.
- **Anchoring above your defensible band with no leverage.** You set the anchor at the 95th percentile because you wanted "headroom." The recruiter politely ends the call. The 75th is the ceiling for a screen-call anchor without competing offers.
- **One band for "all companies in tech."** Bands vary 40%+ by company tier (FAANG vs. mid-tier vs. seed) and by location (SF vs. Austin vs. Berlin). One number across five companies is a sign of underprep.

## Stretch

- **Add a sixth and seventh company** at a different stage / location combination — e.g., one Series-A startup and one fully-remote scaleup. Working with the model across stages makes your numbers more stable.
- **Track the deltas.** For each company, note the spread between high anchor and walkaway. A 25% spread is normal; a 50% spread suggests your level mapping is off (you may be looking at two-level-different bands).
- **Build the "what-if" table.** For each company, work out what the offer would look like in each of three scenarios: no negotiation, you anchor and they meet midway, you anchor and they hit your high. The dollar swing across the three is typically $30k-$80k per offer; seeing the table makes the value of the exercise concrete.
- **Read Patrick McKenzie's negotiation essay end to end** if you haven't yet — pair it with this exercise so the comp data feels embedded in the negotiation strategy, not isolated from it.

## Why this matters

Comp is the beat where the largest dollar amounts move in the shortest time on a call. The 90 minutes you spend on this exercise typically returns $20k-$80k on the first offer that comes in, simply because you set the anchor near the top of band instead of the floor. The same prep transfers across all subsequent offers in the cycle (the comp landscape doesn't shift in 12 weeks).

It also matters at the screen-call beat itself. A candidate who answers the comp question with "$400k TC, based on levels.fyi for L5 at SF tech peers and the posted range on your careers page" sounds completely different from "I dunno, maybe like $350? I'm flexible." The first signals seriousness and homework; the second signals neither. Recruiters move the first kind of candidate forward at a higher rate, on the same evidence, *because of how they handle this 90 seconds*.

## Submission

Commit `c13-week-04/exercise-03-comp-research.md` to your portfolio repo. The table and lever notes will be referenced from your screen-call cheat sheet for the rest of the cycle.
