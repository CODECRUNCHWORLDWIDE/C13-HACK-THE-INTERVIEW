# Exercise 2 — Rate Limiter

**Time:** 60 minutes solo, plus 15 minutes diffing against SOLUTIONS.md.
**Format:** Run the six-phase structure on a 45-minute clock.
**Prerequisite:** Exercise 1 completed; Lecture 3 read.

## The prompt

You are at a virtual onsite. The interviewer says:

> "Hi. We have 45 minutes. I work on our gateway team — we expose a public API to third-party developers, and we need a rate limiter in front of it so we can enforce per-user quotas and protect against abuse. Could you design that for me?"

## What to produce

Run the six-phase structure. Produce:

1. **Requirements clarification** — the scale of the API being protected, the SLO for the rate-limiter overhead, fail-open vs. fail-closed behaviour, the granularity (per-user, per-endpoint, per-IP). (5 min.)
2. **High-level architecture** — where the rate limiter sits in the request path, what its backing store is. (5 min.)
3. **API and data model** — what the rate limiter exposes (the 429 response format and headers) and what the internal data shape is. (10 min.)
4. **Deep dive on the algorithm** — three approaches (fixed window, sliding window, token bucket), trade-offs, committed choice, sketched math. (15 min.)
5. **Trade-offs and scale** — consistency, fail-open, per-region behaviour. (5 min.)
6. **Questions for the interviewer.** (5 min.)

## Constraints

- **The rate limiter is middleware, not a standalone service.** Most rate limiters are in-process in the gateway or app server, with a shared backing store. If you propose a separate rate-limiter service that every request hits, defend it — the extra hop adds latency that may violate the SLO.
- **Pick a scale anchor.** A reasonable default: 1M requests/sec across the protected API. You can pick differently and defend it.
- **Commit to fail-open or fail-closed.** Both are defensible for different APIs. The default for public read APIs is fail-open; the default for write-heavy financial APIs is sometimes fail-closed. Pick and defend.

## Acceptance criteria

- All six phases produced within 45 minutes.
- The architecture diagram shows the rate limiter inline in the request path with a clearly-labelled state store.
- The 429 response includes the canonical headers (Limit, Remaining, Reset, Retry-After).
- The deep dive names three algorithms, picks one with reasoning, and includes the math for the chosen approach.
- The trade-offs include the consistency-vs-accuracy decision and the fail-open-vs-fail-closed decision.

## Scoring rubric

Same as Exercise 1, with one addition:

| Dimension | New-grad passing | Below bar |
|-----------|------------------|-----------|
| Algorithm justified | Three algorithms named, one chosen with math | Picked one, no comparison |
| Latency overhead bounded | Explicit calculation (Redis ops × latency) | Hand-wave "fast enough" |

## Common failure modes

1. **Proposed a separate rate-limiter service.** Adds a network hop. Defensible only at very large scale; for the 1M-req/sec anchor, in-process middleware is the right call.
2. **Used a relational DB as the counter store.** Too slow. Redis or an in-memory counter is the canonical choice.
3. **No mention of fail-open behaviour.** The interviewer's debrief will note "candidate didn't think about what happens when the rate limiter itself fails."
4. **Confused throttling with quotas.** Rate limiting (requests-per-second) and quotas (requests-per-month) are different problems with different solutions. Confirm in Phase 1 which one the interviewer means.
5. **Deep dive was just "we'd use a token bucket."** No math. No comparison. No reasoning about which bucket size or fill rate.

## Variations

- **Run again with per-endpoint limits.** Does the key structure change? (Yes: `rl:user:{u}:endpoint:{e}:{bucket}`.) Does the storage footprint change? (Yes: ~10x.)
- **Run again at 10M req/sec.** Where does the Redis cluster break? (At ~1M ops/sec per Redis node; you'd shard.)
- **Run again with multi-region requirement.** How do you handle cross-region rate limits without strong consistency? (You usually don't; you accept regional independence and let the global rate slightly exceed the configured limit. Senior territory.)
