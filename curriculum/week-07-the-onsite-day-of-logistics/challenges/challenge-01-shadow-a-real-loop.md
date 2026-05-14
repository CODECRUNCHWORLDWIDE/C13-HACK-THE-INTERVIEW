# Challenge 1 — Shadow a Real Loop

**Time:** ~60 minutes (drafting and sending the informational request) plus the actual conversation if accepted, which is the candidate's bonus and not part of the challenge time budget. **Output:** A drafted, sent, and tracked informational request to a working engineer asking to be walked through their experience running interviews from the interviewer side — what the company's loop actually looks like in practice, what the rubric looks like in practice, what makes a candidate stand out, what makes them fail.

## Goal

Most of what candidates know about onsite loops comes from the candidate side: their own experiences, Glassdoor reports, Reddit anecdotes, Cracking the Coding Interview. All of these are useful and all of them are partial. The other side — what the interviewer actually does, what gets written in the debrief, what the hiring committee actually weighs, why specific candidates make it through and others do not — is much less written about because the people who have that view are working engineers who do not have time to blog.

The challenge is to script and send an informational request to a working engineer who runs interviews, asking for 30 minutes of their time to walk you through what they actually do. The request format is the entire skill; the conversation, if it happens, is the bonus.

You will not get a yes from most of the people you ask. The request format below assumes you will need to send 3-5 requests to get 1 accepted conversation. That is normal and is part of the exercise; the practice of asking, framing the ask politely, and receiving polite declines without taking them personally is itself a candidate skill.

## Setup

You need:

- **A target list of 5-10 working engineers** at companies in your target list. Each must:
  - Currently work in software engineering at a company you would want to work for.
  - Have at least 3 years of experience (junior engineers usually do not run loops or do not run them often).
  - Be reachable via a low-friction channel: LinkedIn message, alumni email, a warm introduction from someone in your network.
- **A markdown file**: `c13-week-07/shadow-requests.md`. Tracks who you asked, when, what their response was, and what you learned.
- **A separate file** for the conversation notes, if any of the requests are accepted: `c13-week-07/shadow-conversation-{engineer-name}.md`.

## Process

### Step 1 — Build the target list (15 min)

Open `c13-week-07/shadow-requests.md`. Create a table:

```markdown
# Shadow a real loop — requests

## Target list

| # | Name | Company | Role / level | How I'll reach them | Status |
|--:|------|---------|--------------|---------------------|--------|
| 1 | ___ | ___ | ___ | ___ | drafted / sent / replied / declined / accepted |
| 2 | ___ | ___ | ___ | ___ | ___ |
| 3 | ___ | ___ | ___ | ___ | ___ |
| 4 | ___ | ___ | ___ | ___ | ___ |
| 5 | ___ | ___ | ___ | ___ | ___ |
| 6 | ___ | ___ | ___ | ___ | ___ |
| 7 | ___ | ___ | ___ | ___ | ___ |
| 8 | ___ | ___ | ___ | ___ | ___ |
```

Where to find candidates for the target list:

- **Your school's alumni network.** LinkedIn alumni search for {your school} + {target company} + 3+ years of experience. The "I went to school with someone there" framing is the highest-acceptance one.
- **C13 cohort and adjacent cohorts.** Anyone in the C-Crunch network who has graduated and is now working at a target company.
- **People in your warm network** (former coworkers, former teammates, former managers) who are now at a target company.
- **Authors of public technical content** at the target company. A blog post on their engineering blog, a talk at a conference, an open-source repo. These engineers are already publicly visible and tend to have higher response rates to thoughtful requests.

The list should be 5-10 names. You will not message all of them at once; you will message them in batches of 2-3, wait 5-7 days, then send the next batch if needed.

### Step 2 — Draft the request (20 min)

The request is the load-bearing artefact of the challenge. The structure:

```markdown
Subject: 25 minutes on the interviewer side of {company}'s onsite?

Hi {name},

I'm {your one-line self-intro — student / recent grad / engineer with N
years / specifically: the role you're applying to or the level you're
targeting}. I'm in the middle of an interview cycle and one of the things
I'm trying to understand is how onsite loops look from the *interviewer*
side, not just the candidate side. The candidate side is well-documented;
the interviewer side mostly is not.

I found you through {specific path: alumni search / your blog post on X /
{mutual contact}'s recommendation / your talk at {conference}}.

Would you be open to a 25-minute call sometime in the next 2-3 weeks? I'd
want to ask about:

1. What does a typical loop at {company} actually look like from the
   interviewer's side — your prep, the round itself, the write-up,
   the debrief?
2. What separates a "lean hire" from a "lean no-hire" write-up that have
   the same technical content?
3. What are the most common avoidable failures you see in candidates
   who are otherwise strong?

I'm not asking for inside information, leaked questions, or anything
about specific candidates — just the working-engineer's perspective on
the process. Happy to send my questions ahead so you can decide what
you're comfortable answering.

I'm flexible on time and timezone. Coffee is on me if you're in
{your city}; happy to keep it virtual otherwise. No problem at all if
this isn't a good fit; thanks for considering.

Best,
{your name}
{LinkedIn link or email}
```

The framing notes:

- **The one-line self-intro is short.** Not your resume. One sentence on what you do; one sentence on what you are trying to learn.
- **"I found you through" is specific.** Not "I came across your profile"; specifically how. Alumni search, blog post, mutual contact. Vague paths to discovery read as scraped contact info.
- **The three questions are bounded and named.** Not "I'd like to learn about your work"; specifically these three. The named questions signal that you have done the work to know what to ask.
- **The "I'm not asking for inside information" line is load-bearing.** Most working engineers receive cold messages from candidates asking for leaked interview questions; the explicit disclaimer separates you from that pattern.
- **"Coffee is on me" is a small generosity signal.** Some recipients will accept the offer literally; most will not. The signal is what counts.
- **The closing is professional and accepts a decline cleanly.** "No problem at all if this isn't a good fit" is a face-saving exit for the recipient; it raises the acceptance rate because the cost of saying no is reduced.

### Step 3 — Send the first batch (5 min)

Send 2-3 messages from the target list. Note the date sent in the tracking table.

Do not send all 8 at once. Two reasons:

1. **You may revise the request after the first responses.** If three of three replies are "I'm not sure I can help with this" you have a framing problem and need to fix it before sending more.
2. **Acceptance rate is the calibration.** You want to know how many requests you need to send to get one accepted; sending in batches lets you measure.

### Step 4 — Track responses (ongoing)

In the tracking table, update each row with:

- **Date of any response.**
- **The nature of the response:** declined / accepted / pending / no response.
- **Any specific feedback** the recipient gave on the framing — useful for the next batch.

If the rate is below 1 accepted in 5 sent after a full batch, revise the request. Common revisions:

- **The opening is too long.** Cut it.
- **The ask is too vague.** Tighten the three questions.
- **The path-to-discovery is weak.** Strengthen the connection or pick a stronger target.
- **The timing is bad.** Holiday seasons, end of quarter, mid-week-of-a-launch — recipient is too busy. Reading the recipient's recent activity sometimes signals the right time.

### Step 5 — Run the conversation, if accepted (separately, not on the challenge clock)

If a request is accepted, the conversation:

- **30 minutes maximum.** You said 25; show up to 30. Respecting the time you asked for is the most useful signal of professionalism.
- **The three questions you wrote are the agenda.** Do not introduce new questions; do not turn the call into a job-search pitch.
- **Take notes.** Specific phrases the engineer uses; specific examples; specific recommendations.
- **Close with one specific follow-up offer.** "Would it be useful if I sent you my run-of-show document for your feedback?" — only if it would actually be useful; the call does not require a follow-up.
- **A thank-you message within 24 hours.** One paragraph. Specific reference to one thing they said that you found useful.

In a separate file `c13-week-07/shadow-conversation-{engineer-name}.md`, write up:

- **What they said about each of the three questions** (specific phrases, specific examples).
- **What surprised you.**
- **What you'll change in your own prep based on what they said.**

## Acceptance criteria

- The target list of 5-10 engineers is built.
- The request template is drafted, in the file, and is specific to your situation (not the generic template).
- At least 2-3 requests are sent.
- The tracking table is populated with statuses.
- If any conversation happens, the write-up file exists.
- If no conversation happens in the week (this is common; the challenge is the *sending*, not the *receiving*), the tracking table shows the attempts and you have noted lessons for future batches.

## What success looks like

The challenge is graded on the sending, not on the receiving. Sending three thoughtful requests to working engineers and getting three polite declines is a successful challenge. Sending three thoughtful requests and getting one accepted conversation is a much-better-than-average outcome — the typical conversation produces 2-3 specific habits you would not have learned from public sources alone.

The pattern, across C13 cohorts: the candidates who send 5-8 informational requests per cycle, across the months of their job search, average 1-2 useful conversations. Each conversation is high-leverage; the cumulative effect across a cycle is one of the strongest non-technical preparation moves available.

## Why this challenge matters

The interviewer-side perspective is the single largest information asymmetry in the candidate's preparation. You know what it feels like to be a candidate; you do not know what it feels like to be on the other side of the desk writing the write-up. The conversation produces that information at a level of detail unavailable from any public source — not because the information is secret, but because the people who have it do not have time to write it down for the open web.

The other reason to run this challenge: the muscle of asking strangers for their time, framing the ask well, and accepting declines gracefully is a load-bearing skill across an engineering career. The interview-prep cycle is a low-stakes context to practice it; the request format generalises to mentor outreach, conference networking, cross-team requests, and almost every workplace situation where you need something from someone you do not yet know.

## Stretch — the multi-question conversation

If one of the conversations is particularly generative, ask for a second 30-minute slot in 2-3 months specifically to debrief your job-search outcomes with them. The two-conversation pattern produces dramatically better learning than the one-conversation pattern; the second conversation is short and is focused on what you did and what you learned, not on what you wanted to learn. Most engineers who accept the first call will accept the second; some become long-term mentors.

## Stretch — the public write-up

If the conversation produces particularly useful general lessons (with the engineer's permission and with any company-specific or person-specific details removed), write a short blog post — 500-800 words — about what you learned. The post is part of your portfolio; it signals that you take the prep cycle seriously and that you can produce written artefacts at the level of detail working engineers appreciate. The C13 portfolio repo accepts these as contributions.
