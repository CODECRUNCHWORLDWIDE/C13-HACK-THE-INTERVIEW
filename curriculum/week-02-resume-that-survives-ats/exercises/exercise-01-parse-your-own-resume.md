# Exercise 1 — Parse your own resume

**Time:** ~45 minutes. **Output:** A diagnostic report of what your resume looks like to an ATS.

## Goal

Run your `resume-v1.pdf` (from Week 1, Homework Problem 5) through a free parser and produce a written diagnostic of every field the parser got wrong. The point isn't to fix the resume yet — it's to *see* what the machine sees, so the rest of the week's edits are informed.

## Setup

You need:

- Your current `resume-v1.pdf` exported as a real PDF (not an image; see Lecture 1, §2 for the test).
- A free ATS parser. Pick one:
  - **Resume-Magic**: <https://resume-magic.app/>
  - **Affinda Resume Parser demo**: <https://www.affinda.com/resume-parser>
  - **Jobscan free scan**: <https://www.jobscan.co/> (5/month, requires email)

## Steps

### Step 1 — Confirm your PDF has a text layer (5 min)

On macOS: open the PDF in Preview. Try to select and copy a paragraph. If you can copy text, the layer is there. If you can only select a rectangle (the whole page acts like an image), there's no text layer.

On any OS, command line: `pdftotext resume-v1.pdf -`. Clean text out = good. Garbage or empty = no text layer; re-export from the source.

If your PDF has no text layer, **stop and fix it before continuing.** Re-export from Google Docs / Word / LaTeX / whatever tool you used.

### Step 2 — Run the parser (10 min)

Upload `resume-v1.pdf` to your chosen parser. Wait for the output. Most parsers display a structured view: header fields, work history array, education, skills tags.

Save / screenshot the parser output. You'll reference it in your write-up.

### Step 3 — Score the parser output against reality (20 min)

Open a new file: `c13-week-02/exercise-01-parser-diagnostic.md`. For each of the fields below, mark **CORRECT**, **PARTIALLY CORRECT**, or **WRONG**, and add a short note on what the parser got vs. what reality is.

| Field | Parser saw | Reality | Verdict |
|-------|-----------|---------|---------|
| Name |  |  |  |
| Email |  |  |  |
| Phone |  |  |  |
| LinkedIn URL |  |  |  |
| GitHub URL |  |  |  |
| Location (city/state) |  |  |  |
| Most recent job — title |  |  |  |
| Most recent job — company |  |  |  |
| Most recent job — start date |  |  |  |
| Most recent job — end date |  |  |  |
| Total years of experience computed |  |  |  |
| Number of jobs detected |  |  |  |
| Number of education entries detected |  |  |  |
| Skills tagged | (list) | (list) |  |

### Step 4 — Identify the structural defects (10 min)

Cross-check your resume against the five failures from Lecture 1, §3:

- [ ] Two-column layout? **Yes / No.**
- [ ] PDF is text-source (passed Step 1)? **Yes / No.**
- [ ] Graphics in the header? **Yes / No.**
- [ ] Non-standard section names anywhere? **Yes / No.** (List them.)
- [ ] ASCII-unsafe characters? **Yes / No.** (Open the `pdftotext` output and search for smart quotes `"` `"` `'` `'`, em-dashes `—`, ligatures `ﬁ` `ﬂ`. Note any you find.)
- [ ] Date format consistent across every job? **Yes / No.** (Write out the formats found.)

## Acceptance criteria

- [ ] `c13-week-02/exercise-01-parser-diagnostic.md` exists in your portfolio repo.
- [ ] The 14-row field table is filled in for every row.
- [ ] The 6-item structural checklist is filled in with yes/no + notes.
- [ ] A "Top 3 issues to fix this week" paragraph identifies the three highest-priority defects.
- [ ] The parser output is screenshotted or saved as JSON alongside the diagnostic.

## Common findings (don't be surprised if)

- The parser swapped your title and company on one job.
- A short-term role (under 6 months) was dropped entirely.
- Your "Skills" section parsed as one merged string instead of individual tags.
- Your phone number didn't extract because of formatting (parentheses, dots vs. dashes).
- A side project listed in a "Projects" section was tagged as a job.

These are all common. None are fatal. The point of this exercise is to *find them now*, before any company sees them.

## Stretch

- Run the same `resume-v1.pdf` through **two** parsers. Compare which one extracted more correctly. (They disagree more than you'd expect.)
- Run a friend's resume through the same parser. Compare what works.
- If you used Jobscan, save the JD-match score. You'll compare it to the v2 score in the mini-project.

## Submission

Commit `c13-week-02/exercise-01-parser-diagnostic.md` and any screenshots / parser JSON to your portfolio.
