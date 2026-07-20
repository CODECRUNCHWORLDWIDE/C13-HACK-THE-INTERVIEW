# Week 8 — Exercises

Three exercises. Each runs the same six-phase structure on a 45-minute clock against a progressively larger system-design prompt.

1. **[Exercise 1 — URL shortener walkthrough](exercise-01-url-shortener-walkthrough.md)** — run the full six-phase structure on the canonical URL-shortener prompt, then diff your work against the solution on structure, coverage, and depth (~60 min solo + 15 min diffing)
2. **[Exercise 2 — Rate limiter](exercise-02-rate-limiter.md)** — design an inline rate limiter, deep-diving the three algorithms (fixed window, sliding window, token bucket) and committing to fail-open vs. fail-closed (~60 min solo + 15 min diffing)
3. **[Exercise 3 — News feed](exercise-03-news-feed.md)** — design a reverse-chronological feed, surfacing the celebrity problem yourself and committing to the hybrid fan-out (~75 min solo + 15 min diffing; the prompt is bigger than 1 and 2)

[`SOLUTIONS.md`](SOLUTIONS.md) holds the canonical write-up for all three prompts. Do not open it until your 45-minute clock is up — the exercise is the *running*; the comparison is the post-mortem.

## How to work them

Do them in order: 1 → 2 → 3. Exercise 1 establishes the six-phase loop and the four building blocks (compute, storage, caching, queues) on the simplest prompt; Exercises 2 and 3 list it as a prerequisite. Each prompt adds one signature difficulty — the rate limiter forces the algorithm deep-dive and the fail-open decision; the news feed forces the celebrity problem and the fan-out hybrid. Run every prompt on a real 45-minute timer in the tool your actual round will use (most 2026 rounds are virtual: Excalidraw, CoderPad, or a collaborative whiteboard).

After each timer, read `SOLUTIONS.md` and diff on three dimensions: structure (did all six phases run, did any phase eat another's time), coverage (did you hit the four building blocks and produce numbers), and depth (was the deep-dive a real three-approaches discussion or a hand-wave). Note the single largest gap and drill that — do not redo the whole exercise unless you are below bar on three or more rubric dimensions.

The strongest single rep is running Exercise 1 three times at three different anchor scales (10M / 100M / 1B URLs per day) so the "okay, now imagine 10x the traffic" follow-up lands on rehearsed ground. The exercises also feed the week's challenges: Challenge 2 has you build a rubric and score one of these three write-ups against it.
