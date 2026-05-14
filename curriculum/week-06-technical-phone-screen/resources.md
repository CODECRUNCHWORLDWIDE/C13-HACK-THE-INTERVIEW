# Week 6 — Resources

Free, public, no signup unless noted.

## Shared editors — official docs and free tiers

- **CoderPad** — the most-used shared editor in tech screens. Free tier is fine for practice (no recording on free tier; the interview pads are timed). Read the candidate documentation before Tuesday:
  <https://coderpad.io/resources/docs/coderpad/>
- **HackerRank CodePair** — second-most-used. Different keyboard shortcuts and test-runner UI from CoderPad; the muscle memory does not transfer cleanly. Free trial sufficient for practice:
  <https://www.hackerrank.com/products/codepair>
- **CodeSignal** — used by some companies (Robinhood, Meta for a stretch) for both async and live screens. The "general coding framework" is similar enough to CoderPad that practice transfers; the UI does not:
  <https://codesignal.com/developers/>
- **Karat** — a third-party interview service used by many companies. Karat sessions record by default and the interviewer is a Karat-employed engineer, not from the hiring company. Their candidate guide is the closest public approximation to what their interviewers score:
  <https://karat.com/candidates/>
- **Google Doc / Zoom screen-share / Replit** — fallbacks some smaller companies use. Lower friction than the dedicated tools but no test runner; you'll execute mentally or out of a local terminal.

## Problem banks — the easy tier

The technical phone screen draws almost exclusively from the easy and lower-medium LeetCode tier. Do not grind hards this week.

- **LeetCode — top 100 liked easy problems** (free):
  <https://leetcode.com/problemset/all/?difficulty=EASY>
- **NeetCode 150** — curated set covering the patterns that come up in phone screens. The "Arrays & Hashing," "Two Pointers," and "Strings" categories are the highest-leverage for Week 6:
  <https://neetcode.io/>
- **Blind 75** — a smaller, older, well-known list. Overlaps significantly with NeetCode 150; either is fine:
  <https://www.techinterviewhandbook.org/grind75/>
- **Tech Interview Handbook — algorithm cheatsheets** — short pattern summaries with example problems:
  <https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/>

## Narration and thinking-out-loud

- **Gayle Laakmann McDowell — "Cracking the Coding Interview"** (book; library is fine). Chapter 7 on the interview process and chapter 11 on testing are the most relevant for Week 6; the algorithms chapters are Week 7.
- **Pramp — recorded mock interviews on YouTube** — watch one full mock end-to-end before Friday's pair mock. Notice the narration cadence of strong candidates:
  <https://www.youtube.com/@Pramp>
- **interviewing.io — public recorded mocks** (free archive). Anonymous engineers running real-shape problems. The transcripts include the interviewer's debrief comments — the closest public artifact to "what the scorer is writing":
  <https://interviewing.io/recordings>
- **Yoodli** — AI-assisted speaking feedback; useful for the narration drill in Exercise 2 (transcribes, flags filler words, measures pace). Free tier sufficient:
  <https://yoodli.ai/>
- **Bytebytego — coding-interview narration guide** — short, practical, focused on the spoken-output side of the call:
  <https://bytebytego.com/>

## The four scoring dimensions

- **Google's published interview rubric** — the most-public version of what most companies score on. The "general cognitive ability + role-related knowledge + leadership + Googleyness" axes are Google-specific, but the technical breakdown maps to most companies' screens:
  <https://www.google.com/about/careers/applications/how-we-hire/>
- **Meta's coding-interview overview** — official Meta engineering interview guide; the technical-screen segment is roughly mid-document:
  <https://www.metacareers.com/swe-prep-onsite>
- **Amazon's bar-raiser primer** — Amazon's interview structure is unusual but the technical-screen scoring is broadly representative of bigtech:
  <https://www.amazon.jobs/en/landing_pages/in-person-interview>
- **Tech Interview Handbook — the rubric section** — a synthesised public view of what most rubrics look like:
  <https://www.techinterviewhandbook.org/coding-interview-rubrics/>

## Live-coding tooling

- **A recording app** — Loom, QuickTime, or OBS for screen + audio capture during Exercise 2 and the mini-project. CoderPad's own recording is paid; use one of these for free coverage. Loom free tier captures 5 minutes per recording; OBS is unlimited.
- **A stopwatch** — phone is fine. The 5-minute, 25-minute, and 5-minute beats of the 35-40 minute coding block all benefit from being on the clock during practice.
- **A second monitor or notepad** — for the scratch work that does not belong in the editor. Many candidates lose minutes by writing trace tables in the actual code pane.
- **A wired headset** — audio drops are the most-common avoidable failure during technical screens. Bluetooth dies; wired does not. Worth twenty dollars.

## Style references

- **Coding Interview University** — a long open-source study guide; the section on "the day before the interview" and "how to behave" is the most-relevant Week-6 content:
  <https://github.com/jwasham/coding-interview-university>
- **Clement Mihailescu — AlgoExpert blog posts** (public ones, no signup). The "how to think out loud" essay is the canonical short reference:
  <https://www.algoexpert.io/>
- **Reddit r/cscareerquestions — "interview experiences" tagged threads** — anecdotal but high-signal for what specific company technical screens feel like. Search "{company} phone screen" before you take one:
  <https://www.reddit.com/r/cscareerquestions/>
- **Glassdoor — interview questions by company** — the most-useful Glassdoor surface; reports of actual phone-screen problems from named companies. Take individual reports with skepticism, but the patterns across reports for a given company are real signal:
  <https://www.glassdoor.com/Interview/index.htm>

## Language choice references

- **Python — official tutorial and standard library docs**. Most candidates pick Python for phone screens; it is the highest-readability language for live narration. The collections module (Counter, deque, defaultdict) and the itertools module are heavily used:
  <https://docs.python.org/3/>
- **JavaScript — MDN reference** for the array methods (map, filter, reduce, slice) that account for most of the live-coding surface in JS:
  <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>
- **Java / C++ / Go** — official references. If you pick one of these, be confident in the iteration and collection idioms — fighting with Java's HashMap iteration mid-call is a recognisable tell of the wrong language pick.
- **Tech Interview Handbook — language-choice guide**:
  <https://www.techinterviewhandbook.org/programming-languages-for-coding-interviews/>

## Tools you'll use this week

- **A shared editor** — CoderPad or HackerRank CodePair, free tier, account created before Tuesday.
- **A recording app** — Loom, QuickTime, or OBS. Screen + audio captures for the narration drill and the mini-project.
- **A stopwatch** — phone stopwatch is fine. The narration drill and the 45-minute mock both have timing components.
- **A peer who will play interviewer for 45 minutes** — for Exercise 1 and the mini-project. Ideal: a C13 cohort member, a C2 peer, or a friend at an engineering company.
- **A laptop with a markdown editor** — VS Code, Cursor, anything. The drafts and reflection live in your portfolio repo.
- **A notebook or scratch pad** — for the trace tables, the example-by-hand work, and the brute-force sketches. Do not put trace tables in the shared editor; it confuses the interviewer and wastes characters on the screen.
- **A wired headset** — audio drops are the most-common avoidable failure during a real call. The pair mock should be done with whatever audio setup you plan to use on the real call.

## Style references for the followup-email

- **Pramp — post-interview follow-up examples** — short, well-templated:
  <https://www.pramp.com/>
- **Tech Interview Handbook — the post-interview section** — the standard 24-hour follow-up to the recruiter after a technical screen. Shorter than the HM-screen follow-up:
  <https://www.techinterviewhandbook.org/post-interview/>

## Glossary

| Term | One-line definition |
|------|---------------------|
| **Technical phone screen** | 45-minute live-coding call on a shared editor, run by an engineer (not the hiring manager), usually after the HM screen and before the onsite. One or two easy LeetCode-shape problems. |
| **Shared editor** | A web-based IDE both interviewer and candidate edit in real time. CoderPad, HackerRank CodePair, CodeSignal, Karat, Replit, Google Doc are all variants. |
| **CoderPad** | The most-used commercial shared editor for tech screens. Vendor: CoderPad Inc. Free tier suitable for practice. |
| **HackerRank CodePair** | A second commercial shared editor; UI and shortcuts differ from CoderPad. Used at HackerRank-customer companies. |
| **Karat** | A third-party interviewing service; Karat-employed engineers run screens on behalf of hiring companies. Recorded by default. |
| **The five-phase narration loop** | Restate / example-by-hand / brute force / optimise / code-while-narrating. The structure of a strong live-coding session. |
| **Thinking out loud** | The skill of describing your problem-solving as it happens, in a way the interviewer can score against the rubric. Most candidates underrate it. |
| **The four scoring dimensions** | Problem-solving, coding, communication, and testing. Most rubrics use these four with minor renamings. |
| **The follow-up question** | The interviewer's last 5-10 minutes of the call: complexity analysis, problem extension, production framing, or edge-case probe. Always asked; rarely well-handled. |
| **Brute force first** | The principle that the first solution proposed should be the obvious one, even if O(n²) or worse. Skipping the brute force is a recognisable failure mode. |
| **Examples-by-hand** | Walking through the problem on a concrete input before any coding, to surface ambiguities and confirm the spec. Five minutes here saves twenty later. |
| **Editor hygiene** | Picking a language, naming the function, setting up the test harness, knowing the shortcuts of your editor. The first 90 seconds of the call should be invisible to the interviewer. |

---

*Broken link? Open an issue.*
