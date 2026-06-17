# Week 2 — Resources

Free, public, no signup unless noted.

## ATS parsers you can test against

- **Resume-Magic** — free parser-only view, no account required:
  <https://resume-magic.app/>
- **Affinda Resume Parser (free demo)** — shows the parsed JSON output an enterprise ATS sees:
  <https://www.affinda.com/resume-redactor> and <https://www.affinda.com/resume-parser>
- **Jobscan** — paid, but the free tier lets you run 5 scans/month against any pasted JD:
  <https://www.jobscan.co/>
- **HireBee / SkillSyncer free tier** — keyword-match scoring against a JD:
  <https://skillsyncer.com/>

## Sample resumes worth reading

- **The Pragmatic Engineer — sample resumes archive** (free posts):
  <https://newsletter.pragmaticengineer.com/>
- **Gayle McDowell — "Cracking the Coding Interview" resume chapter** (free sample on the book's site):
  <https://www.crackingthecodinginterview.com/>
- **Tech Interview Handbook — resume section with annotated examples**:
  <https://www.techinterviewhandbook.org/resume/>
- **Posquit0's Awesome-CV LaTeX template** (free template that parses cleanly):
  <https://github.com/posquit0/Awesome-CV>

## Layout templates that parse cleanly

- **JakeGut / Jake's Resume** (LaTeX, free, MIT) — the canonical clean-parsing template:
  <https://github.com/jakegut/resume>
- **Typst CV templates** (free, modern alternative to LaTeX):
  <https://github.com/typst/templates>
- **Google Docs "Resume" templates** — free with a Google account, all parse reasonably:
  Docs > Template Gallery > Resumes (Serif, Coral, Modern Writer)

## Style references

- **AskAManager — "What hiring managers actually look at on a resume"**:
  <https://www.askamanager.org/category/resumes>
- **Manager Tools — "The resume should fit on one page" podcast** (free):
  <https://www.manager-tools.com/2007/03/your-resume-stinks>
- **levels.fyi resume articles**:
  <https://www.levels.fyi/blog/>

## Tools you'll set up this week

- An **ATS parser bookmark** — pick one of the four above and save the link. You'll run your resume through it every time you edit.
- A **PDF preview tool that shows text-vs-image** — macOS Preview, Adobe Acrobat free, or `pdftotext` on the command line.
- A **clean editor for the resume itself** — Google Docs, Word, LaTeX (Overleaf for cloud), Typst, or a Markdown-to-PDF flow. Whichever you'll actually maintain.
- A **keyword-counting helper** — for the tailoring exercise: paste a JD and a resume side-by-side and count overlap. A free option is <https://www.online-utility.org/text/analyzer.jsp>.

## Glossary

| Term | One-line definition |
|------|---------------------|
| **ATS** | Applicant Tracking System — Greenhouse, Lever, Ashby, Workday. Software that ingests your resume. |
| **Parser** | The component of an ATS that extracts structured fields (name, email, jobs, dates) from your file. |
| **PDF (text-source)** | A PDF where text is selectable / copy-pasteable. Parses cleanly. |
| **PDF (image-source)** | A PDF made by scanning or screenshotting. Parses as a blob; OCR required. Avoid. |
| **Two-column layout** | A resume with a sidebar. Most parsers read left-to-right and interleave the content. |
| **Standard section** | Headers a parser recognizes: Experience, Education, Skills, Projects. Not "My Journey." |
| **Keyword match** | How many JD terms (Python, AWS, Kubernetes) appear in the resume. Recruiter sort key. |
| **Duties bullet** | "Responsible for X." Reports the role's scope. Communicates nothing. |
| **Outcome bullet** | "Reduced p99 latency from 1.4s to 220ms by sharding the index." Quantified result. |
| **STAR+R** | Situation, Task, Action, Result. A bullet structure. The +R is the quantified result. |
| **Number density** | Fraction of bullets containing a quantifiable result. Target: ≥40%. |
| **Tailoring** | Adjusting wording / emphasis per JD without changing factual content. |
| **Master resume** | The long version with every bullet you might use. You tailor from this, not from scratch. |

---

*Broken link? Open an issue.*
