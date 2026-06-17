# Lecture 2 — Funnel Math + Target Lists

> **Duration:** ~2 hours. **Outcome:** You can model your own funnel, build a tiered 30-company target list, and explain why "I'll just apply to 200 places" is the wrong shape.

## 1. Why funnel math beats "apply to everything"

The two failure modes of inexperienced job-seekers:

**Failure A — Spray and pray.** Apply to 200 random companies. Get 4 calls. Tank 3 because you didn't prepare for them specifically. End with one offer at a company you didn't really want.

**Failure B — Underfunneling.** Apply to 5 companies you care deeply about. Run perfect processes. End with one offer at the wrong comp because you have no leverage.

Both fail because they don't think about the funnel as a *portfolio* — and like any portfolio, the goal is to optimize across multiple positions with different risk profiles.

The right shape: **30 companies, tiered, run in parallel, with deliberate effort allocation per tier.**

## 2. The 30-company target list

Borrowed (with adaptation) from college admissions: divide your target companies into three tiers.

### Tier A — Reaches (10 companies)

Your dream companies. Compensation is at the top of your band. Bar is high. Realistic-but-stretching.

- Examples: FAANG-tier, major financial / quant firms, Series-D unicorns at fair valuations, top-tier startups.
- Expected outcome: 1-3 offers from this tier if you run a tight process.

### Tier B — Matches (15 companies)

Companies where you'd be a great fit and they'd plausibly want you. Comp meets your floor, role is interesting, leveling is appropriate.

- Examples: Series-B startups, mid-size tech companies, large enterprises, well-funded crypto/AI/biotech firms (if those are aligned with your goals).
- Expected outcome: 3-6 offers from this tier.

### Tier C — Safeties (5 companies)

Real options that you'd take if you couldn't land Tier A or B. **Critically: not "low-quality companies" — companies you would actually accept.** A "safety" you wouldn't accept is not a safety; it's clutter.

- Examples: smaller startups in your geography, established enterprises with reasonable comp, contract-to-hire roles.
- Expected outcome: 2-4 offers from this tier.

### Why 30 specifically

Fewer than 30 and you don't have funnel volume. More than 30 and you can't keep up with the conversations seriously.

The number scales by experience level:
- Junior / new-grad: 30-50 companies (more volume, lower conversion).
- Mid-level: 20-30.
- Senior+: 15-25 (high conversion, less volume needed).

## 3. How to build the list

Three sources, weighted:

### Source A — People who already work there

Open LinkedIn. Search "engineers at $company" for companies you might want to work at. **If you don't know anyone there or one degree away, that company is a harder funnel-entry**, not impossible.

Aim for **8-12 of your 30** to be companies where you have a 1st- or 2nd-degree connection. These are the warmest pipeline entries.

### Source B — Companies hiring publicly

The "Who's Hiring?" Hacker News thread (first weekday of every month). Wellfound. Each company's own careers page. LinkedIn job alerts. Filter to ones whose roles match your level + location preferences.

Aim for **15-20 of your 30** from this layer.

### Source C — Reverse-engineered targets

Companies you DON'T know are hiring, but you want to work at. Often you can:
- Find a recruiter on LinkedIn who works at that company; reach out.
- Identify the hiring manager from public talks / blog posts.
- Watch for them on the next Who's Hiring.

Aim for **3-5 of your 30** here. Slow burn, high reward if it lands.

## 4. The columns of your spreadsheet

By the end of Week 1, your tracking spreadsheet has these columns (you'll build this in the mini-project):

| Column | Type | Why |
|--------|------|-----|
| Company | text | Self-explanatory |
| Tier | A / B / C | Forces honesty |
| First-degree contact? | bool | Whom do I know |
| Source | "HN / referral / LinkedIn / cold" | Tracking what works |
| Role | text | Each company has a specific opening |
| Comp band (researched, range) | numeric | From levels.fyi or similar |
| Stage | enum | "Not started / outreach sent / recruiter screen / HM screen / tech screen / onsite / offer / closed-lost / closed-won" |
| Stage entered date | date | For funnel-time analysis |
| Last contact date | date | When did I last talk to them? |
| Next action | text | "Reply to recruiter by Tuesday" |
| Notes | longtext | What did we discuss |

Update this **after every interaction**. Future-you reviewing it in week 8 will be grateful.

## 5. Funnel math with your actual list

Once your list has 30 entries, project the funnel:

| Tier | Companies | Expected offers (assumes good preparation) |
|------|----------:|-------------------------------------------:|
| A | 10 | 1.0 (10% of reaches yield) |
| B | 15 | 3.0 (20% of matches yield) |
| C | 5 | 1.5 (30% of safeties yield) |
| **Total** | **30** | **~5-6 expected offers** |

The point of having multiple offers is **leverage in negotiation**. Even 2 competing offers radically change the math; 4-5 changes it more.

These percentages assume:
- You actually run the process on each (not just apply).
- You prepare for the tech screens (do C2 in parallel).
- You don't tank the behavioral round.

If you get 0 offers across 30, that's a *prep* problem, not a *funnel* problem. Honest diagnostic in Week 9.

## 6. Time budget

Running 30 conversations is a part-time job. Reasonable allocation across 10 weeks:

| Activity | hrs / wk |
|----------|---------:|
| Outreach (sending messages, following up) | 4-6 |
| Recruiter screens (the actual calls) | 2-3 (varies by week) |
| Tech screens and onsites | 4-8 (varies hugely by week) |
| Preparation (C2 study, behavioral rehearsal) | 6-10 |
| Spreadsheet maintenance + notes | 1-2 |
| **Total** | **~17-30** |

Most weeks: 17-20. The week of a real onsite: 30+.

## 7. Self-check

- Why is 30 the recommended target-list size?
- What's the difference between a Tier-A and a Tier-C company, in *your* definition?
- A friend says "I'll just spray 200 LinkedIn applications." What's wrong with that approach?
- How many of your 30 should ideally have a 1st-degree contact?
- A recruiter from a Tier-A company emailed you cold. What's the conversion math telling you about that lead vs. a Tier-A you cold-applied to?

## Further reading

- **Levels.fyi — "How to negotiate your tech salary":** <https://www.levels.fyi/blog/how-to-negotiate-tech-salary>
- **Patrick McKenzie — "Don't Call Yourself a Programmer":** <https://www.kalzumeus.com/2011/10/28/dont-call-yourself-a-programmer/>
- **Cal Newport — "So Good They Can't Ignore You"** (the "career capital" framing — relevant for picking which jobs to target).
