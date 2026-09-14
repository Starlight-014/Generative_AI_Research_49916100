# Survey instrument (version 03)

Project `GENAI` · Approved under HREC 2026/GENAI/0417 · Administered 15 July - 12 August 2026
Platform: Qualtrics (UQ instance). Median completion time 6 minutes.

Version 03 is the administered version. Changes from v02 are listed at the foot of
this file; v01 and v02 are retained in Git history rather than as separate files.

---

## Section A. About you

**A1.** Which best describes your current role at the university?
Undergraduate student / Postgraduate student (coursework) / Postgraduate student
(research) / Academic staff
→ `role`

**A2.** Which faculty or broad discipline is your main affiliation?
Engineering / Information Technology / Business / Health Sciences / Humanities /
Science / Education / Law
→ `discipline`

## Section B. Use of generative AI tools

**B1.** In the past semester, how often have you used a generative AI tool for
university work?
1 Never · 2 Rarely (once or twice) · 3 Monthly · 4 Weekly · 5 Daily or near-daily
→ `freq_use`

**B2.** Which tools have you used? (select all that apply)
ChatGPT / Claude / Gemini / Copilot / Grammarly / DeepSeek / Other
→ `tools_used`, stored as a semicolon-separated string

## Section C. Perceived benefits

For each statement: 1 Strongly disagree · 2 Disagree · 3 Neither · 4 Agree ·
5 Strongly agree.

**C1.** Generative AI tools improve the quality of my written work. → `benefit_writing`
**C2.** Generative AI tools improve the quality of my code or technical work. → `benefit_coding`
(Respondents who do no technical work select "Not applicable", recorded as 9 and
recoded to missing during cleaning.)

## Section D. Perceived risks

Same 1-5 agreement scale.

**D1.** I am concerned that generative AI tools produce information that is factually
wrong. → `concern_accuracy`
**D2.** I am concerned that generative AI tools make academic misconduct harder to
prevent. → `concern_integrity`
**D3.** I am concerned that relying on generative AI tools will weaken my own skills.
→ `concern_skill_loss`

## Section E. Disclosure and training

**E1.** When you have used a generative AI tool in assessable work, have you disclosed
it as your course or school requires?
Always / Sometimes / Never / I have not used one in assessable work
→ `disclosed_use`

**E2.** Have you received any formal training or induction on the use of generative AI
in academic work? Yes / No
→ `training_received`

## Section F. Overall position

**F1.** Taking everything together, do you regard generative AI tools in higher
education as more of a benefit or more of a problem?
1 Clearly a problem · 2 · 3 Equally both · 4 · 5 Clearly a benefit
→ `overall_stance`

**F2.** *(open text, optional)* Is there anything else you would like to tell us about
your experience with these tools? → analysed with the qualitative strand

---

## Changes from version 02

| Item | Change | Reason |
|---|---|---|
| B1 | Scale points all labelled, not only the endpoints | Pilot respondents read "3" inconsistently |
| C2 | "Not applicable" option added | Pilot respondents in non-technical disciplines were forced to rate a task they never do |
| D2 | Reworded from "encourages cheating" to "makes academic misconduct harder to prevent" | Original wording was leading and conflated the tool with the user |
| E1 | Behaviour question added | The literature measures attitudes to disclosure but rarely the behaviour |
| F1 | Endpoint labels changed from "boon"/"bane" to plain English | Two pilot respondents did not know the word "bane" |
