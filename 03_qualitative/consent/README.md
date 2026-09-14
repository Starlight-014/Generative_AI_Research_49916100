# RESTRICTED — signed consent forms are NOT stored in this repository

Signed participant consent forms are identifiable records. They are held in UQ RDM
and are deliberately excluded from Git by a rule in `.gitignore`.

- **RDM record:** `GENAI-boon-or-bane` → collection `03_consent`
- **Access:** chief investigator only
- **Contents:** 18 signed consent forms, `GENAI_consent_P01..P18_signed.pdf`
- **Retention:** 5 years from publication, then destroyed (HREC condition 4.2)

A blank, unsigned version of the form is publishable and lives at
`05_additional_materials/information_sheets/GENAI_consent-form-blank_20260601_v02.md`.

**Do not commit signed forms here, even to a private repository.** A private GitHub
repository is not an approved storage location for identifiable UQ research data:
the data leaves Australian jurisdiction, access is controlled by individual GitHub
accounts rather than by UQ identity management, and Git history makes deletion
effectively irreversible — an accidental commit cannot simply be deleted, it has to
be purged from every clone.
