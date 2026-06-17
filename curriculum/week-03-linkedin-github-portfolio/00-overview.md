# Week 3 — LinkedIn, GitHub, and the Public Surface

> *Before a recruiter opens your resume, they Google your name. The first three results they find — your LinkedIn, your GitHub, and whatever else surfaces — are the second resume you didn't know you were submitting. This week you bring that second resume up to the standard of the first.*

Welcome to Week 3 of **C13 · Hack the Interview**. Weeks 1 and 2 produced the artifacts a company asks for: a target list, a tracking spreadsheet, and a v2 resume that parses cleanly. Week 3 fixes the artifacts a company *looks up*: your LinkedIn profile and your GitHub account, plus the small handful of other URLs a recruiter will click before deciding to schedule a screen.

The audience this week is different from Week 2. The ATS does not read LinkedIn; LinkedIn's own search does. GitHub is read by a human — usually a hiring manager skimming pinned repos for 90 seconds. The constraints are different. The work is not "polish each surface in isolation" — the work is making sure the resume, the LinkedIn, and the GitHub tell *the same story* and answer the same three questions.

## Learning objectives

By the end of this week, you will be able to:

- **Describe** what a recruiter searches for in LinkedIn Recruiter and how your headline, "About," and Skills section determine whether you appear.
- **Rewrite** a generic LinkedIn headline ("Software Engineer | Passionate about technology") into a specific, role-targeted line that maps to your resume.
- **Diagnose** the five most common failures on an engineer's GitHub profile (empty README, untouched fork graveyard, no pinned repos, broken project READMEs, stale activity graph).
- **Pin** three repositories that demonstrate distinct skills, with READMEs a reviewer can read in under 90 seconds.
- **Write** a project README that opens with the problem, shows a screenshot or sample output in the first screen, and lists how to run it in three commands or fewer.
- **Audit** the public surface a recruiter sees when they search your name, and remove or rewrite anything that contradicts your resume.

## Prerequisites

- You completed **Week 1** and **Week 2**. You have a master resume and at least one tailored version.
- You have a **LinkedIn account** with at least your current/most-recent role listed. (If you don't, create one Monday morning before the lectures.)
- You have a **GitHub account** with at least one repository that's yours (not a fork). If you have nothing, see "Bootstrap path" below.
- You can read your own profile critically. The mini-project requires a peer review.

### Bootstrap path

If your GitHub is empty or near-empty, that's recoverable in one week — but only if you start Monday. Spend the first two days of the week getting *one* real repository up: a small project you've actually shipped, with a real README. The rest of the week's exercises operate on that repo. Don't fake it; bring something genuine, even if it's small.

## Topics covered

- The recruiter's profile workflow: name search, LinkedIn skim, GitHub click-through
- LinkedIn headline as a search-result line — 220 characters that determine whether you appear
- The "About" section as a 200-word resume narrative, written for a recruiter, not a peer
- Skills, endorsements, and the keyword surface LinkedIn Recruiter actually searches
- Experience section parity: the resume and the LinkedIn experience block must agree
- Profile photo, banner, and the cost of cleverness in either
- Open-to-work signals: when to use, when to avoid
- GitHub profile README — the new homepage everyone sees first
- Pinned repositories: choose three, treat them as portfolio pieces
- Project README structure: problem, demo, run-in-three-commands, architecture, license
- The fork graveyard and the activity grid: what they signal, what to clean
- Personal site / portfolio: optional but high-leverage if it exists
- The "Googling your name" audit: what surfaces, what to address

## Weekly schedule

| Day       | Focus                                  | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|----------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | LinkedIn: headline, About, Experience  |    2h    |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Tuesday   | LinkedIn polish + peer skim            |    0h    |    1.5h   |     0h     |    0.5h   |   1h     |     1h       |    0.5h    |     4.5h    |
| Wednesday | GitHub profile + pinned repos          |    2h    |    1.5h   |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5.5h    |
| Thursday  | Project READMEs: one repo to portfolio |    0h    |    1.5h   |     1h     |    0.5h   |   1h     |     1h       |    0.5h    |     5.5h    |
| Friday    | Cross-surface consistency audit        |    0h    |    1h     |     0h     |    0.5h   |   1h     |     2h       |    0.5h    |     5h      |
| Saturday  | Mini-project deep work + peer review   |    0h    |    0h     |     0h     |    0h     |   1h     |     3h       |    0h      |     4h      |
| Sunday    | Quiz + week reflection                 |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0h       |    0h      |     0.5h    |
| **Total** |                                        | **4h**   | **6.5h**  | **1h**     | **3h**    | **6h**   | **7h**       | **2.5h**   | **30h**     |

(Same shape as Week 2. Most of the work is editing prose and READMEs; the lecture load is light because the rules are short. Use the slack for C2.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./00-overview.md) | This overview |
| [resources.md](./01-resources.md) | LinkedIn search references, GitHub README templates, portfolio examples |
| [lecture-notes/01-the-linkedin-profile-recruiters-read.md](./02-lecture-notes/01-the-linkedin-profile-recruiters-read.md) | Headline, About, Experience, Skills — and what LinkedIn Recruiter searches |
| [lecture-notes/02-the-github-profile-that-tells-a-story.md](./02-lecture-notes/02-the-github-profile-that-tells-a-story.md) | Profile README, pinned repos, project READMEs, activity hygiene |
| [exercises/README.md](./03-exercises/00-overview.md) | Three exercises |
| [exercises/exercise-01-rewrite-headline-and-about.md](./03-exercises/exercise-01-rewrite-headline-and-about.md) | Rewrite your LinkedIn headline and About from scratch |
| [exercises/exercise-02-pin-three-best-repos.md](./03-exercises/exercise-02-pin-three-best-repos.md) | Curate and pin three repos to your GitHub profile |
| [exercises/exercise-03-readme-for-your-top-project.md](./03-exercises/exercise-03-readme-for-your-top-project.md) | Write a real README for the strongest of your three pinned repos |
| [challenges/README.md](./04-challenges/00-overview.md) | One stretch challenge |
| [challenges/challenge-01-the-recruiter-skim-test.md](./04-challenges/challenge-01-the-recruiter-skim-test.md) | Have two peers click through your name → LinkedIn → GitHub and report what they saw |
| [quiz.md](./05-quiz.md) | 10 MCQs |
| [homework.md](./06-homework.md) | Six problems (~6h) |
| [mini-project/README.md](./07-mini-project/00-overview.md) | Polished public LinkedIn + GitHub presence, peer-reviewed |

## Stretch goals

- Read **GitHub's official "Profile READMEs" gallery** to see what other engineers ship: <https://github.com/abhisheknaiidu/awesome-github-profile-readme>
- Read **three engineering blogs** of people at your target companies. Bookmark the patterns you'd steal for your own portfolio site if you build one later.
- Browse **levels.fyi's "engineers we admire"** type posts for examples of what a recognizable public surface looks like at staff+ level.
- If you already have a personal site / portfolio, run the **30-second skim test** (from Week 2, Challenge 1) on the homepage with two peers.

## What "done" looks like by Sunday night

By the end of the week, the following should be true. If any of these aren't, stay with this week's work before moving on.

- Your LinkedIn headline is a single 220-character line that names a specific role, 2-3 technologies, and ideally a domain. Not the LinkedIn default. Not "passionate about technology."
- Your LinkedIn About is 180-280 words, follows the four-paragraph structure, contains zero banned phrases, and contains at least one quantified outcome.
- Your LinkedIn Experience section agrees, line by line, with your v2 resume — same titles, same companies, same dates, same locations.
- Your GitHub has a profile README at `github.com/{username}/{username}` that orients a 30-second visitor.
- Three repos are pinned with intent. The strongest of them has a README a hiring manager can read in 90 seconds and a Quick start that works on a fresh clone.
- The first 3 Google results for your full name are current and on-message.
- At least one peer has done the recruiter-skim walk on your three surfaces and reported back. You've applied at least 2 pieces of their feedback.

This is the public-surface baseline. You will revise it once more in Week 8 (after you have screen signal); this week's version is the version that goes live for the rest of the cycle.

## Up next

[Week 4 — The Recruiter Screen Survival Kit](../week-04/) — once your LinkedIn and GitHub agree with your resume, and a peer has confirmed the cross-surface story holds.
