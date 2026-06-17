# Mini-Project — Resume v2: ATS-tested, peer-reviewed

> Your second resume. Not your best ever — you'll revise again in Weeks 4 and 8 once you have interview signal. But the resume you'd send to a Tier-B company tomorrow without flinching.

**Estimated time:** 5-7 hours, spread Thursday-Saturday. The peer review is non-negotiable.

## What you ship

A **resume v2** delivered as three artifacts:

1. **`resume-v2-master.pdf`** — your master version. Long, complete, every bullet you might use. (1-2 pages, depending on level.)
2. **Three tailored versions** — `resume-v2-tier-a.pdf`, `resume-v2-tier-b.pdf`, `resume-v2-stretch.pdf` — corresponding to Exercise 3's three JDs.
3. **A peer-review record** — written transcript of feedback from at least two reviewers, plus the changes you applied or explicitly rejected.

All four files (and the editable sources) committed to `c13-week-02/mini-project/`.

## Acceptance criteria

### Structural (Lecture 1)

- [ ] Single column, every page.
- [ ] PDF is text-source (passes `pdftotext` test).
- [ ] No graphics in the header. Name and contact in plain text.
- [ ] Standard section names only: Experience, Skills, Education, Projects (and a Summary if you use one).
- [ ] Date format consistent across every job (`Jan 2024 – Present` or your chosen format, applied uniformly).
- [ ] No smart quotes, no ligatures, no non-breaking spaces. Run `pdftotext` and grep for non-ASCII.

### Content (Lecture 2)

- [ ] Number-density ≥40% across the master. (Count bullets total; count bullets with a quantified result.)
- [ ] Zero bullets begin with "Responsible for," "Worked on," "Helped," or "Participated in."
- [ ] All bullets in past tense for past roles; current role uses present tense for ongoing work and past tense for completed achievements.
- [ ] Each bullet fits in 1-2 lines (~12-22 words). No 3-line bullets unless genuinely irreducible.
- [ ] Each job lists 3-5 bullets. Strongest bullet first.

### ATS verification

- [ ] Master PDF run through a parser (Resume-Magic / Affinda / Jobscan). Parser output saved as JSON or screenshot in the mini-project folder.
- [ ] Every field the parser extracts is correct (name, email, all jobs with titles + dates, skills list).
- [ ] Each tailored version's keyword match against its JD is ≥75% (use Jobscan or manual counting).

### Tailoring

- [ ] Three tailored versions exist; none are byte-identical to each other or to the master.
- [ ] A changelog file (`tailoring-changes.md`) describes what's different between master and each tailored version.

### Peer review

- [ ] At least two reviewers (peers from C2 / C13 / your study group, or a mentor) have read the v2 master.
- [ ] Their feedback is captured in `peer-review-notes.md`, including: their name (or initials), date, what they said about layout, bullets, and the 30-second skim.
- [ ] You applied at least 3 pieces of feedback. For any feedback you rejected, write a one-line justification.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Parses cleanly | 25% | Every field correct in the parser output |
| Number-density on bullets | 20% | ≥40%, with honest numbers (not inflated) |
| Tailoring effectiveness | 15% | Each tailored version scores ≥75% keyword match against its JD |
| Layout / 30-second skim | 15% | Two peers can identify your most recent title, YoE, and a relevant skill from a 30-second look |
| Peer feedback integration | 15% | Visible changes from review, with justification when rejected |
| One real application sent | 10% | Tier-B submission logged (Homework Problem 4) |

## How to set up the rhythm

Once v2 is shipped, every subsequent application uses this workflow:

1. Read the JD. Extract keywords (~5 min — see Exercise 3).
2. Open the master in your editor. Save-as with the JD's company name.
3. Tailor: reorder skills, reorder bullets, tweak wording (~15 min).
4. Export PDF. Run through parser (~2 min). Confirm fields correct.
5. Submit.

**Total: ~25 minutes per application.** This is what makes 30+ applications across the cycle tractable.

## Stretch

- Build a **LaTeX or Typst source** of your master so tailoring is `\input{tier-a-keywords.tex}` instead of manual reordering. (Optional; only do this if you'll maintain it.)
- Get a **third peer review** from someone outside engineering (a recruiter friend, a manager you've worked with). Their feedback is differently shaped.
- Submit your master to **two parsers** (e.g., Resume-Magic + Affinda). Compare the outputs. If they disagree on a field, the resume is ambiguous; fix the ambiguity.

## Why this matters

The resume is the single document that touches every company on your list. A bad master means 30 applications waste time. A good master means each application is 25 minutes of focused work, and the conversion rate at the recruiter-screen stage rises from "rare" to "most of the time" for roles where you're genuinely qualified.

This is also the document you'll revise again in Weeks 4 and 8 — once you have *interview signal* on what works. Week 2's v2 is the baseline; you don't need it to be perfect, you need it to be defensible.

## Submission

Commit `c13-week-02/mini-project/` to your portfolio repo. The folder should contain:

- `resume-v2-master.pdf` + editable source
- `resume-v2-tier-a.pdf`, `resume-v2-tier-b.pdf`, `resume-v2-stretch.pdf` + editable sources
- `tailoring-changes.md`
- `peer-review-notes.md`
- `parser-output/` (JSON or screenshots from the ATS parser)
- `README.md` (a short index pointing to each file with one-line descriptions)

---

When done: open [Week 3 — The Recruiter Screen Survival Kit](../../week-03/) — coming soon.
