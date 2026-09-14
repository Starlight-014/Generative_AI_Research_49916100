# Generative_AI_Research_49916100

Research data repository for the study **"Using Generative AI Tools: Boon or Bane?"** —
a mixed-methods study of how students and academic staff perceive the benefits and
risks of generative AI in higher education.

Created for **REIT6811 Applied Class 6: Comprehensive Data Handling in Research**,
The University of Queensland, Semester 2, 2026.

> **Synthetic data notice.** The survey data, transcripts and reports in this
> repository are synthetic material created for a teaching exercise on research data
> management. They are internally consistent and fully reproducible, but they are not
> the output of a real study and must not be cited as evidence about generative AI
> use. See `02_quantitative/data/processed/GENAI_data-dictionary_20260814_v01.md`.

---

## 1. What is in this repository

```
Generative_AI_Research_49916100/
├── README.md                    ← you are here
├── .gitignore                   ← what must never be committed, and why
├── Project_logbook.txt          ← running log of version-control activity
├── docs/
│   └── NAMING_CONVENTION.md     ← read this before adding any file
├── 00_admin/                    ← ethics, data management plan, decision log
├── 01_literature/               ← search strategy, screening, bibliography, notes
├── 02_quantitative/             ← survey instrument, data, scripts, outputs, report
├── 03_qualitative/              ← interview protocol, transcripts, codebook, report
├── 04_drafts_reports/           ← proposal, conference paper, final report, slides
├── 05_additional_materials/     ← information sheets, media
└── 99_archive/                  ← superseded material that is still referenced
```

Top-level folders are numbered so that they display in workflow order rather than
alphabetically — `01_literature` precedes `02_quantitative` on every platform, and a
new collaborator can read the tree as a sequence.

| Folder | Contains | Start here |
|---|---|---|
| `00_admin/` | HREC conditions, data management plan, decision and meeting log | `00_admin/ethics/GENAI_ethics-conditions_20260614_v01.md` |
| `01_literature/` | Reproducible record of the literature review | `01_literature/search_strategy/` |
| `02_quantitative/` | Survey strand, end to end | `02_quantitative/reports/` |
| `03_qualitative/` | Interview strand, end to end | `03_qualitative/reports/` |
| `04_drafts_reports/` | Written outputs | `04_drafts_reports/conference_paper/` |
| `05_additional_materials/` | Participant-facing documents and media | `05_additional_materials/information_sheets/` |

Each of the three research streams uses the same internal shape — `instruments/`,
data, `outputs/`, `reports/` — so that knowing where something lives in one stream
tells you where it lives in the others.

## 2. Where to start

**If you want to know what the study found**, read
`02_quantitative/reports/GENAI_survey-analysis-report_20260820_v02.md`, then
`03_qualitative/reports/GENAI_qualitative-insights_20260825_v01.md`. The headline is
that perceived benefit and perceived concern are statistically independent, so the
"boon or bane" framing in the title is the thing the study ends up questioning.

**If you want to check a number**, every figure and table is regenerated from the
cleaned data by the scripts in `02_quantitative/scripts/`, and every change made to
the raw export is listed in
`02_quantitative/data/processed/GENAI_cleaning-log_20260814_v02.md`.

**If you are joining the project**, read this file, then `docs/NAMING_CONVENTION.md`,
then `00_admin/ethics/GENAI_ethics-conditions_20260614_v01.md` — in that order. The
third one governs what you are allowed to add.

## 3. Reproducing the analysis

Requires Python 3.10+ with `pandas`, `scipy` and `matplotlib`.

```bash
cd 02_quantitative/scripts
python 00_generate_synthetic_data.py   # only for this teaching exercise
python 01_clean_survey.py              # raw  -> processed + cleaning log
python 02_analyse_survey.py            # processed -> outputs/tables
python 03_make_figures.py              # processed -> outputs/figures
```

Scripts run in numeric order and each one prints what it did. `01_clean_survey.py`
never writes to `data/raw/`.

## 4. What is deliberately NOT in this repository

This is the most important section for anyone adding files.

| Not committed | Where it lives instead | Why |
|---|---|---|
| Signed consent forms | UQ RDM `03_consent` | Identifiable; a private GitHub repo is not an approved store for identifiable UQ research data |
| Identifiable transcripts and the participant linkage key | UQ RDM `04_transcripts_identifiable` | Re-identification risk |
| Interview audio (~7.9 GB) | UQ RDM `05_recordings` | Voice is biometric; also far past GitHub's practical size limits |
| Photographs of people | UQ RDM `06_media_identifiable` | Identifiable |
| Publisher PDFs of reviewed articles | Retrieved from UQ Library by DOI | Redistribution breaches most subscription licences |
| Slide decks, the full 2,545-row screening log | UQ RDM | Binary or very large; Git cannot diff them usefully |

Every restricted folder contains a `README.md` pointing to the corresponding RDM
record, so the structure stays complete and a reader can always tell that something
exists and where to ask for it.

**Git history is effectively permanent.** Deleting a file in a later commit does not
remove it from the history, and every clone already has a copy. That is why these
rules are enforced by `.gitignore` rather than by care — an accidental `git add .`
must not be able to capture identifiable data in the first place.

## 5. How to contribute

1. **Never commit directly to `main`.** `main` is protected and requires one approving
   review.
2. **Branch from `main`**, naming the branch `<type>/<short-description>`:
   `analysis/ordinal-regression`, `docs/readme-navigation`, `data/wave2-import`,
   `fix/cleaning-log-path`.
3. **Name every file** under `docs/NAMING_CONVENTION.md`. A pull request may be
   rejected on naming alone, because a file named badly today is a file nobody can
   find in a year.
4. **Write commit messages that say what changed and why.** Imperative mood, roughly
   50 characters in the subject line, and a body when the reason is not obvious:

   ```
   Recode platform sentinel 9 to missing in benefit_coding

   The survey platform writes 9 for the "not applicable" option at C2.
   Averaging it as a rating inflated the item mean. The cleaning log now
   records the affected respondent (R019).
   ```

   Not `update`, `fix`, `changes`, or `asdf`. The history is documentation, and it is
   the only documentation nobody can forget to write.
5. **One logical change per commit.** A commit that adds a figure *and* changes the
   cleaning rule cannot be reverted without losing one of them.
6. **Do not commit regenerable outputs by hand.** Run the script. A figure edited
   after generation no longer matches the data and cannot be reproduced.
7. **Open an issue** for anything you notice but are not fixing now, rather than
   leaving it in a meeting note. Issues are visible to whoever picks the work up.
8. **Before you push**, run `git status` and read it. If anything from the table in
   section 4 appears, stop and fix `.gitignore` before committing.

### Pull request checklist

- [ ] Branch named `<type>/<short-description>`
- [ ] Files named per `docs/NAMING_CONVENTION.md`
- [ ] No identifiable, copyright-restricted or large binary files added
- [ ] Outputs regenerated by script, not edited by hand
- [ ] Decision log updated if this changes the data or the analysis
- [ ] One reviewer assigned

## 6. Collaborators and roles

| Role | Responsibility |
|---|---|
| Repository owner / code reviewer | Reviews and merges pull requests, resolves conflicts, maintains `main` |
| Contributors | Work on branches, open pull requests, keep the decision log current |
| Supervisor | Read access; reviews outputs, does not commit |

Access is granted through **Settings → Collaborators** with the least privilege that
lets someone do their job: read for the supervisor, write for contributors, admin for
the owner alone.

## 7. Licence and citation

Code in `02_quantitative/scripts/` is released under the MIT Licence. Documentation
and de-identified data will be released under CC BY 4.0 at publication, when this
repository becomes public and the dataset is deposited in UQ eSpace with a DOI. Until
then the repository is **private** and its contents are not for circulation.

---

*Maintained by Zixuan Dai (49916100) · REIT6811, The University of Queensland ·
Last updated 14 September 2026*
