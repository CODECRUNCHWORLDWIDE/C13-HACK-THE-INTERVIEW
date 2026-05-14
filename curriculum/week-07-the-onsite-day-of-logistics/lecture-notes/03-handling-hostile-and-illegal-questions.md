# Lecture 3 — Handling Hostile and Illegal Questions

> **Duration:** ~1.5 hours. **Outcome:** You can name the seven common hostile-question patterns and reproduce a calm response to each, name the eleven EEOC-protected categories under US federal law and the non-US equivalents, recognise an illegal or impermissible question in real time, deflect it with scripted language that preserves the interview without answering the question, and decide when escalation — to the recruiter, to HR, to the EEOC — is the right move and when continuing the loop is the right move.

> **A note on this lecture.** This is the most legally framed material in C13. The standard for what is allowable in a US employment interview is set by federal statute (Title VII of the Civil Rights Act of 1964, the Age Discrimination in Employment Act of 1967, the Americans with Disabilities Act of 1990, the Pregnancy Discrimination Act of 1978, the Genetic Information Nondiscrimination Act of 2008, the Equal Pay Act of 1963) and enforced by the Equal Employment Opportunity Commission (EEOC). The resources file links the EEOC's pre-employment-inquiries guidance directly; read it. This lecture summarises and operationalises that guidance for the candidate-facing case. It is not legal advice. If a question in a real loop produces an experience you want to act on legally, consult an employment lawyer; the EEOC's intake hotline is also free and is the right first call.

## 1. The hostile question and the illegal question are not the same

Two distinct categories of difficult question. They overlap occasionally; they are mostly separate.

A **hostile question** is one designed (or accidentally functioning) to produce a stress response from the candidate. The question itself is legitimate — it is within the legal frame and within the rubric. "Walk me through a time you disagreed with your manager and how you handled it" is a legitimate behavioural prompt; "Tell me about a project that failed" is a legitimate one; "I notice your last role only lasted ten months — what happened?" is a legitimate one, even though it is uncomfortable. The challenge is composure under stress, not legal exposure.

An **illegal question** (or, more precisely, a question that the EEOC says cannot be the basis of a hiring decision) is one that touches a protected category: age, race, colour, religion, national origin, sex, pregnancy, disability, genetic information, citizenship status beyond legal-right-to-work, or retaliation for protected activity. The question itself is impermissible to base hiring on. The interviewer is sometimes asking deliberately, sometimes accidentally, sometimes from misunderstanding what is allowed. The challenge is to not answer the question, to preserve the interview, and to decide whether to escalate.

This lecture treats hostile questions in Sections 2-4 and illegal questions in Sections 5-9. The two response patterns overlap in some surface tactics (composure, calm tone, deliberate pacing) but differ in core intent (engage versus deflect).

## 2. The seven hostile-question patterns

Most hostile questions in software engineering loops fit one of seven patterns. They are not all bad-faith; several are deliberate calibration tools that produce useful signal when you respond well.

### Pattern 1 — The pushback question

"Your design doesn't handle the case where the queue backs up. What would you do?"

The interviewer challenges a specific decision you made and pushes you to defend or revise it. The calibration target is: do you defend a bad decision out of ego, or do you revise it when shown a weakness?

Response template:

1. **Acknowledge the pushback specifically.** "That's a fair point — I hadn't accounted for the queue back-pressure."
2. **Reconsider visibly.** "Let me think about how to handle it. The options I see are {A}, {B}, {C}. The trade-off between them is..."
3. **Land on a revised position or a tentative one with named uncertainty.** "I'd go with {B} for these reasons; I'd want to validate the assumption that {assumption} holds before committing."

The failure mode: defending the original decision through gritted teeth, or surrendering immediately ("you're right, I'll change it") without engaging with why.

### Pattern 2 — The "why did you make this choice" question

"Why did you choose Postgres for the user table instead of a document store?"

The interviewer drills into a specific past decision. The calibration target is: did you make a deliberate choice or did you do what was already there?

Response template:

1. **Name the constraint that drove the choice.** "The product had hard requirements on relational queries — joins between users and orders, transactional consistency for the checkout flow — and the team already had Postgres operational experience."
2. **Name the alternative you considered.** "We did consider a document store for the user profile specifically, but the join requirement out-weighed the schema flexibility benefit."
3. **Name the trade-off.** "The cost of that choice was that the schema migration when we added social-graph features took two sprints; a document store would have made it cheaper."

The failure mode: "we used Postgres because that's what we use" (no decision; no trade-off; no signal).

### Pattern 3 — The "tell me about a failure" question

"Tell me about a project that failed."

The interviewer asks for a specific recent failure. The calibration target is: do you have the self-awareness to name a real failure with specifics, or do you produce a fake failure that is really a strength in disguise?

Response template:

1. **A real failure, named in one sentence.** "We shipped the recommendation rewrite in Q3 2024 and it was withdrawn three weeks later because the click-through metric dropped 8%."
2. **Your specific role in it.** "I was the tech lead. I underweighted the A/B test results from the staging cohort because the cohort size felt small; I should have run a longer test before committing."
3. **The lesson, applied since.** "I now require an N-week shadow window for any feature touching the recommender stack before full rollout. We've used this on the next two launches."

The failure mode: a "weakness" that is a strength in disguise ("I work too hard"), a failure that is someone else's fault, or a failure with no lesson.

### Pattern 4 — The "what would you do differently" probe

"Walk me through your decision again. What would you change?"

A follow-up to a story or a coding answer. The calibration target is: can you self-critique in real time without surrendering to the critique?

Response template:

1. **Two or three specific things, named concretely.** Not "communicate better"; "I would have written a one-page design doc before the implementation started, circulated it to the three stakeholders by Friday of week one, and incorporated their feedback before week two."
2. **One thing you would not change** (this distinguishes self-critique from over-correction). "The choice of language and the data-model structure I would do the same way; those held up."

The failure mode: a wholesale "I would do everything differently" (reads as if you had no plan) or "I wouldn't change anything" (reads as defensive).

### Pattern 5 — The interrupting interviewer

"Wait, slow down. What did you just say about the index?"

The interviewer interrupts your explanation mid-flow. The calibration target is: how do you handle a redirect under interruption? Do you defend your flow, or do you pivot cleanly to the redirected topic?

Response template:

1. **Stop. Do not finish the sentence you were on.** Interrupting back, even gently, reads as not having heard the redirect.
2. **Acknowledge the pivot.** "Sure — let me back up. The index I was referring to is on {column}."
3. **Resolve the redirected question, then check.** "Does that answer it? I can come back to the original flow once you're satisfied."

The failure mode: pushing through to finish your original sentence, or losing the original flow entirely.

### Pattern 6 — The hypothetical hostile prompt

"Imagine your tech lead has shipped code you think is wrong and is refusing to revert it. What do you do?"

A scenario question with conflict baked in. The calibration target: how do you navigate disagreement with authority?

Response template:

1. **Clarify the scenario.** "Two questions: is the code in production, and have we observed user impact yet?" This buys time and clarifies the question.
2. **Walk through the steps you would take, in order.** "First, I'd put the disagreement in writing — a Slack message or a doc — naming what I think is wrong and why, with the data I have. Second, I'd ask for a 15-minute conversation, focused on the specific concern. Third, if the conversation doesn't resolve it and the impact is severe, I'd escalate one level up — but with the tech lead's knowledge that I'm doing it, not behind their back."
3. **Name the principle.** "The principle is: disagree privately, commit publicly, escalate transparently."

The failure mode: an answer that reads as "I'd never disagree with my tech lead" or one that reads as "I'd immediately go around them to their manager."

### Pattern 7 — The "are you sure?" repeated probe

You give an answer. The interviewer says "Are you sure?" You revise. They say "Are you sure?" again. The calibration target: can you hold a correct position under repeated probing without either capitulating or becoming defensive?

Response template:

1. **The first "are you sure?"** Take it seriously; recheck. "Let me re-verify... yes, I'm confident that {claim}."
2. **The second "are you sure?"** Treat as calibration. "I am — and here's the specific reasoning that grounds it: {one sentence}." Do not over-explain.
3. **The third "are you sure?"** "I am confident in the answer. Is there a specific concern you want me to address?"

The failure mode: revising under each probe until you arrive at an answer you do not actually believe, or becoming defensive ("why do you keep asking?"). Both lose points.

## 3. The general response template for hostile questions

Across the seven patterns, a small set of habits applies:

- **Calm tone.** Match composure, not heat. The interviewer's hostility is the test; calm is the answer.
- **Acknowledge before responding.** "That's a fair point" or "Let me think about that for a second" buys composure and signals openness.
- **Do not match the energy.** Sharp questions land better when answered with the same tempo you used in warm rounds.
- **Take a pause.** A 3-5 second pause before answering is composure, not weakness. The instinct to fill the silence is the instinct to lose.
- **Name your reasoning, even when conceding.** "You're right, and here's why I went the other way originally..."
- **Do not apologise excessively.** One "good point" is enough; three "sorry, sorry, sorry"s reads as panicked.
- **Close cleanly.** End your answer with a complete sentence, not a trailing thought. "...and that's what I'd do." Beat. Wait.

## 4. The hostile interviewer vs. the rude interviewer

Some interviewers are not running a hostile pattern; they are simply rude. The two require different responses.

The hostile-by-design interviewer is calibrating; their hostility has shape, recovers warmth at the closing, maps to a specific dimension (challenge every assumption, push every decision). The rude interviewer is inconsistent — dry on some questions, warm on others, impatient in a personalised way. Lecture 2 covers the distinction in depth.

For the rude interviewer:

- **Do not match.** Their behaviour is a problem; making it two people's problem does not help you.
- **Score the round as fully scored.** Their write-up is still written; the rest of the loop still happens. Bring your normal performance.
- **Surface to the recruiter at the closing, briefly and once.** "{Interviewer name} was a little tough to read; I wasn't sure if I was tracking with them. Did anything come up?" Lets the recruiter recalibrate the interviewer's write-up if there is feedback to give. Do not over-share or characterise; the recruiter knows the interviewer.

The line between rude and hostile-and-illegal is sometimes blurry. If the rudeness includes a question that crosses into a protected category, the question itself is the issue and Sections 5-9 apply.

## 5. The legal frame — the eleven protected categories under US federal law

The Equal Employment Opportunity Commission (EEOC) enforces several federal statutes that together establish protected categories. A hiring decision based on any of these categories is illegal under US federal law. The categories:

1. **Age** — 40 and older. Source: Age Discrimination in Employment Act of 1967 (ADEA).
2. **Race** — Source: Title VII of the Civil Rights Act of 1964.
3. **Colour** — Source: Title VII. (Treated separately from race; covers, for example, discrimination based on skin tone within a race.)
4. **Religion** — Source: Title VII.
5. **National origin** — Source: Title VII.
6. **Sex** — Source: Title VII (as amended). Includes sex stereotyping, sexual orientation, and gender identity following Bostock v. Clayton County (2020).
7. **Pregnancy** — Source: Pregnancy Discrimination Act of 1978 (amends Title VII).
8. **Disability** — Source: Americans with Disabilities Act of 1990 (ADA). Covers physical and mental disabilities; covers perceived disabilities even if not actual.
9. **Genetic information** — Source: Genetic Information Nondiscrimination Act of 2008 (GINA). Includes family medical history.
10. **Citizenship beyond legal-right-to-work** — Source: Immigration Reform and Control Act of 1986 (IRCA). Employers may ask if you have the legal right to work; they may not require citizenship specifically unless legally required for the role.
11. **Retaliation for prior protected activity** — Source: Title VII, ADEA, ADA. Past EEOC complaints, past whistleblowing, past discrimination charges.

State laws often add categories not covered federally — marital status, source of income, hairstyle (the CROWN Act in some states), criminal history (ban-the-box statutes), and others. Local ordinances add more. The federal eleven is the floor; the actual list in your state may be longer.

The EEOC's pre-employment-inquiries guidance translates these categories into "what can and cannot be asked." The summary, from the EEOC's own framing: questions about a protected category are not always illegal, but **basing a hiring decision on the answer** is. In practice, this means that any question that touches a protected category creates legal exposure for the employer if you are not hired — and most interviewers know this, which is why most do not ask such questions. The ones that do are either uninformed, careless, or testing you.

## 6. The categories of question to recognise

In practice, the questions that touch a protected category fall into a small number of patterns. Recognising them in real time is the first skill.

### Age-adjacent questions

- "When did you graduate?" (Inferable age.)
- "How long have you been in the industry?" (Inferable age.)
- "Are you a digital native?" (Coded age question.)
- "Do you think you'd fit in with a young team?" (Coded.)

The first two are softer — they can be answered factually without triggering exposure (your graduation year, your YoE) — but you can also deflect. The third and fourth are sharper; deflect.

### Race, national origin, religion questions

- "Where are you from?" / "Where are you really from?" (National origin.)
- "What kind of name is {your name}?" (Coded national origin.)
- "Do you celebrate {holiday}?" (Religion.)
- "Will you need time off for religious observances?" (Religion.)
- "Do you speak {language} at home?" (National origin.)

All four are deflection-required. The "where are you from" question is the most common; it is almost always asked innocently (small talk) but it is still a protected-category question and still deflectable.

### Sex, pregnancy, family-status questions

- "Are you married?" / "Do you have a partner?" (Sex; also affects family-status protections in some states.)
- "Do you have kids?" / "Are you planning to have kids?" (Pregnancy; family status.)
- "How will you balance this role with your family?" (Family status; sex.)
- "Are you on maternity leave / parental leave?" (Pregnancy.)
- "How would your spouse feel about you working late?" (Sex; family status.)

These are the most-frequent illegal questions in software-engineering loops. The "do you have kids" question lands more in lunch interviews than in formal rounds, often in informal small-talk; deflect anyway.

### Disability and genetic questions

- "Do you have any health conditions we should know about?" (Disability; before an offer is extended, this is illegal under the ADA.)
- "How is your health?" (Same.)
- "Have you ever had a mental-health condition?" (Disability.)
- "Is there a history of {disease} in your family?" (Genetic information; specifically illegal under GINA.)
- "Do you take any medications?" (Disability.)

These are sharper and rarer. The disability questions sometimes come up in physical-office contexts ("can you lift X pounds?" — legal only if the role actually requires it). Software engineering roles rarely have physical requirements; questions about your health in this context are deflectable.

### Citizenship questions

The legal version: "Do you have the legal right to work in the United States, now and ongoing, without sponsorship?" This is allowed; you may answer.

The illegal versions:

- "Are you a US citizen?" (Goes beyond legal-right-to-work.)
- "What's your visa status?" (Goes beyond legal-right-to-work.)
- "Where were you born?" (Coded national origin.)

If you require sponsorship and the role does not offer it, this is legitimate filter content and the recruiter or HM screen should have surfaced it earlier. If the question is asked at the onsite specifically about your country of origin or your specific visa, deflect.

### Salary-history questions

Salary history is not a federally protected category, but salary-history questions are prohibited in many US states (California, New York, Colorado, Washington, Massachusetts, several more). They are also generally bad for the candidate because they anchor the offer to the previous salary rather than to the role's market value.

- "What's your current salary?" (Illegal in many states; bad for you everywhere.)
- "What were you making at your last job?" (Same.)
- "What are your salary expectations?" (Legal; different question; answer with a range.)

The deflection for the salary-history question is different from the other deflections (Section 7's "preserve the interview" framing) — it is a market-anchored redirect, because the salary question is at the offer end of the pipeline, not the legal-protection end.

## 7. The deflection language

The general response to an illegal or near-illegal question has four moves:

1. **Pause for one beat.** Just one. Long enough to compose; not long enough to be obviously gathering yourself.
2. **Bridge to a related, legitimate topic.** "What I can tell you about that is..." or "What's relevant for the role is..."
3. **Pivot to a topic the interviewer was likely actually trying to surface.** Most illegal questions are asked because the interviewer was groping for a legitimate signal and reached for the wrong question.
4. **Continue the round.** Do not draw attention to the moment; do not lecture the interviewer; do not pause to consider whether to escalate. The escalation decision is for after the round.

### Deflection scripts by category

These are scripts. Adapt them; do not recite them. The composure is more important than the exact words.

**Age (graduation year, YoE):**

> "I have {X} years of relevant experience, including the deep work on {project}. Happy to walk through the technical depth on any of it."

(Answers the YoE — which is itself not protected and is often a legitimate role question — and pivots to the work.)

**Where are you from / really from:**

> "I'm based in {city} now. Originally I'm from {country or "the East Coast" or some non-protected reframing}. — but, more relevant, what I can tell you about the role I'm applying for is..."

Or, if you do not want to share even an origin:

> "I've been in {city} for {N} years. What drew me to this role specifically is..."

**What kind of name is {your name}:**

> "It's {one-line factual answer if you want to share, e.g., "Polish"}. What I'd actually love to talk about is the team's recent work on {topic} — I noticed {specific thing}."

Or:

> "Family name. — Speaking of the team, I had a question about {topic}."

**Do you celebrate {holiday}:**

> "I'm happy to work within whatever holiday calendar the team uses. The team's working pattern is something I'd want to know more about — could you tell me how the team handles {related legitimate topic, e.g., on-call rotations}?"

**Will you need time off for religious observances:**

> "I'm not anticipating any unusual scheduling needs. Could you tell me a bit more about the team's working hours and on-call structure?"

(Religious-accommodation requests are a separate post-offer conversation, if relevant.)

**Are you married / do you have a partner:**

> "I keep my personal life out of work conversations, but I'm happy to talk about anything related to the role. For example — I had a question about the team's collaboration style."

**Do you have kids / are you planning to have kids:**

> "That's not something I'd typically discuss in an interview. But I can tell you that I'm fully committed to the role; my work history shows the kind of focus and continuity I bring."

**How will you balance this role with your family:**

> "I manage my time professionally; the role's expectations are something we can discuss directly. What does a typical week look like for the team?"

**Health / disability questions:**

> "I'm not aware of anything that would affect my ability to do the role. Is there a specific physical requirement of the position you wanted to clarify?"

(This redirects to the only legal version of the question — whether you can perform the essential functions of the job, with or without reasonable accommodation.)

**Genetic / family-medical-history questions:**

> "That's not something I'd discuss in an interview. Could you tell me more about the role itself?"

(More abrupt is acceptable here because the question is sharper and more clearly out of bounds.)

**Citizenship beyond legal-right-to-work:**

> "I have the legal right to work in the {US/UK/etc.}. The specifics of my immigration status I'd prefer to discuss with HR if it becomes relevant to the offer process."

**Salary-history question:**

> "I prefer not to anchor on previous compensation. What I can tell you is the range I'm targeting for this role, given my experience and the market data — I'm looking at {range based on levels.fyi for this level and location}."

(The salary-history deflection is the most-rehearsable; Week 9 covers the full negotiation framing.)

### The general script (when you do not have a specific one prepared)

> "I'm not sure that's relevant to the role we're discussing. What I can tell you is..."

This is the universal fallback. It is more abrupt than the category-specific deflections; use it when surprised.

## 8. The reactive moves you should not make

A few responses are tempting and are wrong.

### Do not answer the question

The temptation to answer ("yes, I have two kids") is high, especially because most illegal questions are asked in friendly, small-talk tone. The cost: you give the interviewer information they can — even unconsciously — use in the debrief. The cost is not "the interviewer will use it against you"; it is "the information enters the decision process," which is what the law prohibits.

Answering the question also signals to the interviewer that you do not know what the law says. This is not a hostility-calibration test; failing it does not help you.

### Do not lecture the interviewer

The temptation to say "you can't ask me that, it's against the law" is high in the moment. The cost: you have just made the interviewer your adversary in a conversation that was, until that point, a job interview. Even when you are legally correct, the interviewer will defend themselves and will write a write-up that is much harsher than the round otherwise warranted. The "hostile candidate" write-up is real, recognisable, and almost always loses the loop.

The exception is when the question is sharply and clearly illegal *and you are willing to lose this loop in exchange for a record of escalation*. Section 9 covers the escalation case. For the typical mid-interview illegal question, deflection is the right move; lecture is not.

### Do not joke

The temptation to defuse with humour is high. The cost: the joke does not land for some interviewers, and the question is now in the record. Worse, the joke can sound like you are answering the question by implication ("no, my husband's not bothered by my hours, haha"). The deflection should be composed and unfunny.

### Do not visibly react

The temptation to register surprise — a raised eyebrow, a long pause, a "huh, that's an unusual question" — is high. The cost: the interviewer registers the reaction, sometimes corrects course, sometimes hardens. Better to receive the question with the same composure as any other question, deflect smoothly, and move on. The composure itself is a signal of preparation.

### Do not over-apologise for the deflection

"Oh, I'm sorry, I just — I don't want to — sorry, I prefer not to talk about that." The apology amplifies the awkwardness and makes the deflection look like discomfort rather than principle. State the deflection cleanly, in one sentence. Move on.

## 9. The escalation decision — when to surface, to whom, and how

Most illegal questions are best handled with deflection and a private note for the after-action document. Some warrant escalation.

### The factors that argue for deflection (and a private note)

- **The question was asked in apparent good faith.** The interviewer was making small talk and reached for a question they did not realise was protected.
- **The question is single, not patterned.** One question about your kids in an otherwise normal lunch is different from four questions about your family across two rounds.
- **The deflection worked.** The interviewer accepted the redirect; the conversation moved on; the round held.
- **You are otherwise interested in the company.** If you are mid-loop at a company you genuinely want to work at, escalation has a real cost — not the legal cost (you have rights regardless), but the cost of the conversation you have to have with this same hiring team if you accept an offer later.

For all of these, the right move is: deflect in the moment, write it down in the after-action document, decide later — once the loop is over and you have offers on the table — whether to surface anything with the recruiter.

### The factors that argue for escalation

- **The questioning was patterned.** Multiple questions across one round or across the loop that touch the same protected category. The interviewer was probing, deliberately or not.
- **The questioning was hostile in tone, not just in content.** The illegal question was asked sharply, dismissively, or with implication. Combine an illegal question with a hostile tone and the interviewer has crossed two lines.
- **The questioning continued after a clear deflection.** You deflected; the interviewer pressed. This is no longer accidental.
- **The questioning affected the substance of the round.** The interviewer treated you differently after the question; the round changed; the rubric was affected.
- **You experienced concrete impact in the loop.** You were rejected, and you have reason to believe the protected-category questioning was a factor.

### The escalation paths

**Path 1 — Surface to the recruiter, mid-loop.**

If a round contains a clearly illegal question and you are mid-loop, you can mention it at the closing or in a brief private moment with the recruiter. The script:

> "I want to flag something briefly so you have it. {Interviewer's name}'s round included a question about {category} — {one-sentence specific}. I deflected and the round moved on. Wanted to let you know."

The recruiter will note it. Recruiters have a strong incentive to surface this internally because the company's legal exposure is real; the recruiter will usually take the note seriously and pass it to the appropriate HR contact. The cost to you: low. The benefit: the company can act on the information, either by addressing the interviewer or by adjusting the debrief.

The risk: the recruiter, depending on the company, may close ranks. At small companies or at companies with weak HR functions, the recruiter may report to the hiring manager who is friends with the interviewer; the report may not be acted on. You cannot tell in advance. Use Path 1 when the company is large enough to have a real HR function and the interviewer behaviour was concrete enough to act on.

**Path 2 — Surface to HR, post-loop.**

After the loop is done, you can request a conversation with HR (separately from the recruiter). This is the right path when the issue is significant enough that the recruiter is not the right channel — multiple illegal questions, sharp tone, a sense that the loop was decided on the protected category.

> "I'd like to speak with someone in HR about a couple of moments from my interview. Could you set up a time?"

HR's job is to manage legal exposure. They will take the conversation seriously. The conversation is on the record.

**Path 3 — Decline the role and write a letter.**

If you are offered the role and decline because of the questioning, a brief letter to HR — copying the recruiter — naming the issue is appropriate. The letter is short, factual, and unangry. It establishes a record.

> "Thanks for the offer. I'm declining for several reasons, including {brief factual description of the questioning that occurred}. I wanted to share the context for the benefit of future candidates."

Companies sometimes act on letters like this; sometimes they do not. The letter itself is a useful artefact regardless.

**Path 4 — File a charge with the EEOC.**

For sustained, patterned, or clearly impactful illegal questioning — especially when combined with not being hired — you can file a charge with the EEOC. The charge initiates a federal investigation. The threshold is high; the process is long; the outcome is sometimes a settlement, sometimes nothing, occasionally a finding of cause. Filing a charge is a meaningful step; consult an employment lawyer first if you are considering it.

The EEOC's charge-filing page is in the resources file. The free consultation hotline answers questions about whether a charge is the right step in your specific situation.

### The escalation you should not perform

Public escalation — Twitter, Reddit, LinkedIn — is almost never the right move for a single interviewing experience. The cost to your reputation in the industry is real; the company's response is often to escalate against you in return; the legal record is weaker than a charge filed through the proper channel. If the experience was severe enough to warrant a public statement, it is severe enough to warrant a lawyer first.

## 10. Knowing what is and is not allowed — a quick reference

The full EEOC guidance is in the resources file. A compressed version, for the cheat sheet:

| Category | Allowed | Not allowed |
|----------|---------|-------------|
| Age | "What are your salary expectations?"; YoE-related; date-of-graduation only if relevant to credential check | "How old are you?"; "When were you born?"; "When did you graduate?" if used as proxy for age |
| Race / colour | Nothing race-related at the interview stage | Any race / colour question |
| National origin | "Do you have the legal right to work?"; "Are you fluent in {languages relevant to the role}?" | "Where are you from?"; "What kind of name is that?"; "What's your accent?"; native-language at home |
| Religion | "Can you work the schedule, including {specific times relevant to the role}?" | "Do you celebrate {holiday}?"; "What is your religious affiliation?" |
| Sex / gender / sexual orientation | Nothing sex-related at the interview stage | Marital status, partner questions, gender-identity questions, sexual-orientation questions |
| Pregnancy | Nothing pregnancy-related | "Are you pregnant?"; "Do you plan to have children?"; "Are you on maternity leave?" |
| Disability | "Can you perform the essential functions of the role with or without accommodation?" | "Do you have any health conditions?"; "Have you ever had {condition}?"; "What medications do you take?" |
| Genetic information | Nothing genetic | Family medical history; any genetic-test results |
| Citizenship | "Do you have the legal right to work in the {country}?" | "Are you a US citizen?"; "What's your visa status?"; "Where were you born?" |
| Retaliation | n/a (this is about prior protected activity) | "Have you ever filed a discrimination complaint?"; "Have you ever sued an employer?" |

The pattern: questions about whether you can do the job, on its actual requirements, are allowed. Questions about who you are, in any of the protected dimensions, are not.

## 11. The single most important habit

Rehearse the deflection scripts until they are muscle memory. The reason most candidates fumble illegal questions is that the questions land cold, in a moment when the candidate is tired, the round is going well, the interviewer asked in a warm tone, and the candidate does not have a prepared response.

Exercise 2 of this week is the rehearsal drill. Run it with a peer who is willing to ask the questions in roleplay, ideally in the middle of a behavioural-round mock. The fluency develops in the first one or two practice runs; the muscle memory holds across a real loop.

The rehearsal is the substitute for relying on legal knowledge in the moment. You do not need to be able to cite Title VII of the Civil Rights Act of 1964 in the middle of a round. You need to be able to deflect calmly, in one sentence, without breaking rapport, and the only way to do that is to have rehearsed it.

The EEOC's guidance — the resources file links it directly — gives you the legal floor. The deflection scripts above give you the operational layer. The rehearsal in Exercise 2 gives you the muscle. The combination is what carries a real candidate through a real onsite when the question lands.
