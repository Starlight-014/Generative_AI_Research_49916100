# RESTRICTED — identifiable transcripts are NOT stored in this repository

First-pass transcripts contain participant names, employers, course codes and other
indirect identifiers. They are held in UQ RDM; only the de-identified versions in
`../deidentified/` are tracked by Git.

- **RDM record:** `GENAI-boon-or-bane` → collection `04_transcripts_identifiable`
- **Access:** investigators who have completed transcription training
- **Contents:** 18 transcripts plus the participant linkage key
- **De-identification log:** `../../coding/GENAI_deidentification-log_20260702_v01.md`

The linkage key that maps `P01`–`P18` to participant names is stored only in RDM and
is additionally blocked by the `**/*participant-key*` rule in `.gitignore`.
