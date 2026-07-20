# Week 8 — Homework

Six design drills, ~6 hours total. Run each on a clock. Score each against the rubric you built in Challenge 2. The drills are deliberately spread across the six classic 101-level problems so that, by Sunday night, you have run the structure on every canonical prompt at least once.

The homework is timed practice, not perfection. The point is repetitions on the six-phase structure, the four building blocks, the back-of-envelope estimation, and the trade-offs vocabulary. If you redo a drill, the second time should be 30% faster than the first — that improvement is what the homework is producing.

## Time and weighting

| Drill | Time | Weight in your weekly score |
|-------|------|------|
| HW1 — Chat (one-to-one) | 60 min | Highest weight — most-asked variant |
| HW2 — Distributed cache | 60 min | Highest weight — building-block depth |
| HW3 — Ride-sharing match | 60 min | Medium — geospatial fluency |
| HW4 — Re-run Exercise 1 (URL shortener) at 10x scale | 45 min | Medium — scale rehearsal |
| HW5 — Notification system (variant) | 60 min | Medium — queue and worker depth |
| HW6 — Top-K trending (variant) | 45 min | Low — bonus drill |

Total: ~6 hours. Spread across the week; do not try to do all six on Friday night.

## Rubric (the same rubric you built in Challenge 2)

Score each drill on the seven dimensions:

1. Requirements clarification and scoping
2. High-level system structure
3. API and data model
4. Depth on the deep-dive component
5. Quantitative reasoning (estimation, latency, capacity)
6. Trade-offs and scale
7. Communication and pacing

Levels: No-Hire, Lean Hire (new-grad bar), Hire (L4 bar). For each drill, produce a self-score across all seven dimensions and a one-line summary: which dimension was strongest, which was weakest.

## HW1 — Chat (one-to-one) — 60 min

**Prompt:** "Design a one-to-one chat system. Like WhatsApp, but for this round just one-to-one — no group chat. Users should be able to send and receive messages in real time and see their message history when they open the app."

**Scale anchor:** 10M DAU; 30 messages/user/day.

**Constraints:**

- The real-time delivery has to use WebSocket, not HTTP polling. If you propose polling, defend it explicitly (and lose points unless your defence is unusually good).
- Cassandra (or equivalent wide-column) for message storage. Postgres can work; Cassandra is the canonical answer.
- An online-user registry is required; mention how the registry maps user → gateway server.

**Deep-dive target:** The handoff between the chat service and the gateway when delivering to an online user, versus the persistence + push notification flow when the recipient is offline.

**Estimation target:**

- Messages/day → messages/sec
- Concurrent WebSocket connections (~30-50% of DAU)
- Storage/year for messages

**Senior add (mention):** group chat (next homework variant), E2E encryption, gateway failover, read receipts.

**Self-score against rubric.** Identify the weakest dimension; drill it.

## HW2 — Distributed cache — 60 min

**Prompt:** "Design a distributed cache — like Memcached or Redis cluster. The cache should support GET / SET / DELETE operations, scale horizontally, and survive single-node failures."

**Scale anchor:** 1M ops/sec; 100 nodes; 10TB total memory across the cluster.

**Constraints:**

- Consistent hashing is required. If you propose hash-mod-N, defend it (and lose points; the cache cold-start on rebalance is a real problem).
- The client library knows the hash ring; the cache nodes are just servers. The client-side routing pattern is the canonical answer.
- Eviction policy must be specified; LRU is the default.

**Deep-dive target:** consistent hashing — the ring, the virtual nodes, the rebalance behaviour when a node is added or removed.

**Estimation target:**

- Ops/sec per node (1M / 100 = 10K ops/sec/node)
- Memory per node (10TB / 100 = 100GB/node)
- Network round-trip on a cache operation (~500μs intra-DC)

**Senior add (mention):** cache-aside vs. write-through vs. write-behind, hot-key handling, cache stampede mitigation (request coalescing, lock-on-miss).

## HW3 — Ride-sharing match — 60 min

**Prompt:** "Design the matching service for a ride-sharing app like Uber or Lyft. A rider opens the app, taps 'request ride', and the system finds the nearest available driver within 5 minutes. You don't need to handle payment, ratings, or routing; just the matching."

**Scale anchor:** 10M DAU; 1M active drivers; 100K ride requests/hour peak.

**Constraints:**

- The geospatial index must use geohash or H3. If you propose scanning all drivers and computing distance, defend it (you will lose points; the cost is O(N) per query).
- Redis's native geospatial commands (GEOADD, GEORADIUS, GEOSEARCH) are the canonical answer for the 101 level. H3 (Uber's actual approach) is the senior add.
- Driver locations update every 5 seconds; that produces 200K writes/sec to the geospatial index. Mention this number.

**Deep-dive target:** the geohash neighbourhood search — looking up the 9 cells around the rider's location and unioning the driver sets.

**Estimation target:**

- Driver location updates per second (1M drivers / 5s interval = 200K writes/sec)
- Ride requests per second (peak ~30/sec)
- Latency per match (~10-50ms; well under the 5s SLO)

**Senior add (mention):** H3 hexagonal grid (Uber's actual choice), surge pricing, multi-leg trips, the hotspot problem at major events.

## HW4 — Re-run Exercise 1 (URL shortener) at 10x scale — 45 min

**Prompt:** Same URL shortener prompt as Exercise 1, but with the scale anchor at **1 billion URLs/day** instead of 100M.

**The goal of this drill:** rehearse what changes when the scale jumps an order of magnitude. The architecture skeleton is the same; the building-block choices shift.

**What should change:**

- **Storage:** sharding becomes mandatory. Pick a shard key (e.g., short_code prefix); compute shard count.
- **Ticket server:** must be highly available from day one; deploy two with leader election; allocate ranges larger than 10K (e.g., 100K) to reduce the ticket-server query rate.
- **Cache:** Redis cluster scales by adding nodes; mention the resharding pain.
- **CDN:** mandatory at this scale; an origin pushing 500K reads/sec is expensive in bandwidth.

**What stays the same:**

- The API.
- The data model (per shard).
- The high-level six-box architecture (with sharded boxes).

**Self-score:** the 10x rehearsal is a setup for the trade-offs-and-scale phase of any real round. The interviewer who says "okay, now imagine we have 10x the traffic" is testing whether you can navigate this shift without redesigning.

## HW5 — Notification system — 60 min

**Prompt:** "Design a notification system. Users have multiple devices; notifications should arrive at all of them. The system handles in-app notifications, push notifications, and email. Support fan-out for system-level events like 'all users in city X get an emergency alert'."

**Scale anchor:** 100M users; ~10 notifications/user/day average.

**Constraints:**

- A queue is required between the notification ingestion and the delivery workers. A synchronous design fails the "city X emergency alert fan-out to 10M users in 60 seconds" requirement.
- The delivery should be parallel across channels (push, email, in-app). Different workers per channel; same queue or separate queues, your choice — defend.
- Idempotency is important: the system should not send the same notification twice if a worker crashes mid-delivery.

**Deep-dive target:** the queue + worker fan-out pattern; idempotency via deduplication keys.

**Estimation target:**

- Notifications/sec average (100M × 10 / 86,400 ≈ 12K/sec)
- Peak fan-out for emergency alert (10M users in 60 seconds = 170K/sec)
- Worker count needed for peak

**Senior add (mention):** notification preferences and DND, cross-region delivery, the deduplication problem at scale.

## HW6 — Top-K trending — 45 min

**Prompt:** "Design a 'top trending now' service — like Twitter's trending topics or YouTube's trending videos. The service should produce a top-10 list every minute, based on user activity over the last hour."

**Scale anchor:** 100M events/minute (e.g., views, likes, mentions).

**Constraints:**

- The naive approach (sort all topics by count, take top 10) is O(N log N) and does not fit at scale. A more efficient approach uses a sketch (Count-Min Sketch, HyperLogLog) or a heap of size K.
- Mention "approximate" as an acceptable trade-off. The trending list does not need to be exactly correct; near-correct is fine.

**Deep-dive target:** the Count-Min Sketch (or heap-based) algorithm; the approximation guarantees.

**Estimation target:**

- Events per second (100M / 60s ≈ 1.7M events/sec)
- Memory for the sketch (~10MB for a 1% error guarantee at 1M distinct topics)
- Latency to query the top-K list (~10ms with the right data structure)

**Senior add (mention):** time-windowed sketches, the sliding-window decay, distributed sketches (multiple stream processors merging their sketches).

## End-of-week summary

After all six drills, fill out a summary table:

| Drill | Total time | Lowest-scoring dimension | Drill plan to close |
|-------|-----------|--------------------------|---------------------|
| HW1 | | | |
| HW2 | | | |
| HW3 | | | |
| HW4 | | | |
| HW5 | | | |
| HW6 | | | |

**Across all six,** identify the one dimension you scored lowest on the most often. That is your single biggest gap. The plan to close it is the rest of this week's prep and the first day of next week.

Most candidates' single biggest gap is **quantitative reasoning** — they skip the estimation phase, or they do the arithmetic but do not say it out loud. The fix is mechanical: at minute 3-4 of every round, before transitioning out of requirements clarification, do the DAU → QPS calculation on the board. Train the habit.

The second most-common gap is **trade-offs and scale** — candidates compress the phase to one minute, or skip it entirely when the deep dive runs long. The fix is structural: at minute 35, stop the deep dive regardless of where you are, and pivot to trade-offs. The compressed deep dive is graded better than the missing trade-offs.

## Acceptance criteria

- All six drills completed; each on a clock with self-score.
- The summary table filled out with the one biggest gap identified.
- A specific drill scheduled for the biggest gap before the real round.

## What this homework is preparing you for

The mini-project on Saturday is the full TinyURL write-up with Mermaid diagrams. The homework is the volume that produces the muscle memory for the structure; the mini-project is the polished artefact that demonstrates depth. You need both.
