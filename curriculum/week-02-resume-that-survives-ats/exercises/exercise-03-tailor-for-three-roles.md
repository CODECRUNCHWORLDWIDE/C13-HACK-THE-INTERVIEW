# Exercise 3 — Tailor for three roles

**Time:** ~75 minutes. **Output:** Three tailored versions of your resume — one each for three real JDs from your Week-1 target list.

## Goal

Practice the **tailoring** workflow: from one master resume, produce three role-specific versions in under 25 minutes each. Tailoring is *keyword adjustment + bullet ordering + skills emphasis*, not a full rewrite. Done well, it raises your ATS keyword-match score from ~50% to ~80% per role.

## Process

### Step 0 — Prerequisites

You need:

- A master resume in editable format (not the PDF; the source file — Google Doc / Word / LaTeX / Typst).
- **Three job descriptions** from companies on your Week-1 target list:
  - One Tier-A
  - One Tier-B
  - One that's a *stretch* in a slightly different specialization (e.g., if you're backend, pick a platform / infra role)

Save each JD as a `.txt` file in `c13-week-02/exercise-03/jds/`.

### Step 1 — Extract keywords from each JD (15 min — ~5 min/JD)

For each JD, in `c13-week-02/exercise-03/jd-1-keywords.md` (and `jd-2`, `jd-3`), produce a table:

| Term | Category | Strength | In my master resume? |
|------|----------|----------|----------------------|
| Python | Language | Hard | Yes |
| Kubernetes | Tool | Hard | No |
| OAuth2 | Standard | Hard | No |
| Real-time data pipelines | Domain | Hard | Partial (I have "streaming pipelines") |
| Mentorship | Soft | Soft | No |
| ... | ... | ... | ... |

Categories: `Language / Framework / Tool / Cloud / Methodology / Domain / Standard / Soft`.

Strength: `Hard` (must-have) or `Soft` (nice-to-have).

"In my master resume?" → `Yes / No / Partial`. Partial means a synonym or close form is there but not the exact term.

Aim for 15-25 terms per JD. Most JDs have that many; some have fewer.

### Step 2 — Compute v0 keyword match (5 min — ~90 sec/JD)

For each JD: `(Yes count + 0.5 * Partial count) / total terms * 100`. Write the percentage at the top of the keywords file.

If you're at <50% on a JD that's well-aligned with your background, your master resume is under-using your own keywords. If you're at >80% already, this JD is a strong fit; the tailoring will be light.

### Step 3 — Make a copy of your master resume per JD (5 min)

```
c13-week-02/exercise-03/resume-for-jd-1.pdf    (and .docx / .typ / .tex source)
c13-week-02/exercise-03/resume-for-jd-2.pdf
c13-week-02/exercise-03/resume-for-jd-3.pdf
```

Each starts as an exact copy of the master.

### Step 4 — Tailor each copy (45 min — ~15 min/JD)

For each tailored copy, do **only** these things:

1. **Skills section: reorder.** Move the most relevant skills (per the JD's hard keywords) to the front. Drop skills not relevant to this role.
2. **Skills section: add missing keywords you legitimately have.** If you know Kubernetes and the JD mentions it but your master doesn't list it, add it.
3. **Bullets: reorder within each job.** Within each role, move the bullets most relevant to this JD to the top.
4. **Bullets: tweak wording to match JD terminology.** If your bullet says "container orchestration" and the JD says "Kubernetes" and you used Kubernetes — change the wording. Don't invent.
5. **Summary line (if you have one): rewrite for this role.** One sentence, naming the role you're applying to.

What you **don't** do:

- Don't rewrite bullets from scratch (you did that in Exercise 2).
- Don't fabricate skills or experience.
- Don't bloat the resume past its target length.

### Step 5 — Re-compute keyword match per tailored version (5 min)

For each tailored version: recount. Each should now hit **75-90% keyword match**.

If a JD's match is still below 70% after tailoring, the conclusion is one of:

- The role isn't a real fit. (Honest signal; reconsider applying.)
- You have the experience but it's not surfaced. (Audit your master.)
- You don't have a meaningful skill the JD demands. (Decide: drop the application, or commit to building the skill in the next 1-2 weeks before applying.)

## Acceptance criteria

- [ ] `c13-week-02/exercise-03/` contains three JD `.txt` files and three keyword `.md` files.
- [ ] Three tailored resume PDFs (and editable sources) exist.
- [ ] Each tailored version's keyword match is at least 75%.
- [ ] No two tailored versions are byte-identical.
- [ ] You wrote a 100-word reflection at the bottom of `exercise-03/README.md`: "Which JD was hardest to tailor for, and why?"

## Common mistakes

- **Tailoring by rewriting.** If you're rewriting bullets per JD, you're doing it wrong (and your work will be inconsistent). Tailor at the *level* of skills + ordering + light wording, not by rewriting evidence.
- **Stuffing keywords.** Adding "Kubernetes" 4 times to inflate match score. Doesn't work — the parser dedupes; the recruiter rolls their eyes.
- **Lying.** Don't add skills you don't have. The screen will surface it within 5 minutes.
- **Three versions, three different stories about you.** Each tailored version should still be *recognizably you* — the same career, the same wins, just emphasized differently.

## Stretch

- Add a **change log** at the bottom of each tailored source: "vs. master: added Kubernetes to Skills; reordered bullets in Acme role; rewrote summary." Helps when you compare a year from now.
- Build a small **tailoring checklist** for yourself based on this exercise. You'll reuse it for every application this cycle.
- Run each tailored PDF back through the ATS parser (Exercise 1's tool). Check the keyword tags it produces.

## Why this matters

You will tailor **at least 30 times** this cycle (one per company you actually apply to). The first three are slow; the next 27 are fast — *if* the master resume is right. This exercise locks in the workflow so each subsequent tailoring is 15 minutes, not 60.

## Submission

Commit the JDs, the keyword files, the three tailored resumes, and the reflection to `c13-week-02/exercise-03/`.
