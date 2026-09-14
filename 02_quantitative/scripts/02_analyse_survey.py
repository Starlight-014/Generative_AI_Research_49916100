"""
02_analyse_survey.py -- descriptive and inferential analysis of the cleaned survey.

Reads   : ../data/processed/GENAI_survey-clean_20260814_v02.csv
Writes  : ../outputs/tables/GENAI_item-descriptives_20260818_v01.csv
          ../outputs/tables/GENAI_correlations_20260818_v01.csv
          ../outputs/tables/GENAI_cohort-comparison_20260818_v01.csv

Run 01_clean_survey.py first.

Statistical choices and why:
  * Likert items are ordinal, so the response distribution and median are the
    primary summaries; means are reported alongside only because the literature
    we compare against reports them.
  * Associations between two ordinal items use Spearman rho, not Pearson r.
  * Staff vs student comparisons use Mann-Whitney U, not a t-test, because the
    staff group has n = 8 and the items are ordinal.
  * No correction for multiple comparisons is applied; the analysis is
    exploratory and p-values are read as descriptive, which the report states.

Usage: python 02_analyse_survey.py
"""

from pathlib import Path
import pandas as pd
from scipy import stats

HERE = Path(__file__).resolve().parent
CLEAN = HERE.parent / "data" / "processed" / "GENAI_survey-clean_20260814_v02.csv"
TABLES = HERE.parent / "outputs" / "tables"

ITEMS = {
    "freq_use": "Frequency of use",
    "benefit_writing": "Perceived benefit: writing",
    "benefit_coding": "Perceived benefit: coding",
    "concern_accuracy": "Concern: factual accuracy",
    "concern_integrity": "Concern: academic integrity",
    "concern_skill_loss": "Concern: loss of own skills",
    "overall_stance": "Overall stance (1 = bane, 5 = boon)",
}


def descriptives(df):
    rows = []
    for col, label in ITEMS.items():
        s = df[col].dropna()
        counts = s.value_counts().reindex(range(1, 6), fill_value=0)
        rows.append({
            "item": col,
            "label": label,
            "n": int(s.size),
            "missing": int(df[col].isna().sum()),
            "median": s.median(),
            "mean": round(s.mean(), 2),
            "sd": round(s.std(ddof=1), 2),
            **{f"n_{k}": int(v) for k, v in counts.items()},
            "pct_top2": round(100 * (s >= 4).mean(), 1),
            "pct_bottom2": round(100 * (s <= 2).mean(), 1),
        })
    return pd.DataFrame(rows)


def correlations(df):
    pairs = [
        ("freq_use", "benefit_mean"),
        ("freq_use", "concern_mean"),
        ("freq_use", "overall_stance"),
        ("benefit_mean", "overall_stance"),
        ("concern_mean", "overall_stance"),
        ("concern_accuracy", "overall_stance"),
        ("concern_integrity", "overall_stance"),
        ("concern_skill_loss", "overall_stance"),
        ("benefit_mean", "concern_mean"),
    ]
    rows = []
    for a, b in pairs:
        sub = df[[a, b]].dropna()
        rho, p = stats.spearmanr(sub[a], sub[b])
        rows.append({
            "var_a": a, "var_b": b, "n": len(sub),
            "spearman_rho": round(rho, 3),
            "p_value": round(p, 4),
            "interpretation": (
                "negligible" if abs(rho) < 0.2 else
                "weak" if abs(rho) < 0.4 else
                "moderate" if abs(rho) < 0.6 else "strong"
            ),
        })
    return pd.DataFrame(rows)


def cohort_comparison(df):
    rows = []
    for col, label in ITEMS.items():
        stu = df.loc[df["cohort"] == "Student", col].dropna()
        stf = df.loc[df["cohort"] == "Staff", col].dropna()
        u, p = stats.mannwhitneyu(stu, stf, alternative="two-sided")
        rows.append({
            "item": col, "label": label,
            "n_student": len(stu), "median_student": stu.median(),
            "n_staff": len(stf), "median_staff": stf.median(),
            "mannwhitney_u": u, "p_value": round(p, 4),
        })
    return pd.DataFrame(rows)


def main():
    df = pd.read_csv(CLEAN)
    TABLES.mkdir(parents=True, exist_ok=True)
    print(f"Loaded {len(df)} respondents from {CLEAN.name}")
    print(f"Cohorts: {df['cohort'].value_counts().to_dict()}")

    d = descriptives(df)
    d.to_csv(TABLES / "GENAI_item-descriptives_20260818_v01.csv", index=False)
    print("\n-- Item descriptives --")
    print(d[["item", "n", "median", "mean", "sd", "pct_top2"]].to_string(index=False))

    c = correlations(df)
    c.to_csv(TABLES / "GENAI_correlations_20260818_v01.csv", index=False)
    print("\n-- Spearman correlations --")
    print(c.to_string(index=False))

    k = cohort_comparison(df)
    k.to_csv(TABLES / "GENAI_cohort-comparison_20260818_v01.csv", index=False)
    print("\n-- Student vs staff (Mann-Whitney U) --")
    print(k[["item", "median_student", "median_staff", "p_value"]].to_string(index=False))

    print("\n-- Disclosure behaviour --")
    ct = pd.crosstab(df["training_received"], df["disclosed_use"])
    print(ct.to_string())

    print(f"\nTables written to {TABLES}")


if __name__ == "__main__":
    main()
