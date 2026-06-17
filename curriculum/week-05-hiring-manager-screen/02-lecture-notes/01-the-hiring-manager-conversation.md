# Lecture 1 — The Hiring Manager Conversation

> **Duration:** ~2 hours. **Outcome:** You can name what the hiring manager is evaluating and why it differs from the recruiter, deliver a 4-6 minute "tell me about a recent project" answer with the right structure and ownership language, and survive two layers of drill-down follow-ups on that answer without hand-waving.

## 1. The hiring manager screen is a different call

The first thing to internalise about the hiring manager screen is that it is structurally a different conversation from the recruiter screen, even though both are 30-45 minutes on Zoom with someone from the same company.

The recruiter ran a **fit-and-friction filter** — four pass/fail bits across a structured 30 minutes, optimised to surface a "no" early. The hiring manager is not running that script. The hiring manager has a longer, looser, more conversational call structured around two questions:

- Can this person describe technical work with depth and ownership?
- Do I want this person on my team?

The first question is testable in five minutes. The second is the entire rest of the call.

### Who's on the call

The hiring manager is the person who, if you're hired, will be your direct manager. Their title varies — Engineering Manager, Senior Engineering Manager, Director of Engineering, sometimes Staff or Principal Engineer if the role is at a sub-team without a dedicated manager. What matters is that they have **headcount authority on this specific req**. They asked for the role to be opened. They wrote (or signed off on) the job description. They will run your 1:1s.

This person reads your resume differently from the recruiter. The recruiter was checking whether you sound coherent. The hiring manager is checking whether the work on your resume *resembles* the work on their team and whether you would be the kind of teammate they don't have to babysit.

### What they're evaluating

Five things, roughly in this order of weight:

1. **Technical credibility on your own past work.** Can you describe a recent project in a way that an engineer two levels above you can drill into for ten minutes without finding a hand-wave?
2. **Ownership.** When you describe the project, do *you* show up in the description as someone who made decisions, or does the answer hide behind "the team did X" the whole way through?
3. **Team-fit signal.** Conflict handling, working style, collaboration patterns. The HM is imagining their existing team plus you, and asking: does this person make the team better or harder?
4. **Specific interest in the role.** Not generic "why this company" — but "why this *team* and this *role*," which is a different question one level deeper.
5. **The questions you ask back.** The closing 10-15 minutes of an HM screen is where the strongest candidates separate themselves. The questions you ask are scored, often more than candidates realise.

Note what's *not* on this list: live coding, system design, algorithmic puzzles, comp expectations. The HM screen is almost never where any of those happen. The recruiter handles comp. The technical loop handles coding and design. The HM screen sits between them: behavioural, project-based, and conversational.

### The mental model

The recruiter screen is structured and scored. The hiring manager screen is more like a coffee chat in shape and an interview in stakes. The HM is taking notes, but they are taking different notes — phrases you use, projects you describe, questions you ask, signs of energy when you talk about specific topics. The HM is also pattern-matching you to the engineers they've hired before, especially the ones who worked out and the ones who didn't.

If the recruiter screen was a checkbox form, the HM screen is a colleague's instinctive read after a 40-minute conversation. That read is what they will defend in the next debrief meeting. Your job is to make it easy for them to defend you.

## 2. Recruiter vs. hiring manager — the five-axis comparison

Internalise this comparison; it should shape every preparation choice you make.

| Axis | Recruiter screen | Hiring manager screen |
|------|-------------------|------------------------|
| **Who's on the call** | Internal or agency recruiter; not a technical evaluator. | The manager who will be your boss; usually a current or former engineer; technical. |
| **What they evaluate** | Resume coherence, technical loop survival likelihood, role-specific interest, comp in band. Four pass/fail bits. | Technical credibility on past work, ownership, team-fit, specific interest in *this role*, and the questions you ask. |
| **Anchor question** | "Tell me about yourself" — 2-3 minute self-intro. | "Tell me about a recent project" — 4-6 minute project story, with drill-down. |
| **Failure mode** | Meandering intro, generic "why us," fumbled logistics, no questions. | Vague project (no specifics), team-only ownership ("we built"), no follow-up-survivability, no questions back, badmouthing past manager. |
| **Comp discussion** | Always. Beat 6 of the call. | Almost never. If the HM brings it up, it's an unusual call; deflect to the recruiter politely. |

Two implications worth stating explicitly.

**The recruiter screen is mostly *about you*; the hiring manager screen is mostly *about your work*.** The recruiter wants to know who you are. The hiring manager wants to know what you've built and how. The self-intro at the start of an HM screen, if requested at all, is shorter — 60-90 seconds, not 2-3 minutes — because the manager has already read the recruiter's notes and the resume.

**The HM screen is the first call where you are evaluating *them* in roughly equal weight.** This is your future boss. The candidates who walk out of the call with the strongest impressions almost always asked questions that revealed something about the manager — their communication style, how they make decisions, what their last hire's first 90 days looked like. Lecture 2 is the entire treatment of that side.

## 3. The recent-project anchor — the question that shapes the whole call

In nearly every HM screen, within the first 5-10 minutes, you will hear some variant of:

- "Walk me through a recent project you worked on."
- "Tell me about something you've shipped in the last 6-12 months."
- "What's a piece of work you're proud of?"
- "Pick a project on your resume and tell me about it."

These are the same question. The HM is handing you the microphone to do the single most-important thing on the call: describe technical work with depth and ownership. **Most of the rest of the call is follow-ups on this answer.** That is the load-bearing fact of this lecture.

Candidates who botch the recent-project answer rarely recover. Even with a great rest-of-call, the HM walks away with "the project answer was thin," which is what they write in the debrief. Candidates who nail it can fumble later beats and still move forward, because the anchor answer set the read.

### What the question is actually asking

Three things, simultaneously:

1. **Is the work on your resume real?** Can you describe it at a depth that demonstrates you actually did it, not just witnessed it?
2. **Are you the kind of engineer who makes decisions, or the kind who follows them?** This is the ownership question, embedded in the phrasing of your answer.
3. **Can you talk about technical work in a way I'd be willing to hear at standup every day?** This is the team-fit screen, encoded in how you speak — pace, vocabulary, ability to compress and expand on demand.

The HM is not looking for the "best" project. They are looking for *a* project where the depth holds up. A small project described with real specificity beats a flagship project described in marketing speak.

### Picking the project

Three criteria for the project you describe:

- **Recent.** Last 6-18 months. If your strongest project is from 3+ years ago, the HM will note "their best work is dated," which is a flag at most levels above mid.
- **Owned.** You made non-trivial decisions. "I implemented the design my staff engineer specced" is a weaker answer than "I owned the design and implementation of $component." If you have nothing in the last 18 months you owned, **find one before the call** — even a side project counts at the junior-to-mid level, though it carries less weight at senior+.
- **Specific.** Concrete technologies, concrete numbers, concrete decisions. "Rewrote a service in Go" is thinner than "Rewrote the payments-reconciliation worker from Python to Go because the Python version was hitting 4-hour completion times on the EOM batch; the rewrite landed at 35 minutes with the same correctness guarantees."

If you have multiple candidate projects, **pick the one with the deepest follow-up survivability** — the one you can answer "why X over Y" on, repeatedly, without bluffing. Not the flashiest one.

## 4. The 5-minute project story — the structure

The reliable structure, in six segments, totalling 4-6 minutes spoken. Budget: 60-90 seconds per major segment, less for the openers and closers.

> **Segment 1 — The problem (30-45 sec).** Lead with the problem, not the solution. "At {company}, the {system / team / customer-facing surface} had a problem: {one-sentence description with a number — latency, dollars, users, error rate}. The cost was {concrete consequence — pages, lost revenue, broken SLO, customer complaints}."
>
> **Segment 2 — Your role and the team shape (30 sec).** "I {owned / co-owned with one other engineer / led a team of N} this work. My specific responsibility was {scope — design, implementation, rollout, all three}."
>
> **Segment 3 — The decisions and trade-offs (90-120 sec, the longest segment).** "The key technical decisions were {decision 1, decision 2, decision 3}. The non-obvious one was {decision X}, where we chose {approach A} over {approach B} because {reason}. The trade-off was {what we gave up}."
>
> **Segment 4 — Implementation specifics (45-60 sec).** "Concretely, this meant {2-3 specific technologies, design patterns, or architectural details}. The hardest part was {specific challenge}, which we handled by {approach}."
>
> **Segment 5 — Outcome with a number (30-45 sec).** "The result was {one or two metrics — latency drop, throughput gain, customer impact, dollar number}. {Optional: any incidents, rollbacks, or surprises.}"
>
> **Segment 6 — What you'd change (20-30 sec).** "If I were starting over, I'd {one specific thing — different technology choice, different rollout sequence, earlier customer feedback}. The lesson I took was {one sentence}."

Total: 4-6 minutes. Under 3 minutes reads as thin or rehearsed-to-vagueness. Over 7 minutes reads as not respecting the time budget; the HM will start cutting follow-ups, which is exactly the part of the call that earns your move-forward.

### The two structural rules

**Rule 1 — Problem first, solution second.** Candidates who lead with the solution ("I built a Kafka consumer that...") force the HM to retroactively infer what problem the work solved. Leading with the problem makes the rest of the answer self-justifying.

**Rule 2 — Decisions and trade-offs in the middle, not at the end.** The HM is listening for decision-making depth. Burying the decision-making in the last 30 seconds means you spent most of the answer on description, which is the cheapest content. Put the decisions in the centre of gravity.

### Worked example — before

> "Yeah so at my last company I worked on this microservices project. We were splitting up the monolith — the whole company was doing it. I worked on the part for billing. We used Kubernetes and Go, and I think it went pretty well. We shipped it in like 6 months and it was good. The team did a lot of really interesting work on it. Yeah."

What's wrong: zero problem statement (why was the monolith being split?), zero ownership ("the team did"), zero decisions or trade-offs, zero numbers, zero "what I'd change," vague timeline, and a trailing "yeah." A senior HM stops listening at "I think it went pretty well."

### After

> "At Acme, our billing service was inside a Python monolith that took 25 minutes to deploy end-to-end. The billing path was the highest-incident component — about 60% of our pages in 2023 were billing-related — and the slow deploy meant rollbacks took 25-30 minutes too. The fix was to split billing into its own service.
>
> I owned the design and implementation. The team was me plus one other engineer for the implementation, with a staff engineer reviewing the design.
>
> The key decision was the **boundary**. The instinctive split was 'extract every billing endpoint as one service.' We chose instead to extract two services — pricing-calculation and invoice-write — because the read and write paths had completely different scaling profiles. The trade-off was that we now had two services to operate instead of one, which means more on-call surface. We decided the operational cost was worth the lower coupling between read-heavy pricing and write-heavy invoicing.
>
> Concretely, we moved both services to Go on EKS, with Postgres for the write side and Redis as a read cache for pricing. The hardest part was the migration: we ran the new services in shadow mode for six weeks behind a feature flag, comparing every response against the monolith's response. We caught three subtle correctness bugs in shadow mode before any customer traffic touched the new services.
>
> Result: deploy time for billing went from 25 minutes to 90 seconds. Billing-related incidents in the six months after migration were down 70%. We also unblocked the next team to extract their service because we had built the shadow-mode pattern as reusable tooling.
>
> If I were starting over, I'd cut the shadow period from six weeks to three. We caught all three correctness bugs in the first ten days; the remaining time was confidence-building, not bug-catching. The lesson was that shadow-mode quality is a step function — you either catch bugs early or you're paying for paranoia."

What's load-bearing: a specific problem with a number (25-minute deploy, 60% of pages), explicit ownership ("I owned the design"), a non-obvious decision with a defensible trade-off (two services not one, operational cost vs. coupling), concrete tech (Go, EKS, Postgres, Redis), a specific challenge (shadow mode for six weeks), a specific outcome with a number (25 min → 90 sec, 70% incident drop), and a "what I'd change" with a real reason behind it.

This answer takes about 4 minutes 30 seconds spoken at a normal pace. Word count: ~480. It will survive 10 minutes of follow-up because every claim has specificity behind it.

## 5. Drill-down survivability — the part most candidates aren't ready for

The recent-project story is the setup. The follow-ups are where the HM actually evaluates depth.

An experienced HM will probe each of your decisions with at least two layers of "why?":

- "Why did you split into two services instead of one?"
- "What would have changed your mind?"
- "Did you consider {alternative}?"
- "How did you decide the operational cost was worth it?"
- "What did the other engineer think?"

Each of these is one layer deep. The HM expects each to take 30-60 seconds to answer. They are not trying to trip you up; they are calibrating how deeply you actually thought about the work versus how much you absorbed second-hand from someone else's decision.

### The three layers

The HM's drill-down typically goes:

**Layer 1 — "What was the decision?"** You answered this in the project story. The follow-up confirms it: "you said you split it into two services — why?"

**Layer 2 — "What was the alternative, and why not?"** This is where most candidates start to thin out. If you can name the alternative *and* the specific reason you didn't choose it *and* the conditions under which you would have, you signal you actually owned the decision. If you say "we just went with this," you signal you inherited the decision from someone else.

**Layer 3 — "What would have changed the answer?"** This is the depth check. "Under what conditions would you have made the opposite choice?" Strong answer: "If our read traffic had been within 2x of write, we'd have kept them together — the operational overhead of the split is real and you only earn it back at scale asymmetry of 5x or more." Weak answer: "Hmm, I'm not sure, we just thought the split was right."

Three layers of follow-up survivability on at least *one* of your project decisions is the minimum for a senior screen. Two layers is enough for a mid-level screen. One layer at any level is a yellow flag — it suggests you weren't actually the decision-maker.

### How to prep for drill-down

The week before any HM screen:

1. Pick the project you'll describe.
2. List the **3-5 key decisions** in the project. For each, write:
   - The alternative you didn't choose.
   - One sentence on why you didn't choose it.
   - One sentence on what would have flipped your decision.
3. Read the list aloud. The decisions you can speak fluently are the ones to lead with. The ones you stumble on either need more thought or shouldn't anchor your story.

This is Exercise 1's main task. Most candidates skip it. The candidates who do it walk into HM screens able to answer any drill-down with one of the prepped responses.

### What hand-waving sounds like

Phrases that flag a hand-wave to a hiring manager:

- "Some kind of."
- "Best practices, I think."
- "I'm not sure, but I believe."
- "The way it's usually done."
- "Whatever was already there."
- "We just picked one."
- Switching from "I" to "we" specifically when asked about the technical detail.

Each of these is a tell. The HM hears them and starts watching for the same pattern across the call. Once two or three accumulate, the read shifts to "this person was around the work but didn't drive it."

## 6. Ownership language — "I" vs. "we"

The single most-readable signal in an HM screen is the ratio of "I" to "we" in your project answer, and *where* each pronoun shows up.

### The principle

Use "we" when you genuinely mean the team — the work that was owned collectively, the decisions made in a room with three people. Use "I" when you mean yourself — the design you wrote, the bug you found, the call you made when it was your call.

A clean answer to "tell me about a project" should have **both** pronouns, used in the right places.

- "We had a problem with the deploy time." (Yes — the team had it.)
- "We decided to split into two services." (Acceptable — if the decision was collective. If it was your design and the team ratified it, "I proposed the split, and we decided to go with it" is more accurate and stronger.)
- "I owned the boundary decision and the shadow-mode design." (Yes — these were your calls.)
- "The team caught three bugs in shadow mode" → if you found them, say "I caught" or "we caught" with specifics. The bland "the team" hides the contribution.

### The bad pattern

The most common failure mode at the mid-to-senior level is the **all-we answer**: an entire project story told in first-person plural. "We did this. Then we did that. Then we shipped." It hides every individual contribution and reads as "I was on the team but I'm not sure what *I* specifically did."

The fix is mechanical: when you're drafting Exercise 1, go through every "we" and ask: "is this genuinely the team, or is this me being modest?" Replace the modest "we"s with "I"s. The answer immediately becomes more readable.

### The worse pattern

The other failure mode is the **all-I answer**: every contribution claimed individually, no team mentioned. Reads as either inflated or as someone who doesn't credit collaborators. Worse than the all-we answer at senior+ because management is a collaborative discipline and the HM is screening for someone who can credit others.

The right answer is **mixed**: "I" for decisions you made, "we" for collective work, "the team" sparingly for things that genuinely had no individual owner.

## 7. The team-fit questions

After the recent-project anchor, the HM will pivot to team-fit. These questions come in many forms but reduce to a small number of underlying probes.

### The four team-fit probes

**Probe 1 — Conflict.** "Tell me about a time you disagreed with a teammate / your manager / a tech lead." The HM is checking whether you can describe disagreement without burning a bridge or sounding incapable of disagreement.

**Probe 2 — Collaboration style.** "What kind of team do you work best on?" or "Describe your ideal manager." The HM is matching your stated preferences against their team's actual operating style.

**Probe 3 — Communication.** "How do you handle a situation where someone on the team is consistently underperforming / blocking your work / disagreeing with the technical direction?" Tests the *practice* of communication, not the theory.

**Probe 4 — Self-awareness.** Some variant of "what feedback have you gotten that surprised you?" or "what's something you've changed your mind about in the last year?" Tests whether you've actually grown, or whether you've calcified.

Each gets its own treatment in the homework. Two principles that apply to all four:

- **Specific stories beat general statements.** "I work well with direct, candid managers" is a generic answer. "My current manager gives weekly written feedback in our 1:1, and the candour of it has been the most useful thing about the role" is a specific answer with a verifiable shape.
- **Never badmouth past managers or teammates.** Even if true. The HM cannot verify what you say, and they can absolutely verify that you said it. Variant: even when the conflict story requires you to describe a bad situation, frame it as a situation, not a person.

## 8. The "conflict" question — its own treatment

The conflict question is asked in some form in roughly 80% of HM screens. It deserves the longest treatment among the team-fit probes because the failure modes are loud.

### The two failure modes

**Failure 1 — "I don't really have conflicts."** This reads as: you avoid them (bad for collaboration), or you don't notice them (worse, suggests low social awareness), or you're not being honest. The HM will probe for one anyway. Have a real story ready.

**Failure 2 — The badmouth.** Naming a specific person, describing how they were wrong, describing how you were right, ending the story with vindication. The HM hears: "you're describing a colleague to a stranger and the colleague is the villain." Even if accurate, this is a flag for *how you might describe future colleagues to future strangers* — including the HM themselves.

### The structure that works

Four sentences, in this order:

> **The situation.** "On {project / decision}, my {teammate / tech lead / manager} and I disagreed about {one specific technical or process question}. They wanted {position A}; I thought {position B}."
>
> **The substance.** "The crux was {one-sentence summary of the actual disagreement}. They were focused on {their concern, characterised fairly}; I was focused on {your concern}."
>
> **The resolution process.** "We {wrote a one-pager / set up a 30-minute discussion / brought in a third senior engineer / ran a small experiment}. {What happened}."
>
> **What you took from it.** "In the end we {went with their position / went with mine / hybrid / experimented and let the data decide}. {One sentence on what you learned from the process, not the outcome.}"

Four sentences. Under 90 seconds. The story is not about who was right; it's about how you handled the disagreement. The HM is listening for: did you engage with their position, did you have a process for resolution, did you handle the outcome (whichever way it went) with grace.

### A worked conflict answer

> "On the billing-service split I described earlier, my tech lead and I disagreed about the rollout. They wanted a hard cutover after the shadow period; I thought we should do a percent-based rollout, starting at 5% of traffic. The crux was risk vs. velocity: they were focused on getting the migration done so the team could move on; I was focused on the cost of a correctness bug we hadn't caught in shadow. We set up a 30-minute discussion with our staff engineer to weigh in. We ended up with a percent rollout but compressed — 5%, 25%, 100% over three days instead of two weeks. What I took from it was that the right answer was neither of our original positions; the right answer was a structure that respected both concerns. I've since defaulted to bringing in a third senior voice earlier when the disagreement is about risk weighting."

What works: specific situation, fair characterisation of the other person's concern, a process (not a verdict), an outcome that wasn't a win for either original position, and a learning that's specific. ~95 seconds.

## 9. "Why this team / role?" — the question one level deeper

The recruiter asked "why this company?" The hiring manager asks something subtly different: "why this *team* and this *role*?"

This is a harder question because the team-and-role specifics are usually only knowable from the JD, the recruiter's notes about the team, the HM's own LinkedIn / public output, and what the HM themselves told you in the first 5 minutes of the call.

### The structure

Three threads, ordered most-specific to most-general:

1. **Why this team.** Something specific about the team's scope, recent work, or technical surface. Often comes from a phrase the HM used earlier in the call ("you said the team is moving toward {X} — that's exactly the kind of work I want to be doing"). Listening in the first 15 minutes pays back in this answer.
2. **Why this role.** Something specific about the level / scope / responsibility set in the JD. "The JD mentions ownership of the {component} — I've spent two years adjacent to that surface and would want to own one end-to-end now."
3. **Why this manager.** If you know anything public about the HM (talks, blog posts, open-source work), reference it briefly. If you've worked with someone they've managed in the past, mention that. Skip if you have nothing specific; do not fabricate.

The total answer is 60-90 seconds. Shorter than the "why this company" answer from the recruiter, because the depth is in the specificity rather than the breadth.

### What it should *not* sound like

- A repeat of the recruiter answer. The HM has read the recruiter's notes; they know what you said. Repeating it reads as not having a deeper layer.
- Generic role-shape language. "I'm excited about a senior IC role at a Series B" is the kind of answer that swaps in any company.
- Anything that sounds like comp ("the level you're hiring at is where I want to be"). The HM does not negotiate comp.

## 10. The "trick" or stress questions

Four classic HM stress questions. Each has a known failure mode and a known structure. Drill all four (Challenge 1) and they stop being stressful.

### Question 1 — "What's your biggest weakness?"

The failure modes:

- **Humblebrag.** "I work too hard." The HM rolls eyes, internally.
- **Disqualifying weakness.** "I'm bad at meeting deadlines." The HM writes it down.
- **No remediation.** "I'm bad at $thing. Anyway, moving on." The HM concludes you haven't worked on it.

The structure:

1. Name a **real but bounded** weakness.
2. Describe what it costs you concretely.
3. Describe what you've done about it.
4. Describe one piece of recent evidence that the work is paying off.

> "Concretely — I'm slow at writing design docs. My first drafts take me 2-3x as long as my peers' first drafts because I get stuck on framing. The cost is that I avoid starting them, which delays decisions on my projects. For the last 6 months I've been forcing a 30-minute timeboxed first draft, no matter how rough, and reviewing with a teammate before iterating. My last three design docs all hit a circulated draft within the first day of starting them, where the previous pattern was 3-5 days."

What works: a specific, plausible weakness; an actual cost; an actual remediation; recent evidence. Under 90 seconds.

### Question 2 — "Why should we hire you over the other candidates?"

Often phrased as "what makes you stand out for this role?" or "tell me why we should pick you."

The failure modes:

- **Generic strengths.** "I'm hardworking and a fast learner." Already in the noise floor of every candidate's answer.
- **Comparison to candidates you don't know.** "I'm probably stronger than the others." Reads as overconfident and uninformed.
- **The "I don't know, why don't you tell me" rebound.** Reads as not engaged.

The structure:

1. Name two or three **specific** things about your background that map to *this role's* requirements (not generic strengths).
2. Acknowledge that you don't know the other candidates but speak from the requirements you do know.
3. Close with one sentence that names the specific contribution you'd make.

> "I can't speak to the other candidates, but I can speak to the role. The JD mentions {requirement A} — I've spent three years specifically in that area at {company}. The JD also mentions {requirement B} — the project I described earlier was exactly that surface. And the team description sounds like you're at a stage where someone who's done the {specific thing} can come in and own that without ramp time. That's the contribution I'd be making."

What works: specific requirement-to-experience mapping, honesty about not knowing the field, a concrete contribution. ~60 seconds.

### Question 3 — "What would you do in the first 90 days?"

This is the question most candidates underprep, because it requires having thought about the role beyond the interview.

The failure modes:

- **Generic ramp answer.** "I'd meet with everyone on the team and understand the codebase." The HM has heard this 100 times. It's the floor of the rubric, not the ceiling.
- **Promising work you can't promise.** "I'd ship $thing in the first month." Reads as not understanding the team.
- **No structure.** A list of random activities with no through-line.

The structure that works:

1. **First 30 days — listen.** Specific 1:1s, codebase reading, on-call shadowing, documentation review. Name 2-3 specific intake activities.
2. **Days 30-60 — small contributions.** Smallest meaningful production change to demonstrate you can ship. Name what you'd look for as a candidate first PR.
3. **Days 60-90 — first ownership.** What you'd want to own by day 90. Frame as a question to the HM as much as a statement ("I'd want to be the on-call point for $component by day 90 — does that match what you'd expect?").

> "Days 0-30 I'd treat as pure intake — 1:1s with everyone on the team and the two adjacent teams, reading the last 6 months of design docs and the on-call runbook, shadowing one on-call rotation. Days 30-60 I'd be looking for the smallest meaningful production change — ideally a bug fix or a small refactor in a part of the codebase I want to learn well — to demonstrate I can land changes without breaking anything. Days 60-90 I'd want to be moving toward owning a piece — for this role, probably the {component you'd guess from the JD}. I'd want to validate that timeline with you, though — what does ramp usually look like for the team?"

What works: a real plan, ending in a question that confirms expectations. ~90 seconds.

### Question 4 — "Why are you leaving your current role?"

The HM version of this question goes deeper than the recruiter's. The recruiter heard the dignified non-answer; the HM may probe.

Use the same structure as the recruiter screen (push, pull, timing) but expect a one-layer follow-up:

- "You said you want to go deeper into {Y}. What specifically about your current role makes that hard?"
- "Have you talked to your current manager about that?"
- "What would have to change at {current company} for you to stay?"

The answer to each:

- The structural reason ("the team's roadmap doesn't include $Y for the next 12 months and the company's strategic direction is elsewhere").
- The honest version ("I have — we've discussed it; my manager agreed the role I want isn't likely to exist here in the timeframe I care about").
- The bounded version ("if {specific unlikely change}, I'd reconsider; that's not on the cards").

This is where many candidates leak frustration about their current role. Don't. The HM is listening for whether your reasoning is structural (a feature of the role/company shape) or interpersonal (a feature of someone you work with). Structural is fine; interpersonal is a flag.

## 11. The five common failure modes

The HM screens that go badly almost always fail one of these five ways:

1. **Vague project story.** No specific problem, no specific decisions, no numbers. Reads as someone who didn't drive their own work.
2. **Team-only ownership.** "We did this, we did that" for 5 minutes, with no "I" markers. Hides individual contribution.
3. **No follow-up survivability.** First "why?" gets an answer; second "why?" gets a hand-wave. Suggests the decisions weren't actually yours.
4. **No questions back.** "Nope, you covered everything." Lower engagement signal than at the recruiter screen, because the HM is genuinely offering to answer hard questions.
5. **Badmouthing.** Any negative framing of a current/past colleague or manager, however justified. Recorded as a flag in the debrief.

Each failure mode is fixable with preparation. None require talent. All are still common.

## 12. The HM's own read — what they're writing in the debrief

After the call, the HM will write 3-5 sentences for the recruiter and (if you advance) the rest of the loop. The structure of that write-up is roughly:

- One sentence: who you are and what you've done. ("Senior backend engineer, 5 years at payments-adjacent companies, currently at {company}.")
- Two sentences: what you said about your project, characterised. ("Walked through the billing-service split with depth — owned the design and shadow-mode rollout, articulated the operational-cost trade-off cleanly under follow-up.")
- One sentence: team-fit read. ("Came across as collaborative, asked specific questions about how the team makes design decisions.")
- One sentence: recommendation. ("Move forward to {technical screen / system design}, would be a strong fit on the team based on this conversation.")

If your call produces a write-up shaped like that, you're moving forward. If the project sentence is "described the project but couldn't go deep on the design choices," you're getting a "maybe" at best.

The single most actionable framing for the HM screen: imagine the HM writing those 3-5 sentences after your call. Are the sentences specific enough to defend you in a debrief, or are they bland enough that you'll get filtered out by someone else's stronger write-up?

## 13. Note-taking during the call

Two principles carry from Week 4, plus one specific to HM screens.

- **Capture facts, not impressions.** Team size, on-call rotation structure, the manager's tenure, the project priorities they describe, any specific technologies they mention.
- **Capture the manager's phrasing.** When the HM describes the team's goals or their own management style, write the exact phrase. You'll use it later — in the closing questions, in the follow-up email, or in subsequent rounds where the same phrase comes up.
- **Capture red flags.** This is the HM-specific bit. If the manager says something that gives you pause — vague answers to your questions, descriptions of the team that don't match the JD, hesitation around comp or growth questions — write it down. Don't react in the moment. Process later.

The minimum capture into your tracking spreadsheet:

- HM's name, title, tenure.
- Team size and structure.
- Stated current priorities for the team.
- Any specific upcoming work or projects the HM mentioned.
- Your top three red flags or yellow flags (if any).
- Your top two questions to follow up on in the next round (technical screen).

## 14. The post-HM-screen follow-up

Different from the recruiter follow-up. Sent within 24 hours, typically to the recruiter (who forwards to the HM) or directly to the HM if you have their email.

> Subject: Thanks for today — {your name}, {role}
>
> Hi {HM first name},
>
> Thanks for the time today. Two things stood out from our conversation: {one specific thing the HM said about the team or the work — proving you listened} and {one specific thing about the role that connects to your background}.
>
> I've been thinking about {one thing they raised — a problem the team is working on, a technical decision they mentioned}. {Two sentences: a brief, substantive thought, not a sales pitch.}
>
> Looking forward to next steps. Happy to share any prior work or references that would be useful for the rest of the team.
>
> Best,
> {Your name}

The differences from the recruiter follow-up:

- **Names a specific topic from the conversation.** Proof you listened in a way that's specific to *this* call.
- **Includes a substantive thought.** Two sentences that demonstrate you can continue the technical conversation outside the interview window. This is the HM-specific lever; most candidates skip it.
- **Slightly longer.** 4-6 sentences vs. the recruiter's 3-4. The HM has more bandwidth for longer follow-ups than the recruiter does.

Total: under 150 words. Anything longer reads as overinvested.

## 15. Self-check

- What's the anchor question of the HM screen, and how is it different from the recruiter's anchor?
- Name the six segments of the 4-6 minute recent-project answer, in order.
- A candidate describes their project entirely in "we" pronouns for 5 minutes. What's the read, and what's the fix?
- The HM drills down: "why X over Y?" → "what would have changed your mind?" → "what about Z?". What does each layer test?
- The conflict question has two classic failure modes. Name them.
- "Biggest weakness" — name a structure that produces a defensible answer in four sentences.
- "First 90 days" — what's the three-phase structure, and what does the third phase typically end with?
- The HM is writing 3-5 sentences in the debrief about you. What does the strong version of the "project sentence" look like vs. the weak version?

## Further reading

- **Will Larson — "Manager READMEs":** <https://lethain.com/manager-readme/>
- **Camille Fournier — "The Manager's Path"** (book; chapters 4-5 most relevant).
- **Pragmatic Engineer — "How tech companies hire engineers" multi-part series:** <https://newsletter.pragmaticengineer.com/>
- **Tech Interview Handbook — behavioural section:** <https://www.techinterviewhandbook.org/behavioral-interview/>
- **Lara Hogan — "Questions for your potential new boss":** <https://larahogan.me/blog/questions-for-your-potential-new-boss/>

When the project anchor and the drill-down survivability are clear, move to [Lecture 2 — Asking the Right Questions Back](./02-asking-the-right-questions-back.md). The closing 10-15 minutes of the HM screen is where you separate yourself; it deserves its own treatment.
