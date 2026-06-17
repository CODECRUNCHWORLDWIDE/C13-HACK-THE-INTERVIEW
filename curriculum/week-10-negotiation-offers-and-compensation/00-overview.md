# Week 10 — Offers, Negotiation, and Compensation Literacy

> *The interview loop ends with an email. The email lands at 4:47 on a Thursday afternoon, three days after the onsite, and it carries the line "we would like to extend you an offer," followed by a base number, a sign-on number, a stock number, and a deadline. Most candidates, at this moment, do one of three things. They sign within twelve hours because they are afraid the offer will be withdrawn. They negotiate clumsily — by quoting a number they read on Blind, by trying to leverage an offer they do not actually have, by saying the word "lowball" in writing — and lose two thousand dollars of goodwill in the process. Or they freeze, sit on the offer for nine days, miss the deadline, and lose the offer altogether. The negotiation conversation is the only round of the loop in which the candidate has more leverage than the company. Most candidates do not know this, do not act like it, and do not realise the leverage was theirs until the offer is countersigned and the leverage is gone.*

Welcome to Week 10 of **C13 · Hack the Interview** — the final week of the track. Week 9 closed the loop on the live coding round; Week 8 covered system design; Weeks 4 through 7 walked the loop from recruiter screen through onsite day. The interview process, in the abstract, is now complete. Week 10 covers what happens after the loop — the offer letter, the negotiation conversation, the multi-offer comparison, the cost-of-living adjustment, the questions to ask before signing, the way to decline an offer without burning the bridge — and it is the week most candidates undertrain for because they are still treating "got the offer" as the finish line.

The offer is not the finish line. The offer is the start of the only negotiation the candidate will have on this job until two performance cycles from now. Whatever number gets signed in the next two weeks is, statistically, the number that will compound into raises, RSU refresh grants, and the comparable-comp baseline for the next role. A new-grad who signs at $170k total comp and a peer who negotiates to $185k will, over the four-year vesting window, differ by roughly $60,000 in pre-tax earnings — not because one is a better engineer, but because one spent forty-five minutes on a phone call that the other one was too afraid to make. The asymmetry is brutal. Week 10 closes the asymmetry.

The week leans on three free corpora. **Patrick McKenzie's "Salary Negotiation: Make More Money, Be More Valued" essay** (free on kalzumeus.com, written in 2012, still the canonical reference) is the single best free document on the negotiation conversation in tech; the principles are timeless even though some of the numbers in the original have moved. **levels.fyi** is the free crowdsourced compensation database that has become the de facto reading room for new-grad-to-staff comp in tech; the week includes a structured walkthrough of how to filter it, what the "stock per year" number means and does not mean, and the calibration loop for cross-checking a single data point against the distribution. **The U.S. Bureau of Labor Statistics (BLS) Occupational Employment and Wage Statistics** is the free government data set that anchors the cost-of-living conversation; the week includes the BLS metro-area lookup as a sanity check on numbeo's crowdsourced numbers. The 2024 FTC non-compete ruling — partially blocked by the courts but still the directional signal on how non-competes are read in the U.S. labour market — gets a short section in Lecture 2.

> **Track wrap-up sidebar — C13 · Hack the Interview, weeks 1 through 10**
>
> | Week | Title | What it shipped |
> |-----:|-------|-----------------|
> | 1 | The hiring pipeline | The map: applied → screened → onsite → offer → signed. The drop-off rates at each stage. The single number that matters (offer-rate-per-applied). |
> | 2 | Resume that survives ATS | The two-pass resume. Keyword density. The bullet-rewrite drill from "responsible for" to "shipped X that drove Y." |
> | 3 | LinkedIn, GitHub, portfolio | The triangle of public presence. The headline rewrite. The pinned repos. The portfolio site at the new-grad level. |
> | 4 | Recruiter screen survival | The 30-minute conversation. The salary expectations dodge. The "what are you looking for" framing. |
> | 5 | Hiring manager screen | The team-fit conversation. The questions back. The behavioural seedbed for the onsite. |
> | 6 | Technical phone screen | The 45-minute shared editor. The narration loop. The "I am thinking about X" filler. |
> | 7 | The onsite day-of logistics | The room-reading. The legal frame. The multi-round endurance. The lunch interview. |
> | 8 | System design 101 | The four building blocks. Back-of-envelope estimation. Six canonical problems at the 101 level. |
> | 9 | Live coding interview | The six-phase structure. The four failure modes. The record-and-watch loop. |
> | 10 | Offers, negotiation, and compensation literacy | (You are here.) Reading the offer letter. Total comp arithmetic. The negotiation call. The multi-offer decision. |
>
> Ten weeks. Twenty-eight day-by-day plans. Approximately 280 hours of structured work. The candidate who has shipped all ten weeks is interview-ready at the new-grad-to-L4 level for the standard tech onsite loop. The senior-level depth — the staff-engineer architecture interview, the bar-raiser at depth, the principal-level behavioural overlay — is in the C13 senior-track companion track (planned for a future C13 expansion). The new-grad-to-L4 baseline is what C13 ships.

## Learning objectives

By the end of this week, you will be able to:

- **Read** the offer letter line by line. Identify the base salary, the signing bonus, the stock grant, the vesting schedule, the cliff, the at-will clause, the non-solicit, the assignment-of-inventions clause, the arbitration clause, and the deadline. Know which of those are negotiable, which are boilerplate, and which deserve a lawyer review before signing.
- **Compute** total compensation across the four-year vesting window. Break out year-1 (with sign-on), year-2 through year-4 (no sign-on, post-cliff stock), and the four-year sum. Distinguish RSUs from options; compute the strike-price implications of options when the company is private and pre-IPO.
- **Run** the levels.fyi reading-room walkthrough end-to-end. Filter by company, level, location, and year. Read the percentile distribution. Compute the median, the 25th percentile, and the 75th percentile for the company-level-location triple. Recognise which data points are crowd-flagged as suspect and which are calibration-quality.
- **Hold** the negotiation conversation on the phone or by email. Get the recruiter's first move before stating your own number. Use a competing offer when you have one and frame the negotiation honestly when you do not. Push on the salary range. Recognise the recruiter's escalation phrases — "let me see what I can do," "the team is firm on this one," "we have headroom on the equity but not the base" — and respond to each in kind.
- **Identify** the four common negotiation failure modes: stating your number first, leveraging an offer you cannot substantiate, accepting the verbal offer without a written follow-up, and signing before the deadline runs out. Each has a recovery pattern; each is recoverable from if caught early.
- **Decline** an offer gracefully when you have decided to take a different one. Send the email, name the company you accepted, leave the door open for the future, and recognise the small industry — the recruiter you decline today is on the LinkedIn DM list for the next role.
- **Evaluate** offers across cost of living. Use the BLS metro-area wage data and a free crowdsourced source (numbeo or NerdWallet's free calculator) to convert a San Francisco offer to its Austin-equivalent. Recognise the limits of cost-of-living adjustments — taxes, commute, housing burn rate, and the unquantifiable "do I want to live here" factor are the actual decision drivers.
- **Ask** the questions before signing that the offer letter does not answer: PTO carryover and accrual rate, on-call expectations and frequency, the performance review cadence and calibration cycle, the equity refresh policy, the remote-work policy in writing, the relocation reimbursement claw-back, and the start-date flexibility.

## Prerequisites

- You have an offer in hand, an offer being drafted, or a realistic expectation that an offer will land in the next two to four weeks. Week 10 is the only week of C13 in which the just-in-time framing matters; the negotiation conversation is the wrong conversation to run hypothetically with no real offer on the table. If you are six months from your first offer, run Week 10 anyway and re-run it the week the offer lands.
- You completed **Week 4 — the recruiter screen** and ran the "what are you looking for in compensation" dodge at least once for real. The dodge is the seed of the negotiation conversation; the candidate who stated their number in Week 4 is starting Week 10 with reduced leverage.
- You have a **rough sense of your own walk-away number** — the minimum total comp at which you would say yes — and your **target number** — the comp at which you would say yes without hesitation. Both numbers should be informed by levels.fyi and BLS, not by Blind hearsay or a single friend's offer.
- You have **45 minutes of uninterrupted time** for the negotiation phone call when the moment comes. The negotiation is not a back-and-forth Slack thread; it is a phone call in which the candidate's tone, pauses, and willingness to sit in silence are read by the recruiter. The 45-minute uninterrupted block is the prerequisite for the call going well.
- You have **read Patrick McKenzie's essay end to end** before starting the week, or you commit to reading it Monday morning. The essay is approximately 14,000 words; the read time is 90 minutes; it is the single highest-ROI free document on negotiation in tech. The rest of the week sits on top of it.

### Bootstrap path

If you are entering Week 10 with no offer in hand and no realistic expectation of one in the next month, run the bootstrap before Tuesday:

1. Pick a real company and a real level (e.g. "Google L3 new-grad in Mountain View"). Look up the median, 25th-percentile, and 75th-percentile total comp on levels.fyi. Write the three numbers down. Compute the spread.
2. Look up the BLS metro-area wage for "software developer, applications" in the same metro. Write that number down. Note the gap between the BLS median (the labour-market floor) and the levels.fyi median (the tech-company premium).
3. Read Patrick McKenzie's essay. Take notes on the four moves you do not currently know how to make.
4. Start Lecture 1.

The bootstrap is not a substitute for the live conversation; it is the calibration baseline that the live conversation sits on top of. The candidate who runs the bootstrap is the candidate who walks into the negotiation knowing the difference between a real number and a vibe.

## Topics covered

- Reading the offer letter line by line: base, signing bonus, RSU grant, vesting schedule, cliff, at-will clause, non-solicit, non-compete (where still enforceable), assignment-of-inventions, arbitration, deadline
- Total compensation arithmetic across the 4-year vesting window: year-1, year-2 through year-4, the four-year sum; sign-on as a one-time payment; RSU vesting schedules (4-year cliff, 4-year monthly, 25/25/25/25, the Amazon back-loaded 5/15/40/40 schedule)
- RSUs versus options: the difference at private-company pre-IPO stage, the strike price, the 409A valuation, the tax treatment at vest versus exercise, the "options are worth zero until they are not" framing
- The levels.fyi walkthrough: filtering by company, level, location, year; reading the distribution; the difference between a single anecdotal data point and a calibrated median; the "this number looks too high or too low" recognition
- The negotiation conversation: getting the recruiter's first move, the salary range push, the "what are you looking for" dodge revisited, the competing-offer leverage, what NOT to disclose, the four escalation phrases and the response to each
- The four negotiation failure modes: stating your number first, leveraging an offer you cannot substantiate, accepting verbal without written follow-up, signing before the deadline
- Declining offers gracefully: the email template, the small-industry framing, the door-open phrasing, the recruiter who is on your LinkedIn DM list five years from now
- Cost of living evaluation: BLS metro-area wage data, numbeo crowdsourced cost-of-living index, NerdWallet's free cost-of-living calculator, the limits of all three; taxes (state income tax, San Francisco premium), commute, housing burn rate
- The pre-signing question list: PTO accrual and carryover, on-call expectations, performance review cadence, equity refresh policy, remote-work policy in writing, relocation claw-back, start-date flexibility
- The 2024 FTC non-compete ruling and its implications: the partial court block, the directional signal, the state-by-state enforceability matrix, the practical advice for new-grads (non-competes are largely unenforceable in California, partially enforceable in Florida and Texas, and the new-grad should not panic but should still read the clause)

## Weekly schedule

| Day       | Focus                                                | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|------------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Reading the offer letter + total-comp arithmetic     |    2h    |    0h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4h      |
| Tuesday   | levels.fyi walkthrough + BLS calibration             |    1.5h  |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4.5h    |
| Wednesday | The negotiation conversation (lecture 3) + scripts   |    2h    |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Thursday  | Negotiation drills (exercises 1, 2, 3)               |    0h    |    2h     |     1h     |    0.5h   |   1h     |     0.5h     |    0.5h    |     5.5h    |
| Friday    | Multi-offer / cost-of-living + decline drill         |    0h    |    1.5h   |     1h     |    0.5h   |   1h     |     1h       |    0.5h    |     5.5h    |
| Saturday  | Mini-project — full pipeline run                     |    0h    |    0h     |     0h     |    0h     |   1h     |     3.5h     |    0h      |     4.5h    |
| Sunday    | Quiz + reflection + track wrap-up                    |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0.5h     |    1h      |     2h      |
| **Total** |                                                      | **5.5h** | **5.5h**  | **2h**     | **3h**    | **6h**   | **5.5h**     | **3.5h**   | **31h**     |

(Slightly heavier than Week 9 because the mini-project is the C13 capstone — full offer-evaluation, negotiation rehearsal, and signed-or-declined decision narrative. The Sunday block also doubles as the C13 track retrospective.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./00-overview.md) | This overview and the C13 track wrap-up sidebar |
| [resources.md](./01-resources.md) | Patrick McKenzie's essay, levels.fyi reading-room links, BLS metro-area wage data, NerdWallet and numbeo free calculators, the 2024 FTC non-compete ruling primary source, sample offer letters, additional free reading |
| [lecture-notes/01-reading-the-offer-letter.md](./02-lecture-notes/01-reading-the-offer-letter.md) | The offer letter line by line, total-comp arithmetic, RSUs vs options, vesting schedules including the Amazon back-loaded schedule, the four-year compounding math |
| [lecture-notes/02-the-levels-fyi-reading-room.md](./02-lecture-notes/02-the-levels-fyi-reading-room.md) | How to filter levels.fyi, how to read the distribution, the BLS calibration, the cost-of-living conversion, the difference between new-grad and senior comp reading |
| [lecture-notes/03-the-negotiation-conversation.md](./02-lecture-notes/03-the-negotiation-conversation.md) | The phone call from "hi" to countersigned. The recruiter's first move. The salary range push. The competing-offer frame. The four escalation phrases. Declining gracefully. The pre-signing question list. |
| [exercises/exercise-01-the-first-move-drill.md](./03-exercises/exercise-01-the-first-move-drill.md) | A 30-minute solo drill on getting the recruiter to name a number first, with three role-play scenarios |
| [exercises/exercise-02-the-counter-offer-drill.md](./03-exercises/exercise-02-the-counter-offer-drill.md) | A 45-minute drill on counter-offering against a specific number; calibrating the ask; running the "let me see what I can do" loop |
| [exercises/exercise-03-the-multi-offer-frame.md](./03-exercises/exercise-03-the-multi-offer-frame.md) | A 30-minute drill on using a competing offer honestly, including the "I do not have a written competing offer" branch |
| [exercises/SOLUTIONS.md](./03-exercises/SOLUTIONS.md) | Strong-response scripts for each exercise, the inner-monologue narration, the recruiter's likely counter-moves and the response to each |
| [challenges/challenge-01-the-exploding-offer.md](./04-challenges/challenge-01-the-exploding-offer.md) | The "you have 48 hours to decide" drill — recognising artificial deadlines, asking for an extension, the language to use |
| [challenges/challenge-02-the-decline-email.md](./04-challenges/challenge-02-the-decline-email.md) | The decline-gracefully drill — write the email that closes the offer without closing the door for next time |
| [quiz.md](./05-quiz.md) | 12 questions, final-exam format, covering offer-letter literacy, total-comp arithmetic, levels.fyi reading, negotiation moves, cost-of-living math |
| [homework.md](./06-homework.md) | Six homework items including the "write your own salary letter" drill, plus the rubric |
| [mini-project/README.md](./07-mini-project/00-overview.md) | The C13 capstone — full offer-evaluation + negotiation rehearsal + decision narrative |
| [mini-project/RUBRIC.md](./07-mini-project/RUBRIC.md) | The self-grading rubric for the capstone |
| [mini-project/comp-calculator.py](./07-mini-project/comp-calculator.py) | A small Python helper for the comp-calc arithmetic, with type hints, that the capstone leans on |
| [mini-project/COMP-SPREADSHEET-TEMPLATE.md](./07-mini-project/COMP-SPREADSHEET-TEMPLATE.md) | The plain-text spreadsheet template (column headings, sample row, formulas) the capstone uses for offer comparison |

## Stretch goals

- Read **Patrick McKenzie's "Salary Negotiation" essay** end to end, twice. The first read picks up the framing; the second picks up the specific phrases that work because they have been tested across hundreds of negotiations. Annotate the second read; pick three phrases to use in your own conversation; rehearse them out loud. The essay is free at kalzumeus.com/2012/01/23/salary-negotiation/.
- Browse the **levels.fyi data dump** for the three companies on your shortlist, going back two years and filtering to your level. Compute the median, the 25th, the 75th, and the 90th percentile by hand or with a small script. The act of computing the distribution — rather than glancing at the top-line number — is what produces the calibrated read. The data dump is free at levels.fyi/data.
- Pull the **BLS Occupational Employment and Wage Statistics** for "software developer, applications" (SOC code 15-1252) in your target metro from bls.gov/oes. The BLS median is the labour-market floor; the levels.fyi median is the tech-company premium. The ratio between them tells you how much of the tech-company offer is the company-specific equity overhang and how much is the underlying labour-market wage. The ratio is typically 1.4 to 2.5 in the major metros.
- Read the **FTC's 2024 non-compete final rule** (the rule was partially enjoined by a Texas federal court in August 2024 but remains the directional signal). The text is free at ftc.gov/non-competes. The new-grad in California should know the rule does not change much there (non-competes have been unenforceable in California since the 1870s); the new-grad in Florida or Texas should read the rule with more care.
- Run the **NerdWallet free cost-of-living calculator** and the **numbeo cost-of-living index** for the same source-destination pair (e.g. San Francisco to Austin). The two will disagree by 10-25%. The disagreement is informative — it tells you the spread of crowdsourced cost-of-living data. Use the BLS metro wage as the calibration anchor between them.
- Run **at least one mock negotiation conversation with another human** — a study partner, a roommate, a friend who has negotiated their own offer. Give them the recruiter's script (in the Lecture 3 appendix) and run the call live for 30 minutes. The simulated pressure of being on a phone call with another voice is qualitatively different from rehearsing alone in your room.
- Read **one Blind or Glassdoor "negotiation outcome" post** for each company on your shortlist. The posts are noisy and survivorship-biased (the candidate who got a $30k bump posts; the candidate who got $0 does not). Pattern-match across at least five posts before drawing conclusions. The pattern is more useful than the individual data point.

## What "done" looks like by Sunday night

By the end of the week, the following should be true. If any of these aren't, stay with this week's work before the next offer lands.

- You can **read an offer letter line by line** and identify the base, sign-on, RSU grant, vesting schedule, cliff, at-will clause, non-solicit, assignment-of-inventions, arbitration, and deadline. You know which lines are negotiable, which are boilerplate, and which deserve a lawyer review.
- You can **compute total comp** across the four-year vesting window for any standard offer in under five minutes — by hand, with the comp-calculator helper, or in a spreadsheet. You can break out year-1 (sign-on included), year-2 through year-4 (no sign-on), and the four-year sum.
- You can **run the levels.fyi walkthrough** end to end. You can filter, read the distribution, compute the median and the percentile spread, recognise crowd-flagged suspect entries, and produce a calibrated "this offer is at the 40th percentile for this company-level-location" read.
- You can **hold the negotiation conversation** on the phone for 30-45 minutes. You can get the recruiter's first move, push on the range, use a competing offer honestly, run the four escalation phrases, and ask for the written follow-up before agreeing to anything in writing.
- You have **identified the four negotiation failure modes** and you can articulate the recovery move for each: state-your-number-first (recover by re-anchoring on the recruiter's range), unsubstantiated leverage (recover by withdrawing the leverage and resetting on the substantive case), accepting verbal without written (recover by emailing for the written follow-up immediately), signing-before-deadline (no recovery; do not do this).
- You can **decline an offer gracefully**. You have written at least one decline email in the homework. You know the door-open phrasing and the small-industry framing.
- You can **evaluate offers across cost of living**. You have used the BLS metro wage, numbeo, and NerdWallet on at least one source-destination pair. You can articulate the limits of cost-of-living adjustments.
- You can **ask the pre-signing questions** without sounding adversarial: PTO accrual and carryover, on-call expectations, performance review cadence, equity refresh policy, remote-work policy in writing, relocation claw-back, start-date flexibility.
- You have **completed the C13 capstone mini-project**: a written offer-evaluation, a rehearsed negotiation, and a final decision narrative. The capstone is the artefact you carry out of the track.

This is the new-grad-to-L4 negotiation baseline. The senior-track depth — the staff-engineer multi-offer compaction across four companies, the equity-refresh strategy across a multi-year retention horizon, the founder-to-IC offer conversation — is in the C13 senior-track companion week (planned for a future C13 expansion). The new-grad-to-L4 baseline is what Week 10 ships.

## C13 track retrospective

Week 10 is the last week of C13. Before closing the laptop on Sunday night, take 30 minutes for the track retrospective. Open the README of each of Weeks 1 through 10 and re-read the "what done looks like" section at the bottom. For each week, write one sentence on what landed and one sentence on what did not. The pattern of "what did not" across the ten weeks is the input to the next track you run — whether that is the C13 senior-track companion, a parallel C-track on a different specialisation, or a return to C1 for the foundational depth.

The interview loop, end to end, is a learned skill. The candidate who has shipped C13 has the structural baseline. The candidate who has shipped C13 *and* run one full real interview loop with one real offer has the calibrated baseline. Both are valuable. C13 produces the first; the next 90 days produce the second.

## Up next

C13 is complete. The natural next tracks, depending on direction:

- **C7 · Crunch Wire** for the systems-and-networks depth that turns the L4 baseline into the L5 baseline over a 24-week semester.
- **C23 · CRUNCH-AGENTS** for the agent-and-tooling skill that the 2026 hiring market is paying a premium on.
- **C1 · Code Crunch Convos** as a return to the Python foundations, if the foundational depth is the gap surfaced by the C13 retrospective.

The next offer will land in three weeks or three months. The work of Week 10 — the offer-letter literacy, the comp arithmetic, the negotiation conversation, the multi-offer frame, the cost-of-living math — is the work that compounds across every offer for the next 30 years. The first offer is where the muscle is built. The tenth offer is where the muscle pays.
