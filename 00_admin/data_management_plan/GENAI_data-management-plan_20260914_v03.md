# Data management plan — "Using Generative AI Tools: Boon or Bane"

Project code `GENAI` · Version 03 · 14 September 2026
Prepared against the UQ Library Research Data Management Plan Checklist
(<https://guides.library.uq.edu.au/research-and-teaching-staff/research-data-management-plan/checklist>).

## 1. What data the project produces

| Stream | Data types | Formats | Approx. volume | Sensitivity |
|---|---|---|---|---|
| Literature review | Search strategies, screening decisions, bibliography, reading notes | `.md`, `.csv`, `.bib` | < 10 MB (excl. publisher PDFs) | Low — but PDFs are copyright-restricted |
| Quantitative | Survey instrument, raw export, cleaned dataset, scripts, figures, tables | `.csv`, `.py`, `.md`, `.png`, `.pdf` | ~50 MB | Low once de-identified; raw export is indirectly identifying |
| Qualitative | Interview protocol, consent forms, audio, transcripts, codebook | `.docx`, `.pdf`, `.wav`, `.txt`, `.md` | ~8 GB (audio dominates) | **High** — identifiable |
| Drafts and reports | Proposal, conference paper, final report, slides | `.md`, `.docx`, `.pdf`, `.pptx` | ~200 MB | Low, but embargoed pre-publication |
| Additional materials | Information sheets, photographs, other media | `.pdf`, `.jpg`, `.mp4` | ~3 GB | Mixed — photographs of people are identifiable |

## 2. Where each stream is stored (three-tier model)

**Tier 1 — GitHub (this repository).** Code, documentation, de-identified tabular
data, and text-based drafts. Chosen because these are the artefacts that change
often, need line-level version history, and benefit from pull-request review.
Repository visibility: for a study holding real participant data, **private** until
publication, then released publicly with a DOI minted through UQ eSpace. The copy used
for the REIT6811 exercise is **public**, so that group members could fork it without
first being invited as collaborators; that is acceptable only because it holds
synthetic data and nothing identifiable has ever been committed.

**Tier 2 — UQ Research Data Manager (RDM).** The authoritative store for
everything identifiable, copyright-restricted or large: signed consent forms,
audio recordings, identifiable transcripts, photographs of participants, the
participant linkage key, and publisher PDFs. RDM is chosen because it is the
University's approved location for sensitive research data, is backed up and
geographically replicated by ITS, applies role-based access control, and satisfies
the 5-year minimum retention obligation without further action by the team. Each
restricted folder in this repository contains a `README.md` pointing to the
corresponding RDM record instead of the files themselves.

**Tier 3 — UQ eSpace.** Long-term publication and archival of the de-identified
dataset and outputs at project close, with a citable DOI.

Working copies on personal machines are treated as disposable; nothing is
authoritative until it is committed to Tier 1 or deposited in Tier 2.

## 3. Access control

| Asset | Who has access | Mechanism |
|---|---|---|
| This repository (exercise copy) | Public; changes arrive as pull requests from forks, merged by the owner | Public GitHub repo, synthetic data only |
| Repository for a real-data study | Named investigators + supervisor | Private GitHub repo, collaborator invitations, `main` protected |
| RDM: consent forms, linkage key | Chief investigator only | RDM record permissions, restricted collection |
| RDM: audio, identifiable transcripts | Investigators who completed the transcription training | RDM record permissions |
| De-identified transcripts and survey data | All team members | Tier 1 repository |
| Published outputs | Public, post-embargo | eSpace, CC BY |

De-identification happens before data crosses from Tier 2 to Tier 1, never after.
Participant names are replaced with codes `P01`–`Pnn`; the code-to-name key is
held only in RDM and is never committed — it is also blocked by a `.gitignore`
rule so that an accidental `git add .` cannot capture it.

## 4. Backup

Tier 1 is held in three places at all times: the GitHub remote, each
collaborator's local clone, and the nightly RDM mirror of the repository archive.
Tier 2 is backed up by UQ ITS with off-site replication; no separate team-managed
backup is required, which is the main practical reason for preferring RDM over a
consumer cloud drive. The 3-2-1 target (three copies, two media, one off-site) is
therefore met for every stream without manual copying.

## 5. Retention and disposal

Minimum five years from publication under the *Australian Code for the Responsible
Conduct of Research*; the ethics approval for this project commits to retaining
identifiable data for five years and then destroying it, while the de-identified
dataset is retained indefinitely in eSpace. Audio recordings are destroyed once
transcription is verified and the paper is accepted, which is recorded as a task
in `00_admin/project_management/`.

## 6. Documentation and metadata

Every dataset directory carries a `README.md` giving provenance, collection date,
variable definitions and known limitations. The survey dataset additionally has a
machine-readable data dictionary at
`02_quantitative/data/processed/GENAI_data-dictionary_20260814_v01.md`. Project-level
metadata follows the RDM record fields, which map to the ANDS/RIF-CS schema, so
that no separate metadata exercise is needed at deposit time.

## 7. Open items

- Confirm whether the conference target permits preprint deposit before the
  embargo lifts (affects when Tier 1 flips to public).
- Decide the embargo period for the de-identified interview transcripts; the
  consent form permits sharing but participants were not asked about a timeframe.

## Changes in version 03

- Tier 1 visibility and the access-control table now distinguish the public copy used
  for the REIT6811 exercise from the private repository a real-data study would use.
- Checklist link updated. The UQ Library guide moved from `/for-researchers/` to
  `/research-and-teaching-staff/`, and the old address no longer resolves.
