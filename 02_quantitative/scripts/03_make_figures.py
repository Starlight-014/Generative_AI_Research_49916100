"""
03_make_figures.py -- figures for the survey analysis report.

Reads   : ../data/processed/GENAI_survey-clean_20260814_v02.csv
Writes  : ../outputs/figures/GENAI_fig1_item-distributions_20260818_v01.{png,pdf}
          ../outputs/figures/GENAI_fig2_benefit-vs-stance_20260818_v01.{png,pdf}

Run 01_clean_survey.py first. Figures are regenerated from the cleaned data on
every run, which is why they are committed as outputs rather than edited by hand:
a figure that cannot be reproduced from a script is not evidence.

Design choices:
  * Ordinal items are shown as the full stacked response distribution, not as a
    bar of means -- with n = 60 a mean of 3.5 hides whether opinion is split or
    clustered, and that distinction is the finding.
  * Individual respondents are plotted in Figure 2 rather than group averages,
    because some stance levels contain fewer than ten people.
  * Palette is colourblind-safe (Okabe-Ito); no dual axes; no pie charts;
    y-axis starts at zero on the count axis.

Usage: python 03_make_figures.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
CLEAN = HERE.parent / "data" / "processed" / "GENAI_survey-clean_20260814_v02.csv"
FIGS = HERE.parent / "outputs" / "figures"

# Okabe-Ito, ordered light (disagree) to dark (agree)
SCALE = ["#F0E442", "#E69F00", "#CC79A7", "#0072B2", "#004C6D"]
ACCENT = "#0072B2"
GREY = "#666666"

ITEMS = [
    ("freq_use", "Frequency of use"),
    ("benefit_writing", "Benefit: writing"),
    ("benefit_coding", "Benefit: coding"),
    ("concern_accuracy", "Concern: accuracy"),
    ("concern_integrity", "Concern: integrity"),
    ("concern_skill_loss", "Concern: skill loss"),
    ("overall_stance", "Overall stance"),
]

plt.rcParams.update({
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "-",
    "figure.dpi": 150,
    "savefig.bbox": "tight",
})


def save(fig, stem):
    FIGS.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIGS / f"{stem}.{ext}")
    plt.close(fig)
    print(f"  wrote {stem}.png / .pdf")


def fig1_distributions(df):
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    labels = [lab for _, lab in ITEMS]
    y = np.arange(len(ITEMS))
    left = np.zeros(len(ITEMS))
    for rating in range(1, 6):
        widths = [int((df[col].dropna() == rating).sum()) for col, _ in ITEMS]
        ax.barh(y, widths, left=left, height=0.66, color=SCALE[rating - 1],
                edgecolor="white", linewidth=0.6, label=str(rating))
        left += np.array(widths, dtype=float)
    for i, (col, _) in enumerate(ITEMS):
        s = df[col].dropna()
        ax.text(left[i] + 0.7, y[i], f"md {s.median():.0f}  n {s.size}",
                va="center", fontsize=7.5, color=GREY)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 72)
    ax.set_xlabel("Number of respondents")
    ax.set_title("Response distribution across survey items (n = 60)", loc="left", fontsize=10)
    ax.legend(title="Rating (1 = low, 5 = high)", ncol=5, fontsize=7.5,
              title_fontsize=7.5, frameon=False,
              loc="upper center", bbox_to_anchor=(0.5, -0.20))
    ax.grid(axis="y", visible=False)
    save(fig, "GENAI_fig1_item-distributions_20260818_v01")


def fig2_benefit_vs_stance(df):
    rng = np.random.default_rng(6811)
    sub = df[["benefit_mean", "overall_stance", "cohort"]].dropna()
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    for cohort, marker, colour in (("Student", "o", ACCENT), ("Staff", "^", "#D55E00")):
        s = sub[sub["cohort"] == cohort]
        ax.scatter(s["overall_stance"] + rng.uniform(-0.14, 0.14, len(s)),
                   s["benefit_mean"] + rng.uniform(-0.06, 0.06, len(s)),
                   s=32, marker=marker, facecolor=colour, edgecolor="white",
                   linewidth=0.6, alpha=0.85, label=f"{cohort} (n = {len(s)})")
    med = sub.groupby("overall_stance")["benefit_mean"].median()
    ax.plot(med.index, med.values, color=GREY, linewidth=1.4, linestyle="--",
            marker="_", markersize=16, label="Median benefit at each stance")
    ax.set_xticks(range(1, 6))
    ax.set_xlabel("Overall stance (1 = clearly a bane, 5 = clearly a boon)")
    ax.set_ylabel("Mean perceived benefit")
    ax.set_title("Perceived benefit against overall stance", loc="left", fontsize=10)
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    save(fig, "GENAI_fig2_benefit-vs-stance_20260818_v01")


if __name__ == "__main__":
    data = pd.read_csv(CLEAN)
    print(f"Generating figures from {CLEAN.name} ({len(data)} respondents)...")
    fig1_distributions(data)
    fig2_benefit_vs_stance(data)
    print("Done.")
