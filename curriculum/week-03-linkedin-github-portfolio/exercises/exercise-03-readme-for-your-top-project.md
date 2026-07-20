# Exercise 3 — README for your top project

**Time:** ~75 minutes. **Output:** A real, runnable, reviewer-friendly README for the **main project** repo from Exercise 2.

## Goal

Of the three repos you pinned in Exercise 2, the **main project** carries the most weight. A hiring manager who clicks into it will read its README and decide what kind of engineer you are. This exercise builds that README from scratch using the 8-section structure from Lecture 2, §6.

## Setup

You need:

- The repo you tagged as **Main** in Exercise 2. Clone it locally if you haven't.
- 30 minutes where you can actually run the project yourself, end-to-end, on a clean checkout. (This often reveals broken setup steps that the README will need to address.)
- A markdown editor.
- A screenshot tool (macOS `Cmd-Shift-4`, Windows Snip & Sketch, or `screencapture` CLI). Optionally a tool to capture a short GIF (LICEcap, Kap on Mac, ScreenToGif on Windows).

## Process

### Step 1 — Run the project from scratch yourself (15 min)

In a fresh shell, simulate a hiring manager who just cloned your repo and has no context:

```bash
cd /tmp
git clone {your-repo-url}
cd {repo-name}
# What's the next command?
```

Try to get it running using only what's in the current README. Note every place you got stuck:

- Did `make`/`npm install`/`pip install` work without surprise?
- Was there a config file or env var you forgot to mention?
- Did you need a dependency (Postgres, Redis, etc.) the README doesn't list?
- Did the demo command produce the output the README implies?

Write down every friction point. This list drives the **Quick start** rewrite in Step 4.

### Step 2 — Capture a screenshot or demo output (10 min)

A README without visible output is invisible to the skim reader. Capture one of:

- **A screenshot** of the project running (web UI, dashboard, terminal). Save as `docs/demo.png` in the repo.
- **An animated GIF** of a short demo (5-15 seconds, under 5 MB). Save as `docs/demo.gif`.
- **A sample terminal session** as text (`docs/example-output.txt`). For CLI tools.
- **A 5-line code example** showing how to use the library, ready to paste at the top of the README. For libraries.

Pick the form that fits your project. A web app should show a screenshot; a CLI tool should show terminal output; a library should show a 5-line usage example.

### Step 3 — Draft the README using the 8-section structure (35 min)

Open the repo's `README.md` and **start over** — keep nothing from the old version unless it's specifically right. Build, in order:

```markdown
# {Project name}

{One-sentence description — what it is and what problem it solves. ~20 words.}

{Visual: image, GIF, code example, or terminal session. First screen of the README.}

## Quick start

```bash
{command 1}
{command 2}
{command 3}
```

{One sentence describing what the reader should see after running the above.}

## Why

{1-2 short paragraphs. What problem motivated this. What alternatives existed.
 Why those alternatives weren't enough. What this project does that's different.}

## How it works

{Short architecture description. 4-6 bullets or a small diagram.
 For libraries: API surface + design decision.
 For applications: component breakdown + key technology choices.}

## Status

- **Works:** {what's solid}
- **Rough:** {what's there but unpolished}
- **Not yet:** {what's planned but unbuilt}

## Tech

{One line listing the main technologies. Languages, frameworks, databases, deploy target.}

## License

{One line: MIT / Apache-2.0 / etc. + link to LICENSE file.}
```

**Constraints:**

- Total length: **200-500 lines** of markdown (roughly 800-2,000 words).
- The first 30 lines (the description, the visual, the Quick start) must stand alone — a reader who reads only those 30 lines should walk away with a correct impression of what the project is and how to run it.
- Every command in Quick start must work on a clean checkout. Test by following Step 1 again on a freshly-cloned copy.
- The **Why** section must not start with "This is a project I built for class" or "I made this to learn X." Lead with the problem; the motivation is implied.
- The **Status** section must be honest. If something doesn't work, say so.

### Step 4 — Verify the Quick start (10 min)

In a fresh shell again:

```bash
rm -rf /tmp/{repo-name}
cd /tmp
git clone {your-repo-url}
cd {repo-name}
# Run exactly the commands from your Quick start, in order.
```

Did it run end-to-end? If no, fix the README and try again. **The Quick start must work** — if a reviewer hits an error in the first 3 commands, they bounce.

### Step 5 — Add a LICENSE if missing (5 min)

If your repo has no LICENSE file, add one. The default for most personal portfolio projects is MIT. Either:

- Use GitHub's "Add file → Create new file → LICENSE" — GitHub offers a license-picker UI.
- Or paste the MIT license text from `https://opensource.org/license/mit` and replace the year and copyright holder.

A repo without a license technically can't be legally used by others; the absence reads as carelessness. Fix it.

## Acceptance criteria

- [ ] README is rewritten, not edited from the old version.
- [ ] First 30 lines contain: title, one-sentence description, visual, Quick start.
- [ ] Quick start has been **tested on a fresh clone** and runs end-to-end.
- [ ] Why, How it works, Status, Tech, License sections all present.
- [ ] Total length 200-500 lines of markdown.
- [ ] Status section is honest — at least one item under "Rough" or "Not yet."
- [ ] LICENSE file exists in the repo.
- [ ] `docs/demo.{png,gif}` or equivalent exists and is referenced in the README.
- [ ] A teammate / peer (or, lacking that, you yourself in a different terminal) successfully ran the Quick start and reported success.

## Common mistakes

- **README written before the visual.** Always have the visual ready first. If the project doesn't produce something visible, find a way (a screenshot of a passing test suite, a sample API response, a terminal trace).
- **Three-paragraph "About this project" before any code.** Cut. The reader wants to see it run before they read the philosophy.
- **Untested Quick start.** The single most common README failure. If `pip install` errors on a fresh machine because `requirements.txt` is missing one dependency, the README has lied.
- **Buzzwords in the description.** "Enterprise-grade, scalable, performant" — cut. Use specific nouns: "Postgres-backed," "supports retries," "no external dependencies."
- **Architecture diagram drawn in ASCII or hand-drawn.** Optional, but if you include one, make sure it's legible at first glance. A confusing diagram is worse than no diagram.

## Stretch

- Add a **`CONTRIBUTING.md`** if you'd realistically welcome PRs. One paragraph is enough.
- Add a **GitHub Actions CI badge** at the top of the README. (Use shields.io for the badge URL.) The badge shows your tests pass — small but real signal.
- Write a **short blog post** (300-600 words) about the project: what you built, what you learned, what you'd do differently. Link it from the README. This is the highest-leverage stretch — it gives recruiters a second artifact to share.
- Run the **30-second skim test** (from Week 2, Challenge 1) on your README. Have a peer look at it for 30 seconds, then ask: "what does this project do?" Did they answer correctly?

## Why this matters

The pinned-repo README is, in many hiring loops, the only piece of your real code a hiring manager will read. The screen interviewer often opens this README 5 minutes before the call, skims it, and walks in with the question "tell me about this project" already loaded.

If the README is structured and clear, the screen becomes a guided tour: you walk through the architecture you've already documented, and the manager has context to ask good follow-ups. If the README is missing or weak, the screen becomes an interrogation: you're explaining from scratch under time pressure, and every minute spent on context is a minute not spent on the technical signal.

**Build the README once, well, and it pays off across every hiring loop for years.**

## Submission

The README lives in the repo, not in your portfolio. Commit and push to the repo. Also commit a note to `c13-week-03/exercise-03-readme-link.md` listing:

- The repo URL.
- The Quick-start verification result.
- The before/after line count of the README.
- Any decisions you made about scope (what you cut, what you kept).
