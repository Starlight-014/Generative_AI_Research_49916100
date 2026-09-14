# Data dictionary -- GENAI cleaned survey dataset

File: `GENAI_survey-clean_20260814_v02.csv` · 60 rows (one per respondent) · UTF-8, comma-separated
Produced by `../../scripts/01_clean_survey.py` from `../raw/GENAI_survey-export_20260812_v01.csv`.

| Variable | Type | Values | Source | Notes |
|---|---|---|---|---|
| `respondent_id` | string | `R001`-`R060` | assigned by platform | Not linkable to any individual; no linkage key exists for the survey strand |
| `role` | categorical | Undergraduate; Postgraduate (coursework); Postgraduate (research); Academic staff | A1 | Capitalisation normalised during cleaning |
| `discipline` | categorical | 8 levels | A2 | Whitespace trimmed during cleaning |
| `freq_use` | ordinal 1-5 | 1 Never .. 5 Daily | B1 | 1 missing (R008) |
| `tools_used` | string | semicolon-separated tool names | B2 | Multi-select; split on `;` before counting |
| `benefit_writing` | ordinal 1-5 | 1 Strongly disagree .. 5 Strongly agree | C1 | |
| `benefit_coding` | ordinal 1-5 | as above | C2 | 1 missing (R019, answered "not applicable") |
| `concern_accuracy` | ordinal 1-5 | as above | D1 | |
| `concern_integrity` | ordinal 1-5 | as above | D2 | |
| `concern_skill_loss` | ordinal 1-5 | as above | D3 | |
| `training_received` | binary | Yes; No | E2 | |
| `disclosed_use` | categorical | Always; Sometimes; Never | E1 | |
| `overall_stance` | ordinal 1-5 | 1 Clearly a problem .. 5 Clearly a benefit | F1 | Primary outcome |
| `benefit_mean` | derived, continuous | 1.0-5.0 | derived | Mean of `benefit_writing`, `benefit_coding`; uses the available item where one is missing |
| `concern_mean` | derived, continuous | 1.0-5.0 | derived | Mean of the three `concern_*` items |
| `cohort` | derived, binary | Student; Staff | derived from `role` | Collapses the three student roles |
| `n_tools` | derived, integer | 1-3 | derived from `tools_used` | Count of semicolon-separated entries |

## Known limitations

- **Convenience sample.** Recruitment was by course announcement and staff mailing
  list, so the 52:8 student-to-staff ratio reflects who was reachable, not the
  population. Staff estimates rest on n = 8 and should not be reported without that n.
- **Self-report throughout.** `freq_use` and `disclosed_use` in particular are
  subject to social desirability bias, and disclosure is the item where a respondent
  has the clearest incentive to answer inaccurately.
- **Cross-sectional.** The association between frequency of use and perceived
  benefit (rho = 0.68) is not evidence of a direction; heavy users may become
  enthusiasts or enthusiasts may become heavy users, and this design cannot separate
  the two.
- **Ordinal items treated as ordinal.** Means and standard deviations are reported
  for comparability with the published literature, but all inference uses rank-based
  methods.

## Synthetic data notice

This dataset was generated for the REIT6811 Applied Class 6 exercise on research data
handling. It is **synthetic teaching data**, not the output of a real study, and must
not be cited as evidence about generative AI use. The generator is
`../../scripts/00_generate_synthetic_data.py`, seeded so that the file is reproducible.
