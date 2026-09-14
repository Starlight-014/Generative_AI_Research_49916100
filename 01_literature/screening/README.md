# Screening records

`GENAI_screening-log_20260722_v01.csv` records one row per unique record, with the
title/abstract (`ta_`) and full-text (`ft_`) decision and, where excluded, the single
governing reason. Reasons are drawn from a closed list so that they aggregate into a
PRISMA flow diagram without recoding:

- `not education setting`
- `not generative AI`
- `not perceptions/attitudes`
- `not peer reviewed`
- `language limit`
- `pre-2022 primary studies only`
- `duplicate`
- `full text unavailable`

**The committed file is an extract of the first 20 records**, kept small enough to
diff usefully in a pull request. The complete 2,545-row log is a working spreadsheet
in RDM (`02_literature/screening`) because a file of that size produces unreadable
diffs and merge conflicts that Git cannot help to resolve.

Double screening: 10% of records (n = 255) were screened independently by a second
reviewer; Cohen kappa = 0.81. Disagreements and their resolution are recorded in
`GENAI_screening-disagreements_20260722_v01.md` in the same RDM collection.
