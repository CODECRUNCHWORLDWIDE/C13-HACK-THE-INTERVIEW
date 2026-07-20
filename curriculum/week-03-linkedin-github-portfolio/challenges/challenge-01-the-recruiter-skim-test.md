# Challenge 1 — The recruiter skim test

**Time:** ~60 minutes. **Difficulty:** Easy/Medium. **Materials:** Your updated LinkedIn + GitHub, a stopwatch, two willing peers.

## Problem

A recruiter who's interested in you typically does the following in 60-90 seconds:

1. Googles your full name. Notes the first 3 results.
2. Clicks your LinkedIn. Reads the headline, photo, current title, and first 3 lines of About.
3. Clicks your GitHub link from the LinkedIn or the resume. Looks at the profile README and the pinned repos.
4. Maybe clicks into one pinned repo and skims the top of its README.
5. Decides whether to schedule the screen.

You're going to find out whether your three surfaces (Google results, LinkedIn, GitHub) tell a *consistent and current* story when read in that order, by someone who has never met you.

## The protocol

### Part A — Self-walk (10 min)

In a **private / incognito browser window** (not logged into anything), do the recruiter walk yourself:

1. Search Google for `"Your Full Name"`. Note the first 5 results.
2. Click your LinkedIn from the search. Read for 30 seconds. Close the tab.
3. From memory, write down what you saw on LinkedIn.
4. Open your GitHub directly (not logged in). Read for 60 seconds. Close the tab.
5. From memory, write down what you saw on GitHub.

Capture in `c13-week-03/challenge-01-skim-test.md`:

- **Google results:** Did your LinkedIn surface in the top 3? Your GitHub? Anything that didn't belong (an old account, a namesake who confuses)?
- **LinkedIn 30-second recall:** What's your current title and company (as you remember reading them)? Was your photo current? What did the first sentence of your About say? Any keyword nouns you remember?
- **GitHub 60-second recall:** What did the profile README tell you about who this person is? What were the three pinned repos and what does each do (in one phrase)?

The point: **what you remember is what a recruiter remembers.** If you struggle to recall a current title or a pinned repo's name, the layout has buried the signal.

### Part B — Peer walk (40 min — including coordination)

Find **two peers** — one who knows your work, one who doesn't. The "doesn't know you" peer is the more valuable signal.

For each peer:

1. Send them a one-line message: **"Search my name on Google, then click through to LinkedIn and GitHub. Spend 90 seconds total. Then I'll ask you questions."**
2. Don't preface, don't direct, don't share links. The search is the test.
3. After 90 seconds, send them this question set:
   - What's the most recent title and company you saw? (Test of LinkedIn headline + current-title fields.)
   - What technologies would you say this person works with? Name up to 5.
   - What's the most recent / current project they're working on? (Test of LinkedIn About / GitHub profile README parity.)
   - Of the pinned repos on GitHub, what does each one do? Name them.
   - On a scale of 1-5, how clear is this person's professional shape? (5 = "I could pitch them to a hiring manager in one sentence." 1 = "I have no idea what they do.")
   - Was there anything confusing, contradictory, or stale?

4. **Wait for their answers before sharing context.** Do not coach mid-walk.

### Part C — Diagnose (10 min)

Compare the three walks (your self-walk + two peer walks) in your write-up. For each question:

- Did all three surfaces converge on the *correct* answer?
- Did anyone surface a *wrong* answer? If so, which surface caused the wrong impression?
- Did peer 1 (who knows you) and peer 2 (who doesn't) report *the same picture*? If not, the public surfaces are sending different signals than your in-person reality.
- Any contradictions across LinkedIn / GitHub / Google results? (E.g., LinkedIn says "Senior Backend Engineer at Acme"; GitHub profile README says you're an "ML researcher at BetaCo." Pick one or explain.)

Close the write-up with a **Top 3 cross-surface fixes** section listing the three changes most likely to improve the next person's walk.

## Acceptance criteria

- [ ] `c13-week-03/challenge-01-skim-test.md` contains:
  - Your self-walk results (Google, LinkedIn, GitHub).
  - Two peer-walk transcripts (questions + their answers).
  - A per-question diagnosis comparing the three walks.
  - A "Top 3 cross-surface fixes" section.
- [ ] You have applied at least **one** of the fixes before submitting the mini-project.

## Common findings

- **Google surfaces something stale.** An old Twitter, a 2014 blog post, a high-school site. The fix: lock down or delete the old account, or push more recent signal to crowd it out.
- **Headline read as different from current title.** Your LinkedIn headline calls you "Backend Engineer" but the current-role field calls you "Software Engineer II." Peers reported confusion. Fix: align.
- **GitHub pinned repos didn't match the LinkedIn story.** LinkedIn says "payments engineer"; GitHub pins are three machine-learning notebooks. Either the LinkedIn is wrong about your focus, the pins are wrong, or you genuinely have two specializations and need to pick one for this cycle.
- **No GitHub link from LinkedIn.** The peer found the LinkedIn but couldn't get to the GitHub without searching separately. Fix: add the GitHub URL to your LinkedIn contact info and About.
- **The profile README contradicted the About.** Your LinkedIn About says you're shipping the X service at Acme; your GitHub profile README says "Currently building Y on my own." Both true, perhaps — but the contradiction makes the reader pause. Pick the framing that's most current.

These are all common. None require throwing anything away. Each is a 5-15 minute fix once you see it.

## Stretch

- Run the test with **a non-engineer peer** as well. A friend who works in marketing or design will read your surfaces with fresh eyes and catch jargon you've stopped noticing.
- Run the test on **a target company's career page**: search for their job posting, then search your name in their applicant portal context (if you can simulate it). What story is your public surface telling about your fit?
- Reverse the test: do the walk on a peer's public surface. Tell them what you remember from each step. Notice the patterns; the next time you audit your own, you'll be sharper.

## Why this matters

By Week 3 you've spent ~50 hours on resume, LinkedIn, and GitHub. The fear is local: you've stared at each surface so long you've stopped seeing it. The peer walk is a 30-minute correction — it tells you what the *outside view* shows, before a recruiter or hiring manager makes that view consequential.

The fixes that come out of this exercise are usually small. Five-minute edits. But the cumulative effect — the headline matches the GitHub, the GitHub pins match the resume, the Google result is current — is the difference between "this person is together" and "I'm not sure what's going on here." The first gets a screen; the second does not.

## Submission

Commit `c13-week-03/challenge-01-skim-test.md` to your portfolio repo. Optional: include the (anonymized) peer transcripts.
