# Survey analysis report

Project `GENAI` · Version 02 · 20 August 2026
Data: `../data/processed/GENAI_survey-clean_20260814_v02.csv` (n = 60)
Analysis: `../scripts/02_analyse_survey.py`, `../scripts/03_make_figures.py`
Tables: `../outputs/tables/` · Figures: `../outputs/figures/`

> **Synthetic data.** This report analyses the synthetic teaching dataset described in
> `../data/processed/GENAI_data-dictionary_20260814_v01.md`. The numbers are internally
> consistent and reproducible but are not evidence about real generative AI use.

## 1. Respondents

Sixty usable responses after cleaning: 52 students (24 undergraduate, 14 postgraduate
coursework, 14 postgraduate research) and 8 academic staff. One duplicate submission
and one platform sentinel value were removed during cleaning; two item-level missing
values remain and are not imputed, so n is stated for every statistic.

The 52:8 split is the dominant limitation of this analysis. Staff results rest on
eight people and are reported as descriptive only.

## 2. Use and perceived benefit

Use is high: the median frequency is 4 (weekly), and 54.2% of respondents rate their
use at 4 or 5 (n = 59). Students use these tools more than staff — median 4 against
median 3, Mann-Whitney U, p = 0.005 — and this is the **only** item on which the two
cohorts differ at conventional levels.

Perceived benefit is higher for writing (median 4, 55.0% at 4-5) than for coding
(median 3, 47.5% at 4-5), and the two track frequency of use strongly: Spearman
rho = 0.68 between frequency and mean perceived benefit (n = 59, p < 0.001).

That correlation is the result most easily over-read. The design is cross-sectional,
so it is equally consistent with heavy users coming to see more benefit and with
people who expect benefit using the tools more. Nothing here separates the two.

## 3. Concern

Concern is widespread and is not confined to sceptics. Factual accuracy is the
leading worry (median 4, 61.7% at 4-5), ahead of loss of one's own skills (median 4,
53.3%) and academic integrity (median 3, 48.3%). Staff and student medians do not
differ on any concern item.

## 4. The central finding: benefit and concern are independent

Mean perceived benefit and mean concern are **uncorrelated** (rho = 0.02, n = 60,
p = 0.88). Concern also fails to predict the overall stance (rho = -0.02, p = 0.86),
while perceived benefit predicts it moderately (rho = 0.50, p < 0.001).

The practical reading is that respondents are not arranging themselves along a single
boon-to-bane axis. A respondent can rate the accuracy risk at 5 and still place
themselves at 4 on overall stance, and many do. The overall stance question is
effectively answered on benefit alone, with concern held alongside it rather than
subtracted from it.

This directly contradicts the framing in the project title, and supports the argument
in `rudolph2023chatgpt` that the boon/bane binary is the wrong instrument. It is the
result the final report should lead with, and it is also a warning about item F1: a
single "on balance" question compresses two independent dimensions into one number
and loses the more interesting structure. Future waves should report benefit and
concern separately rather than as a net position.

## 5. Disclosure

Disclosure is partial: 38.3% disclose always, 45.0% sometimes, 16.7% never. Only 30%
of respondents have received any formal training.

Trained respondents disclose *less* consistently than untrained ones (27.8% always
against 42.9%). With 18 trained respondents this is almost certainly noise, and it is
reported here only so that it is not quietly dropped if a later wave reverses it. It
should not appear in the final report as a finding.

## 6. What this analysis does not support

- **No causal claim.** Every association above is cross-sectional.
- **No population estimate.** The sample is a convenience sample recruited through
  course announcements and a staff mailing list.
- **No staff-student contrast beyond frequency of use.** With n = 8 staff, the
  non-significant results are uninformative rather than evidence of no difference.
- **No correction for multiple comparisons** is applied across the nine correlations
  and seven cohort tests, so individual p-values near 0.05 should not be read as
  confirmatory. The two results reported as findings (rho = 0.68 and rho = 0.50)
  survive a Bonferroni correction comfortably; none of the others do.

## 7. Next steps

1. Feed Section 4 into the interview guide — ask directly how respondents hold high
   benefit and high concern at the same time. This is now the main link between the
   quantitative and qualitative strands.
2. Recruit staff deliberately rather than opportunistically for wave 2.
3. Replace F1 with separate benefit and concern summary items.
