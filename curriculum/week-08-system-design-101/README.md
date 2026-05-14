# Week 8 — System Design 101: FAANG-Style Design Rounds for New-Grad and L4

> *Coding rounds filter for "can you build a 30-line function in 45 minutes." Design rounds filter for something different: can you reason about a system you have never built, at a scale you have never operated, in front of an interviewer who has built and operated that scale, without freezing, without bluffing, and without disappearing into one corner of the problem for 40 of the 45 minutes. The design round does not score whether you arrive at the "right" architecture — there is rarely a single right one. It scores how you navigate the space.*

Welcome to Week 8 of **C13 · Hack the Interview**. Week 7 produced the day-of logistics, the room-reading, the legal frame, the deflection language, and the 4-hour onsite mock. The pipeline keeps moving. The candidates who landed an onsite this cycle have already run their first one, or are running it this week, or have one scheduled in the next 2-3 weeks. Week 8 returns to the technical surface — but to the part of the technical surface that most new-grad and early-career candidates have spent the least preparation time on.

System design is the round where the variance between candidates is largest. Two candidates with identical LeetCode scores can produce wildly different design rounds — one passes the new-grad bar comfortably, one fails it outright — and the difference is almost never raw knowledge. The difference is method. A method for what to say in the first 5 minutes. A method for how to spend the middle 30 minutes. A method for when to commit to a specific number versus when to call it "depends." A method for when to admit "I have not built this" and what to do next.

For new-grad and L4 candidates, the design round at most FAANG-tier companies is not a deep-systems exam. It is a *baseline competence* exam: can you talk about an API, draw a diagram, name a database, estimate a back-of-envelope number, and identify two trade-offs. Pass the baseline and you pass the round; miss the baseline and no amount of distributed-systems theory rescues you. Week 8 builds the baseline.

The week is not a substitute for *Designing Data-Intensive Applications* or for actually building distributed systems at work. It is the round-specific layer above whatever depth you already have. Candidates with a year of backend experience and Week 8's method will outperform candidates with three years of backend experience and no method, in the same way that Week 6 candidates with the narration loop outperformed silently brilliant candidates in the technical screen.

## Learning objectives

By the end of this week, you will be able to:

- **Run** the 45-minute design round on a structured timing: 5 minutes of requirements clarification, 5 minutes of high-level architecture, 10 minutes of API and data model, 15 minutes of deep dive on one component, 5 minutes of trade-offs and scale, 5 minutes for the interviewer's questions and yours. Hit each transition out loud; never disappear silently into one phase for 25 minutes.
- **Identify** the four building blocks every distributed system is composed of — compute (stateless servers and workers), storage (relational, document, key-value, blob), caching (in-memory caches in front of storage), queues (asynchronous messaging between services) — and reach for them as the default vocabulary in the high-level phase.
- **Estimate** back-of-envelope numbers in under two minutes: daily active users to queries per second, queries per second to peak QPS, item size to storage per year, request size to bandwidth, read-write ratio to cache sizing. The arithmetic is grade-school; the discipline is the cost.
- **Apply** Jeff Dean's "Numbers Every Programmer Should Know" — L1 cache, main memory, SSD, network round-trip, datacenter round-trip — as the latency calibration behind every design decision. Distinguish "this is a 1ms problem" from "this is a 100ms problem" from "this is a 1-second problem."
- **Design** the six classic 101-level problems at the level expected for a new-grad or L4 candidate: URL shortener (TinyURL), rate limiter, news feed, chat (one-to-one and group), distributed cache, ride-sharing match. Hit the four building blocks in each; produce a defensible high-level diagram; name two trade-offs.
- **Read** the rubric: what passing a new-grad design round looks like vs. what a senior L5+ candidate is expected to add (multi-region failure modes, deeper consistency analysis, capacity planning for a 100x scale event, organisational scoping of the design). Recognise that you are not being scored against the senior bar; recognise that interviewers occasionally drift the question up to senior depth and that the strong move is to surface the level shift, not to pretend you can answer it cold.
- **Recover** from the two most-common design-round failure modes: the "I have never seen this system" freeze and the "I have built exactly this system at work and now I am giving the round my opinions instead of designing one" drift.

## Prerequisites

- You completed **Week 7**. The onsite logistics, the room-reading, the hostile-question deflection are on muscle memory. The 4-hour mock revealed at least one gap — Week 8 will close one of them.
- You have **completed at least one CS data-structures course or its equivalent** (linked lists, hash tables, trees, heaps, graphs). Week 8 assumes you can answer "what data structure backs a key-value store" without looking it up.
- You have **basic HTTP fluency** — what a GET versus a POST does, what a status code is, what a header is, what a JSON payload looks like. If any of these are shaky, spend an hour on MDN's HTTP overview before Monday (linked in resources).
- You have **written at least one backend service**, even a toy one, even just a Flask or Express app talking to SQLite. The course-project depth is enough. Total-greenfield candidates should run the bootstrap path below.
- You have **drawn a system diagram at least once in your life**, on a whiteboard or in Excalidraw or on paper. The muscle is shockingly thin in candidates who have only read about distributed systems and never drawn one.

### Bootstrap path

If your backend experience is minimal, run the bootstrap before Tuesday:

1. Spin up a Flask "Hello World" app that talks to a local Postgres or SQLite. ~30 minutes.
2. Put an Nginx reverse proxy in front of it on localhost. ~30 minutes.
3. Put a Redis cache in front of one read endpoint. ~30 minutes.
4. Write down the architecture as a four-box diagram: client, Nginx, Flask, Postgres, with Redis as a fifth box on the side.

That toy stack contains four of the five building blocks the week relies on. The week's design problems are scaled-up versions of the same shape. If you cannot reproduce the toy stack, the week's lectures will feel abstract; if you can, the lectures will feel like the formalisation of something you have already touched.

If you have only one week of prep and a design round on Friday, prioritise in this order: Lecture 1 (the 45-minute structure), Exercise 1 (the URL shortener walkthrough), the mini-project end-to-end design write-up. Skip the homework drills if you must; do not skip the mini-project.

## Topics covered

- The 45-minute design round as a timed performance: the six phases, the timing budget, the transitions out loud, the recovery moves when one phase eats another phase's budget
- The four building blocks of every distributed system: compute, storage, caching, queues. The variants of each, the costs, the default choice at the 101 level
- The 101-level storage taxonomy: relational (Postgres, MySQL), document (MongoDB), key-value (Redis, DynamoDB), wide-column (Cassandra), blob (S3). When each is the obvious default
- The 101-level caching taxonomy: in-process cache, distributed cache (Redis, Memcached), CDN. The cache-aside and write-through patterns. Cache invalidation as the canonical hard problem
- The 101-level queue taxonomy: message queue (RabbitMQ, SQS), distributed log (Kafka). Pub/sub vs. work queue. When async is the right answer
- Back-of-envelope estimation: DAU to QPS, average QPS to peak QPS (typically 3-5x), storage per record times records per year, request size times QPS for bandwidth, read-write ratio for cache hit-rate sizing
- Jeff Dean's latency numbers, the 2010 version, updated for modern hardware: L1 ~0.5ns, main memory ~100ns, SSD random read ~150μs, datacenter round-trip ~500μs, cross-region round-trip ~50-150ms
- The CAP theorem at the 101 level (you have to mention it; you do not have to lecture on it) and the consistency-availability trade-off as it appears in design rounds
- The six classic 101 problems: URL shortener, rate limiter, news feed, chat, distributed cache, ride-sharing match. The canonical solution shape for each
- The new-grad-passing rubric vs. the senior-passing rubric: what depth is expected at L3/L4 vs. L5+, what the interviewer is and is not allowed to expect from a new grad
- Diagram conventions: the boxes, the arrows, the labelled edges, when to use a sequence diagram vs. an architecture diagram, the Mermaid syntax for shared editors
- The two failure modes: the freeze ("I have never seen this") and the drift ("I have built this and I am opining instead of designing")
- The senior-drift drift: when the interviewer pushes the question above the candidate's level, how to recognise it, how to ask for the level recalibration without losing the round

## Weekly schedule

| Day       | Focus                                                | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|------------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | The 45-minute structure + four building blocks       |    2h    |    0h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     4h      |
| Tuesday   | Back-of-envelope estimation + latency numbers        |    1.5h  |    1.5h   |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Wednesday | The six classic problems (lecture 3)                 |    2h    |    1h     |     0h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Thursday  | Design exercises (URL shortener, rate limiter)       |    0h    |    2h     |     1h     |    0.5h   |   1h     |     0h       |    0.5h    |     5h      |
| Friday    | News feed exercise + senior-drift challenge          |    0h    |    1.5h   |     1h     |    0.5h   |   1h     |     1h       |    0.5h    |     5.5h    |
| Saturday  | Mini-project — full TinyURL design write-up          |    0h    |    0h     |     0h     |    0h     |   1h     |     3.5h     |    0h      |     4.5h    |
| Sunday    | Quiz + reflection + peer review of mini-project      |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0.5h     |    0.5h    |     1.5h    |
| **Total** |                                                      | **5.5h** | **6h**    | **2h**     | **3h**    | **6h**   | **5h**       | **3h**     | **30.5h**   |

(Comparable to Week 7 in total budget; the exercise load is slightly higher because each design exercise is a 40-90 minute write-up rather than a 20-minute drill.)

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./README.md) | This overview |
| [resources.md](./resources.md) | ByteByteGo free posts, High Scalability, DDIA free chapters, Jeff Dean's latency numbers, AWS / GCP / Azure free architecture references |
| [lecture-notes/01-the-45-minute-design-round.md](./lecture-notes/01-the-45-minute-design-round.md) | The six-phase structure, the four building blocks, transitions out loud, recovery from a phase that ran long |
| [lecture-notes/02-back-of-envelope-and-latency-numbers.md](./lecture-notes/02-back-of-envelope-and-latency-numbers.md) | DAU-to-QPS, storage-per-year, bandwidth, peak vs. average; Jeff Dean's latency table; when to commit to a number, when to call it "depends" |
| [lecture-notes/03-the-six-classic-problems.md](./lecture-notes/03-the-six-classic-problems.md) | URL shortener, rate limiter, news feed, chat, distributed cache, ride-sharing — the canonical 101-level shape of each |
| [exercises/exercise-01-url-shortener-walkthrough.md](./exercises/exercise-01-url-shortener-walkthrough.md) | 60-minute solo design of a URL shortener, with a sample-strong-answer SOLUTIONS.md |
| [exercises/exercise-02-rate-limiter.md](./exercises/exercise-02-rate-limiter.md) | 60-minute solo design of an API rate limiter, with a sample-strong-answer SOLUTIONS.md |
| [exercises/exercise-03-news-feed.md](./exercises/exercise-03-news-feed.md) | 75-minute solo design of a social news feed, with a sample-strong-answer SOLUTIONS.md |
| [challenges/challenge-01-senior-drift.md](./challenges/challenge-01-senior-drift.md) | The "interviewer pushed the question to senior depth" drill — recognise and recalibrate |
| [challenges/challenge-02-the-rubric.md](./challenges/challenge-02-the-rubric.md) | Build the new-grad vs. L5+ rubric in your own words and score one of your exercise write-ups against it |
| [quiz.md](./quiz.md) | 10 questions on phase timing, building blocks, estimation, the six problems |
| [homework.md](./homework.md) | Six design drills (~6h), with rubric and time estimates |
| [mini-project/README.md](./mini-project/README.md) | The full TinyURL clone end-to-end design write-up — requirements, API, data model, deep dive, trade-offs, scale, with Mermaid diagrams |

## Stretch goals

- Read **Alex Xu's free ByteByteGo blog post on the URL shortener**. It is the canonical free reference for the most-asked design problem; the post is short and the diagrams are clean. The paid Volume 1 book repeats and extends this; the free blog post is enough for the new-grad bar.
- Read **the High Scalability post archive's "real-life" series**. Pinterest, Instagram, Stack Overflow, Discord, Slack, Reddit, Twitter — each post is one company's actual architecture at one point in time. Read at least two; the gap between the textbook design and the production reality is the most-useful single thing you can carry into an interview.
- Read **Designing Data-Intensive Applications, Chapter 1 (free preview on O'Reilly)**. Kleppmann's framing of "reliability, scalability, maintainability" is the right vocabulary for the trade-offs phase of any design round. The full book is paid but the public library carries it.
- Watch **Jeff Dean's "Building Software Systems at Google" talk** (Stanford, 2010, free on YouTube). It is the source of the "numbers every programmer should know" table; the table has aged surprisingly well. Hearing him narrate the numbers fixes them in memory in a way that reading them does not.
- Watch **one full system-design mock on interviewing.io's public archive**, ideally one labelled "L4" or "new grad." The pacing reveals what the round actually feels like and which 5-minute windows the strong candidates spend on which work.
- If you are interviewing at AWS, GCP, or Azure: read at least one **reference architecture** from the cloud provider's documentation. They are free, they are detailed, and the vocabulary aligns with what your interviewer will use.

## What "done" looks like by Sunday night

By the end of the week, the following should be true. If any of these aren't, stay with this week's work before moving on.

- You can talk through the **six phases of a 45-minute design round** by name, the time budget for each, the transition phrase you say out loud at each phase boundary, and one recovery move for when one phase eats into the next.
- You can name the **four building blocks** (compute, storage, caching, queues) and, for each, the 101-level taxonomy (relational/document/KV/blob; in-process/distributed cache/CDN; message queue/distributed log) and the default choice for a 101-level design problem.
- You can do a **back-of-envelope estimation** from a single DAU number: DAU → QPS average → QPS peak → storage per year → bandwidth per second, all on a whiteboard in under two minutes, with arithmetic you can defend.
- You can recite **Jeff Dean's latency numbers** at the order-of-magnitude level: L1 ~ns, RAM ~100ns, SSD ~100μs, network within datacenter ~500μs, cross-region ~100ms. You know which decisions each number bounds.
- You have **designed the URL shortener end-to-end** in the mini-project — requirements, API, data model, deep dive on the ID generation, trade-offs, scale — with Mermaid diagrams and a written rubric self-score.
- You have **designed two more of the six classic problems** (rate limiter and news feed in the exercises) at the level of detail expected for a new-grad round.
- You have **a written rubric**, in your own words, of what new-grad-passing looks like vs. what L5+ would add — and you can score your own write-ups against it without flinching.
- You have **identified at least one specific weak spot** in your design fluency (most candidates: a building block they have never used, or a problem class they have never seen) and have a plan for closing it before the real round.

This is the design-round baseline. The senior-level depth — multi-region failure, deeper CAP analysis, organisational scoping — is in the C13 senior-track companion week (planned for a future C13 expansion). The new-grad-to-L4 baseline is what Week 8 ships.

## Up next

[Week 9 — Behavioural Depth and the Hiring-Manager Round](../week-09/) — once the design-round structure, the building blocks, the estimation, and the six classic problems are on muscle memory. Week 9 returns to the behavioural surface from Week 5, this time at the depth required for the full onsite behavioural round, the bar-raiser round at Amazon, and the hiring-manager final conversation: the STAR-format deep dive, the conflict question, the leadership-principle prep at Amazon, the "tell me about a time you failed" recovery, and the questions you ask back.
