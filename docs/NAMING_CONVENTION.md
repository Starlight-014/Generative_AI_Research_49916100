# File naming convention

Adapted from the Harvard Medical School Data Management Working Group guidance on
file naming conventions
(<https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions>).
Every file added to this repository must follow the pattern below. Reviewers may
reject a pull request on naming grounds alone.

## Pattern

```
GENAI_<content-description>_<YYYYMMDD>_v<NN>.<ext>
```

| Element | Rule | Example |
|---|---|---|
| `GENAI` | Fixed project code, so a file is identifiable once it leaves the repository | `GENAI` |
| `<content-description>` | 2–4 words, lower case, hyphen-separated, describing content not container | `survey-analysis-report` |
| `<YYYYMMDD>` | ISO 8601 basic date of the *content*, not of the upload. Sorts chronologically as text | `20260812` |
| `v<NN>` | Two-digit version, zero-padded, incremented on any substantive change | `v02` |
| `<ext>` | Lower case, open or widely readable format preferred | `.csv`, `.md`, `.py` |

Interview and participant-level files carry the de-identified participant code
immediately after the content description: `GENAI_transcript_P01_20260705_v01.txt`.

## Rules

1. **No spaces.** Use `_` between elements and `-` inside an element. Spaces break
   command-line tools, URLs and some backup systems.
2. **No special characters** other than `_`, `-` and the single extension dot.
   Avoid `& $ % # @ ! * ? < > : " / \ |` — several are illegal in Windows paths
   and `:` `/` `\` are illegal or meaningful on every platform.
3. **Dates as `YYYYMMDD`.** `20260812` sorts correctly; `12-08-2026` does not, and
   `08/12/2026` is ambiguous between Australian and US readers.
4. **Zero-pad all numbers.** `v02`, `P01`, `01_clean_survey.py` — otherwise `v10`
   sorts before `v2`.
5. **Version in the filename, not in words.** Never `final`, `FINAL_v2`,
   `final_really`, `latest` or a person's initials. The authoritative version is
   the highest `vNN`; the full history is in Git.
6. **Keep total path length short.** Windows still enforces a 260-character
   default limit, and this repository is nested four levels deep in places.
7. **Lower case for extensions and descriptions.** Git on Windows and macOS is
   case-insensitive by default but case-*preserving*, which silently produces
   duplicate paths on Linux.
8. **Describe content, not status or author.** `GENAI_codebook_20260810_v03.md`,
   not `zd_codebook_updated.md`. Authorship and update time are recorded by Git.

## Worked examples

| Good | Poor | Why the poor version fails |
|---|---|---|
| `GENAI_survey-export_20260812_v01.csv` | `survey data FINAL.csv` | spaces, no date, no version, "FINAL" is not a version |
| `GENAI_transcript_P03_20260708_v01.txt` | `Interview with Sarah 8-7-26.docx` | identifiable, ambiguous date, closed format |
| `GENAI_conference-paper_20260901_v02.md` | `paper v2 (ZD edits) copy.md` | parentheses, spaces, "copy", author initials |
| `01_clean_survey.py` | `cleaning script new.py` | scripts are prefixed by run order, not renamed |

## Scripts are the exception

Files in `02_quantitative/scripts/` are prefixed with their execution order
(`01_`, `02_`, `03_`) rather than a date and version, because the pipeline order
is the information a reader needs first. Their history is tracked by Git alone,
which is why the filename must stay stable across revisions.
