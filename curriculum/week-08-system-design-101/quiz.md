# Week 8 — Quiz

Ten questions. Lectures closed.

---

**Q1.** A candidate has 45 minutes for a system-design round. They spend the first 12 minutes asking detailed requirements questions. They feel they have been thorough. Which best describes the cost of the choice?

- A) No cost — the requirements phase is the most important and time spent here is always well spent.
- B) The cost is borne entirely in Phase 6 (questions for the interviewer); the candidate will simply have fewer questions to ask.
- C) The cost compounds across the remaining four phases (high-level, API, deep dive, trade-offs) and most often shows up as a deep dive that is shorter than the 15-minute budget, a trade-offs phase that is rushed or skipped, and an overall debrief writeup that reads "candidate could not be evaluated on the deep dive." The 5-minute target on requirements is not a suggestion; it is the runway the rest of the round needs.
- D) The candidate should always spend ~15 minutes on requirements regardless of the time budget.

---

**Q2.** The four building blocks of every 101-level distributed system are:

- A) Microservices, containers, Kubernetes, service mesh.
- B) Compute (stateless servers and workers), storage (relational, document, key-value, blob), caching (in-memory caches in front of storage), and queues (asynchronous messaging between services).
- C) HTTP, JSON, REST, OAuth.
- D) AWS, GCP, Azure, on-premise.

---

**Q3.** A candidate is designing a URL shortener and the prompt specifies 100M new URLs per day. Their estimation produces:

- Average writes: 1,200/sec
- Peak writes: 5,000/sec
- Storage per year: 7TB raw

The interviewer asks "what's your actual infrastructure storage footprint over a year?" The strongest response is:

- A) "7 terabytes — that's what the math says."
- B) "Roughly 25-30TB, applying a 4x multiplier for indexes, replication (typically 3-way), and a 30-day backup retention window. The infrastructure footprint is meaningfully larger than the raw data; that matters for capacity planning."
- C) "It depends — I can't commit to a number."
- D) "About 100TB to be safe."

---

**Q4.** Jeff Dean's latency numbers, at the order-of-magnitude level, place an SSD random read at:

- A) ~1 ns
- B) ~100 ns
- C) ~100 μs (microseconds, between 16μs for NVMe and 150μs for SATA)
- D) ~10 ms

---

**Q5.** In a news-feed design, the "fan-out on write" strategy is most problematic when:

- A) The follower count is small (under 100 followers per user).
- B) A user with a very large follower count (millions) posts. A single post triggers millions of timeline writes, which is expensive and asymmetric. The hybrid approach — fan-out on write for normal users, fan-out on read for celebrity users — addresses this; the threshold (e.g., 100k followers) is a tunable knob.
- C) The user is logged out.
- D) The post is text-only.

---

**Q6.** A candidate is asked, mid-design-round, "What's your CAP-theorem trade-off here?" They have heard of CAP but cannot articulate the trade-off at depth. The strongest response is:

- A) Bluff confidently: "I'd pick AP because availability matters more than consistency for this use case." (and hope the interviewer doesn't probe)
- B) "I know the concept — CAP forces a choice between consistency and availability under partition — but I haven't designed at the depth where the trade-off feels concrete to me. The high-level shape of the answer is [partial answer]. I'd want to be more careful than I can be in 4 minutes; happy to take it as a follow-up." Calibrate honestly; do not bluff.
- C) "I don't know what CAP is."
- D) Pretend to be confused by the question and ask the interviewer to define every term.

---

**Q7.** A rate limiter for a public API at 1M requests/sec needs to add <10ms of overhead. The candidate proposes Redis as the counter store. The latency math:

- A) Two Redis ops per request × ~50μs each ≈ 100μs of overhead; well within the SLO.
- B) Redis is too slow for this; use a relational database instead.
- C) Each request requires a Redis transaction with multiple locks; ~50ms of overhead.
- D) Latency depends on the region; cannot be computed.

---

**Q8.** A candidate finishes the deep-dive phase with 6 minutes left. They look at the clock and realise they have not yet articulated any trade-offs. The strongest move is:

- A) Skip the trade-offs phase entirely; go straight to "what questions do you have for me?"
- B) Spend the remaining 6 minutes in the deep dive to make sure that section is complete.
- C) Compress the trade-offs into 3-4 minutes: name two explicit trade-offs you made, one thing that changes at 10x scale, and one failure mode you didn't handle. Take the closing 2-3 minutes for the questions phase. The debrief writeup will note "candidate articulated trade-offs concisely under time pressure," which is positive.
- D) Ask the interviewer for a 5-minute extension.

---

**Q9.** A candidate is designing a chat system. They propose HTTP long-polling for message delivery. The interviewer asks "why not WebSocket?" The strongest response is:

- A) "WebSocket adds complexity; long-polling is simpler and works at scale."
- B) "You're right — WebSocket is the standard approach for real-time delivery. I went to long-polling because I wasn't sure if the prompt allowed WebSocket. Let me redesign: each client opens a WebSocket connection to a gateway server; an online-user registry tracks which gateway holds which user; the chat service routes incoming messages to the correct gateway. WebSocket gives us ~100ms delivery vs. ~1-2 seconds for long-polling and a fraction of the connection overhead."
- C) "HTTP is always preferred over WebSocket because it works with all proxies."
- D) "I don't know what WebSocket is."

---

**Q10.** The new-grad-passing bar for a system-design round is best summarised as:

- A) Producing a complete production-ready architecture with every detail specified.
- B) Knowing every distributed-systems paper that has been published in the last 20 years.
- C) Running the six-phase structure on a 45-minute clock; hitting the four building blocks at the high-level phase; producing back-of-envelope numbers; one deep dive with three approaches and a defended choice; two named trade-offs; one acknowledgement of what the senior bar would add. The bar is the *method*, demonstrated visibly, on a defensible 101-level design; not the perfection of the final diagram.
- D) Memorising the architectures of FAANG companies and reproducing them verbatim.

---

## Answer key

<details>
<summary>Reveal after attempting</summary>

1. **C** — The 12 minutes spent on requirements is paid for by the remaining four phases. The most common visible cost is a compressed deep dive (which is the highest-weight scoring dimension) and a skipped trade-offs phase. The 5-minute budget on requirements is the runway the round needs.
2. **B** — Compute, storage, caching, queues. The 101-level vocabulary is by-block, not by-cloud-provider or by-protocol. (A) names trends; (C) names protocols; (D) names providers. All three are real but none is the building-block taxonomy.
3. **B** — The infrastructure storage footprint includes indexes (~10-30% of data), replication (3x for typical replicated systems), and backups (30-50% over a 30-day retention window). The 4x rule of thumb is defensible. (A) under-counts; (D) over-counts; (C) is the non-answer that fails to commit.
4. **C** — SSD random read is ~16μs for NVMe and ~150μs for SATA; at the order-of-magnitude level, "~100μs" is the right answer. (A) is L1 cache; (B) is main memory; (D) is HDD seek.
5. **B** — Fan-out on write is cheap for normal users (200 followers = 200 writes) and expensive for celebrities (10M followers = 10M writes for one post). The hybrid handles this. (A), (C), (D) are not the failure mode.
6. **B** — The Template B response from Challenge 1 — surface the level shift, give an honest partial answer, propose a follow-up. (A) is the bluff failure mode; (C) collapses; (D) is dishonest. The debrief writeup on (B) reads "candidate calibrated well under pressure," which is a positive signal.
7. **A** — Two Redis ops (GET + INCR, or MGET + INCR pipelined) at ~50μs each is ~100μs of overhead, comfortably under the 10ms SLO. (B) is wrong (relational DBs are too slow); (C) over-states the cost (no locks for atomic counters); (D) avoids the math.
8. **C** — Compress the trade-offs to 3-4 minutes rather than skip them. The trade-offs phase is one of the highest-weighted scoring dimensions; skipping it entirely is a strong negative. Compressing it concisely is positive. (A) loses the round; (B) over-invests in the already-complete deep dive; (D) is unprofessional.
9. **B** — Acknowledge the better answer; redesign on the fly; explain the WebSocket pattern (gateway + online-user registry); cite the latency difference. (A) is wrong (WebSocket is the standard); (C) is wrong (WebSocket works with modern proxies); (D) collapses the round.
10. **C** — The bar is the method, demonstrated visibly. Six phases on the clock; four building blocks; numbers; one deep dive; two trade-offs; one acknowledgement of senior calibration. (A) over-states the bar; (B) is irrelevant; (D) is the failure mode of memorisation-over-method.

</details>

If under 7, re-read the lecture you missed. If 9+, you're ready for the homework.
