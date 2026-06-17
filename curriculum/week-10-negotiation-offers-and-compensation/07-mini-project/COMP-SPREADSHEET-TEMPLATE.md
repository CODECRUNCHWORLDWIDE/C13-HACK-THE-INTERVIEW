# Comp-Calc Spreadsheet Template

A plain-text spreadsheet template for the C13 capstone. Copy the column headings into a real spreadsheet (Google Sheets, Excel, Numbers) for the working version; this Markdown file is the structural reference and the sample row.

## Why a spreadsheet exists alongside the Python helper

The comp-calculator.py helper is for the candidate who is comfortable editing a small Python script and running it from the terminal. The spreadsheet is for the candidate who prefers a visual side-by-side comparison and who plans to share the working file with a friend or a partner during the deliberation window. The two are interchangeable; pick the one that matches your workflow.

Some candidates run both — the Python helper to validate the arithmetic, the spreadsheet to show the comparison to non-technical advisors. Either is fine.

## Column structure

Set up your spreadsheet with the following columns:

### Sheet 1 — Offer details

| Column | Heading | Type | Description |
|-------:|---------|------|-------------|
| A | Offer name | text | Short label, e.g. "Company A" |
| B | Company | text | Full company name |
| C | Level | text | E.g. "L4", "E4", "SDE II" |
| D | Location | text | Metro, e.g. "Seattle, WA" |
| E | Base salary | currency | Annual base in USD |
| F | Sign-on Y1 | currency | One-time year-1 sign-on |
| G | Sign-on Y2 | currency | One-time year-2 sign-on (0 if standard schedule) |
| H | Stock total (4 yr) | currency | Total stock grant in USD |
| I | Target bonus % | percentage | E.g. 0.15 for 15% |
| J | Vesting schedule | text | "flat_25_25_25_25" or "amazon_5_15_40_40" |
| K | Cliff (months) | number | Standard is 12 |
| L | Equity type | text | "RSU" or "option" |
| M | Decision deadline (days) | number | Standard is 7-14; under 5 flags exploding |
| N | levels.fyi 25th pct | currency | From homework Item 2 |
| O | levels.fyi median | currency | From homework Item 2 |
| P | levels.fyi 75th pct | currency | From homework Item 2 |
| Q | BLS metro median (cash) | currency | From homework Item 2 |

### Sheet 2 — Year-by-year breakdown (computed)

| Column | Heading | Type | Formula (referencing Sheet 1 row) |
|-------:|---------|------|------------------------------------|
| A | Offer name | text | =Sheet1!A2 |
| B | Year | number | 1, 2, 3, 4 |
| C | Base | currency | =Sheet1!E2 |
| D | Sign-on | currency | Y1: =Sheet1!F2; Y2: =Sheet1!G2; Y3, Y4: 0 |
| E | Stock vested | currency | See vesting formula below |
| F | Target bonus | currency | =Sheet1!E2 * Sheet1!I2 |
| G | Year total | currency | =C+D+E+F |

### Sheet 3 — Comparison summary (computed)

| Column | Heading | Type | Formula |
|-------:|---------|------|---------|
| A | Offer name | text | =Sheet1!A2 |
| B | Year-1 total | currency | =Sheet2!G2 |
| C | Year-2 total | currency | =Sheet2!G3 |
| D | Year-3 total | currency | =Sheet2!G4 |
| E | Year-4 total | currency | =Sheet2!G5 |
| F | 4-year total | currency | =SUM(B:E) |
| G | 4-year average | currency | =F/4 |
| H | Y1 percentile placement | text | =IF(B<Sheet1!N2, "<25th", IF(B<Sheet1!O2, "25-50th", IF(B<Sheet1!P2, "50-75th", ">75th"))) |

## Vesting formula for stock vested per year (column E in Sheet 2)

For the flat 25/25/25/25 schedule:

```text
Year 1: =Sheet1!H2 * 0.25
Year 2: =Sheet1!H2 * 0.25
Year 3: =Sheet1!H2 * 0.25
Year 4: =Sheet1!H2 * 0.25
```

For the Amazon 5/15/40/40 schedule:

```text
Year 1: =Sheet1!H2 * 0.05
Year 2: =Sheet1!H2 * 0.15
Year 3: =Sheet1!H2 * 0.40
Year 4: =Sheet1!H2 * 0.40
```

In Google Sheets or Excel, you can use an IF formula on the vesting-schedule column to select the right multiplier:

```text
=IF(Sheet1!J2="amazon_5_15_40_40",
    IF(B2=1, Sheet1!H2*0.05,
    IF(B2=2, Sheet1!H2*0.15,
    IF(B2=3, Sheet1!H2*0.40, Sheet1!H2*0.40))),
    Sheet1!H2*0.25)
```

## Sample row — Company A (filled in)

### Sheet 1 — Offer details (row 2)

| Field | Value |
|-------|-------|
| Offer name | Company A |
| Company | Major Public Tech |
| Level | L4 |
| Location | Seattle, WA |
| Base salary | $165,000 |
| Sign-on Y1 | $25,000 |
| Sign-on Y2 | $0 |
| Stock total (4 yr) | $240,000 |
| Target bonus % | 15% |
| Vesting schedule | flat_25_25_25_25 |
| Cliff (months) | 12 |
| Equity type | RSU |
| Decision deadline (days) | 10 |
| levels.fyi 25th pct | $245,000 |
| levels.fyi median | $275,000 |
| levels.fyi 75th pct | $310,000 |
| BLS metro median (cash) | $191,000 |

### Sheet 2 — Year-by-year breakdown

| Offer | Year | Base | Sign-on | Stock vested | Target bonus | Year total |
|-------|-----:|-----:|--------:|-------------:|-------------:|-----------:|
| Company A | 1 | $165,000 | $25,000 | $60,000 | $24,750 | $274,750 |
| Company A | 2 | $165,000 | $0 | $60,000 | $24,750 | $249,750 |
| Company A | 3 | $165,000 | $0 | $60,000 | $24,750 | $249,750 |
| Company A | 4 | $165,000 | $0 | $60,000 | $24,750 | $249,750 |

### Sheet 3 — Comparison summary

| Offer | Y1 total | Y2 total | Y3 total | Y4 total | 4-yr total | 4-yr avg | Y1 percentile |
|-------|---------:|---------:|---------:|---------:|-----------:|---------:|---------------|
| Company A | $274,750 | $249,750 | $249,750 | $249,750 | $1,024,000 | $256,000 | 50-75th |

## Comparison example — three offers side by side

For the capstone scenario in mini-project/README.md with the three offers (Company A major tech, Company B Amazon, Company C startup), Sheet 3 with all three offers populated would look approximately like:

| Offer | Y1 total | Y2 total | Y3 total | Y4 total | 4-yr total | 4-yr avg | Y1 percentile |
|-------|---------:|---------:|---------:|---------:|-----------:|---------:|---------------|
| Company A | $274,750 | $249,750 | $249,750 | $249,750 | $1,024,000 | $256,000 | 50-75th |
| Company B (Amazon) | $235,000 | $250,000 | $290,000 | $290,000 | $1,065,000 | $266,250 | 25-50th in Y1, 50-75th by Y4 |
| Company C (startup) | $310,000 | $295,000 | $295,000 | $295,000 | $1,195,000 | $298,750 | depends on equity outcome |

The pattern is informative:

- **Company A** is the steady mid-tier offer. Year-1 is between the levels.fyi median and 75th percentile; the four-year arithmetic is consistent.
- **Company B (Amazon)** is back-loaded. Year-1 looks worse than Company A; year-4 looks better. The candidate who plans to stay 4 years gets more comp; the candidate who leaves at year 2 gets less.
- **Company C (startup)** has the highest paper total. The dollar value of the stock is the offer-letter optimistic case; the expected value is lower, possibly substantially lower. The candidate should not treat the $1.195M four-year total as comparable to Company A's $1.024M without an explicit probability-weighting on the startup equity.

The spreadsheet is the visual artefact of the trade-off. Looking at this table makes the comparison concrete in a way that staring at the offer letters does not.

## Cost-of-living adjustment columns (optional)

If the offers are in different metros, add three columns to Sheet 3:

| Column | Heading | Description |
|-------:|---------|-------------|
| I | Source metro | The metro of this offer |
| J | Target metro | The metro you would compare to (typically the metro of the other offer) |
| K | COL-adjusted 4yr avg | The 4-year-average comp converted to the target metro's purchasing power |

The conversion factor comes from NerdWallet or numbeo; multiply the 4-year-average comp by the conversion factor. For example, $256k in Seattle converted to Austin via NerdWallet might multiply by 0.78 to produce $200k Austin-equivalent.

The COL-adjusted comparison is the cleanest way to compare offers in different metros. The qualitative factors (which metro you actually want to live in, family proximity, climate, etc.) are a separate layer that the spreadsheet cannot capture.

## Walk-away and target columns

If you want a single-glance view of "is this offer acceptable?", add two columns to Sheet 3:

| Column | Heading | Description |
|-------:|---------|-------------|
| L | Walk-away (Y1) | Your minimum acceptable year-1 total comp |
| M | Above walk-away? | =IF(B2>=L2, "YES", "NO") |

The walk-away number is your private number from the homework. The "above walk-away?" column gives a Boolean signal for each offer.

## Suggested workflow

For the capstone:

1. **Sheet 1 — Fill in the offer details for each offer in play.** This is the data-entry step. Pull from the offer letters.
2. **Sheet 2 — Verify the year-by-year breakdown is computing correctly.** Spot-check the year-1 total against your by-hand calculation.
3. **Sheet 3 — Read the comparison summary.** This is the artefact you bring into the decision rationale section of the capstone.
4. **Add cost-of-living and walk-away columns if useful.** Not every capstone needs them; add when the scenario requires.
5. **Export Sheet 3 as a PNG or paste as a Markdown table into the capstone document.** This is what goes into section 2 of the capstone.

The spreadsheet is a working tool, not a final artefact. The artefact is the capstone narrative. The spreadsheet is the calibration document that the narrative references.

## What this template does not handle

- **Share-price drift on RSU grants.** The spreadsheet assumes the stock-grant value at vest equals the grant-date value. In reality, the share price drifts; year-2 stock-vest value can be 1.5x or 0.5x the grant-date value. Plan for the grant-date value; treat drift as upside or downside.
- **Equity refresh grants.** Most companies grant an annual RSU refresh at the performance review. The refresh is on top of the initial grant. The template does not model this; for a multi-year comp projection including refresh, add a column for "estimated annual refresh" in Sheet 1 and add it to years 2-4 in Sheet 2.
- **Options at private companies.** The spreadsheet treats option-grant values as RSU-equivalent dollar values. This is the offer-letter optimistic case; the expected value of a private-company option grant is typically 30-50% lower than the offer-letter dollar after probability-weighting for liquidity outcomes. Adjust by hand if comparing a startup option grant to a public-company RSU grant.
- **State and federal taxes.** The 4-year totals are pre-tax. The cost-of-living adjustment columns approximate the post-tax purchasing power; for a precise post-tax comparison, apply the state-tax tables in resources.md.
- **Bonus variability.** The spreadsheet uses target bonus as the assumption. Actual bonus is target × company-performance multiplier × individual-performance multiplier. In a flat year with a "meets expectations" rating, actual is approximately target; in a bad year, actual is 60-70% of target. Plan around target; treat outperformance as upside.

The template is intentionally a planning baseline, not a precise forecast. The precision is in the negotiation conversation, not in the spreadsheet.
