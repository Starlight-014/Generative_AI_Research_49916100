# 01_literature — literature review stream

Contains the *reproducible record* of the literature review: what was searched,
what was screened in or out and why, the bibliography, and the synthesis notes.

## What is here

| Folder | Contents |
|---|---|
| `search_strategy/` | Database-by-database search strings and result counts, so the search can be re-run and audited |
| `screening/` | Title/abstract and full-text screening decisions with exclusion reasons, one row per record |
| `bibliography/` | Zotero export in BibTeX; this is the single source of truth for citations |
| `notes/` | Synthesis matrix and thematic reading notes |

## What is NOT here

**Publisher PDFs of the articles themselves.** Redistributing a subscription PDF
through a repository breaches most publisher licence agreements, including where the
repository is private, because access is granted to the individual under UQ's
subscription rather than to the project. Team members retrieve full text through the
UQ Library using the DOI recorded in the bibliography. The rule
`01_literature/**/*.pdf` in `.gitignore` enforces this.

Open-access articles under a CC licence are the exception and may be committed, but
must record the licence in the commit message.
