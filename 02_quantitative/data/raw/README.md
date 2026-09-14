# raw/ -- READ ONLY

The survey platform export exactly as downloaded on 12 August 2026. **Nothing in this
folder is ever edited**, including to fix an obvious typo. Corrections are made by
`../../scripts/01_clean_survey.py` and recorded in the cleaning log, so that every
value in the analysis can be traced back to what the respondent actually submitted.

This is the single most important rule in the repository. A raw file that has been
"just quickly fixed" cannot be distinguished from one that has not, and the audit
trail is lost silently.

If the export is ever re-downloaded (for example after late responses arrive), add it
as a **new** file with a new date rather than overwriting this one, and update the
path at the top of `01_clean_survey.py`.

| File | Downloaded | Rows | Notes |
|---|---|---|---|
| `GENAI_survey-export_20260812_v01.csv` | 2026-08-12 | 61 | Includes one duplicate submission (R045) and one platform sentinel value; both handled in cleaning |
