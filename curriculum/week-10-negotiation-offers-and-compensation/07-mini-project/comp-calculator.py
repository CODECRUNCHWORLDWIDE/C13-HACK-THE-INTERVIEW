"""
comp-calculator.py
==================

A small helper for the C13 Week 10 capstone.

Computes four-year total compensation for a software-engineering offer under
the two most common vesting schedules in U.S. tech (flat 25/25/25/25 with a
1-year cliff, and the Amazon-style 5/15/40/40 back-loaded schedule with
year-1 and year-2 sign-on offsets). Also produces a side-by-side comparison
across multiple offers and a per-offer percentile placement against a user-
supplied levels.fyi distribution.

The helper is deliberately small. It is meant to be read and modified by the
candidate, not run as a library. All values are in U.S. dollars; all
percentages are decimals (0.10 = 10%); all years are integers; all schedules
are explicit.

Usage:
    python3 comp-calculator.py

The script writes a comparison table to stdout. Edit the OFFERS list at the
bottom of the file with your own offers before running.

No external dependencies. Tested with Python 3.10+.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


VestingSchedule = Literal["flat_25_25_25_25", "amazon_5_15_40_40"]


@dataclass
class Offer:
    """A single offer-in-hand description.

    Fields:
        name:           A short label for the offer (used in the output).
        company:        Company name.
        level:          Level designation (e.g. "L4", "E4", "SDE II").
        location:       Metro area (used for cost-of-living and BLS lookups).
        base:           Annual base salary in USD.
        sign_on_y1:     One-time year-1 sign-on bonus in USD (0 if none).
        sign_on_y2:     One-time year-2 sign-on bonus in USD (0 if none).
                        Most offers have sign_on_y2 = 0; Amazon uses both.
        stock_total:    Total dollar value of the stock grant over 4 years.
                        For RSUs, this is the grant-date value at the
                        published share price. For options, this is the
                        offer-letter dollar value, which is optimistic.
        target_bonus_pct: Target annual bonus as a decimal of base.
                        (0.10 = 10% target bonus; 0.15 = 15%, etc.)
        vesting:        The vesting schedule. One of:
                        - "flat_25_25_25_25": 25% per year, 1-year cliff
                        - "amazon_5_15_40_40": Amazon back-loaded schedule
        cliff_months:   Months until the first vest. Default 12 (1-year cliff).
                        For schedules without a cliff, set to 0.
        equity_type:    "RSU" for public-company or post-IPO grants.
                        "option" for private-company option grants.
                        Used for narrative only; arithmetic is identical.
        decision_deadline_days: Days from offer-letter date to decide.
                        Standard is 7-14; under 5 is an exploding offer.
    """

    name: str
    company: str
    level: str
    location: str
    base: float
    sign_on_y1: float
    sign_on_y2: float
    stock_total: float
    target_bonus_pct: float
    vesting: VestingSchedule
    cliff_months: int = 12
    equity_type: Literal["RSU", "option"] = "RSU"
    decision_deadline_days: int = 10


@dataclass
class YearBreakdown:
    """One year of a 4-year total-comp computation."""

    year: int
    base: float
    sign_on: float
    stock_vested_value: float
    target_bonus: float

    @property
    def total(self) -> float:
        return self.base + self.sign_on + self.stock_vested_value + self.target_bonus


@dataclass
class TotalCompComputation:
    """The full 4-year breakdown for one offer."""

    offer_name: str
    year_1: YearBreakdown
    year_2: YearBreakdown
    year_3: YearBreakdown
    year_4: YearBreakdown
    notes: list[str] = field(default_factory=list)

    @property
    def four_year_total(self) -> float:
        return (
            self.year_1.total
            + self.year_2.total
            + self.year_3.total
            + self.year_4.total
        )

    @property
    def four_year_average(self) -> float:
        return self.four_year_total / 4.0

    @property
    def year_1_total(self) -> float:
        return self.year_1.total


def compute_total_comp(offer: Offer) -> TotalCompComputation:
    """Compute the 4-year total comp for an offer.

    The function assumes:
        - The target bonus is paid in full each year (full target, not
          prorated). For prorated year-1 (e.g. starting mid-year), reduce
          the year-1 target bonus by hand.
        - Cliff vesting means 100% forfeiture before the cliff date. After
          the cliff, the vesting proceeds at the stated rate.
        - Stock grant value at vest equals the grant-date value (i.e. we
          do not model share-price drift). This is the planning-baseline
          assumption; the actual vest-date value will differ.
    """
    base = offer.base
    bonus = offer.base * offer.target_bonus_pct
    stock = offer.stock_total

    if offer.vesting == "flat_25_25_25_25":
        # 1-year cliff; 25% vests at month 12; remaining 75% vests linearly
        # over years 2-4 (modelled here as 25% per year, since the candidate-
        # facing total is what matters for negotiation).
        y1_stock = stock * 0.25
        y2_stock = stock * 0.25
        y3_stock = stock * 0.25
        y4_stock = stock * 0.25
    elif offer.vesting == "amazon_5_15_40_40":
        y1_stock = stock * 0.05
        y2_stock = stock * 0.15
        y3_stock = stock * 0.40
        y4_stock = stock * 0.40
    else:
        # Defensive: unknown schedule defaults to flat with a note
        y1_stock = stock * 0.25
        y2_stock = stock * 0.25
        y3_stock = stock * 0.25
        y4_stock = stock * 0.25

    year_1 = YearBreakdown(
        year=1,
        base=base,
        sign_on=offer.sign_on_y1,
        stock_vested_value=y1_stock,
        target_bonus=bonus,
    )
    year_2 = YearBreakdown(
        year=2,
        base=base,
        sign_on=offer.sign_on_y2,
        stock_vested_value=y2_stock,
        target_bonus=bonus,
    )
    year_3 = YearBreakdown(
        year=3,
        base=base,
        sign_on=0.0,
        stock_vested_value=y3_stock,
        target_bonus=bonus,
    )
    year_4 = YearBreakdown(
        year=4,
        base=base,
        sign_on=0.0,
        stock_vested_value=y4_stock,
        target_bonus=bonus,
    )

    notes: list[str] = []
    if offer.vesting == "amazon_5_15_40_40":
        notes.append(
            "Amazon-style back-loaded schedule: 5/15/40/40. Year-1 and year-2 "
            "sign-on cash offsets the back-loading. The candidate who leaves "
            "at month 25 walks away with sign-on + 20% of stock."
        )
    if offer.decision_deadline_days < 5:
        notes.append(
            f"Exploding offer flag: {offer.decision_deadline_days}-day "
            "deadline is below the candidate-friendly norm. Request an "
            "extension to 7-10 days before doing substantive comp work."
        )
    if offer.equity_type == "option":
        notes.append(
            "Equity is options, not RSUs. The dollar value above is the "
            "offer-letter optimistic case; expected value is lower. Plan "
            "around base + sign-on; treat stock as upside."
        )

    return TotalCompComputation(
        offer_name=offer.name,
        year_1=year_1,
        year_2=year_2,
        year_3=year_3,
        year_4=year_4,
        notes=notes,
    )


def percentile_placement(year_1_total: float, distribution: dict[int, float]) -> str:
    """Locate the year-1 total comp in a percentile distribution.

    The distribution dict maps percentile (10, 25, 50, 75, 90) to total
    comp at that percentile for the relevant company-level-location triple.

    Returns a human-readable placement string.
    """
    if not distribution:
        return "no distribution provided"

    percentiles = sorted(distribution.keys())
    if year_1_total < distribution[percentiles[0]]:
        return f"below the {percentiles[0]}th percentile"
    if year_1_total >= distribution[percentiles[-1]]:
        return f"at or above the {percentiles[-1]}th percentile"

    for i in range(len(percentiles) - 1):
        low_p = percentiles[i]
        high_p = percentiles[i + 1]
        low_v = distribution[low_p]
        high_v = distribution[high_p]
        if low_v <= year_1_total < high_v:
            # Linear interpolation between the two named percentiles
            frac = (year_1_total - low_v) / (high_v - low_v) if high_v > low_v else 0.0
            interp_pct = low_p + frac * (high_p - low_p)
            return f"approximately the {interp_pct:.0f}th percentile"

    return "outside the named percentile range"


def format_offer_summary(
    offer: Offer,
    comp: TotalCompComputation,
    distribution: dict[int, float] | None = None,
) -> str:
    """Produce a human-readable summary of one offer."""
    lines: list[str] = []
    lines.append(f"=== {offer.name} ({offer.company} {offer.level}, {offer.location}) ===")
    lines.append(f"  Base salary:          ${offer.base:>10,.0f}")
    lines.append(f"  Sign-on Y1:           ${offer.sign_on_y1:>10,.0f}")
    if offer.sign_on_y2 > 0:
        lines.append(f"  Sign-on Y2:           ${offer.sign_on_y2:>10,.0f}")
    lines.append(f"  Stock (4yr total):    ${offer.stock_total:>10,.0f}")
    lines.append(f"  Target bonus:         {offer.target_bonus_pct * 100:>10.1f}%")
    lines.append(f"  Vesting:              {offer.vesting}")
    lines.append(f"  Equity type:          {offer.equity_type}")
    lines.append(f"  Decision deadline:    {offer.decision_deadline_days} days")
    lines.append("")
    lines.append("  Year-by-year breakdown:")
    for yb in (comp.year_1, comp.year_2, comp.year_3, comp.year_4):
        lines.append(
            f"    Year {yb.year}: base ${yb.base:>9,.0f} + "
            f"sign-on ${yb.sign_on:>7,.0f} + "
            f"stock ${yb.stock_vested_value:>9,.0f} + "
            f"bonus ${yb.target_bonus:>8,.0f} = ${yb.total:>10,.0f}"
        )
    lines.append("")
    lines.append(f"  Year-1 total:         ${comp.year_1_total:>10,.0f}")
    lines.append(f"  4-year total:         ${comp.four_year_total:>10,.0f}")
    lines.append(f"  4-year average:       ${comp.four_year_average:>10,.0f}")

    if distribution is not None:
        placement = percentile_placement(comp.year_1_total, distribution)
        lines.append("")
        lines.append(f"  Distribution placement (Year-1): {placement}")

    if comp.notes:
        lines.append("")
        lines.append("  Notes:")
        for note in comp.notes:
            lines.append(f"    - {note}")

    return "\n".join(lines)


def format_comparison_table(offers: list[Offer], comps: list[TotalCompComputation]) -> str:
    """Produce a side-by-side comparison table."""
    if not offers:
        return "(no offers to compare)"

    header = (
        f"{'Offer':<15} {'Year-1':>12} {'Year-2':>12} {'Year-3':>12} "
        f"{'Year-4':>12} {'4yr total':>13} {'4yr avg':>12}"
    )
    rows: list[str] = [header, "-" * len(header)]
    for offer, comp in zip(offers, comps):
        rows.append(
            f"{offer.name:<15} "
            f"${comp.year_1.total:>10,.0f}  "
            f"${comp.year_2.total:>10,.0f}  "
            f"${comp.year_3.total:>10,.0f}  "
            f"${comp.year_4.total:>10,.0f}  "
            f"${comp.four_year_total:>11,.0f}  "
            f"${comp.four_year_average:>10,.0f}"
        )
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Edit the OFFERS list below with your own offers, then run:
#     python3 comp-calculator.py
# ---------------------------------------------------------------------------

OFFERS: list[Offer] = [
    Offer(
        name="Company A",
        company="Major Public Tech",
        level="L4",
        location="Seattle, WA",
        base=165_000,
        sign_on_y1=25_000,
        sign_on_y2=0,
        stock_total=240_000,
        target_bonus_pct=0.15,
        vesting="flat_25_25_25_25",
        cliff_months=12,
        equity_type="RSU",
        decision_deadline_days=10,
    ),
    Offer(
        name="Company B",
        company="Amazon",
        level="L5",
        location="Seattle, WA",
        base=170_000,
        sign_on_y1=50_000,
        sign_on_y2=35_000,
        stock_total=300_000,
        target_bonus_pct=0.0,  # Amazon historically does not use target bonus
        vesting="amazon_5_15_40_40",
        cliff_months=12,
        equity_type="RSU",
        decision_deadline_days=10,
    ),
    Offer(
        name="Company C",
        company="Series-C Startup",
        level="Senior",
        location="San Francisco, CA",
        base=180_000,
        sign_on_y1=15_000,
        sign_on_y2=0,
        stock_total=400_000,
        target_bonus_pct=0.0,
        vesting="flat_25_25_25_25",
        cliff_months=12,
        equity_type="option",
        decision_deadline_days=14,
    ),
]


# Optional: levels.fyi distribution for the primary offer's triple.
# Edit with your own data from the homework Item 2.
PRIMARY_DISTRIBUTION: dict[int, float] = {
    25: 245_000,
    50: 275_000,
    75: 310_000,
    90: 350_000,
}


def main() -> None:
    comps: list[TotalCompComputation] = [compute_total_comp(o) for o in OFFERS]

    print()
    print("=" * 80)
    print("C13 Week 10 Capstone — Comp-Calculator Output")
    print("=" * 80)
    print()

    # Per-offer summaries
    for offer, comp in zip(OFFERS, comps):
        distribution = PRIMARY_DISTRIBUTION if offer is OFFERS[0] else None
        print(format_offer_summary(offer, comp, distribution))
        print()

    # Side-by-side comparison
    print("=" * 80)
    print("Side-by-side comparison")
    print("=" * 80)
    print()
    print(format_comparison_table(OFFERS, comps))
    print()

    # Footer
    print("=" * 80)
    print(
        "Output is for planning purposes only. The stock-grant dollar values "
        "assume no share-price drift; the actual vest-date values will differ. "
        "Run the levels.fyi distribution and BLS cross-check separately."
    )
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
