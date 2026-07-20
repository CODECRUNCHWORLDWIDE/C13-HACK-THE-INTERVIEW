# Exercise 1 — URL Shortener Walkthrough

**Time:** 60 minutes solo, plus 15 minutes diffing against SOLUTIONS.md.
**Format:** Run the six-phase structure on a 45-minute clock. Produce the artefacts on a whiteboard, a text document, or a Mermaid file — whatever your real round will use.
**Prerequisite:** Lecture 1 (six-phase structure), Lecture 2 (estimation), Lecture 3 (URL shortener canonical solution).

## The prompt

You are sitting in front of an interviewer at a mid-sized tech company's onsite. The interviewer says:

> "Hi, I'm Alex. We have 45 minutes. I'd like you to design a URL shortener — a service that takes a long URL and gives back a short one, like bit.ly or tinyurl. Let's get started."

The interviewer is silent except for clarifying questions. They will not pre-narrate the phases for you. They will not stop you when you run long on one phase. They will note in their debrief writeup whether you ran the structure, hit the building blocks, produced numbers, and named trade-offs.

## What to produce

Run the six-phase structure on a clock. At each phase boundary, speak the transition phrase out loud (or write it on the document as a section header — same effect for the artefact). Produce:

1. **A requirements clarification section** — your written-down version of what Alex said the system is, the scale assumption you committed to, the read-write ratio, the non-functional priorities, and the scope boundary. (5 min.)
2. **A high-level architecture diagram** — five to seven boxes, arrows labelled. Use Mermaid syntax or a sketch. (5 min.)
3. **The API and data model** — three to five endpoints, two to three tables. Schema with types. (10 min.)
4. **A deep dive on short-code generation** — three approaches, trade-offs, committed choice, sketched implementation, second diagram. (15 min.)
5. **A trade-offs and scale section** — two trade-offs you made, one thing that changes at 10x, one failure mode you didn't handle. (5 min.)
6. **Two questions for the interviewer** — one technical, one about the team. (5 min.)

Use a 45-minute timer. When the timer hits each phase boundary (5, 10, 20, 35, 40 minutes), check whether you are at the right point and adjust. Resist the temptation to keep working past 45.

## Constraints

- **Do not look at SOLUTIONS.md until your 45 minutes is up.** The exercise is the running; the comparison is the post-mortem.
- **Pick a defensible scale anchor.** Lecture 3 suggested 100M URLs/day. You can pick something different — 10M/day, 1B/day — and defend it. The interviewer will accept any defensible anchor; what they will not accept is no anchor.
- **Use whatever tooling matches your real round.** Most rounds in 2026 are virtual; the shared editor is typically Excalidraw, CoderPad, or a collaborative whiteboard. Practice in the tool you will be in.
- **Speak out loud, or write the transitions explicitly.** If you are practicing solo and silent, write each transition as a section header in the document: "## Phase 1 — Requirements", etc. The verbal habit is what you are building.

## Acceptance criteria

The exercise is complete when:

- You produced all six phase artefacts within 45 minutes (some shorter is fine; over-running phases is the failure mode to watch).
- The architecture diagram has five to seven boxes, each labelled.
- The API has at least three endpoints with HTTP method, path, and one-line description.
- The data model has at least two entities with field names and types.
- The deep dive has three named approaches, one committed choice with reasoning, and a second diagram for the chosen approach.
- The trade-offs section names at least two explicit trade-offs and one failure mode.
- You have written down two questions for the interviewer.

## After the timer

Read SOLUTIONS.md. Diff your work against it on three dimensions:

1. **Structure.** Did you run all six phases? Did any phase eat another phase's time? Did you produce transitions?
2. **Coverage.** Did you hit the four building blocks (compute, storage, caching, queues)? Did you produce numbers (DAU → QPS → storage)?
3. **Depth.** Was your deep dive a real engineering discussion (three approaches, defended choice) or a hand-wave?

Note the largest single gap. That is the thing to drill next. The drill is repetition — run the same exercise next week with a 45-minute timer and see if the gap closed.

## Scoring rubric (self-evaluation)

| Dimension | New-grad passing | Below bar |
|-----------|------------------|-----------|
| Ran all six phases | All six produced | Skipped one (typically trade-offs) |
| Stayed on time | Within 5 min of the 45-min budget | Ran 60+ min |
| Spoke/wrote transitions | At each phase boundary | None or only initial |
| Four building blocks | All four named | Missed caching or queues |
| Numbers produced | DAU → QPS → storage in under 3 min | No numbers or wrong by 10x+ |
| Deep dive depth | Three approaches, defended choice | One approach, no defence |
| Trade-offs explicit | Two named | None, or only hand-wavy mentions |

Score yourself honestly. If you are below bar on three or more dimensions, redo the exercise next week before the real round. If you are below bar on one, drill that specific dimension; do not redo the whole exercise.

## Common failure modes

The five most common ways new-grad candidates fail this exercise:

1. **Spent 20 minutes on requirements clarification** trying to be thorough. Lost the back half of the round. Fix: hard 5-minute cap; set the timer.
2. **Forgot the queue.** Drew compute, storage, cache; never mentioned the queue, even though analytics-style writes naturally use one. Fix: explicit checklist of the four blocks before transitioning out of Phase 2.
3. **Deep dive was "we'd use Redis."** Two sentences. No trade-offs. No alternative considered. Fix: the three-approaches rule; never commit to a technology without naming at least one alternative you considered.
4. **No numbers.** Did the design entirely qualitatively. Fix: state the DAU anchor in Phase 1; do the QPS calculation out loud in Phase 1 or early Phase 2.
5. **Stopped at "and then we scale."** The trade-offs phase was "we'd add more servers." Fix: name the specific thing that breaks at 10x and the specific fix.

## Variations to run if you have extra time

Run the exercise three times with three different anchor scales:

- **10M URLs/day** (mid-size SaaS) — does any building block change? Storage probably fits a single node.
- **100M URLs/day** (large consumer) — the baseline; this is what most real rounds will anchor to.
- **1B URLs/day** (FAANG-scale) — the senior anchor; sharding is mandatory; ticket server needs redundancy from day one.

The same six phases. The same four building blocks. Different numbers at each scale produce different deep-dive emphasis. The exercise of running the same prompt at three scales is the single best preparation for the round where the interviewer says "okay, now imagine we have 10x the traffic."
