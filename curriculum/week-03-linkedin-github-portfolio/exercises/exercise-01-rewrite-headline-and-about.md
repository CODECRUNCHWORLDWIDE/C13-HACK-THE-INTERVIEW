# Exercise 1 — Rewrite headline and About

**Time:** ~60 minutes. **Output:** A new LinkedIn headline (3 candidates, one chosen) and an About section that maps to your resume.

## Goal

Replace the default-LinkedIn or generic-tagline version of your headline and About with the search-targeted, resume-aligned versions described in Lecture 1. Produce three headline candidates and pick one. Write a 200-280 word About from scratch — do not edit the old one.

## Setup

You need:

- Your **current v2 resume** (from Week 2 mini-project). The new LinkedIn must agree with it.
- Your **current LinkedIn profile** open in a browser tab.
- A second browser tab in **private / incognito mode**, also on your LinkedIn URL — to view the logged-out version.
- A markdown file to draft in: `c13-week-03/exercise-01-headline-and-about.md`. Don't edit LinkedIn directly until the drafts are reviewed.

## Process

### Step 1 — Audit the current state (10 min)

In your draft file, paste the current state:

```markdown
## Current state

**Current headline:**
> [paste verbatim]

**Current About (first 3 lines, as visible in logged-out view):**
> [paste]

**Current About (full text):**
> [paste]
```

Then, in 2-3 sentences, name what's wrong. Use the failure patterns from Lecture 1, §3 and §4. Examples:

- "Headline is LinkedIn's default 'Backend Engineer at Acme.' No technologies, no domain."
- "About opens with 'I'm a passionate software engineer.' No specific outcomes anywhere."
- "About lists 12 frameworks and no actual project."

### Step 2 — Extract the keyword pool from your resume (10 min)

Open your v2 resume. List, in your draft file:

- **Your target role(s).** Up to two role-shaped descriptors — e.g., "Senior Backend Engineer," "Platform Engineer."
- **Your top 5 technologies.** The languages, frameworks, and platforms most central to the roles you're applying to.
- **Your domain.** One or two phrases — "payments," "ML infrastructure," "developer tools," "ETL for healthcare claims."
- **Your strongest 3 outcomes.** Paraphrased from your resume's STAR+R bullets. One sentence each.

This pool is the raw material for both the headline and the About. Everything you write must come from this list.

### Step 3 — Draft three headline candidates (15 min)

Using the structure from Lecture 1, §3 — `{Specific role} | {2-3 technologies} | {Optional: domain or company} | {Optional: signal}` — produce three headlines.

Vary them. One should lean technology-first, one domain-first, one signal-first. Each must be ≤220 characters.

```markdown
## Headline candidates

**Candidate A (tech-first):**
> Senior Backend Engineer | Python, PostgreSQL, AWS | Payments infrastructure at Acme

**Candidate B (domain-first):**
> Payments infrastructure engineer (Python/Go) | Building idempotent settlement systems at Acme

**Candidate C (signal-first):**
> Senior Backend Engineer, open to staff-level platform roles | Python, AWS, distributed systems | ex-Stripe, now at Acme
```

Then, in one line per candidate, write **what query each best matches** — the recruiter search this candidate is optimized for. Example: "Candidate A matches `backend Python AWS payments`; Candidate B matches `payments engineer`; Candidate C matches `staff platform engineer`."

**Pick one.** Justify in one sentence: "Choosing B because my Tier-A target list is dominated by payments-domain companies, and the domain-first phrasing surfaces in domain-keyword searches."

### Step 4 — Draft the About from scratch (20 min)

**Do not edit the existing About.** Start fresh, in your draft file. Follow Lecture 1, §4's four-paragraph structure:

```markdown
## About — draft v1

**Paragraph 1 — current shape of work** (1-2 sentences):
> [Your name, role, employer, the 1-2 specific things you build.]

**Paragraph 2 — what you've shipped** (3-4 sentences):
> [Your top 3 outcomes from your resume, rewritten as prose. Each outcome must include a number or a specific named system.]

**Paragraph 3 — what's next** (2-3 sentences):
> [The kind of role you're targeting, the technologies you're deepening, the stage / size of company.]

**Paragraph 4 — contact close** (1 line):
> [Email or "DM me on LinkedIn." One line, not a paragraph.]
```

Constraints:

- Total word count: **180-280**. Count it.
- **Zero** instances of "passionate," "lifelong learner," "team player," "self-starter," "thrives," or "results-driven."
- Every paragraph must contain at least one **specific noun** that maps to your resume (a system you built, a technology you use, a metric you moved).
- At least one **quantified outcome** in Paragraph 2.

### Step 5 — Read in the logged-out view test (5 min)

The logged-out view of LinkedIn shows ~3 lines of About before truncation. Test:

1. In your draft file, simulate the truncation: copy the first ~3 lines (roughly 220 characters) of your draft About.
2. Read those 3 lines alone. Do they:
   - Name your current role and employer?
   - Name at least one specific technology or domain?
   - Read as a complete-sentence opening, not a fragment?

If no to any: rewrite the opening sentence. The first 3 lines must work as standalone bait for the click.

### Step 6 — Apply to LinkedIn (5 min)

Once your draft is ready:

1. Update your LinkedIn headline to the chosen candidate.
2. Update your About to the chosen draft.
3. Save. Wait 60 seconds.
4. Open your profile in a **private browser window** (logged-out view).
5. Confirm: headline displays correctly, no characters truncated weirdly, the first 3 lines of About show what you intended.
6. Screenshot the logged-out view and save to `c13-week-03/exercise-01-screenshots/` for the mini-project.

## Acceptance criteria

- [ ] `c13-week-03/exercise-01-headline-and-about.md` exists.
- [ ] Current-state audit captures the verbatim before-state and a 2-3 sentence diagnosis.
- [ ] Keyword pool listed: target role(s), top 5 technologies, domain, 3 strongest outcomes.
- [ ] Three headline candidates, each with a query-match justification.
- [ ] One chosen headline, with a one-sentence rationale.
- [ ] About draft is 180-280 words, follows the four-paragraph structure, contains zero banned phrases, and contains at least one quantified outcome.
- [ ] First-3-lines test passed (or rewrite documented).
- [ ] LinkedIn updated; logged-out screenshot saved.

## Common mistakes

- **Buzzword tagline imported from the old version.** "Passionate about technology" sneaking back in because it sounded fine in isolation. Reread; cut.
- **Headline that lists 7 technologies.** Three is the cap; four reads stuffed.
- **About that's a resume bullet list in prose form.** The About is narrative, not a Skills paragraph. If every sentence starts "I have experience in...," restructure.
- **First sentence that fails the 3-line test.** The opening must work as standalone — don't bury the lede.
- **Headline-resume mismatch.** Your LinkedIn says "Senior Backend Engineer"; your resume says "Software Engineer." Mismatch is worse than either. Pick one and propagate.

## Stretch

- Run the same exercise on **two peers' headlines and Abouts.** Note: which one of the three candidates would *you* click, and why? Feedback gets sharper when you've graded others first.
- Translate your About to a **second language** if you're targeting roles where bilingual matters. Both versions should pass the 3-line test.
- Write the same headline in **three lengths**: a 220-char version (mobile), a 260-char version (desktop), and a 100-char version (search-result preview). Save all three; you may swap as the cycle evolves.

## Why this matters

The headline is read by every recruiter who finds you. The About is read by every recruiter who clicks. These two fields together drive the inbound-message rate that determines whether you spend the next 8 weeks waiting on companies or having more screens than you can take.

A great resume with a default LinkedIn headline gets ~30% of the inbound it should. A great resume with a search-targeted headline closes that gap immediately, no other work required.

## Submission

Commit `c13-week-03/exercise-01-headline-and-about.md` and the logged-out screenshots to your portfolio repo.
