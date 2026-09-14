# De-identification procedure and log

Applied to every transcript before it moves from the RDM identifiable collection into
`../transcripts/deidentified/` and therefore into this repository. The step is
one-way: nothing in this repository can be used to re-identify a participant, and the
key that could is held only in RDM.

## Procedure

1. Transcribe from audio into the identifiable transcript (RDM only).
2. Verify the transcript against the audio; correct errors at this stage, not later.
3. Replace, in this order:
   - participant and interviewer **names** with `P nn` and `I`
   - **third-party names** (supervisors, colleagues, students) with `[SUPERVISOR]`,
     `[COLLEAGUE]`, `[STUDENT]`
   - **course codes** with `[COURSE]`, **schools and faculties** with `[SCHOOL]`,
     **disciplines** with `[DISCIPLINE]`
   - **employers and organisations** with `[EMPLOYER]`
   - **specific tool names** with `[TOOL]` *where the combination of tool, role and
     discipline would narrow the participant to a small group*; otherwise tool names
     are retained, since they are analytically important
4. Read the whole transcript once more asking a single question: could a colleague in
   the same school identify this person from what remains? Redact further if yes.
5. Record the redaction categories used in the transcript header.
6. Second reviewer repeats step 4 independently before the file is committed.

## Why indirect identifiers matter more than names here

Removing names is the easy part and is not sufficient. In a study whose participants
are drawn from one university, a phrase such as "the second year of a research
masters in X, supervised by Y, who coordinates the 400-student course Z" identifies a
person completely without using a single name. The four-hundred-student course figure
in P03 was retained only after checking that more than one course in the university
matches it.

## Log

| Participant | De-identified | Reviewer 2 | Categories redacted | Notes |
|---|---|---|---|---|
| P01 | 2026-07-09 | 2026-07-10 | DISCIPLINE, COURSE, SUPERVISOR, TOOL | Supervisor is identifiable within the school; both mentions redacted |
| P02 | 2026-07-10 | 2026-07-11 | DISCIPLINE, COURSE, TOOL, EMPLOYER | Employer named a small firm; redacted |
| P03 | 2026-07-12 | 2026-07-14 | DISCIPLINE, COURSE, SCHOOL, COLLEAGUE | Enrolment figure retained after checking it is not unique |
| P04-P18 | 2026-07-14 to 2026-07-29 | completed | see transcript headers | Log continues in the RDM copy |

## Residual risk

Two participants described incidents specific enough that a close colleague might
recognise them even after redaction. Both were contacted, shown the redacted passage,
and asked whether they were comfortable with it being quoted; one asked for a further
change, which was made. That consultation is recorded in the RDM collection and is
the reason P07 and P13 carry a `v02` transcript.
