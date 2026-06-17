# Exercise 2 — Why this company

**Time:** ~90 minutes. **Output:** A three-reason "why this company?" answer for each of your five Tier-A targets, each at the level of specificity described in Lecture 1 §5.

## Goal

Produce five drafted answers, one per Tier-A target, each containing three concrete reasons that pass the "could-this-be-said-about-any-other-company" test. The output is a per-company section in a single markdown file, ready to drop into your screen-call cheat sheet.

## Setup

You need:

- Your **Tier-A target list** from Week 1's mini-project. Pull the top 5 by your current priority order — the companies you'd most want to be screening with in the next 4 weeks.
- **Open tabs**: each target's company website, engineering blog, careers page, and LinkedIn page.
- A **markdown file**: `c13-week-04/exercise-02-why-this-company.md`.
- ~20 minutes of focused research time per company × 5 = ~100 minutes total. (You may finish faster on familiar companies and slower on new ones.)

If you have fewer than 5 Tier-A targets, do this exercise for whatever you have and add the rest as you build the target list out.

## Process

### Step 1 — Pick the five (5 min)

In your draft file, list the five companies you're prepping. For each, note one line on *why this company is on your Tier-A list* — the same answer you wrote in Week 1's target-list exercise. This is the *internal* answer; you're about to write the *recruiter-facing* answer.

```markdown
## Tier-A targets for this prep

1. **{Company 1}** — {one-line: why they're on your Tier-A list}.
2. **{Company 2}** — ...
3. **{Company 3}** — ...
4. **{Company 4}** — ...
5. **{Company 5}** — ...
```

### Step 2 — Per-company research (15 min × 5 = 75 min)

For each company, run the 20-minute research budget from Lecture 1, §5:

```markdown
### {Company N} — research notes

**5 min — engineering blog / public technical content.**
- Most recent 2-3 posts: [titles + 1-line summaries].
- The one I can speak to in detail: [pick one; 2-3 sentences on what it covers and why it's relevant to you].

**5 min — stage and shape.**
- Stage: {Series X / public / private mature / etc.}.
- Engineering headcount estimate: ~{N} (source: LinkedIn employee count, Pragmatic Engineer post, public reports).
- Business shape: {what they sell, to whom, primary product surface}.
- One-sentence stage description: [your own words, the way you'd say it on a call].

**5 min — people / team signal.**
- Engineers I'd notice: {Name + role + why noteworthy — talk given, open-source repo maintained, blog post, etc.}.
- Anything specific about the team you'd be joining: [if findable; otherwise note "team not visible from outside, ask on the call"].
- Any open-source or public-output you've actually engaged with: [be honest — if the answer is "none yet," write that].

**5 min — draft the three-reason answer.**
[See Step 3 below.]
```

A few research notes:

- **Engineering blogs.** Almost every tech company over ~50 engineers has one. Search `{company name} engineering blog` or check `eng.{company-domain}` / `engineering.{company-domain}` / `{company-domain}/blog/engineering`. If the company has no engineering blog, that itself is information; pivot Reason 1 to a product or technical detail you can speak to from public docs.
- **Stage.** Crunchbase free tier shows last round / size. LinkedIn employee count is a rough engineer-count proxy (engineering is typically 30-60% of total headcount at tech companies).
- **People signal.** Search "{company} engineering" on YouTube for conference talks. Check the company's GitHub org for active maintainers. If a senior engineer there has a public profile (blog, Twitter / X, GitHub), spend 2 minutes reading their recent output.

### Step 3 — Draft the three-reason answer (per company, inside the 15-min budget)

Using the structure from Lecture 1, §5:

```markdown
### {Company N} — "Why this company?" — draft

**Reason 1 — Product or technical specifics:**
> [Spoken-style sentence naming a specific artifact (blog post, open-source release, technical decision) and why it draws you in. 20-40 seconds spoken; 50-80 words.]

**Reason 2 — Stage / scope / business-shape fit:**
> [Spoken-style sentence on the kind of company they are (stage, size, business model) and why that fits where you want to be. 20-40 seconds.]

**Reason 3 — Specific person or team signal (optional):**
> [Spoken-style sentence on a named person, team, or visible output that drew you in. Skip if no honest signal exists; substitute a fourth product / business specific reason instead.]

**Total estimated spoken time:** ~90-120 sec.
**Specificity test:** Could every reason here apply to a different company by changing one word? (If yes, rewrite.)
```

### Step 4 — Specificity audit (10 min, after all 5 are drafted)

Once you have five drafted answers, sit with all of them open. Audit each:

For each reason in each company's draft, ask: **could a recruiter at a different company (one you didn't research) hear this answer with their company's name substituted, and not notice the substitution?**

- "Your engineering blog post on the new ledger architecture" → if you substitute "your engineering blog post on the new $thing," the substitution is obvious. **Passes.**
- "I really admire the technical culture there" → substitute "I really admire the technical culture at $any-company." **Fails.** Rewrite.
- "Your stage — Series B, ~80 engineers, payments as the core product" → reasonably specific; passes for *this* set of companies but is generic across the Series-B-fintech category. **Borderline; consider sharpening.**

The audit should produce 0-3 rewrites per company. After rewrites, none of the three reasons in any of the five drafts should fail the substitution test.

## Acceptance criteria

- [ ] `c13-week-04/exercise-02-why-this-company.md` exists.
- [ ] Five Tier-A targets listed with their internal one-line rationale.
- [ ] For each of the five, research notes include:
  - At least one engineering blog post or public technical artifact, by name.
  - A stage / size description in your own words.
  - At least one person, team, or output signal — or an honest "none yet" with a substitute.
- [ ] For each of the five, a three-reason answer is drafted (Reasons 1, 2, 3) in spoken-style prose.
- [ ] Each three-reason answer is 50-150 words per reason, 90-120 seconds total spoken time.
- [ ] Specificity audit passed: every reason in every draft survives the company-name-substitution test.
- [ ] The five drafts are formatted so you can drop the answer for whichever company calls you into your screen-call cheat sheet without further editing.

## Common mistakes

- **The "you're doing exciting work" answer.** Every variant of "I'm really excited about what you're building" / "your work is impressive" / "I admire your engineering culture" reads as zero homework. The recruiter has heard each of these phrases 500 times. Replace with a *specific* sentence about a specific thing they built.
- **The single-axis answer.** Three reasons all about the same dimension (e.g., all three are "I like your engineering blog"). Diversify across product, stage/business, and people/team.
- **The "great culture" reason.** "Your culture seems great" — unverifiable, generic. Either name a specific culture artifact (a published values doc, an engineering-team interview podcast, a Glassdoor pattern you noticed) or drop the reason.
- **The fabricated person signal.** Claiming you watched a talk you haven't watched. Recruiters who work closely with their engineers can spot this immediately. Honest "I noticed the team's open-source release of X" beats fabricated "I really admire $engineer's work."
- **Researching for 60 minutes per company.** The 15-minute budget per company is calibrated. The point is *targeted* prep, not exhaustive. Set a timer.

## Stretch

- **Sixth and seventh.** Add two more companies from your Tier-B list — the next batch you expect to engage with. Same structure.
- **The level-specific reason.** For each company, identify what the specific level you're targeting (Senior, Staff, etc.) entails at that company specifically. A "Senior at Stripe" is shaped differently from "Senior at Acme"; if you can speak to that difference in Reason 2, it lands harder.
- **The decline-graceful version.** Draft a one-sentence answer to "and what about us makes this *not* a fit?" — the harder follow-up some recruiters use. Honest, brief, named.
- **The reverse exercise.** For one of the five companies, write the three-reason answer you'd give *if you were not at all interested*. Compare the two drafts; the diff is exactly what specificity feels like.

## Why this matters

The "why this company" answer is the highest-leverage beat after the self-intro. It is also the beat most candidates underprep, because they think company research is fungible. It is not. The recruiter is scoring you against a candidate pool where 80% gave a generic answer and 20% gave a specific one. The specific 20% move forward at a higher rate, and the recruiter remembers them at offer time.

The 90-minute time cost for this exercise pays back across the entire cycle. The five drafts are reusable for as long as those companies remain on your target list, and the structure transfers verbatim to companies 6-30 with diminishing per-company prep time (10 minutes by the tenth company, because you'll have internalised the pattern).

## Submission

Commit `c13-week-04/exercise-02-why-this-company.md` to your portfolio repo. The five drafts will be referenced from your screen-call cheat sheet for the rest of the cycle.
