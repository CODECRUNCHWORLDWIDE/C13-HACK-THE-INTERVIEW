# Exercise 1 — Build the spreadsheet

**Time:** ~45 min. **Output:** A shared, readable, version-controlled tracking dashboard.

## Goal

By the end of this exercise, you have **one** file or sheet that:

- Has the 11 columns from Lecture 2's table.
- Has 5 example rows pre-filled (real companies — pick ones you're considering).
- Is version-controlled or shared somewhere durable (Google Sheets, an Airtable, a `.md` file in your portfolio repo).

## The 11 columns (recap)

| # | Column | Type | Example value |
|--:|--------|------|---------------|
| 1 | Company | text | Stripe |
| 2 | Tier | A / B / C | A |
| 3 | First-degree contact? | bool | yes (Alex Chen) |
| 4 | Source | enum | Referral / HN / LinkedIn / Cold / Wellfound |
| 5 | Role | text | Senior Backend Engineer (Payments) |
| 6 | Comp band researched | range | 220-300k base, 90-150k equity |
| 7 | Stage | enum | Outreach sent |
| 8 | Stage entered date | date | 2026-05-13 |
| 9 | Last contact date | date | 2026-05-13 |
| 10 | Next action + due | text + date | Follow up by 2026-05-20 |
| 11 | Notes | longtext | "Alex referred me; sent note to recruiter Maria Lopez" |

## Setup steps

### A. Pick your tool

- **Google Sheets** — easiest, sharable, free. Recommended default.
- **Airtable** — slicker UI, free tier sufficient. Good if you'll add custom views.
- **Notion database** — fine, but harder to bulk-edit.
- **`tracking.md` in your portfolio repo** — version-controlled but worse UX.

### B. Create the columns

Type or paste the 11 column headers. Set column types correctly (date columns as dates, etc.).

### C. Add five example rows

Pick **5 real companies** you might want to work at. Don't make them all Tier-A — practice tiering. Fill in:

- Company name
- The tier you'd assign and why
- Whether you have a 1st-degree contact
- A plausible source (Hacker News, LinkedIn, referral, cold)
- A role title (look it up on their careers page; use a real opening)
- A researched comp band from levels.fyi
- Stage = "Not started"
- (Leave dates blank for now)
- Next action = "Research first"
- Notes = empty or "to research"

### D. Add the dropdown / validation

- Tier column: dropdown of `A / B / C`.
- Stage column: dropdown of `Not started / Outreach sent / Recruiter screen / HM screen / Tech screen / Onsite / Offer / Closed-lost / Closed-won`.

Why: keeps the data clean so you can filter and sort later.

### E. Commit / share

- If Google Sheets: set sharing to "viewable by anyone with the link" (or restricted to peers in your study group).
- If `.md` file in your repo: commit.

## Acceptance criteria

- [ ] The spreadsheet exists at a stable URL or file path.
- [ ] It has all 11 columns.
- [ ] It has 5 example rows fully populated.
- [ ] The Tier and Stage columns have validation/dropdowns.
- [ ] The link or path is recorded in your portfolio repo's `c13-week-01/exercise-01.md`.

## Stretch

- Add a "Days in current stage" computed column (today's date − stage entered date).
- Add a "Funnel summary" cell showing count per Stage.
- Set up a weekly reminder (Google Calendar / Apple Reminders) to update the spreadsheet every Friday.

## Why this matters

This spreadsheet is the operating dashboard for the next 10+ weeks. The candidates who get the offers they want are the ones who update theirs religiously. The candidates who *don't* end up confused in Week 6 about which company asked them what.

## Submission

Commit `exercise-01.md` (with the link to your sheet, or the markdown file itself) to your portfolio repo.
