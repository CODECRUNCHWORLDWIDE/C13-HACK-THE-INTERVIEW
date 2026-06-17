# Lecture 2 — Bullets: From Duties to Outcomes

> **Duration:** ~2 hours. **Outcome:** You can spot a duties-shaped bullet, rewrite it as STAR+R with a quantified result, hit the 40% number-density target, and apply consistent tense and voice across the whole document.

## 1. Why most bullets are wasted lines

Open ten engineering resumes at random. You'll see lines like these:

> - Responsible for backend services
> - Worked on the payment system
> - Helped improve the platform's performance
> - Participated in code reviews
> - Contributed to the migration from monolith to microservices

These are **duties bullets**. They describe the *scope* of your job, not what you *did inside the scope*. They communicate nothing a recruiter or hiring manager doesn't already infer from your title.

A senior engineer at a payments company was "responsible for backend services." Of course they were. That's what the title means. The line burns a row of vertical space and tells the reader nothing.

The fix: **every bullet must answer the question "what happened because you were there?"** If you can replace yourself with any other engineer at the same level and the bullet remains true, the bullet is a duties bullet and should be cut or rewritten.

## 2. The duties-bullet antipattern, in detail

The duties bullet has a few characteristic shapes. Learn to recognize them on sight.

### Shape A — "Responsible for X"

> - Responsible for designing and implementing REST APIs.

Translation: "I had a job description that said I'd build APIs." OK. What APIs? How many? Did they work? Were they fast? Did anyone use them?

### Shape B — "Worked on X"

> - Worked on the search team's indexing service.

Translation: "I was on a team that did indexing." What did *you* do? What did *you* improve? What did *you* ship?

### Shape C — "Helped X"

> - Helped reduce the build time of our CI pipeline.

Translation: "Someone on my team did a thing. I was on the team." If you did it, say so. If you contributed a piece, name the piece.

### Shape D — "Participated in X"

> - Participated in design reviews, on-call rotations, and architecture discussions.

Translation: "I showed up to meetings I was invited to." Everyone at your level did this. Cut.

### Shape E — The job-description paste

> - Designed, developed, and deployed scalable, maintainable, high-performance distributed systems using Python, Go, and Kubernetes.

Translation: I copied my employer's career-page boilerplate. The buzzwords are present; the substance is not. Recruiter scrolls.

**Spot-check:** if your bullet starts with *Responsible*, *Worked*, *Helped*, *Participated*, *Assisted*, or *Contributed*, it's almost certainly a duties bullet. Rewrite or cut.

## 3. STAR+R: the bullet structure that works

Borrowed from behavioral-interview convention, adapted for resumes:

- **S — Situation.** The context. (Often implicit from the job, so omit unless it adds signal.)
- **T — Task.** What needed to happen.
- **A — Action.** What you specifically did.
- **R — Result.** The outcome, in numbers.
- **+R** — the second R: the **quantified result**. The number that makes the bullet load-bearing.

In practice, a resume bullet compresses STAR+R into one sentence, with the Result-with-number leading or anchoring it. The format roughly:

```
[Verb in past tense] [specific action] [with specific tool/method],
   [result with a number].
```

### Examples — duties to outcomes

**Before (duties):**
> - Responsible for improving the performance of the search service.

**After (STAR+R):**
> - Reduced search service p99 latency from 1.4s to 220ms (84%) by replacing the regex-based query parser with a precompiled state machine.

What's load-bearing in the rewrite:

- **The verb** is past tense and specific: *Reduced*, not *Improved*.
- **The number** is concrete and contains a *before* and *after*: 1.4s → 220ms.
- **The mechanism** is named: regex parser → precompiled state machine. A reader can imagine the work.
- **The magnitude** is in there twice: the absolute (1.4s to 220ms) and the percent (84%). Magnitude is worth re-stating.

**Before:**
> - Worked on the CI/CD pipeline.

**After:**
> - Cut CI pipeline duration from 22 minutes to 6 minutes by parallelizing the test matrix across 8 runners and caching the Docker layer build, saving ~280 engineer-hours/month across the 40-person team.

**Before:**
> - Helped migrate the monolith to microservices.

**After:**
> - Led the extraction of the billing service from the monolith into a standalone Go service over 4 months, eliminating 60% of cross-team deploy blockers and reducing average deploy time from 38 minutes to 9.

**Before:**
> - Participated in code reviews and design discussions.

**After (or cut):**
> - Reviewed ~200 PRs in 2024, including 3 design docs for the new pricing engine; identified the race condition in the cache invalidation path that would have caused stale-price reads at scale.

(If you can't construct an outcome bullet from "participated in code reviews," cut the bullet.)

## 4. Where the numbers come from

The most common objection: "but my work isn't measurable." It usually is — you just haven't measured it.

Sources of numbers, in rough order of strength:

### A — Performance and reliability

- **Latency:** before/after p50, p95, p99. (1.4s → 220ms.)
- **Throughput:** requests/second, items/hour, MB/sec. (50k rps → 180k rps.)
- **Error rate:** percent of failed requests; percent reduction in error rate. (0.7% → 0.05%.)
- **Uptime / availability:** "raised availability from 99.5% to 99.95%."
- **Resource consumption:** CPU, memory, cost. ("Cut Lambda cost from $4,200/mo to $900/mo.")

### B — Engineering efficiency

- **Build / CI time:** ("CI from 22min to 6min.")
- **Deploy frequency / cycle time:** ("From weekly to 4×/day.")
- **Time to first PR for new hires.** ("Reduced onboarding ramp from 5 weeks to 12 days.")
- **Test coverage:** ("From 34% to 78%.")
- **Bug recurrence rate** or **mean time to recovery (MTTR).** ("MTTR from 47min to 8min on the auth subsystem.")

### C — Business / product

- **User adoption:** ("Feature reached 40% of MAU in 6 weeks.")
- **Revenue impact:** ("Pricing experiment increased ARPU by 11%.")
- **Cost saved:** ("Right-sized our RDS fleet, saving $18k/month.")
- **Churn / retention:** ("Reduced D7 churn from 14% to 9%.")
- **Conversion:** ("Lifted checkout completion from 71% to 79%.")

### D — Team / scope

- **People impact:** ("Mentored 3 junior engineers through their L3 promotions.")
- **Project scope:** ("Owned the rewrite of a service handling 12M req/day.")
- **Cross-team coordination:** ("Drove a 5-team migration over 7 months.")

### E — If all else fails: counts and timeframes

- "Shipped 4 production services in 18 months."
- "Reviewed 200+ PRs in 2024."
- "Led 6 design reviews; 5 went to production."

These are weaker than performance / business numbers, but they beat zero numbers.

## 5. When you don't have numbers — what to do

You worked on a project and you genuinely don't know what changed. Three legitimate moves:

1. **Ask.** Slack your old manager or teammate: "I'm updating my resume — do you remember the rough magnitude of the latency improvement on the search rewrite?" Most people will tell you.
2. **Reconstruct.** You don't need a perfect number. You need an honest order-of-magnitude. "About a 3x improvement" is fine if you remember it was somewhere between 2x and 5x. "Roughly 100k users" is fine if you remember it was tens or hundreds of thousands.
3. **Cut.** If you genuinely can't construct any honest number for a bullet, the bullet probably wasn't worth including. Use the line for a different accomplishment that *is* measurable.

**Do not invent numbers.** A senior engineer interviewing you will sniff out invented metrics in 30 seconds. ("Increased system performance by 200%" — by what measure? on which workload? compared to what baseline?) Vague numbers are worse than no numbers.

## 6. The number-density target: ≥40%

Across your full resume, **at least 40% of bullets should contain a quantified result.** A typical mid-level resume with 4-5 jobs and 3-4 bullets each has 15-20 bullets total; 6-8 of those should have a number.

Why 40%? Because:

- **Below 30%**: the resume reads as duties-heavy. The recruiter doesn't see signal.
- **40-60%**: ideal. Quantified-where-it-matters, qualitative-where-quantifying-would-be-forced.
- **Above 80%**: starts to read as performative ("Increased team happiness by 25%" — no you didn't). Numbers everywhere stop carrying weight.

**Audit your own resume.** Count total bullets. Count bullets with at least one number that represents a real measurement. Compute the ratio. If it's <40%, the bullets to rewrite are the ones with the weakest verbs ("worked on," "helped," "participated").

Exercise 2 walks you through exactly this audit.

## 7. Tense and voice

### Tense

- **Past roles: past tense.** "Reduced," "shipped," "led," "built."
- **Current role: present tense for ongoing work, past tense for completed achievements.**
  - Ongoing: "Lead the platform-infra team of 6 engineers."
  - Completed: "Cut deploy time from 38 minutes to 9 minutes in Q1 2026."

The most common error: writing past-tense bullets for your current role. "Led the team" reads as if you no longer do; "Lead the team" or "Leading the team" is correct. Match the verb tense to whether the action is ongoing.

### Voice

- **Active voice always.** "Reduced latency by 40%." Not "Latency was reduced by 40%."
- **You are the subject of every bullet.** "Led the migration." Not "The migration was led."
- **No "I" — implied subject.** "Designed the indexing service." (Not "I designed the indexing service.")
- **No "we" — when it's "we," say which part you did.** Not "We migrated the platform to Kubernetes" — but "Designed and implemented the autoscaler component of the platform's K8s migration; the full migration spanned 4 engineers over 6 months."

The "we" rule has bite. A bullet that hides your specific contribution behind a team accomplishment is unfalsifiable and reads as such. Hiring managers ask: "what part did *you* do?" — and if your bullet doesn't answer, you've wasted the line.

## 8. Verbs that work, verbs that don't

### Strong verbs (use these)

For building: **Built**, **Designed**, **Architected**, **Implemented**, **Shipped**, **Launched**, **Deployed**.

For improving: **Reduced**, **Cut**, **Increased**, **Raised**, **Optimized**, **Streamlined**, **Refactored**.

For leading: **Led**, **Owned**, **Drove**, **Coordinated**, **Mentored**.

For investigating: **Diagnosed**, **Identified**, **Debugged**, **Root-caused**.

For shipping: **Released**, **Rolled out**, **Migrated**, **Rewrote**.

### Weak verbs (rewrite or cut)

- **Responsible for** — duties. Always rewrite.
- **Worked on** — vague. Always rewrite.
- **Helped** — minimizes your contribution. Always rewrite.
- **Participated** — passive. Always rewrite.
- **Assisted** — same.
- **Contributed to** — vague unless followed by the specific contribution.
- **Used** — "Used Python to..." Cut the prefix; lead with what you did.
- **Was involved in** — every word is filler.
- **Engaged in** — same.

The verbs to *cut on sight*: Responsible, Worked, Helped, Participated, Assisted, Engaged. If a bullet starts with one of these, rewrite the whole bullet, don't try to swap the verb.

## 9. Bullet length: aim for one line, accept two

A resume bullet is read in 2 seconds. If it doesn't fit in one or two lines, it's not read.

**Target:** 1 line per bullet, 2 lines max. Three-line bullets are a flag that the bullet is doing too much; split it or trim.

**Word count:** roughly 12-22 words per bullet. Less than 12 is often a duties bullet ("Built REST APIs in Python."); more than 22 is a paragraph hiding inside a bullet.

A useful test: **read the bullet out loud.** If you ran out of breath, it's too long. If it felt thin, add specificity.

## 10. Order of bullets within a job

Within each job, the **strongest bullet goes first.** This is the bullet the recruiter sees in their 30-second skim. It should be:

- Quantified.
- Specific.
- Closest in shape to the role you're applying to.

The duties-bullet trap: starting with "Responsible for backend services" before listing the actual achievements below. Cut the lead-in. Lead with the win.

Within a job, 3-5 bullets is the right count. Fewer than 3 and the role looks thin; more than 5 and the page gets cluttered.

## 11. The "would your manager sign off?" test

Before any bullet ships, ask: **would my last manager read this and nod, or would they wince?**

The wince comes from:

- Inflated numbers ("Improved performance 1000%" when it was 30%).
- Credit-stealing ("Led the migration" when you owned 1 of 5 services).
- Vague claims dressed in specific language ("Architected the platform" when you wrote a design doc that was partly adopted).

Honest bullets read stronger than inflated ones. A recruiter who suspects you of credit-stealing on the resume assumes you'll credit-steal on the team. Wince-free bullets win.

## 12. Worked examples — five rewrites end-to-end

### Example 1 — From a backend resume

**Before:**
> - Built and maintained REST APIs in Python and Django.

The verb is acceptable ("Built") but the bullet is generic — every backend engineer at every company "built APIs."

**After:**
> - Built the public REST API for Acme's billing service (Python/Django, 6 endpoints, ~12k req/min peak); reduced average payload size 38% by switching list responses to streaming JSON.

What changed: named the service, the technology, the scale, and a specific improvement. The bullet now answers "what was distinctive about this work?"

### Example 2 — From a data engineer resume

**Before:**
> - Worked on data pipelines for the analytics team.

**After:**
> - Rebuilt the daily ETL pipeline feeding the company's executive dashboards: migrated from Airflow 1 to Airflow 2 + dbt, reduced end-to-end runtime from 6h 20min to 1h 45min, eliminated 4 manual restart incidents per quarter.

What changed: named the migration, the tools, the time reduction, and a downstream reliability metric (the 4 incidents).

### Example 3 — From a frontend resume

**Before:**
> - Responsible for the checkout page UI.

**After:**
> - Led the redesign of the checkout flow (React + TypeScript) over Q3 2024; A/B test showed a 7.2% lift in completion rate and a 14% reduction in time-to-purchase on mobile.

What changed: the verb ("Led" not "Responsible for"), the timebox (Q3 2024), and two business metrics (completion rate, time-to-purchase).

### Example 4 — From a new-grad resume with a class project

**Before:**
> - Built a chat app for my distributed systems class.

**After:**
> - Built a Raft-replicated chat server (Go, ~1,400 LOC) supporting 50 concurrent clients with <100ms broadcast latency; placed 2nd of 28 teams in the class leaderboard for throughput-under-failure.

What changed: named the algorithm (Raft), the language, scale, a latency number, and a relative ranking. A class project becomes load-bearing.

### Example 5 — From an SRE / platform resume

**Before:**
> - Helped improve the reliability of our production systems.

**After:**
> - Diagnosed and fixed the recurring memory leak in our Envoy proxy fleet (~340 hosts) that was causing weekly Sev-2 incidents; root cause was a connection-pool config interaction with HTTP/2 backpressure. Sev-2s in that subsystem dropped from 1/week to 0 over the next 6 months.

What changed: replaced "helped" with two strong verbs (diagnosed, fixed), named the system (Envoy), scaled it (340 hosts), gave the root cause briefly (proof it was you), and quantified the outcome over a defensible time window.

The pattern across all five: **name the system, name the action, name the number.** Three concrete things per bullet. Strip everything else.

## 13. Self-check

- What are the five shapes of the duties-bullet antipattern?
- Rewrite this bullet to STAR+R: *"Responsible for the data pipeline."* (Make up a plausible number.)
- What's the target number-density across the whole resume? Why not 100%?
- A current role's bullets are all in past tense. What's wrong?
- "We migrated the system to Kubernetes." Why is this a weak bullet, and how do you fix it?
- Name three strong verbs and three to avoid.

## Further reading

- **Pragmatic Engineer — "Engineering resumes that get interviews":** <https://newsletter.pragmaticengineer.com/>
- **Levels.fyi — sample resumes by level:** <https://www.levels.fyi/blog/>
- **AskAManager — "Why your resume bullets don't work":** <https://www.askamanager.org/category/resumes>

When both lectures are clear, the [exercises](../03-exercises/00-overview.md) get you to a parsed, rewritten, tailored v2 resume.
