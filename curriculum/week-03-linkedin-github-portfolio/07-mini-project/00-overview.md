# Mini-Project — Polished Public Surface: LinkedIn + GitHub, Peer-Reviewed

> By the end of this week, the three surfaces a recruiter and hiring manager will read — your resume (from Week 2), your LinkedIn, and your GitHub — agree with one another and tell a single, current, defensible story. The mini-project is the consolidation step.

**Estimated time:** 5-7 hours, spread Thursday-Saturday. The peer review is non-negotiable.

## What you ship

A **polished public surface** delivered as four artifacts:

1. **Updated LinkedIn profile** — headline, About, Experience, Skills, photo, and Featured (if relevant) all current and aligned with the v2 resume.
2. **Updated GitHub profile** — profile README at `github.com/{username}/{username}`, three intentionally pinned repos, fork graveyard cleaned, top repo's README polished to portfolio quality.
3. **A cross-surface consistency record** — `cross-surface-summary.md` documenting what each surface says about the same facts.
4. **A peer-review record** — written notes from at least one peer who has walked the full recruiter-skim path (Google → LinkedIn → GitHub), plus the changes you applied or explicitly rejected.

All artifacts (the source markdowns; logged-out screenshots of LinkedIn and GitHub; the peer-review notes) committed to `c13-week-03/mini-project/`. The LinkedIn and GitHub changes themselves live on those platforms; you commit the *evidence* (screenshots, links, notes) to your portfolio.

## Acceptance criteria

### LinkedIn (Lecture 1)

- [ ] Headline is the chosen candidate from Exercise 1 — contains a specific role, 2-3 technology nouns, and ideally a domain or signal. ≤220 characters.
- [ ] Photo is current, face visible, neutral background.
- [ ] Banner is at least neutral (not the default geometric pattern, but also not a low-resolution stretched image).
- [ ] About is the 180-280 word version from Exercise 1: four-paragraph structure, ≥1 quantified outcome, zero banned phrases ("passionate," "lifelong learner," etc.).
- [ ] First 3 lines of About (the logged-out preview) name your current role, employer, and at least one specific technology or domain.
- [ ] Every job in your v2 resume's Experience section also appears on LinkedIn with the same title, company, dates, and location.
- [ ] Skills section: top 3 are the three most-relevant-to-target-roles skills. Total list is curated (no dead languages from 10 years ago at the top).
- [ ] Open-to-Work signal is on **at least** in recruiter-only mode (public mode at your discretion).
- [ ] Logged-out view tested in a private browser window; screenshot saved.

### GitHub (Lecture 2)

- [ ] Profile README is live at `github.com/{username}/{username}/README.md` and renders on your profile page.
- [ ] Profile README is 100-250 words, follows the §5 structure (intro / currently working on / notable projects / elsewhere), with no animated GIF banners, no skills lists, no "passionate" copy.
- [ ] Three repos are pinned (or two, with documented rationale).
- [ ] Each pinned repo has at least a working README. The **main project** pinned repo's README meets the 8-section structure from Lecture 2, §6 — including a tested Quick start that runs end-to-end on a fresh clone.
- [ ] LICENSE present in each pinned repo.
- [ ] Fork graveyard reduced: no more than ~5 visible forks on the profile.
- [ ] Logged-out profile view tested in a private browser window; screenshot saved.

### Cross-surface consistency

- [ ] `cross-surface-summary.md` exists. Lists, for at least these 8 facts, what each of the three surfaces (resume / LinkedIn / GitHub) says, with a "Consistent? Yes / Minor / No" verdict:
  - Current title
  - Current company
  - Years of experience implied
  - Top 3 technologies
  - Primary domain
  - Most prominent project / outcome
  - Location
  - Contact email
- [ ] Every `No` row has a documented decision (which surface gets updated, and what to).

### Peer review

- [ ] At least **one peer** has done the full Challenge-1 recruiter-skim walk on your three surfaces. Their notes are in `peer-review-notes.md` and include:
  - Their initials or name (with permission).
  - Date of the walk.
  - The questions you asked (the standard set from Challenge 1) and their answers.
  - Their 1-5 score on "how clear is this person's professional shape?"
  - At least 3 concrete pieces of feedback.
- [ ] You applied at least 2 pieces of feedback. For any feedback you rejected, write a one-line justification.

### Google audit (light)

- [ ] First-3-Google-results screenshot (or list) saved.
- [ ] If anything in those results is stale or contradicts your current story, action documented (deleted / locked / pushed-down / accepted-as-is with rationale).

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| LinkedIn headline + About quality | 20% | Headline contains the target query nouns; About passes the 3-line test; ≥1 quantified outcome |
| GitHub profile README + pin curation | 20% | README is current, three pins are intentional and distinct; fork graveyard cleaned |
| Top pinned repo's README | 20% | Reviewer can run the project end-to-end from the Quick start; reads as written-for-the-reader |
| Cross-surface consistency | 15% | Resume / LinkedIn / GitHub agree on every fact in the 8-row table; no unresolved `No` rows |
| Peer-review integration | 15% | At least 2 pieces of peer feedback visibly applied; rejected items have one-line justifications |
| Google audit | 10% | First 3 Google results are current, on-brand, or addressed |

## How to set up the rhythm

Once the mini-project ships, every subsequent resume revision needs a 10-minute propagation step:

1. Update the resume's bullet / title / date.
2. Open LinkedIn → Experience → edit the same bullet / title / date.
3. If the change is significant: re-read the About — does it still match?
4. If the change involves a new project / skill: update the GitHub profile README's "Currently working on" section.
5. If the change affects your headline-worthy nouns: rewrite the headline.

**Total: ~10 minutes per significant resume change.** This is the price of keeping the three surfaces aligned through the cycle. Skip it once and the drift starts; skip it three times and the cross-surface story breaks.

The same 10-minute habit applies for the **other direction**: if you learn something on a screen ("they were really interested in my K8s experience"), propagate the emphasis to the resume's Skills line *and* the LinkedIn headline *and* the GitHub profile README's "currently working on."

## How to run the peer review

The peer review is the load-bearing part of this mini-project. Here is the protocol:

1. **Pick the peer.** Ideal: a C2 or C13 cohort member at roughly your level. Acceptable: any technical friend who has been on a hiring side recently. Avoid: a close friend who knows your work too well to skim with fresh eyes.

2. **Send a one-line request.** "Hey — I'm doing the Week-3 mini-project. Can you spend ~15 minutes doing a recruiter-skim walk on my LinkedIn and GitHub? I'll send the protocol."

3. **Send the Challenge-1 protocol.** Have them search your name, click LinkedIn, click GitHub, click one pinned repo. Time-box: 5 minutes total.

4. **Ask the Challenge-1 question set.** Write down their answers verbatim — don't filter, don't argue.

5. **Don't defend; record.** Resist the urge to explain why the headline "is really fine actually" or why the pinned repo "is more impressive than it looks." The peer's first impression *is* the recruiter's first impression. Record it.

6. **Decide what to apply.** For each piece of feedback: apply, reject (with one-line reason), or defer (with a date by which you'll revisit).

7. **Write up in `peer-review-notes.md`.** All of the above, plus a final 3-sentence reflection on what the review surfaced that you hadn't seen yourself.

## Stretch

- **Run the peer review with two peers** — one technical, one not. The non-technical peer catches jargon you've stopped noticing.
- **Add a Featured item on LinkedIn** — a link to your strongest pinned GitHub repo, a conference talk, or a blog post. Featured items render above Experience and add a second signal.
- **Build a simple personal landing page** — one HTML file, your name, a 100-word About, links to your three pinned repos, LinkedIn, and email. Host it on GitHub Pages (free). This is 2 hours of work; pays off for years as the "Google your name" anchor result.
- **Run the Week-2 30-second test** on the *main pinned repo's README* — show it to a peer for 30 seconds, then ask "what does this project do?" If they can't answer, the README opening needs work.

## Why this matters

The resume is the artifact a company *asks for*. The LinkedIn and GitHub are the artifacts a company *looks up*. By Week 3, the cost of misalignment isn't theoretical — every application you've sent this week, every recruiter who saw your resume from Week 2, may have followed up by checking the public surface. If those surfaces are stale, contradictory, or buzzword-heavy, the screen call you were hoping for didn't happen.

This is also the last week before active recruiter contact. From Week 4 onward, you'll have inbound conversations on calendar — and inbound recruiters look up the public surface *before* the call, not after. The polished version of LinkedIn + GitHub from this week is what they read while they're deciding what to say to you. Make it count.

## Submission

Commit `c13-week-03/mini-project/` to your portfolio repo. The folder should contain:

- `linkedin-screenshots/` — logged-out view of your profile (full page + first-3-lines-of-About close-up).
- `github-screenshots/` — logged-out view of your GitHub profile + the main pinned repo's README rendered.
- `cross-surface-summary.md` — the 8-row consistency table with verdicts and decisions.
- `peer-review-notes.md` — the peer's walk-through, question answers, score, and the changes you applied.
- `google-audit.md` — first 3 Google results for your name; any cleanup actions taken.
- `README.md` — a short index pointing to each file with one-line descriptions, plus links to your live LinkedIn URL and GitHub profile URL.

---

When done: open [Week 4 — The Recruiter Screen Survival Kit](../../week-04/).
