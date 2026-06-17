# Lecture 2 — Back-of-Envelope Estimation and Latency Numbers

> **Duration:** ~1.5 hours. **Outcome:** You can convert a single DAU number to QPS, peak QPS, storage per year, and bandwidth in under two minutes using arithmetic you can defend out loud. You can recite Jeff Dean's latency numbers at the order-of-magnitude level and use them to bound design decisions. You can recognise when to commit to a number and when to call a number "depends."

## 1. Why the numbers matter

The design round implicitly grades you on a question you may never hear out loud: *do you have a quantitative model of the system, or are you reasoning about it as a pure architecture diagram?* Two candidates can produce the same five-box diagram. The candidate who can also say "this database sees roughly 1,200 writes per second on average, peaking around 5,000 during US-evening hours, with each record at 200 bytes, so the working set is about 20 GB after a year" is operating on a different level than the candidate who said "it scales" and moved on.

The arithmetic is grade-school. The discipline is not. Most new-grad candidates have not practiced doing this arithmetic out loud, on a clock, while also drawing a diagram and explaining a trade-off. The numbers feel hard because of the simultaneity, not the difficulty.

Two skills:

1. **Quantitative estimation** — turning user-facing scale numbers (DAU, requests/day) into infrastructure-facing numbers (QPS, GB/year, Mbps).
2. **Latency calibration** — knowing the order of magnitude of common operations, so that you can tell whether the system you designed will hit the SLO it needs.

Both belong in your spoken vocabulary by the end of the week. The exercises will rehearse them in context; this lecture establishes the table you reach for.

## 2. The estimation toolkit

The full toolkit for a 101-level round fits on a single index card. Memorise it.

### Conversions

| From | To | Conversion | Mnemonic |
|------|-----|-----------|----------|
| DAU | requests/day | DAU × actions per user per day | If users hit your service N times/day on average |
| requests/day | QPS average | requests/day ÷ 86,400 | 86,400 s/day; round to 100,000 for the round |
| QPS average | QPS peak | × 3 to 5 | Most consumer systems are 3-5x peakier than uniform |
| records | bytes | records × record size | Record size from the schema |
| QPS × payload size | bandwidth | direct | bytes/s; divide by 1,250,000 for Mbps |

### Daily-life numbers

The numbers you should be able to commit to memory by Thursday:

- **Seconds in a day:** 86,400. Round to **10^5** for arithmetic in your head.
- **Days in a year:** 365. Round to **400** or **3 × 10^2.5** depending on the math style you prefer.
- **A Twitter post:** ~280 chars + metadata ≈ **1 KB**.
- **A short tweet/text message:** **~200 bytes** uncompressed.
- **A standard JSON API response:** **1-10 KB** for a typical resource.
- **A user-profile photo:** **~200 KB** after compression.
- **A short video:** **5-50 MB** depending on length and quality.
- **One year of seconds:** ~31 million. Round to **3 × 10^7**.

### The factor-of-ten ladder

Every distributed-systems decision lives on a logarithmic scale. The factors:

| Magnitude | Scale | What it looks like |
|-----------|-------|--------------------|
| 10^3 | 1,000 | A typical school's user base. A single database handles it trivially. |
| 10^6 | 1 million | Mid-size SaaS. Single database with read replicas. |
| 10^7 | 10 million | Large SaaS. Sharded database, distributed cache. |
| 10^8 | 100 million | Top-100 consumer app. Multi-region considerations begin. |
| 10^9 | 1 billion | FAANG-scale. Multi-region, custom infrastructure. |
| 10^10 | 10 billion | Hyperscale. Custom hardware, full datacenter operations. |

For new-grad and L4 rounds, you will almost always work at 10^7 to 10^8 scale. Numbers above 10^9 are senior-bar; the interviewer who pushes you there is drifting upward (see Lecture 3 and Challenge 1).

## 3. The standard estimation walk

For every problem, run the same four-step estimation as the requirements phase wraps. Out loud, with arithmetic on the diagram surface.

### Step 1: DAU → average QPS

Start from DAU. Pick an actions-per-user-per-day number based on the system type.

| System type | Actions/user/day | Reasoning |
|-------------|------------------|-----------|
| URL shortener (writes) | 0.1 - 1 | Most users do not create URLs; the ones who do create a few |
| URL shortener (reads) | 10 - 100 | Each URL is clicked many times by many people |
| News feed (reads) | 10 - 50 | Users scroll the feed many times per day |
| News feed (writes) | 0.5 - 2 | Most users post less than once per day |
| Chat (messages sent) | 10 - 100 | Heavy users post many messages |
| Rate limiter | matches the wrapped service | Whatever the service does |

For 100M DAU on a news feed with 50 reads/user/day:

```text
reads/day = 100M × 50 = 5 × 10^9
average QPS = 5 × 10^9 / 86,400
            ≈ 5 × 10^9 / 10^5
            = 5 × 10^4
            = 50,000 reads/sec average
```

The arithmetic out loud: "Five times ten to the ninth, divided by about ten to the fifth, that's five times ten to the fourth — fifty thousand reads per second average."

### Step 2: average → peak

Multiply by 3 to 5 for consumer systems. The peak is typically the US-evening hours for US-centric services; global services have flatter peaks (~2x).

For the news feed example:

```text
peak QPS = 50,000 × 4 = 200,000 reads/sec peak
```

The arithmetic out loud: "Four times that for peak; two hundred thousand reads per second."

### Step 3: storage per year

Records per day × record size × 365.

For 100M DAU on a news feed posting 1 post/user/day, with each post at 1 KB:

```text
new records/day = 100M × 1 = 10^8
storage/day = 10^8 × 1 KB = 10^8 KB = 10^5 MB = 10^2 GB = 100 GB
storage/year = 100 GB × 365 ≈ 36 TB
```

The arithmetic out loud: "Hundred million records per day, one kilobyte each, that's a hundred gigabytes per day, roughly thirty-six terabytes per year before any indexes or replication overhead."

### Step 4: bandwidth

QPS × payload size = bytes per second. Convert to Mbps by dividing by 1.25M (close enough to 10^6 for round-numbers).

For the 200,000 peak QPS news feed reads, each returning 50 KB of feed:

```text
bandwidth = 200,000 × 50 KB = 10^7 KB/s = 10^4 MB/s = 10 GB/s
          ≈ 80 Gbps
```

The arithmetic out loud: "Two hundred thousand reads per second times fifty kilobytes per response — that's ten gigabytes per second of egress, about eighty gigabits per second. That's a non-trivial bandwidth bill; we'd want a CDN in front to amortise it."

The fourth number is where the candidate transitions from "I did some math" to "I understand what the math means." Saying the number forces a design implication.

## 4. When to commit and when to defer

The estimation produces a specific number. The candidate has to decide: do I commit to this number, or do I say "it depends"?

**Commit when:**

- The interviewer gave you a scale number and you computed downstream from it. The interviewer wants you to do the arithmetic; commit.
- The number is the input to a downstream design choice you are about to make. If you are choosing between Postgres and Cassandra based on write volume, commit to the write-volume number so the choice has a reason.
- The number is in the comfortable range for the magnitude (10^7 ± 1). Confidence within an order of magnitude is enough.

**Defer when:**

- The number depends on a product decision you have not made and the interviewer has not given you. "How many messages per chat conversation per day? It depends on whether this is 1-to-1 chat (10 messages average) or a group chat (50 messages average). I'll assume 1-to-1 unless you want me to model both."
- You can do the arithmetic but the result is more than two orders of magnitude off from what feels right. Stop, sanity-check the assumption, redo.
- The interviewer asks you a question you cannot answer in 30 seconds. "I don't know the exact bandwidth for 4K video off the top of my head — somewhere in the 10-25 Mbps range per stream. Do you want me to use 20 Mbps as a working number?" The candidate who admits the gap and proposes a working assumption beats the candidate who guesses and gets caught.

The committal pattern: state the assumption out loud, then commit to the number, then proceed. "Assuming 50 messages per chat per day, that's five times ten to the ninth messages per day across all users, fifty thousand per second average, two hundred thousand peak."

## 5. Jeff Dean's latency numbers

Jeff Dean's 2010 slide table, updated for modern hardware. The numbers below are the 2020-era values; use them as the order-of-magnitude reference behind every latency decision.

| Operation | Latency | Mnemonic |
|-----------|---------|----------|
| L1 cache reference | ~0.5 ns | Fastest accessible memory |
| L2 cache reference | ~7 ns | 14x L1 |
| Branch mispredict | ~5 ns | Pipeline cost |
| Mutex lock/unlock (uncontended) | ~25 ns | |
| Main memory reference (DRAM) | ~100 ns | 200x L1 |
| Compress 1 KB with Snappy | ~3 μs | |
| Send 1 KB over 1 Gbps network | ~10 μs | |
| SSD random read | ~16 μs (NVMe), ~150 μs (SATA) | Modern NVMe is faster than 2010 |
| Read 1 MB sequentially from memory | ~3 μs | |
| Round-trip within same datacenter | ~500 μs | Half a millisecond |
| Read 1 MB sequentially from SSD | ~1 ms | |
| Disk seek (spinning) | ~10 ms | Effectively obsolete in modern designs |
| Read 1 MB sequentially from disk | ~20 ms | Spinning; SSD is 20x faster |
| TCP packet round-trip, same continent | ~10-50 ms | |
| TCP packet round-trip, cross-continent | ~80-150 ms | US-coast-to-EU |
| TCP packet round-trip, antipodal | ~250-300 ms | US to Singapore |

The numbers compress to five magnitudes you should keep in working memory:

1. **CPU/cache:** **nanoseconds**. ~1ns is the floor.
2. **Main memory:** **~100 ns**.
3. **SSD read or in-DC network:** **microseconds to ~1 ms**. Treat this as the floor for any operation that leaves the process.
4. **Cross-region network:** **tens to ~100 ms**. Treat this as the floor for any operation that crosses a continent.
5. **Disk seek (HDD):** **~10 ms**. Almost never appears in modern designs; mention only if you know the system uses spinning disk.

### Using the numbers in a round

The latency numbers are the calibration for the question "is this design fast enough?"

- The round-trip from your app server to a Postgres replica in the same datacenter is **~1-2 ms**, dominated by the network and the query plan. If you need 50ms p99, you have plenty of headroom; if you need 5ms p99, you are close to the floor and the cache is doing the work.
- A cache miss to Redis is **~1 ms**. A cache hit (from the local node) is **~100 μs**. The 10x gap is the reason caches earn their keep on hot read paths.
- A cross-region call (us-east to eu-west) is **~100 ms**. Any user-facing operation that crosses regions on the critical path is automatically over your SLO unless the SLO is very loose. The fix is to keep the critical path local and replicate asynchronously.
- A disk seek (HDD) is **~10 ms**. Modern designs use SSD because the 100x improvement is real. Mention the disk-seek number only if you are designing storage for cold data or backups.

### A worked latency walk

For the URL shortener redirect path: client → CDN → load balancer → app server → cache (Redis) → respond with 302.

```text
client to nearest CDN edge:   ~20 ms (geographic dependent)
CDN cache check (hit):        ~1 ms
CDN to origin (on miss):      ~30 ms cross-region or 5 ms intra-region
load balancer:                ~1 ms
app server processing:        ~1 ms
Redis cache hit:              ~1 ms
total (CDN hit):              ~21 ms p50
total (origin, cache hit):    ~28 ms p50
total (origin, cache miss):   ~33 ms p50
```

The arithmetic out loud: "On a CDN hit, twenty milliseconds, dominated by the user's geographic distance. On origin, twenty-eight milliseconds for a cache hit. On a cache miss to Postgres, thirty-three. All well within a hundred-millisecond redirect SLO."

The candidate who can produce a latency walk like this in 90 seconds is operating at a level the interviewer will note in the debrief.

## 6. The peak-to-average problem

The trickiest single estimation in a design round is the peak-to-average ratio. Get it wrong by a factor of ten and the entire infrastructure plan is off.

The default multipliers:

- **Consumer apps with US-evening peak:** 3-5x. Twitter, Instagram, news, video.
- **Global consumer apps:** 2-3x. Spotify, WhatsApp, services with even global distribution.
- **Enterprise SaaS (business hours):** 5-10x. Slack, GitHub, Notion — quiet on weekends, peaky in business hours.
- **Bursty event-driven:** 10-100x. A flash sale on an e-commerce site, a livestream of a major event, a viral tweet. Mention only when relevant.

The 101-level default unless the prompt suggests otherwise: **5x**. That number is a defensible average across consumer systems; the interviewer will rarely push back. If the prompt is enterprise-shaped or event-shaped, name the multiplier explicitly.

The estimation phase is for average; the capacity-planning phase (Phase 5, trade-offs and scale) is for peak. State both:

> "Average reads are fifty thousand per second; peak around two hundred thousand. The compute pool needs to handle peak, so I'd size for ~250k QPS with some headroom — call it three hundred app servers at ~1k QPS each."

## 7. The round-the-back math: storage and indexes

The naive storage calculation undercounts. The real number includes:

- **Data:** the raw records.
- **Indexes:** typically 10-30% of data size for a few well-chosen indexes.
- **Replication:** 2-3x for replicated systems (one primary, two replicas is the typical default).
- **Snapshots and backups:** 30-50% of data over a backup-retention window.

The 101-level shortcut: **multiply the naive storage by 3-5x** to get the "actual infrastructure storage." For the news feed example:

```text
naive storage/year = 36 TB
actual storage/year = 36 × 4 = ~150 TB
```

State this in the round when storage is on the critical path of the trade-offs phase: "Thirty-six terabytes of raw data per year, but with indexes, three-way replication, and a thirty-day backup window, we're at roughly a hundred and fifty terabytes of actual storage."

## 8. Bandwidth, the silent killer

Bandwidth costs are the line item that catches candidates by surprise. The egress fee from AWS or GCP is meaningful; the architectural impact is more meaningful.

For the news feed at 200,000 peak QPS × 50 KB response:

```text
peak egress = 200,000 × 50 KB/s
            = 10^7 KB/s
            = 10 GB/s
            = 80 Gbps
```

Eighty gigabits per second is a non-trivial number. At AWS public egress prices, that's roughly $7,000/hour or $5M/month for a system running at peak. Two design moves drop it dramatically:

1. **CDN.** A CDN with a 90% hit rate cuts origin egress by 10x. The CDN's own egress is cheaper per byte by ~5x.
2. **Compression.** gzip on the JSON response cuts size by 5-10x. Brotli is slightly better. Both are essentially free.

A senior candidate who calls out the bandwidth cost in the trade-offs phase is showing senior calibration. A new-grad candidate who at least mentions "we'd want a CDN to take pressure off the origin" is showing the right reflex.

## 9. The order-of-magnitude check

Every back-of-envelope calculation has an order-of-magnitude sanity check. Run it before you commit to a number that drives a design decision.

The checks:

- **Is this database load achievable on a single machine?** A modern single-node Postgres handles ~10K writes/sec and ~50K reads/sec comfortably. If your design is above that, you need sharding or a different database.
- **Is this storage achievable on a single machine?** A single modern machine holds ~10TB of SSD comfortably. Above that, you need sharding or distributed storage.
- **Is this bandwidth achievable on a single machine?** A single modern NIC pushes ~25 Gbps. The horizontal pool can push more; the per-machine cap matters for the load balancer and the database.
- **Is this latency achievable for this geography?** If your SLO is 50ms and your users are in Asia and your servers are in us-east, the latency floor is already 200ms; the design cannot meet the SLO without changing the topology.

Saying the sanity check out loud is the highest-leverage 15 seconds of the trade-offs phase: "The single-node Postgres caps at about 10k writes per second; we're projecting 50k; we need sharding from day one."

## 10. The numbers you commit to memory

Before the homework on Friday, commit these to memory. They are the working set you reach for in a round.

**Magnitudes:**

- Seconds in a day: ~10^5 (precise: 86,400)
- Seconds in a year: ~3 × 10^7
- Tweet/short message size: ~1 KB
- JSON API response: ~1-10 KB
- Photo: ~200 KB
- Short video: ~10 MB

**Defaults:**

- Peak-to-average ratio for consumer systems: **5x**
- Single-node Postgres ceiling: **~10K writes/sec, ~50K reads/sec**
- Storage overhead (indexes + replication + backups): **~4x raw data**
- Distributed cache hit rate (well-tuned): **~90-99%**

**Latency anchors:**

- Memory access: **~100 ns**
- SSD read: **~100 μs to 1 ms**
- Intra-DC network round-trip: **~500 μs**
- Cross-region network round-trip: **~100 ms**

These numbers are the floor. The exercises and the mini-project will exercise them in context. By Sunday, the table should be vocabulary, not lookup.

## What to take into the exercises

By the end of this lecture, you should be able to do four things on a clock:

1. **Convert a DAU number to peak QPS** in under 60 seconds, with arithmetic the interviewer can audit.
2. **Compute one-year storage** with the 4x infrastructure overhead in under 60 seconds.
3. **Recite the five latency-magnitude anchors** (nanoseconds, microseconds, milliseconds for local, tens of milliseconds for in-DC network, hundreds for cross-region).
4. **State a sanity check** ("is this on a single machine?") after every quantitative claim that drives a design choice.

Lecture 3 builds on this by walking through the six canonical 101-level problems with the structure of Lecture 1 and the quantitative scaffolding of Lecture 2 applied together. Each problem has a "the numbers" sub-section that uses the estimation methodology you just learned.
