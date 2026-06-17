# Exercise 3 — News Feed

**Time:** 75 minutes solo (the prompt is bigger than Exercise 1 and 2), plus 15 minutes diffing against SOLUTIONS.md.
**Format:** Run the six-phase structure on a 45-minute clock. Then take an extra 15-30 minutes to fill in the bits you ran out of time for in the round, so the SOLUTIONS.md diff is meaningful.
**Prerequisite:** Exercises 1 and 2 completed; Lecture 3 read.

## The prompt

The interviewer is a senior engineer at a social-product company. They say:

> "I'd like you to design a news feed — the kind of feed a user sees when they open an app like Twitter or Instagram. Reverse chronological for this round; don't worry about ranking. Let's go."

## What to produce

Run the six-phase structure. Produce:

1. **Requirements** — scale (DAU, follow count, post rate), SLO (feed-load latency, freshness), the celebrity problem (you should surface this in requirements, not wait for the deep dive). (5 min.)
2. **High-level architecture** — at least three boxes labelled "Cassandra", "Redis", "Kafka" (or equivalents); the fan-out worker pattern visible. (5 min.)
3. **API and data model** — feed read with pagination cursor; post creation; the UserTimeline schema. (10 min.)
4. **Deep dive on fan-out** — fan-out on write vs. fan-out on read vs. the hybrid; commit to hybrid; sketch the celebrity threshold and the merge-on-read path. (15 min.)
5. **Trade-offs and scale** — Cassandra choice, hybrid choice, what changes at 10x DAU. (5 min.)
6. **Questions.** (5 min.)

## Constraints

- **The celebrity problem must come up.** If you do not raise it, the interviewer almost certainly will. Raising it yourself is a stronger signal than waiting to be asked.
- **The cache is per-user, not global.** Each user has their own pre-computed feed. The cache key is `feed:{user_id}`; the value is a sorted set of post_ids.
- **Use Cassandra (or an equivalent wide-column store) for UserTimeline.** The access pattern — partition by user_id, sort by timestamp DESC, time-ordered writes — fits Cassandra natively. Postgres can be made to work but the senior reader will note that you picked the harder option.
- **Use a queue for fan-out.** The fan-out workers must be decoupled from the post service; a synchronous fan-out blocks the post creation on the slowest follower.

## Acceptance criteria

- All six phases produced within 45 minutes (then extra time to fill gaps).
- The architecture has at least: load balancer, feed service, post service, Cassandra, Redis, Kafka, fan-out worker pool.
- The data model has Post, Follow, and UserTimeline as three distinct entities.
- The deep dive names fan-out on write, fan-out on read, and the hybrid; commits to the hybrid with a celebrity threshold.
- The trade-offs section mentions cross-region replication as the failure mode you didn't fully handle.

## Scoring rubric

Additions to the Exercise 1 rubric:

| Dimension | New-grad passing | Below bar |
|-----------|------------------|-----------|
| Surfaced the celebrity problem | In Phase 1 or early Phase 2 | Only when asked |
| Picked the right database for UserTimeline | Cassandra (or equiv) with reasoning | Postgres without reasoning |
| Queue between post and fan-out | Present with named technology | Synchronous fan-out |
| Cache shape correct | Per-user, sorted set, keyed by user_id | Global, list, keyed by post_id |

## Common failure modes

1. **Forgot the queue entirely.** Fan-out was inline in the post service. The candidate did not realise this blocks post-creation on the slowest follower.
2. **Treated celebrity as an afterthought.** The trade-offs section had a footnote about celebs; the deep dive did not feature the hybrid. The interviewer will steer there and the candidate will appear to be reasoning live rather than from preparation.
3. **No mention of feed cache.** Every feed read goes to Cassandra. The 200ms SLO is in jeopardy.
4. **The data model conflated Post and UserTimeline.** They are different. The Post is the canonical record (one row per post). The UserTimeline is the per-user precomputed feed (one row per (user_id, post_id)).
5. **Said "we'd shard the database" without specifying the shard key.** The shard key for UserTimeline is user_id (so each user's feed is on one shard); the shard key for Post is post_id (or author_id, for locality). Different choices, different reasons.

## Variations

- **Run again with a ranking model.** What changes? The Cassandra schema needs to support ranking-feature lookup; the feed read becomes "fetch candidate posts, score, top-K." Senior territory; mention as a follow-up.
- **Run again with stories (24-hour ephemeral posts).** What changes? The Post table needs a TTL; the cache strategy is different (everything is hot until it expires).
- **Run again as Instagram (photo-heavy) vs. Twitter (text-heavy).** What changes? Storage shape (blob store for photos, separate from Post metadata); CDN strategy; bandwidth math.
