# Exercise 2 — Pin three best repos

**Time:** ~75 minutes. **Output:** A curated GitHub profile with a profile README, three intentionally pinned repos, and hidden/archived clutter.

## Goal

Audit your current GitHub profile against the five failure modes from Lecture 2, §3. Then choose three repos to pin (with reasons), set up your profile README, and clean up the long tail. The result is a profile that a hiring manager can read in 90 seconds and walk away with a correct impression.

## Setup

You need:

- Your GitHub account, logged in.
- A second browser tab in **private / incognito mode**, also on your GitHub profile URL — to see what an outside viewer sees.
- A markdown file: `c13-week-03/exercise-02-github-audit.md`.

## Process

### Step 1 — Audit (15 min)

In your draft file, open with a structured audit. Use the five failure modes from Lecture 2.

```markdown
## GitHub audit — before

**Profile URL:** github.com/yourhandle

**Profile README present?** Yes / No
> If yes, paste the current content. If no, mark "TO CREATE."

**Pinned repos (current):**
1. [repo-name] — [one line on what it is]
2. ...
(0, 3, or 6 — note the count)

**Total public repos:** [N]
**Of those, forks:** [F]
**Of those, your originals:** [N - F]

**Most recent commit on any repo:** [date]
**Activity grid density (rough):** Dense / Medium / Sparse / Dead

**Failure-mode checklist (from Lecture 2, §3):**
- [ ] Failure 1 — No profile README
- [ ] Failure 2 — No pinned repos / wrong pinned repos
- [ ] Failure 3 — Pinned repos with broken or absent READMEs
- [ ] Failure 4 — Fork graveyard (>20 forks visible)
- [ ] Failure 5 — Stale activity / dead account appearance
```

Check the boxes that apply. **Don't be defensive.** Most engineers have 3+ of these. The audit is the input to the cleanup.

### Step 2 — Inventory your repos (15 min)

In the same file, produce a table of every public repo you own:

| # | Name | Type (original / fork) | Has README? | Status (active / stale / archived / experimental) | Worth pinning? (Y/N/Maybe) | One-line description |
|---|------|------------------------|-------------|---------------------------------------------------|---------------------------|----------------------|

Be honest in the "Worth pinning?" column. A pin-worthy repo:

- Is yours (not a fork).
- Has at least a working README (or you can write one this week).
- Demonstrates real engineering (not a 30-line script unless the script is unusually clever).
- Has something visible — a screenshot, sample output, or runnable demo.
- Is something you'd defend in a 5-minute conversation with a senior engineer.

Most engineers' tables come out with 2-5 maybes. That's normal.

### Step 3 — Choose three (10 min)

From your "maybe" set, choose three using the breakdown from Lecture 2, §7:

- **One main project repo** — your deepest piece of work.
- **One breadth repo** — different skill or technology.
- **One polish repo** — small, clean, easy to run.

Write the chosen three in your audit file with a 2-3 sentence justification each:

```markdown
## Pinned-repo decision

**Main:** [repo-name]
> Why: [what this demonstrates — language, scale, architectural choice. Why this over the other candidates.]

**Breadth:** [repo-name]
> Why: ...

**Polish:** [repo-name]
> Why: ...
```

If you have fewer than three pin-worthy repos, **that's a signal**. Decide now: spend the rest of this week building one small but real repo to fill the gap (and pin only what you have until then), or pin two and leave the third slot empty. Two pinned strong repos beat three slots where one is weak.

### Step 4 — Set up the profile README (15 min)

Create the repo `github.com/{your-username}/{your-username}` if it doesn't exist. (Repo name must equal your username, case-sensitive.) Initialize with a `README.md`.

Using the structure from Lecture 2, §5, draft your profile README:

```markdown
# {Your name}

{One-sentence intro: who you are, what you do, the 1-2 technologies to associate with you.}

## Currently working on

- {Bullet 1 — what you're building / learning / shipping}
- {Bullet 2}

## Notable projects

- **[{repo-name}](link)** — {one sentence: what it is, what it demonstrates}
- **[{repo-name}](link)** — ...
- **[{repo-name}](link)** — ...

## Elsewhere

- Site / blog: {URL if you have one}
- LinkedIn: linkedin.com/in/{handle}
- Email: {address}
```

Constraints:

- 100-250 words total.
- No "skills" lists.
- No animated GIFs, ASCII art, badge marquees, GitHub stats widgets.
- No "passionate about technology" or near-synonym.
- Every project bullet is one sentence and names the repo by link.

Commit the README to the profile repo. Open your profile in a private browser window; confirm the README renders above the pinned repos area.

### Step 5 — Pin and clean up (10 min)

In GitHub UI:

1. On your profile, click **Customize your pins**.
2. Pin the three chosen repos. Save.
3. For each fork or experimental repo you don't want visible: open the repo's settings → consider deleting (if you don't need it), archiving (if it's done), or making it private (if you might come back to it).
4. For each remaining original repo: confirm it has at least a stub README. (You don't need to polish all of them this week — Exercise 3 polishes the top one. The rest just need to not look broken.)

### Step 6 — Confirm in the logged-out view (5 min)

Open your profile in a private window. Check:

- The profile README renders at the top, formatted correctly.
- Three pinned repos appear above the fold. Click each — does it open to a README that has at least the structure?
- Below the fold, the public repo list is curated (no obvious tutorial-fork dump).
- The activity grid: if mostly gray, does the profile README mention where your real work lives?

Screenshot the logged-out profile view and save to `c13-week-03/exercise-02-screenshots/`.

## Acceptance criteria

- [ ] `c13-week-03/exercise-02-github-audit.md` contains the audit, the inventory table, the three-repo decision with justifications, and the profile README draft.
- [ ] Profile README is live at `github.com/{username}/{username}` and renders on your profile page.
- [ ] Three repos are pinned (or two, with documented reason).
- [ ] Each pinned repo has at least a stub README (full polish in Exercise 3).
- [ ] Fork graveyard reduced: no more than ~5 visible forks on the profile, unless they're genuine contribution destinations.
- [ ] Logged-out screenshot of the profile saved.

## Common mistakes

- **Pinning by recent activity instead of quality.** GitHub's auto-suggestions are not a curation tool. Pick intentionally.
- **A profile README with no project links.** The README is a directory; if it doesn't direct visitors to specific repos, it's filler.
- **Hiding everything.** A profile with 3 pinned repos and 0 other public ones can look thin. Some longer-tail repos are fine, as long as none of them are embarrassing.
- **Pinning a repo whose `main` branch doesn't run.** A pinned project that errors on `git clone && make` is worse than no pin.
- **Animated GIF banner in profile README.** Strip.

## Stretch

- For each unpinned-but-worth-keeping repo, write a one-paragraph README polish (5 min each). Aim for none of your visible repos having a "TODO" README.
- Browse 5 profiles from the **awesome-github-profile-readme** gallery. Find one whose structure you like but rephrase nothing — just structure, not voice.
- Look up the profiles of 3 engineers at your Tier-A target companies (their LinkedIn often links to GitHub). Compare their pin choices. What patterns hold across them?

## Why this matters

Your GitHub is the third surface a recruiter sees (after the resume and the LinkedIn) and the **first** surface a hiring manager opens before the screen. The pinned repos are the framing — they tell the manager what kind of engineer to expect in the conversation tomorrow. Wrong pins = wrong expectations = bad screen.

This exercise also surfaces the question: **do you have three repos worth pinning at all?** If the answer is no, you've identified the most important thing to spend the rest of this cycle on outside of C2: build one real, complete, well-documented repo that will pin for the next 3 years.

## Submission

Commit `c13-week-03/exercise-02-github-audit.md`, the logged-out screenshots, and (separately) push your profile README to `github.com/{username}/{username}`.
