# Week 2 — The Resume That Survives the ATS

> *Your resume is parsed by software before it's read by a human. Of every 100 resumes submitted to a Greenhouse-backed posting, ~70 are filtered or misparsed before a recruiter ever sees them. The skill is not "make a beautiful resume" — the skill is "produce a document that parses cleanly AND reads well AND ranks high on the keyword query the recruiter actually runs."*

Welcome to Week 2 of **C13 · Hack the Interview**. Week 1 got your pipeline architecture in place: spreadsheet, target list, outreach drafts. Week 2 fixes the single asset every one of those companies will see: your resume. By Sunday you have a v2 resume that's been parsed by a real ATS, peer-reviewed, and rewritten bullet-by-bullet from duties into outcomes.

This week is shorter on theory than Week 1 and longer on actual rewriting. Plan to throw away half of what you currently have.

## Learning objectives

By the end of this week, you will be able to:

- **Describe** what Greenhouse, Lever, Ashby, and Workday actually do to a PDF when it lands in the queue.
- **Identify** the structural failures (two-column, header graphics, non-standard section names, date inconsistency, ASCII-unsafe characters) that cause silent reject before any human reads the file.
- **Test** your own resume in a free parser and read the output critically.
- **Rewrite** a duties-shaped bullet ("Responsible for X") into a STAR+R bullet with a quantified result.
- **Hit** the number-density target: at least 40% of bullets contain a quantifiable result.
- **Tailor** one master resume into three role-specific versions in under 30 minutes each, by adjusting keyword density rather than rewriting wholesale.
- **Diagnose** your own resume's failure modes using the 30-second test the way a busy recruiter actually skims.

## Prerequisites

- You completed **Week 1**. You have a spreadsheet of 30 companies and a `resume-v1.pdf` baseline (from Homework Problem 5).
- You have access to a PDF-capable editor: Google Docs / Microsoft Word / LaTeX / Typst / Markdown-to-PDF. Whichever you prefer; the format isn't the lesson.
- You have **two real job descriptions** from companies on your Week-1 target list saved to disk. Pick a Tier-A and a Tier-B.
- You can read your own work critically. If not, schedule a 30-minute peer review with someone from C2 or your study group; the mini-project requires it.

## Topics covered

- What an ATS actually parses, with examples from Greenhouse, Lever, Ashby, and Workday
- Why two-column layouts produce interleaved nonsense in 80% of parsers
- Standard section headers (and the cost of clever alternatives)
- PDF-from-text-source vs. PDF-from-image: the difference matters
- ASCII-safe characters: smart quotes, em-dashes, ligatures
- Date format consistency: one format across every job
- The keyword-matching layer: how a recruiter's saved search ranks you
- The "duties bullet" antipattern and why "Responsible for X" wastes a line
- The STAR+R format: Situation, Task, Action, Result — with the Result quantified
- Number-density: ≥40% of bullets should contain a measurable outcome
- Tense and voice: past tense for past roles, active voice always
- Tailoring vs. rewriting: when to swap keywords, when to rebuild

## Weekly schedule

| Day       | Focus                                  | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|----------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | What the ATS actually sees             |    2h    |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Tuesday   | Parse your own resume + diagnose       |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     1h       |    0.5h    |     4.5h    |
| Wednesday | Bullets: duties to outcomes            |    2h    |    1.5h   |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5.5h    |
| Thursday  | Rewrite five bullets + measure         |    0h    |    1.5h   |     1h     |    0.5h   |   1h     |     1h       |    0.5h    |     5.5h    |
| Friday    | Tailoring for three roles              |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     2h       |    0.5h    |     5.5h    |
| Saturday  | Mini-project deep work + peer review   |    0h    |    0h     |     0h     |    0h     |   1h     |     3h       |    0h      |     4h      |
| Sunday    | Quiz + week reflection                 |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0h       |    0h      |     0.5h    |
| **Total** |                                        | **4h**   | **7h**    | **1h**     | **3h**    | **6h**   | **7h**       | **2.5h**   | **30.5h**   |

(Week 2 runs a bit lighter than Week 1 because most of the labor is rewriting your own document. Use the slack to do the C2 problems your tech screen will ride on.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./00-overview.md) | This overview |
| [resources.md](./01-resources.md) | Free ATS parsers, sample resumes, style references |
| [lecture-notes/01-what-the-ats-actually-sees.md](./02-lecture-notes/01-what-the-ats-actually-sees.md) | Parser behavior, layout, formatting, keyword matching |
| [lecture-notes/02-bullet-rewrites-from-duties-to-outcomes.md](./02-lecture-notes/02-bullet-rewrites-from-duties-to-outcomes.md) | STAR+R, the number-density target, tense and voice |
| [exercises/README.md](./03-exercises/00-overview.md) | Three exercises |
| [exercises/exercise-01-parse-your-own-resume.md](./03-exercises/exercise-01-parse-your-own-resume.md) | Run your v1 through a parser; diagnose |
| [exercises/exercise-02-rewrite-five-bullets.md](./03-exercises/exercise-02-rewrite-five-bullets.md) | Rewrite 5 of your weakest bullets |
| [exercises/exercise-03-tailor-for-three-roles.md](./03-exercises/exercise-03-tailor-for-three-roles.md) | Three tailored versions for three real JDs |
| [challenges/README.md](./04-challenges/00-overview.md) | One stretch challenge |
| [challenges/challenge-01-the-30-second-test.md](./04-challenges/challenge-01-the-30-second-test.md) | Skim your resume like a recruiter does |
| [quiz.md](./05-quiz.md) | 10 MCQs |
| [homework.md](./06-homework.md) | Six problems (~6h) |
| [mini-project/README.md](./07-mini-project/00-overview.md) | Resume v2, ATS-tested, peer-reviewed |

## Stretch goals

- Read **Gergely Orosz's "Engineering Resumes That Get Interviews"** (free Pragmatic Engineer post): <https://newsletter.pragmaticengineer.com/p/preparing-for-the-systems-design>
- Browse **levels.fyi's "Salary Negotiation Tips"** archive for resume examples by role.
- Read the **Tech Interview Handbook's resume section** end-to-end: <https://www.techinterviewhandbook.org/resume/>
- Find **three resumes from staff+ engineers** on public portfolios (their personal site / GitHub). Read what they emphasize at that level.

## Up next

[Week 3 — The Recruiter Screen Survival Kit](../week-03/) — once your v2 resume has been peer-reviewed and parsed cleanly.
