# Lecture 2 — The Comp Conversation

> **Duration:** ~2 hours. **Outcome:** You can name a defensible compensation range with a confident high anchor, distinguish base from total comp, decide whether to name the first number or deflect, and use levels.fyi to translate a target company and level into a band you can defend with public data.

## 1. The comp question is on every screen, and most candidates botch it

Beat 6 of nearly every recruiter screen contains some version of:

- "What are your compensation expectations?"
- "What kind of base salary are you targeting?"
- "Any number in mind for total comp?"
- "What were you making at your last role?" (Banned in many US states. Still asked.)

The candidate's typical response, in roughly this order of frequency:

1. **The hedge.** "Whatever's competitive for the role, really — I'm flexible."
2. **The undersell.** "Around $X." (Names a number 15-30% below band.)
3. **The unjustified ask.** "$Y." (Names a number with no reasoning, then can't defend it when pressed.)
4. **The decline.** "I'd rather hear from you first."
5. **The defensible answer.** "Targeting total comp in the $A-$B range, base ideally in the $C-$D range, based on levels.fyi data for {level} at peer companies in {location}."

Only the last one preserves your negotiating position **and** signals seriousness. The rest cost you money — sometimes tens of thousands of dollars per offer — and several read as unprofessional besides.

This lecture is about getting you to answer #5 by default, on every screen, without flinching.

## 2. The components of a compensation offer

Before you can name a number, you need to know what the number contains. A typical full-time tech compensation package has four parts. The recruiter is fluent in all four; you need to be too.

### Base

The annual cash salary, paid in regular paychecks. The most-comparable component across companies because it doesn't depend on equity volatility or bonus realisation.

Bands vary by company, level, and location. A senior engineer in San Francisco at a public tech company is typically in the $180k-$240k base range; the same engineer in Austin or Berlin will see different bands; the same engineer at a Series-A startup may see lower base + more equity.

### Equity (RSUs / options)

**RSUs (Restricted Stock Units)** at public companies: a grant of shares that vests over time (typically 4 years, with various vesting schedules — quarterly, monthly, or front-loaded). At grant date, the recruiter quotes "X dollars of RSUs over 4 years" or "X dollars annualised."

**Options** at private companies: the right to buy shares at a fixed strike price. Worth nothing until a liquidity event (IPO, acquisition). The recruiter quotes a percentage of the company or a dollar value at a recent valuation.

**Annualisation rule.** Always think of equity as the per-year value, not the headline 4-year number. A "$400k RSU grant over 4 years" is $100k/year of equity comp. Recruiters quote the 4-year number to make offers look larger.

### Signing bonus

A one-time cash payment, usually paid in the first 1-3 months of employment, sometimes with a clawback if you leave within 12-24 months. Typical range: $10k-$50k for senior IC roles; larger at FAANG-tier; sometimes zero at startups.

The signing bonus is one of the most-negotiable line items in an offer because it costs the company a one-time charge against their hiring budget, not an ongoing cost against headcount. Recruiters are often authorised to move signing without escalating.

### Annual bonus

A target cash bonus paid annually, usually expressed as a percentage of base (e.g., "10% target bonus" = 10% of base, paid if you and the company hit targets). Some companies have no annual bonus; some have a guaranteed first-year bonus; some are entirely target-based.

### Total comp (TC)

The sum: `base + (equity / vesting years) + (signing / N) + (annual bonus target)`. This is the headline number levels.fyi reports. When a recruiter asks "what are you targeting for total comp," they mean this number.

**The mental model.** Four components. The recruiter optimises a four-dimensional offer. You should know which lever the recruiter is most likely to pull at your level and target company — at FAANG-tier senior+, the equity lever moves most; at early-stage startups, base + equity percentage are the negotiation; at mid-stage scaleups, signing and base are most-flexible.

## 3. levels.fyi — the canonical public reference

levels.fyi is the most-used public compensation database in tech. Self-reported, weighted, and large enough that the medians are reliable for major companies and locations.

### What you can look up

- **Company + level + location → median TC, base, equity, bonus.** Click into any company's page; filter by location and level.
- **Percentile distributions.** For each company/level/location combo, levels.fyi shows the 25th, 50th, 75th, and 90th percentiles. These are the actual numbers reported by candidates who took offers.
- **Level mapping.** levels.fyi has a "level mapping" page that translates roughly between companies — "Senior at Google ≈ E5 at Meta ≈ Senior at Stripe ≈ L4 at Airbnb." Useful but imperfect; trust the median TC over the level label.
- **Historical data.** Trends over the last 12-24 months. Useful in volatile years; comp at most tech companies fell 5-15% from 2022 peaks through 2024.

### How to read the percentiles

A levels.fyi page shows a band like:

> Senior Software Engineer, San Francisco
> Median TC: $390k · Base $200k · Equity $150k · Bonus $40k
> 25th percentile: $340k · 75th: $440k · 90th: $510k

What this means:

- The **median (50th)** is the centre of mass. Half of reported offers are above, half below.
- The **75th percentile** is where strong candidates with leverage (competing offers, deep specialisation, internal advocate) typically land.
- The **90th percentile** is where exceptional cases land — typically requires a competing offer at peer-tier, exceptional seniority for the level, or an unusual specialty.
- The **25th percentile** is where candidates who didn't negotiate, took the first offer, or were hired in a soft market typically land.

### Your target on levels.fyi

For a typical week-4 candidate (resume in shape, no competing offers yet), your defensible target is **between the 50th and 75th percentile** for your target company / level / location. Below the 50th means you accepted less than half of comparable candidates; above the 75th typically requires explicit leverage you don't yet have on a screen call.

The high anchor is the 75th. The base case is the 60th-65th. The walkaway minimum is the 40th-50th.

### Caveats

- **Self-reporting bias.** People who reported offers on levels.fyi are slightly more comp-aware than the average candidate, which biases the medians upward by 5-10% compared to the true population.
- **Stale data.** During large market shifts (2022 → 2023, e.g.), reported data lags. Cross-check with at least one current job posting from the company that includes a salary range (many US states require this).
- **Small-company gaps.** levels.fyi is thick for FAANG and major scaleups; thin for sub-100-person companies. For startups, you'll often see only 1-3 reports, which is not enough to anchor on. Use Pragmatic Engineer's comp posts and h1bdata.info as cross-references.
- **Location skew.** Same level at same company can vary 30-40% by location. Always filter by location.

## 4. The "who names the first number" question

There is a small ritual at the start of the comp conversation about who names the first number. The conventional advice is "never name first." The honest answer is: it depends, and in 2025 it depends less than it used to, because pay-transparency laws have shifted the dynamic.

### The classical advice (still partially correct)

The argument: whoever names the first number sets the anchor for the negotiation. If you name $180k and the company was planning to offer $220k, you just lost $40k. So: deflect, ask for their range, name yours only after.

This was the default playbook for a decade. It is still useful as a fallback, and Patrick McKenzie's negotiation essay is built around variations of it.

### The 2025 reality

Several shifts:

- **Pay-transparency laws.** California, Colorado, New York, Washington, Illinois, and the EU now require posted salary ranges on most job postings. The "company range" is often public before the call. The classical advice — "ask them for their range" — no longer has the same value when the range is already on the JD.
- **Recruiters expect a number.** Most recruiters at major companies will press you for a number, politely, three times. The deflection that worked in 2015 reads as evasive in 2025.
- **levels.fyi.** Both sides know what levels.fyi reports. The negotiation is no longer asymmetric in information.

### The current playbook

Four scenarios:

#### Scenario A — The JD has a published salary range

Read it before the call. The published range is the company's pre-approved band for that role at that level. Your job:

- If your high anchor falls inside the published range: name your number, anchored at the top third of the published range. "I was targeting the top of the range you've posted — around $X-$Y."
- If your high anchor exceeds the published range: name your number anyway, with one sentence of justification ("based on levels.fyi data for the level and my five years in payments specifically, I was targeting around $Z"). This signals you've done homework; the recruiter will either tell you the role can't go that high or take it to the hiring manager.
- If your number is below the published range: name the range, not the lower number. "Inside the range you've posted." Don't undercut the published floor; that just signals you don't know your worth.

#### Scenario B — No published range, the recruiter asks first

Default: name your range. Anchor at the top of your defensible band (the 75th percentile from levels.fyi for the company / level / location).

> "Targeting total comp in the $X-$Y range, base ideally between $A and $B, based on levels.fyi data for {level} at peer companies in {location}. Happy to discuss the mix — I value equity and signing as well as base."

The structure:

1. Name a **range**, not a point. (~20% spread, e.g., $360k-$430k.)
2. Anchor at the **top of the range** with the **base** they're most likely to remember.
3. Cite the **source** (levels.fyi or a competing posted range).
4. Signal **flexibility on mix** without flexibility on TC.

#### Scenario C — No published range, you want to defer

Sometimes you genuinely don't have enough information. The legitimate deflection:

> "I'd love to learn more about the role, the team, and the level before locking in a number — can you share the rough band you have approved for this role?"

This works on the **first** ask. If the recruiter pushes again ("we'd really like a number from you"), you switch to Scenario B. Do not deflect twice; the second deflection reads as evasion, not professionalism.

#### Scenario D — They ask what you make at your current job

In several US states (CA, NY, MA, CT, IL, others) and in the EU, asking about salary history is illegal. In other places it is legal but increasingly seen as poor practice.

The correct response, in any jurisdiction:

> "I'd rather discuss target comp than history — for context, I'm targeting {your range} based on the level and the market."

You are not legally obligated to disclose, even where the question is legal. Recruiters who push past this are signalling something about the company's culture; note it.

## 5. The high anchor — what it is and why it matters

The "high anchor" is the first compensation number named in the negotiation, set deliberately at the top of your defensible band. Anchoring is a well-documented cognitive effect: subsequent numbers in the negotiation cluster around the anchor.

### Setting the anchor

Three components:

1. **Defensible.** You can point to public data (levels.fyi, JD, a peer's posted offer) that supports the number.
2. **Top of band, not above.** The anchor is the 75th percentile of your reasonable band, not a number plucked from nowhere. Numbers above your defensible band invite a "we can't do that here" that ends the conversation early.
3. **Stated with confidence.** No hedging adverbs ("just," "only," "kind of"). State the number; pause; let it sit.

### Why "with confidence" matters mechanically

If you name $X and immediately add "but I'm flexible, that's just a starting point, totally negotiable, whatever you can do is fine," the recruiter writes down $X minus 10-15%. The hedge is read as "the candidate doesn't actually believe the number."

**The pause.** After you name the number, stop talking. Count to four silently. Let the silence sit. The recruiter will respond — sometimes with a "let me check," sometimes with a confirmation, occasionally with "that's higher than our band." All three are useful information. Most candidates fill the silence with self-justification that erodes the anchor.

## 6. The flinch — what the recruiter's reaction tells you

A practiced recruiter has a calibrated response to candidate comp asks. The micro-reactions are surprisingly readable:

- **Flat acknowledgement.** "Got it, that's noted." → Your number is comfortably inside the band. They are not flinching because they don't have to.
- **Verbal pause / "let me look into that."** → Your number is near the top of band or slightly above. They may need to escalate.
- **Quick downward push.** "We're typically more in the $X range for this level." → Your anchor is above band. They are pulling you back to the middle.
- **Polite end of conversation.** "That's helpful — I'll get back to you on next steps." → Your number is significantly above band, or the role's band doesn't fit.

None of these is a failure state. The flinch is information. If you get a flat acknowledgement, you may have anchored too low and should anchor higher next time. If you get a polite end, you have either mis-targeted the role's level or mis-read the market and should research more.

## 7. Range vs. point

The recruiter will almost always ask you to convert your range to a point. "You said $360k-$430k — what's the specific number you're targeting?"

The response, in three options ordered by negotiating strength:

1. **Stay on the range, repeat the top.** "I'm anchoring at the top of that range — around $420k-$430k total." Restates the high end as the working number without naming a point.
2. **Convert to a point at the top.** "$425k total comp." Names a point, but at the top of your stated range, preserving anchor.
3. **Convert to a point at the middle (only if pressured and you have a reason to).** "Mid-range, around $395k." Concedes ground. Use sparingly.

Most candidates default to option 3 because the recruiter's push feels like pressure. The push is a routine probe; the correct response is most often option 1 or 2.

## 8. Base, total, and the lever conversation

Different companies negotiate on different levers. Knowing which lever you have leverage on, at which company, matters more than the total target.

| Company stage | Most-flexible lever | Least-flexible lever |
|---------------|---------------------|----------------------|
| FAANG-tier, public | Equity (RSU grant size) | Base (band-constrained) |
| Mid-stage scaleup | Signing, equity refresh | Base (band-constrained but more give than FAANG) |
| Series A-B startup | Equity percentage, signing | Cash (often capped by runway) |
| Mature private | Base, signing | Equity (often standard grants) |

The implication for the recruiter screen: when the recruiter asks "what are you targeting," you should ideally know the company's flexibility shape. If they're FAANG-tier and your anchor is base-heavy, you've targeted the wrong lever — they have less give there than on equity. Restructure your ask.

**Example.** A senior IC targeting Google. Public, FAANG-tier. levels.fyi median for L5 (Senior) in SF: $200k base, $200k equity/yr, $40k bonus → $440k TC. You target $440k. The recruiter has very little room on the base ($200k is the band centre; can stretch to $215-225k at the top), more room on the equity grant ($800k-$1.1M over 4 years is the typical L5 range), and the signing bonus ($30-60k is in policy). Your high anchor should reflect this: "$220k base, $1.1M RSU grant, $50k signing — about $500k TC on a 4-year average." Targeting the right lever lets you anchor high without breaking the model.

## 9. Worked example — the full 90-second comp exchange

A complete recruiter-screen comp exchange, narrated.

**Recruiter:** "Can you share what kind of compensation you're targeting for this role?"

**You** (pause one beat, name the range, name the source): "Sure. I'm targeting total comp in the $360k-$430k range, base ideally between $200k and $220k, based on levels.fyi data for Senior Software Engineer at peer SF tech companies. Happy to discuss the mix — I value equity and signing as well as base."

**Recruiter:** "That's helpful. The top end of what you mentioned is above where this role typically lands — we're usually closer to $360-$390 TC. Is the lower end of your range still workable?"

**You** (acknowledge, hold the anchor, restate the lever you have flexibility on): "Yeah, that range overlaps with where I am. The $360 floor is workable, especially if there's flexibility on the equity side or a signing component. I'd want to talk through the mix once we have a better sense of fit."

**Recruiter:** "Got it, that's noted. I'll share the band with the hiring team when we move forward."

What just happened:

- You anchored at the top of your defensible band ($430k).
- The recruiter flinched and pulled the band down ($360-$390).
- You acknowledged but didn't capitulate; you reasserted flexibility on the lever (equity / signing) rather than on TC.
- The negotiation is now anchored between $360 and $430, with the eventual offer most likely landing in the $380-$410 zone — well above where it would have landed if you had named "around $350" up front.

**The whole exchange took 90 seconds.** This is the part of the call where the largest dollar swings happen. The preparation cost (Exercise 3) is one to two hours of levels.fyi research per target company. The return on that prep is often $20-$80k over the offer.

## 10. The five comp failure modes

1. **The hedge.** "I'm flexible, whatever's competitive." Reads as no homework. The recruiter takes the floor of the band.
2. **The unjustified ask.** A number with no reasoning. When the recruiter asks "what's that based on?" you have nothing to say. The number is then discounted.
3. **The under-anchor.** Naming the 25th percentile because you didn't know the band. Recruiter happily writes it down. You leave $30-$80k on the table.
4. **The over-anchor without leverage.** Naming the 95th percentile with no competing offer, no exceptional specialty, and no signal that supports it. The recruiter politely ends the conversation.
5. **The salary-history disclosure.** Volunteering "I was making $X at my last job" in jurisdictions where the recruiter can't ask. Even where legal, this anchors the new offer to the old role, not the new market. Don't volunteer.

## 11. Comp at the recruiter screen vs. at offer stage

Important framing: **the recruiter screen is not the negotiation.** The recruiter screen is the *anchor-setting* moment. The actual negotiation happens after the loop, when an offer is on the table and you have signal (and possibly competing offers).

At the screen call:

- You set the anchor.
- You confirm your number is inside their band.
- You signal flexibility on the mix without flexibility on TC.

You do **not**:

- Get into hard negotiation on $5k increments.
- Threaten competing offers (you don't have any yet).
- Ask for the exact offer structure.

The full negotiation playbook (counter-offers, competing offers, the offer-letter walk-through, the "I need to discuss with my partner" deferral) is a Week 11-12 topic when you actually have offers. Patrick McKenzie's essay and Haseeb Qureshi's two-part series are the right deep references at that stage; this week, you are setting the anchor that gets you to the table.

## 12. A note on equity at private companies

If the role is at a private company, the equity portion of the offer is the most-uncertain component. Recruiters will quote a dollar value at the most-recent valuation (e.g., "$200k of options over 4 years at the Series C valuation"). That dollar value may or may not materialise.

What to actually ask, on the screen or shortly after:

- **Latest valuation, date, and round.** "Was the Series C valued at $1.2B in March 2024?"
- **Strike price vs. preferred price.** Options' real value is sensitive to dilution and to the exit price. The strike-vs-preferred-price ratio is a quick proxy.
- **Vesting schedule.** Standard is 4 years with a 1-year cliff. Variants exist (front-loaded, 5-year, no-cliff).
- **What happens on exit.** Acceleration on acquisition? Single-trigger? Double-trigger? Specifics here are negotiable.
- **Strike-extension window if you leave.** Standard is 90 days post-departure to exercise. Some companies extend to 7-10 years (significantly better for you).

You don't need these answers on the screen. But you do need to know to ask them before you accept an offer, because the quoted equity value at private companies overstates the realised value by 30-70% on average.

## 13. Location, remote, and geographic banding

Most large tech companies operate **geographic comp bands** — the same role at the same level pays differently in San Francisco, Austin, New York, Berlin, London, and São Paulo. The recruiter will ask your location on the screen (logistics beat) partly because the answer changes the band they apply.

### How the bands are structured

Three common patterns:

- **Tier banding.** The company defines geographic tiers — e.g., Tier 1 (SF/NYC), Tier 2 (Seattle/Austin/Boston), Tier 3 (most other US), Tier 4 (LCOL US). Each tier has a multiplier on the base band: Tier 1 = 100%, Tier 2 = ~92%, Tier 3 = ~85%, Tier 4 = ~75%. Equity grants are typically flat across tiers, so total-comp deltas are smaller than base deltas.
- **City-by-city.** Some companies (notably FAANG-tier) publish per-city bands. levels.fyi typically captures these well — filter by exact city.
- **One global band.** Some fully-remote-native companies (GitLab, Buffer, Automattic in earlier years) use a single global band, sometimes adjusted only by cost-of-living index. Rare; the recruiter will tell you if so.

### Implications for the screen call

- **Know your tier on levels.fyi.** Your high anchor for SF differs by 15-25% from your high anchor for Austin at the same FAANG-tier company. Don't quote the SF number while applying for the Austin role.
- **Remote roles often anchor to a tier.** "Fully remote" rarely means "we pay everyone the SF rate." Ask the recruiter: "Does the comp depend on my home location, and if so, what's the tier structure?"
- **Relocation flexibility is a lever.** If you're willing to move to a higher-tier city, the offer comp may be higher. If you're not, name your tier early so the recruiter sets the right band internally.

## 14. The follow-up: when comp is partially deferred

In a non-trivial fraction of screen calls, the recruiter will defer the comp specifics to a later stage: "We can talk specific numbers once the loop is closer to offer." This is sometimes legitimate, sometimes a tactic.

The right candidate response:

- **Accept the deferral once.** "Sure — for context I'm targeting $X-$Y TC, and if that's out of band let me know so we don't waste each other's time."
- **State your range anyway.** Even if they defer, leave the anchor on the table. The recruiter writes it down regardless of whether they confirm it now.
- **Re-raise at the hiring-manager round.** If comp wasn't pinned at the recruiter screen, ask the hiring manager at the end of their round (or the recruiter again before the next stage): "I want to make sure my target comp is inside band before we invest more time on both sides."

The cost of *not* raising it again is that you complete a 4-stage loop, get an offer, and find out the offer is well below your walkaway. Better to surface the misalignment in week 1 than week 5.

## 15. Self-check

- Define base, equity, signing, annual bonus, and total comp. Which is most-comparable across companies, and why?
- Your target company / level / location on levels.fyi shows: 50th percentile $390k, 75th percentile $440k. What's your high anchor on the screen call, and why not the 90th?
- A recruiter asks "what are you currently making?" in California. What's the correct response?
- You named $420k. The recruiter said "that's above where we typically land." Name two responses, one that preserves your anchor and one that surrenders it. Which do you use, and why?
- You're interviewing at a Series-B startup. Their cash band is tight, but they're flexible on equity percentage. You target $X TC. How does the lever flexibility shape *what specifically you ask for*?
- "The flinch" is the recruiter's reaction to your anchor. What does each of {flat acknowledgement, verbal pause, quick downward push} tell you?
- The classical advice is "never name the first number." Why is this less true in 2025, and what's the current playbook for Scenario A (published range on the JD)?

## Further reading

- **Patrick McKenzie — "Salary Negotiation: Make More Money, Be More Valued":** <https://www.kalzumeus.com/2012/01/23/salary-negotiation/>
- **Haseeb Qureshi — "Ten Rules for Negotiating a Job Offer":** <https://haseebq.com/how-not-to-bomb-your-offer-negotiation/>
- **levels.fyi — "How to negotiate tech salary":** <https://www.levels.fyi/blog/how-to-negotiate-tech-salary>
- **Pragmatic Engineer — comp deep-dives** (search "compensation" in newsletter archive): <https://newsletter.pragmaticengineer.com/>
- **Holloway — "The Holloway Guide to Equity Compensation"** (long-form reference for private-company equity): <https://www.holloway.com/g/equity-compensation>

When the comp conversation is clear, the [exercises](../03-exercises/00-overview.md) take you to a written script, three drafted "why this company" answers, and a comp-band spreadsheet for your top 5 targets.
