# interim/ — intentionally not tracked

Intermediate files produced part-way through the cleaning pipeline. They are fully
regenerable from `../raw/` by running `../../scripts/01_clean_survey.py`, so
committing them would add churn and repository size without adding information.
This folder is excluded in `.gitignore` except for this note.

Keep the folder itself, because the scripts expect the path to exist.
