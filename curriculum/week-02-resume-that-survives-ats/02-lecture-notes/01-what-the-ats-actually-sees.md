# Lecture 1 — What the ATS Actually Sees

> **Duration:** ~2 hours. **Outcome:** You can describe what Greenhouse, Lever, Ashby, and Workday do to a resume PDF, identify the five structural failures that get a resume silently rejected, and run your own resume through a parser and read the output critically.

## 1. The ATS is not your audience. The ATS is the door.

Every conversation about resumes online conflates two readers:

1. The **ATS parser** — software that ingests your PDF, extracts fields, and queues you for the recruiter's saved search.
2. The **human recruiter** — who spends ~30 seconds skimming the top of the file before deciding to keep going or move on.

These two readers want different things. The parser wants a structured document that converts cleanly into a database row. The recruiter wants a narrative they can summarize to the hiring manager in 60 seconds. A resume that wins one and loses the other is still a losing resume.

The good news: **the constraints are compatible.** A document built for the parser also reads cleanly for the recruiter. The patterns that fail the parser — two-column sidebars, header graphics, decorative fonts — are also the patterns that make a recruiter's eyes glaze. There is no tradeoff. Designing for the parser is designing for the recruiter.

## 2. What the parser actually does

Every major ATS (Greenhouse, Lever, Ashby, Workday, Recruitee, Jobvite, iCIMS) follows roughly the same four-stage pipeline:

```
       PDF upload
            ↓
   1. Text extraction (PDF -> raw text stream)
            ↓
   2. Section detection (find "Experience," "Education," "Skills")
            ↓
   3. Field parsing (per section: extract job title, company, dates, bullets)
            ↓
   4. Keyword indexing (tag the candidate with all matched skills/tools)
            ↓
        Candidate record
            ↓
   Recruiter queue, sortable by JD-keyword overlap
```

Each stage has failure modes. We'll walk through each.

### Stage 1 — Text extraction

The parser opens your PDF and tries to extract a stream of text. If your PDF was **exported from a text source** (Google Docs > Download > PDF, Word > Save as PDF, LaTeX > pdflatex), this is trivial: the PDF contains an actual text layer, and extraction is loss-free.

If your PDF was **made from an image** (you scanned a printed copy; you screenshotted your Word doc; you exported a Figma design as PDF), there is no text layer. The parser sees a blob. Some ATSes run OCR; many don't. Either way, you've added noise.

**Test it yourself.** Open your PDF in any text editor or run `pdftotext your-resume.pdf -` on the command line. If you get clean text back, you're fine. If you get garbage or nothing, fix the export.

### Stage 2 — Section detection

The parser scans for headers it recognizes. It does not parse semantic meaning — it pattern-matches against a small set of known strings:

- **Experience** (also: "Work Experience," "Professional Experience," "Employment History")
- **Education**
- **Skills** (also: "Technical Skills," "Core Competencies")
- **Projects** (also: "Personal Projects," "Side Projects")
- **Certifications**
- **Publications**
- **Summary** or **Objective**

Headers like "My Journey," "What I've Done," "Stuff I'm Proud Of" — clever, human, *fails the parser*. The parser silently drops the section or merges it into the previous one. Whatever you wrote there becomes invisible.

**Use boring headers.** "Experience" is correct. "My Career Adventure" is wrong.

### Stage 3 — Field parsing per section

Inside Experience, the parser tries to find, for each job:

- The **company name**
- The **job title**
- The **start date** and **end date**
- The **bullets** describing the role

It uses positional heuristics — the title is usually bolder or larger than the bullets, the dates are usually right-aligned, the company is usually adjacent to the title. **When you violate these conventions, the parser guesses wrong.**

Common parser confusions:

- Title and company on different lines with no clear association → parser mismatches them.
- Dates written in inconsistent formats across jobs ("2023-Present" then "May '22 to August '22") → parser fails to extract one or both.
- Bullets indented under a sub-section that's nested inside the role → parser flattens them or drops them.
- Two-column layout with experience on the right and skills on the left → parser reads left-to-right, line by line, and produces interleaved nonsense like "Python — Senior Engineer at Acme — TypeScript — Built the…"

### Stage 4 — Keyword indexing

The parser tags your candidate record with every recognized skill/tool/technology it found in the document. These tags are what the recruiter searches against.

When a recruiter has 200 candidates in the queue for a "Senior Backend Engineer" role, they run a saved search like:

```
title:"backend engineer" AND skills:Python AND skills:PostgreSQL AND yoe:>=4
```

You either match or you don't. **The keywords must appear literally in your resume.** Synonyms don't count. If the JD says "PostgreSQL" and your resume says "relational databases," you don't match. If the JD says "Kubernetes" and your resume says "container orchestration," you don't match.

This is not because the recruiter is dumb. This is because the recruiter has 200 records and 90 minutes. Synonym-matching is the candidate's job.

### How the four major ATSes differ

The pipeline above is shared. The implementation details differ:

- **Greenhouse** uses Resumator/Sovren under the hood for parsing. Generally tolerant; relatively forgiving of layout but strict on field associations. Most candidates encounter Greenhouse at startups and growth-stage tech companies.
- **Lever** uses its own parser; in practice it's the most layout-tolerant of the four, but its keyword search is the simplest (substring match, case-insensitive). Common at YC-backed startups and Series A-C companies.
- **Ashby** is newer and more sophisticated than Greenhouse / Lever. Better at understanding context (it can sometimes infer "Kubernetes" from a bullet that mentions "K8s"), but its admin UI surfaces parser errors prominently — meaning recruiters *see* when your file parsed badly and may pass on it for that reason alone.
- **Workday** is the strictest of the four. Used by most large enterprises and Fortune 500s. It demands almost-canonical layout and reliably mishandles anything decorative. If your resume is going to a Workday-backed company, assume it will be parsed *least* generously.

You won't know which ATS a given company uses unless you've seen the application URL (the domain often gives it away: `boards.greenhouse.io`, `jobs.lever.co`, `*.ashbyhq.com`, `*.workday.com`). When in doubt, **design for Workday-grade strictness** — anything that passes Workday will pass the other three.

### What the parser can't do

It's also worth being explicit about what the parser *doesn't* do, despite Twitter rumor:

- It doesn't read your resume "intelligently" and judge fit. That's the recruiter.
- It doesn't penalize you for the file size, the font choice (so long as it's standard), or whether you used Times New Roman vs. Calibri.
- It doesn't reject you for missing certain words. It scores you. The recruiter decides the cutoff.
- It rarely runs adversarial sentiment analysis or "soft skill" extraction — those are marketing claims more than deployed reality at most companies on your target list.

Optimizing for the parser is, in practice, optimizing for *cleanliness*: clean structure, clean text, clean keyword presence. There is no clever exploit.

## 3. The five structural failures

Here are the five most common reasons a resume gets silently dropped by an ATS. Each is fixable in under 10 minutes.

### Failure 1 — Two-column layout

The sidebar pattern: skills/contact info on the left, experience on the right. Looks polished. Parses as garbage. **Single column always.** If you want sub-sections (skills vs. languages), use horizontal separation within the column, not vertical columns.

### Failure 2 — PDF made from an image

You designed your resume in Canva, exported it as an image, then "converted to PDF." Or you scanned your printed copy. The PDF has no text layer. The parser sees nothing or runs lossy OCR.

**Always export from a text source.** Google Docs, Word, LaTeX, Typst, Pages — all fine. Canva can be fine *if* you export the PDF correctly (some Canva templates flatten everything; check by running `pdftotext`).

### Failure 3 — Graphics in the header

Your photo, a banner, a logo, an "icon" next to your phone number. The parser sees an image and either skips it or fails to associate it with anything. Your name and contact info, which are in or near the graphic, get lost.

**Header is plain text.** Name, email, phone, LinkedIn URL, GitHub URL, city/state. No photo. No icons. No background color.

### Failure 4 — Non-standard section headers

"Crew" instead of "Experience." "Toolbox" instead of "Skills." "Where I've Been" instead of "Education." Cute. Invisible to the parser.

**Boring headers always.** You can be clever in the bullets.

### Failure 5 — ASCII-unsafe characters

Smart quotes (`"` instead of `"`). Em-dashes typed as the typographic character (`—` vs. `--`). Ligatures (`ﬁ` instead of `fi`). Non-breaking spaces. These come from your word processor "helping you." The parser may render them as `?` or `&#8211;` or just drop them.

**Use ASCII whenever you can.** Straight quotes, double-hyphens for em-dashes (or just use a single hyphen). If your editor auto-corrects, turn it off.

### Contact info — the field most candidates botch

Half of "parser missed my name" complaints are from candidates who put their name inside a graphical header, a banner, or a non-standard text box. The fix is boring and immediate:

- **Name**: first line of the document. Plain text. Bold and slightly larger than body text (14-18pt). No icons next to it.
- **Email**: plain text. Use a professional address — `firstname.lastname@gmail.com` beats `darkninja420@example.com` by 100%. The parser doesn't care; the recruiter does.
- **Phone**: one consistent format. `+1 415 555 0142` parses better than `(415) 555.0142`. International candidates: include the country code.
- **LinkedIn URL**: full URL, not just `LinkedIn` as a word. `linkedin.com/in/yourhandle` is fine; don't link the word "LinkedIn" to a hidden URL — the parser sees the visible string.
- **GitHub URL**: same pattern. `github.com/yourhandle`. If your GitHub is empty, address that *before* listing it.
- **Location**: city and state (or country). Not a full address. Including a location helps recruiters filter by region; omitting it can drop you from location-restricted searches.

What **not** to put in the contact line: full street address, photo, date of birth, marital status, nationality, religion. In the US these are illegal for the employer to consider; in most other jurisdictions the convention varies, but defaulting to none is safe.

## 4. Date format consistency

Every job entry has a start date and (sometimes) an end date. Use **one format across the entire document.** Pick one:

- `Jan 2024 – Present`
- `2024-01 – Present`
- `January 2024 – Present`

Mix any two and the parser fails to associate at least one of your jobs with its dates. Then your "5 years of experience" becomes "1 year of experience" in the parser's view, and you fall below the `yoe:>=4` filter in the recruiter's saved search.

Pick one. Use it everywhere. If you use "Present" for your current role, capitalize it consistently — don't write "present" once and "Present" the next time.

For short-term roles, **show the duration explicitly**, not just the start month: `Jun 2024 – Aug 2024 (3 months)`. Otherwise a recruiter does the math wrong (or skips it), and a 3-month internship reads as 3 years.

## 5. Keyword matching per JD

The recruiter's saved search is the gate. To pass:

1. **Read the JD carefully.** Highlight every noun that names a tool, language, platform, methodology, or domain. ("Python," "AWS," "Kubernetes," "ETL," "PCI compliance," "OAuth2.")
2. **For each highlighted term, check your resume.** If you legitimately have the skill, the literal term must appear in the resume. Not a synonym. The term.
3. **If a term isn't on your resume but you have the skill**, add a bullet or a Skills line that includes it — with truthful context.
4. **If a term isn't on your resume because you don't have the skill**, leave it off. Honest signal beats keyword stuffing. Recruiters notice.

This is *tailoring*, and it's the work of 15-25 minutes per role. Exercise 3 walks you through it.

### How many keywords are enough?

Different ATSes use different scoring. A defensible rule:

- Hit **80%+ of the technical keywords** for the role (the languages, frameworks, tools).
- Hit **60%+ of the methodology / domain keywords** ("agile," "PCI compliance," "ETL pipelines").
- Don't worry about the soft-skill keywords ("communicates well," "team player"). They don't get filtered on.

## 6. Testing your own resume in a parser

Before you submit a resume anywhere, run it through a free parser. Three good options:

- **Resume-Magic** (<https://resume-magic.app/>): shows the parsed structure as JSON.
- **Affinda's demo parser**: shows what an enterprise-grade ATS sees.
- **Jobscan free tier** (5/month): scores your resume against a pasted JD.

Read the output critically. For each field the parser extracted, ask: **is this correct?**

- Is your name the literal value of the `name` field? (Or did it grab a section header?)
- Are all your jobs listed in the work-history array? (Or did it miss one?)
- Are the start/end dates correct for every job? (Or did one default to null?)
- Are the skills the right skills? (Or did it tag you with random words from your bullets?)

If anything is wrong in the parser's output, **fix the resume**, don't argue with the parser. The recruiter sees what the parser saw, not what you intended.

## 7. The recruiter's 30-second skim

After the parser does its work, a recruiter actually opens your PDF. They have 30 seconds. They are scanning for:

1. **Your most recent title and company.** Top of the experience section. Should be obvious in <2 seconds.
2. **Total years of experience.** They eyeball the dates.
3. **A signal that you match this role.** A bullet or skills line that contains the JD's key term.
4. **Anything weird.** A 3-year gap. A jumble of unrelated jobs. A title that doesn't match the level they're hiring for.

If those four signals land in 30 seconds, you advance. If they have to dig, you don't.

**Implications for layout:**

- Most-recent role first, with title bold, company adjacent, dates right-aligned.
- A `Skills` section near the top — *after* the headline, *before* the experience details — so the keyword scan is instant.
- Bullets are short. Three lines is the upper limit. Six lines per bullet is unread.

## 8. Length: one page or two?

The internet argues about this. The defensible rule:

- **Junior / new-grad / less than 3 years of experience: 1 page.** No exceptions.
- **Mid-level / 3-7 years: 1 page if you can, 2 pages if you must.** Default to 1.
- **Senior / 7+ years: 1-2 pages.** Most senior engineers can still fit on 1 page if they cut ruthlessly.
- **Staff+ / 10+ years: 2 pages.** Sometimes 3 if you have major patents, publications, or a research career.

A 1-page resume that's well-organized is always stronger than a 2-page resume with padding. **If you're at 1.3 pages, cut to 1.** The line "page 2 has my projects" almost never holds up; the projects section gets read 50% as often as page 1.

## 9. The order of sections

For most candidates:

```
Header (name, contact, GitHub, LinkedIn, city)
Skills (one line or two — keywords, by category)
Experience (most recent first)
Projects (only if they add signal beyond your jobs)
Education (most recent first; new grads put this above Experience)
```

For new grads or career-changers:

```
Header
Education (with relevant coursework if your major is non-CS)
Projects (carry more weight than experience for new grads)
Experience (internships, part-time, research)
Skills
```

For senior+:

```
Header
Summary (2-3 lines, optional — usually deletable)
Experience
Skills
Education (terse, just degree and school)
```

## 10. File format and filename

PDF is the universal answer. There is no scenario where you should send a `.docx` if you can send a `.pdf`. Word documents render differently depending on the recipient's font installations, Word version, and OS — your carefully spaced layout can collapse into a wall of text on a different machine. PDF locks the rendering.

Two PDF subspecies to be aware of:

- **PDF/A** — an archival subset, fine for ATS.
- **Image-based PDF** — what you get from `Print > Save as PDF` on a Mac with the wrong setting, or from Canva's "Print PDF" export. Has no text layer; parser sees nothing. Always run `pdftotext` to verify.

**Filename convention:** `Firstname-Lastname-Resume.pdf` or `Firstname-Lastname-Resume-YYYY-MM.pdf`. Some ATSes display the filename to the recruiter; a file named `final_v4_REAL.pdf` reads as careless. Spaces in filenames are fine in most ATSes but underscores or hyphens are safer.

For tailored versions on disk, keep the recruiter-visible name clean: `Jane-Doe-Resume.pdf` — not `Jane-Doe-Resume-Stripe-Tailored.pdf`. The recruiter doesn't need to know it's tailored. Internal organization can happen in your folder structure.

## 11. What the ATS shows the recruiter

After parsing, the recruiter sees something like this — the *candidate card* — in the ATS UI:

```
Jane Doe                              [Resume] [Application]
jane.doe@example.com  |  +1 415 555 0142
San Francisco, CA  |  linkedin.com/in/janedoe

Current: Senior Backend Engineer @ Acme (Jan 2022 - Present, 4y)
Previous: Backend Engineer @ Beta Corp (Jul 2019 - Dec 2021, 2.5y)

Skills: Python, PostgreSQL, AWS, Kubernetes, Django, Redis, Kafka
Match score: 87% (vs. Senior Backend Engineer JD)

[Notes section, empty]
[Tags: high-priority]
```

The card is generated entirely from the parser's output. If your parsed-name field is "Jane Doe Resume" instead of "Jane Doe," that's what the recruiter sees. If your most-recent title was misparsed, that's what they see. **The card is the recruiter's first impression** — and they often decide whether to open the PDF based on the card alone.

This is why Exercise 1 — parsing your own resume — matters more than rewriting bullets. If the card is wrong, no number of beautiful bullets saves you.

## 12. Self-check

- What are the four stages an ATS pipeline goes through after you upload a PDF?
- Name three section-header strings the parser recognizes and three it doesn't.
- A two-column resume parsed as "Python — Senior Engineer at Acme — TypeScript — Built the…" What's the fix?
- Your resume has dates in two different formats. What's the failure mode in the recruiter's queue?
- The JD says "Kubernetes." Your resume says "container orchestration." Why does that lose?
- How do you confirm your PDF has a text layer rather than being a flattened image?

## Further reading

- **Tech Interview Handbook — Resume section (end-to-end):** <https://www.techinterviewhandbook.org/resume/>
- **Affinda — "How resume parsers work" (free article):** <https://www.affinda.com/blog/how-resume-parsers-work>
- **AskAManager — "Resume mistakes that knock you out":** <https://www.askamanager.org/category/resumes>
