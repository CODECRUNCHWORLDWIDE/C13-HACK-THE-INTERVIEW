# Lecture 3 — Outreach, Recruiters, and the ATS

> **Duration:** ~2 hours. **Outcome:** You can write a cold-outreach message that reads as written by a person, you understand how recruiter incentives shape the conversation, and you know what the ATS does to your resume before any human sees it.

## 1. Outreach messages that work

Most "interview outreach" templates online are garbage. They sound like template-output because they ARE template-output, and the recipient knows.

### What does NOT work

```
Dear Hiring Manager,

I am writing to express my interest in your position. I am a
passionate software engineer with experience in Python, JavaScript,
and full-stack development. I am a quick learner and a team player.
I would love the opportunity to contribute to your dynamic team.

Best,
Candidate Template
```

Every word in that message could appear on every other candidate's message. The recipient skims and discards. The signal you're sending is "I sent this to 200 people."

### What does work

```
Hi $name,

I noticed $company is hiring on the search team. I read $name's
2024 blog post on the indexing rewrite — the section on incremental
shard rebuilds was the most concrete writeup of that problem I've
seen this year.

I'm currently a backend engineer at $current-company; my work
includes $specific-thing that overlaps with what you described.
Resume attached; would there be 20 minutes in the next few weeks
to chat about whether there might be a fit?

Best,
$your-name
$github-url
```

What works in that version:

1. **Specific reference** to something they wrote / built. Proves you read.
2. **Your specific overlap** with their work. Not "I'm passionate"; an actual technical claim.
3. **Bounded ask** — 20 minutes, "in the next few weeks." Easy yes.
4. **Self-contained signal** — GitHub URL means they can validate quickly.

### The 60-second test

After you write a draft, set it down. Come back in an hour. Ask:

- **Could this exact message be sent to 5 other companies, unchanged?** If yes, rewrite.
- **Did I demonstrate I know something specific about them?** If no, do 20 more minutes of research, then rewrite.
- **Am I asking for less than 30 minutes of their time?** If asking for an hour, scale back.
- **Did I attach proof I'm not full of it?** GitHub link, blog post, conference talk — something.

## 2. Warm vs cold outreach

| Mode | Recipient | Conversion to call | When to use |
|------|-----------|:------------------:|-------------|
| Cold (ATS) | Recruiting team | 1-5% | When you have no contact and the public application is the only path |
| Cold (LinkedIn InMail) | Recruiter or HM | 8-20% | When you can identify the recruiter for that role |
| Cold email | Recruiter or HM (if you can find email) | 12-25% | Same but bypasses LinkedIn rate limiting |
| Warm referral | Recruiter via your contact | 30-50% | When you have 1st-degree contact |
| Warm referral with intro | Recruiter via mutual contact | 50-70% | Highest yield form of outreach |

**Implication:** spend the first hour of outreach time finding the human, not writing the message. The message is the easy part once you know who's reading it.

## 3. How to find the right person

Three reliable techniques:

### Technique A — LinkedIn structured search

Filter to "$company" + "recruiter" or "talent acquisition" or "people partner." Sort by recency of activity. The one who's been active in the last week is probably actively hiring.

### Technique B — Hacker News "Who's Hiring?"

First weekday of every month. Posts are by hiring managers themselves. Reply directly to the manager.

### Technique C — Conference talks + blog posts

If a senior engineer at your target company gave a talk in the last 12 months, they're "discoverable" and frequently respond to thoughtful outreach.

## 4. Recruiter incentives

Recruiters work in two flavors, with different incentive structures:

### External / agency recruiters

Paid 15-25% of first-year base by the company. They get paid if you accept. They get paid more if your salary is higher. Incentive: close you fast.

But also: they have *multiple* candidates and *multiple* clients. They want the deal that closes. If you're slow or unclear, they de-prioritize you.

### Internal / in-house recruiters

Salaried + sometimes a per-hire bonus. They have a "req" (a requisition) they need to fill. Their boss wants it filled this quarter.

Incentive: close at a number the hiring manager is happy with. Internal recruiters are LESS aligned with maximizing your comp than external (they have a budget; you negotiating up costs their boss).

### Implications for you

- Both types want you to close. Both types want you to close at the lower end of band.
- Both types are useful allies in the *process* and adversaries in the *negotiation*.
- Be friendly. Reply quickly. But: do NOT trust the recruiter's framing of "this is the best we can do."

## 5. The ATS — what it does to your resume

The ATS (Applicant Tracking System — Greenhouse, Lever, Ashby, Workday, etc.) is the software the company uses to manage applicants. It does several things to your resume before any human sees it:

1. **Parses** the file into structured fields (name, email, phone, work history, education).
2. **Tags** based on keyword presence ("Python," "5+ years," location).
3. **Ranks** against the job-description keywords. (Some ATSes do this; many don't.)
4. **Routes** to the right recruiter / queue.

What this means:

- **Use a standard layout.** No two-column resumes. No decorative graphics. The parser will mangle them.
- **Include the keywords from the job description.** If the JD says "Python, Django, PostgreSQL," your resume should literally say those words. (Honest signal — only if you actually know them.)
- **PDF, exported from a text-source.** Not a scanned image. Not a Word doc converted weirdly. A clean PDF.
- **Filename matters less than format**, but `Firstname-Lastname-Resume.pdf` is the convention.

### Common ATS resume bugs

- Skills listed as a column (parses as one merged string).
- Two-column layout (parses as interleaved nonsense).
- Important text inside an image (invisible to parser).
- Dates in non-standard formats ("2-3 years" instead of "2023-2024").
- Header with name/email inside a "header" section the parser ignores.

### Test it

Paste your resume into <https://resume-magic.app/> (or any free ATS parsing tool — there are several). See what comes out. If the fields look wrong, fix the resume.

## 6. The follow-up

Most candidates fail to follow up. This is free conversion you're leaving on the table.

### The pattern

1. **Send outreach.** Wait 5 business days.
2. **One follow-up** — short, polite, references your earlier message: "Following up on the note below in case it got buried. Happy to share more about $project if useful."
3. **Wait 7 business days.** If no reply, mark as cold. Move on.
4. **Optionally**, in 3-6 months, re-engage with a new angle (e.g., "saw you launched $thing, I noticed X about it").

Do NOT:
- Follow up daily.
- Follow up with "just bumping this up" with no new content.
- Take silence personally.

## 7. Self-check

- The 60-second test asks four questions. Recall three.
- Why is warm outreach 5-10x more effective than cold?
- What incentive does an external recruiter have that an internal one doesn't?
- Your two-column resume parsed badly in the ATS. What's the fix?
- A target company hasn't replied in 5 business days. What's the next move? In 12 days?

## Further reading

- **Patrick McKenzie — "How to negotiate":** <https://www.kalzumeus.com/2012/01/23/salary-negotiation/>
- **AskAManager archive — "Resume mistakes":** <https://www.askamanager.org/category/resumes>
- **levels.fyi negotiation guide:** <https://www.levels.fyi/blog/how-to-negotiate-tech-salary>

When all three Week 1 lectures are clear, the [exercises](../03-exercises/00-overview.md) get you to a working spreadsheet and 5 outreach drafts.
