# Week 8 — Resources

Free, public, no signup unless noted. The week leans on four classes of source: (1) ByteByteGo's free blog and free YouTube content for the canonical 101-level problem walkthroughs, (2) the High Scalability archive for real-company architecture writeups, (3) the free preview chapters of *Designing Data-Intensive Applications* and other canonical references, and (4) Jeff Dean's public talks for the latency-numbers vocabulary.

The week deliberately avoids paid courses, paywalled chapters, and signup-walled content. The free corpus on system design at the 101 level is large enough to ship the week without any paid material. If you find the free material insufficient for a deep dive, the paid resources are listed at the bottom as optional follow-ups for after the loop.

## ByteByteGo — free blog and free videos

Alex Xu's *System Design Interview* books are the most-cited single reference for the 101-level design round. The books are paid. ByteByteGo's blog and YouTube channel publish free content that overlaps substantially with the book material and is the canonical free source for the canonical 101 problems.

- **ByteByteGo blog** — the main blog page with the free posts. The newsletter is free; the deep-dive paid posts are clearly marked. The free post archive is the relevant target for Week 8:
  <https://blog.bytebytego.com/>
- **ByteByteGo YouTube channel** — short (5-15 minute) animated videos for each of the canonical problems. The URL shortener video, the rate limiter video, the news feed video, the chat video, the distributed cache video — all free. The pacing is fast; pause and sketch the diagrams as you watch:
  <https://www.youtube.com/@ByteByteGo>
- **Free chapter previews of System Design Interview Volume 1** — Amazon and Google Books usually surface the URL-shortener chapter (Chapter 8 in older editions) in the free preview. The preview rotates; if the URL-shortener chapter is not visible, the rate-limiter chapter usually is:
  <https://www.amazon.com/System-Design-Interview-Insiders-Guide/dp/B08CMF2CQF>

Read the free blog posts in the order: URL shortener → rate limiter → news feed → chat → distributed cache → ride-sharing. That order matches the lecture sequence and matches the order from easiest to hardest at the 101 level.

## High Scalability — real-company architecture writeups

High Scalability is the long-running blog of real-world architecture postmortems and feature-launch writeups. The site has been operating since 2007; the archive is deep. The most-useful Week-8 reads are the "Real Life Architecture" series and the "Stack Overflow Architecture" series. The gap between the textbook design from ByteByteGo and the production architecture on High Scalability is the most-useful single thing you can carry into a real design round — it grounds your defaults in real systems rather than in interview-prep fiction.

- **High Scalability — main**:
  <http://highscalability.com/>
- **High Scalability — "Real Life Architectures" tag**:
  <http://highscalability.com/real-life-architectures>
- **High Scalability — Stack Overflow Architecture (2016, classic):**
  <http://highscalability.com/blog/2016/2/29/a-1000x-faster-stack-overflow-database.html>
- **High Scalability — Instagram architecture (early):**
  <http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html>
- **High Scalability — Discord (storing billions of messages):**
  <http://highscalability.com/blog/2018/4/9/how-discord-stores-billions-of-messages.html>
- **High Scalability — Pinterest (growth and architecture):**
  <http://highscalability.com/blog/2013/4/15/scaling-pinterest-from-0-to-10s-of-billions-of-page-views-a.html>

Read at least two of these before Wednesday. The Discord post is particularly useful — it shows the exact "we switched from Cassandra to ScyllaDB" decision that a senior candidate would mention in a chat-design trade-offs phase, framed in the company's own words. You are not expected to recite this in a new-grad round; you are expected to recognise that production trade-offs exist and are sometimes the answer to "what would you change if you had more time?"

## Designing Data-Intensive Applications — free chapter excerpts

Martin Kleppmann's *Designing Data-Intensive Applications* (often abbreviated DDIA) is the canonical depth reference for distributed systems. The full book is paid. The publisher (O'Reilly) and Amazon offer free previews that consistently include Chapter 1 ("Reliability, Scalability, and Maintainability") and parts of Chapter 2 ("Data Models and Query Languages"). Both are directly relevant to Week 8's trade-offs vocabulary.

- **DDIA — official site**:
  <https://dataintensive.net/>
- **O'Reilly free chapter 1 preview** — the "Reliability, Scalability, Maintainability" framing that every design-round trade-offs phase should use:
  <https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/>
- **DDIA references and further reading** — Kleppmann's own list of the papers and books behind each chapter, free on the official site. The references for chapters 1, 2, 5, 6, 9, 11 are the most-relevant Week-8 reading:
  <https://github.com/ept/ddia-references>

The full book is widely available at public libraries (Libby, Hoopla, OverDrive). If you have library access and the time before your design round, read chapters 1, 5 ("Replication"), 6 ("Partitioning"), and 9 ("Consistency and Consensus") in that order. These four chapters are the senior-bar reading; the new-grad bar does not require them but the candidate who has skimmed them performs visibly better in the trade-offs phase.

## Jeff Dean's "Numbers Every Programmer Should Know"

Jeff Dean's talk and slides from the early 2010s established the canonical latency table that every design round implicitly references. The original numbers are slightly dated for modern hardware (SSDs are faster, networks are faster, RAM is faster); the order-of-magnitude relationships are still valid. Lecture 2 treats the updated 2020-era numbers; the original slides are the primary source.

- **Jeff Dean — "Building Software Systems at Google" (Stanford, 2010, free YouTube)**. The talk includes the latency-numbers slide; pause around minute 17 to see the table. The full talk is 55 minutes; the latency segment is ~3 minutes:
  <https://www.youtube.com/watch?v=modXC5IWTJI>
- **Jeff Dean — "Designs, Lessons and Advice from Building Large Distributed Systems" (slides)**. The keynote slides with the latency table on slide 24:
  <https://research.google.com/people/jeff/stanford-295-talk.pdf>
- **Latency numbers interactive visualisation** (Colin Scott) — an updated, interactive version of the table that lets you scrub through time from 1990 to projected 2020:
  <https://colin-scott.github.io/personal_website/research/interactive_latency.html>

The visualisation is the highest-leverage single resource for the latency vocabulary. Spend 10 minutes on it; the order-of-magnitude intuitions are the kind of thing the round will probe by asking "is that fast or slow?" without giving you a baseline.

## AWS, GCP, Azure — free reference architectures

The three large cloud providers publish detailed reference architectures for the kinds of systems Week 8 asks you to design. These are free, vendor-flavoured (each provider's architecture uses their own services), and the vocabulary aligns with what your interviewer will use if they work at a cloud-using company.

- **AWS Architecture Center**:
  <https://aws.amazon.com/architecture/>
- **AWS — URL shortener reference architecture** (search the architecture center for "URL shortener"):
  <https://aws.amazon.com/blogs/compute/build-a-serverless-private-url-shortener/>
- **AWS — Well-Architected Framework** (free, comprehensive). Chapter on reliability is the most-cited:
  <https://aws.amazon.com/architecture/well-architected/>
- **Google Cloud Architecture Center**:
  <https://cloud.google.com/architecture>
- **Azure Architecture Center**:
  <https://learn.microsoft.com/en-us/azure/architecture/>

If you are interviewing at AWS specifically, the AWS Well-Architected Framework is mandatory reading. If you are interviewing at Google, the GCP architecture pages plus Jeff Dean's talk are the canonical pair. If you are interviewing at Azure or Microsoft, the Azure Architecture Center plus its "patterns" subsection. The vocabulary mismatch ("you said S3, I would say Cloud Storage") will be quietly noted; using the company's vocabulary is a small but real signal.

## Free academic papers — the senior-bar reading

The original papers behind the systems Week 8 references are free, well-written, and short enough to read in a 30-60 minute sitting each. New-grad candidates are not expected to have read them; reading even one materially upgrades your trade-offs vocabulary.

- **Google's MapReduce paper (2004)** — Dean and Ghemawat. The canonical batch-processing paper; the lineage of Hadoop, Spark, and every large-scale data pipeline since:
  <https://research.google/pubs/pub62/>
- **Google's Bigtable paper (2006)** — Chang et al. The wide-column data model; the lineage of HBase, Cassandra, ScyllaDB:
  <https://research.google/pubs/pub27898/>
- **Amazon's Dynamo paper (2007)** — DeCandia et al. The canonical eventually-consistent KV store; the lineage of DynamoDB, Cassandra, Riak:
  <https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf>
- **Google's Spanner paper (2012)** — Corbett et al. The globally-distributed strongly-consistent database; the lineage of CockroachDB, YugabyteDB, TiDB:
  <https://research.google/pubs/pub39966/>
- **Facebook's Memcache paper (2013)** — Nishtala et al. The canonical distributed-cache-at-scale paper; the production reality behind the textbook "put Redis in front of the database":
  <https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf>
- **Kafka paper (2011)** — Kreps, Narkhede, Rao. The canonical distributed-log paper:
  <https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf>

Read one before Wednesday; the Dynamo paper is the highest-leverage single read for the design-round trade-offs vocabulary. It introduces consistent hashing, quorum reads/writes, vector clocks, and hinted handoff — every one of which can come up in a trade-offs phase.

## HTTP and API design — free references

- **MDN — HTTP overview**. The canonical free reference for HTTP fundamentals. The "Overview" and "Methods" pages are mandatory pre-reading for any candidate whose HTTP fluency is shaky:
  <https://developer.mozilla.org/en-US/docs/Web/HTTP>
- **MDN — HTTP status codes** — the full list with one-paragraph explanations:
  <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>
- **Google — API Design Guide** (free). The canonical reference for "what does a clean REST API look like" — the API phase of every design round implicitly scores against guidelines like these:
  <https://cloud.google.com/apis/design>
- **Microsoft — REST API Design Guidelines** (free, on GitHub):
  <https://github.com/microsoft/api-guidelines>
- **OpenAPI / Swagger spec** (free) — the standard for API definition. You do not need to write OpenAPI in the round; recognising it is a useful signal:
  <https://swagger.io/specification/>

The Google API Design Guide is the highest-leverage single read for the API phase. Most new-grad candidates produce a vaguely-RESTful API in the design round that fails small-but-noticeable conventions (verbs in URLs, plural-singular mismatch, status-code misuse). Twenty minutes with the guide closes most of those.

## Mermaid diagram syntax — free reference

The mini-project requires Mermaid diagrams; many shared editors (CoderPad, HackerRank, GitHub markdown, GitLab markdown, the Atlassian suite) render Mermaid inline. Knowing the syntax means you can produce a clean diagram on a shared editor when whiteboard is not an option.

- **Mermaid — official documentation**:
  <https://mermaid.js.org/>
- **Mermaid — flowchart syntax** (the most-relevant for architecture diagrams):
  <https://mermaid.js.org/syntax/flowchart.html>
- **Mermaid — sequence diagram syntax** (the most-relevant for API and request-flow diagrams):
  <https://mermaid.js.org/syntax/sequenceDiagram.html>
- **Mermaid Live Editor** (free, browser-based, no signup) — paste a diagram, see it render. Use this to sanity-check the syntax before committing it to a shared editor in a round:
  <https://mermaid.live/>

The lectures use Mermaid for every diagram. The mini-project requires it. Spend 30 minutes with the Live Editor on Monday; the syntax is small enough to commit to memory and the round-time savings are real when the shared editor renders it natively.

## Other canonical free references

- **The Twelve-Factor App** (Heroku, free) — the canonical short statement of "what a well-designed service looks like." Twelve principles, two paragraphs each, all directly relevant to the deep-dive phase:
  <https://12factor.net/>
- **Site Reliability Engineering** (Google, full book free online) — the canonical SRE reference. Chapters on monitoring, capacity planning, and incident response are the most-relevant for Week 8's scale-and-trade-offs phase:
  <https://sre.google/sre-book/table-of-contents/>
- **The Site Reliability Workbook** (Google, free online) — the companion to the SRE book, with practical exercises. Chapters on SLOs and on alerting are the most-useful for the trade-offs phase:
  <https://sre.google/workbook/table-of-contents/>
- **AWS Builders' Library** (free) — Amazon's published essays on how they build the systems they run. The "Caching challenges and strategies" essay is the canonical 101-level caching read:
  <https://aws.amazon.com/builders-library/>
- **Martin Fowler — bliki (architecture essays)** — short, free, canonical writeups on patterns like CQRS, Event Sourcing, Microservices, the strangler-fig pattern. Use the "DataLake," "MicroservicePremium," and "MonolithFirst" essays to inoculate yourself against the "always use microservices" interview answer:
  <https://martinfowler.com/bliki/>
- **The C4 model** (Simon Brown, free) — the canonical lightweight architecture-diagram model. The "Container" and "Component" diagram levels are what your design-round diagrams will most resemble:
  <https://c4model.com/>

## Practice surfaces — free mock infrastructure

- **Pramp** — free peer-to-peer mock interview matching, including system-design rounds. The match algorithm pairs you with a peer at a similar level; you alternate interviewer and interviewee. Free with a Google or GitHub account:
  <https://www.pramp.com/>
- **interviewing.io — public archive**. The paid product is the mock-interview marketplace; the free public archive includes recorded mocks across coding, design, and behavioural. Watching one design mock in full is the highest-leverage single hour of Week-8 prep:
  <https://interviewing.io/recordings>
- **Excalidraw** (free, browser-based) — the canonical free diagramming tool for system design. No signup. The "library" includes pre-built shapes for common system-design components:
  <https://excalidraw.com/>
- **draw.io / diagrams.net** (free, browser-based) — the heavier-weight free diagramming alternative. Better for formal diagrams; slower for the napkin-sketch style of a design round:
  <https://app.diagrams.net/>

The Pramp peer match is the closest free analogue to a real design round. The match is rough — the peer's level is variable, the question quality varies — but the practice of running a 45-minute structured design out loud in front of another human is high-leverage and impossible to fake solo.

## What this week deliberately does not assign

- **Paid courses** — System Design Interview by Alex Xu (paid book), Grokking the System Design Interview by Educative (paid), DesignGuru (paid), and similar. The free corpus is sufficient for the 101-level bar. If you have the budget and want a paid resource, Alex Xu Volume 1 is the most-recommended; treat it as a follow-up after the loop, not as a prerequisite.
- **Leetcode-style system-design "questions"** — there are paid drill platforms that gamify system-design problems. The format does not match the real round and the gamification produces wrong intuitions. Skip them.
- **YouTube "I solved a FAANG system design interview" content from non-credentialed creators** — the variance is enormous; the bad content is confidently wrong; the time cost is high. If you want video content, ByteByteGo and Gaurav Sen are the two channels with consistent technical accuracy. Watch them.

## What to read this week, in order

If you have ~6 hours of resource-reading budget across the week, spend it in this order:

1. **MDN HTTP overview + Google API Design Guide** (Monday) — 60 minutes. Closes the API-phase fundamentals.
2. **One ByteByteGo blog post: URL shortener** (Monday) — 30 minutes.
3. **One ByteByteGo blog post: rate limiter** (Tuesday) — 30 minutes.
4. **Jeff Dean's Stanford talk, minutes 15-25 (the latency section)** (Tuesday) — 15 minutes.
5. **Colin Scott's latency visualisation** (Tuesday) — 15 minutes.
6. **DDIA Chapter 1 (free O'Reilly preview)** (Wednesday) — 45 minutes.
7. **One ByteByteGo blog post: news feed** (Wednesday) — 30 minutes.
8. **One High Scalability post: Discord or Stack Overflow** (Thursday) — 30 minutes.
9. **One academic paper: Dynamo or Memcache at Facebook** (Friday) — 60 minutes.
10. **Mermaid Live Editor, syntax practice for flowchart + sequence diagram** (Saturday morning) — 30 minutes, before the mini-project.

This sequence is the minimum-viable Week-8 reading. If you have more time, the High Scalability archive is the deepest free well to fall into; the AWS Builders' Library is the second-deepest. Both reward repeat reading; neither demands a single sitting.
