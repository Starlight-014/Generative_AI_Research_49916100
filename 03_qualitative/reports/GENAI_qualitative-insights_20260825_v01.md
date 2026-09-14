# Qualitative insights report

Project `GENAI` · Version 01 · 25 August 2026
Data: 18 de-identified transcripts (`../transcripts/deidentified/`, extract of 3 committed here)
Coding: `../coding/GENAI_codebook_20260810_v03.md`, matrix `../coding/GENAI_coding-matrix_20260812_v02.csv`

> Synthetic teaching data. See the note in the quantitative data dictionary.

## The question this strand was asked to answer

The survey found that perceived benefit and concern are statistically independent
(rho = 0.02, n = 60): people hold both at once, and the overall "boon or bane"
question is answered on benefit alone. The interviews were asked to explain how that
is possible. Three themes answer it.

## Theme 1. Verification is what makes the benefit safe, and expertise is what makes verification possible

Every participant who reported high benefit also reported a verification practice,
and the practices differ in a way that matters. P02 trusts the tool more for code than
for prose on entirely rational grounds: *"With code you do not have to trust it, you
just run it... If it is wrong about an essay, it is wrong confidently and you cannot
tell."* Code carries its own oracle; prose does not.

P03 states the general case from the other side: *"the filter is the expertise. If you
already know the answer it is a fast assistant. If you do not, it is a confident
stranger."* Six of twenty generated questions were usable, and the value of the tool
lay entirely in being able to tell which six.

This resolves the survey's puzzle. Benefit and concern are independent because they
are not opposed quantities: concern is about the output, and benefit is realised at
the point the user filters it. A participant with a working filter can rate both at 5
without contradiction. It also predicts where the arrangement fails — for users whose
filter is weakest, which is exactly the novice population the assessment debate is
about.

## Theme 2. The tool substitutes for an unavailable person, not only for effort

The strongest benefit accounts are not about speed. P01 does not use the generated
text at all — *"I almost never use the text. I use the reaction"* — and the reason is
supply: *"[SUPERVISOR] has maybe twenty minutes a fortnight for me."* P02's equivalent
is *"being available at 1am."*

This is why code `B2 Access to a responsive other` was split from `B1 Time and volume`
in codebook v03. The distinction has a practical consequence: if the benefit is
substituting for scarce human attention, then the institutional response that competes
with it is not a better detector but more contact time, and the participants who gain
most are those with least access to staff.

## Theme 3. The costs participants name are not the costs the institution debates

Academic integrity was raised, but rarely as the participant's own concern. P02
regards it as *"overblown for my course because our assessment is practical."* What
participants volunteered instead:

- **Capability erosion, reported in the first person.** P01: *"I think I have got
  worse at sitting with a bad paragraph... Now there is a button."* P02 noticed it
  in an offline exam. This maps onto the survey item `concern_skill_loss`, the second
  highest concern at 53.3% agreement, and the interviews show it is an observed
  change, not a hypothetical.
- **Privacy, raised only by staff.** P03 draws an absolute line at student data:
  *"That is a privacy line, not a quality one."* This is why `C4` was separated from
  `C2` in v03 — the two had been conflated, and they imply different policies.
- **Opacity of others' use** (`C6`). P03 on a colleague's peer review: *"I do not
  know, and I cannot ask."* This concerns the erosion of a professional trust relation
  rather than a rule, and no survey item captures it.
- **Governance inconsistency**, which was near-universal. P01: *"every course has its
  own version and they contradict each other."* P02 does not know whether finding a
  bug counts as content creation. P03 reports the same problem across publishers.
  Participants are not asking for permission; they are asking for one rule.

## What the two strands together support

1. The boon/bane framing should be retired as an analytic device and kept only as the
   public framing the study interrogates. Both strands show the dimensions are
   independent.
2. Verification capability is the variable that should be measured in wave 2, because
   it is what separates a participant for whom high concern and high benefit coexist
   from one for whom it does not.
3. The institutional recommendation with support from both strands is rule
   consistency, not rule severity. Only 30% of survey respondents had any training,
   and every interview raised inconsistency unprompted.

## Limits

Eighteen interviews, one institution, self-selected from the survey respondents who
volunteered for follow-up — which over-represents people willing to discuss their use.
Participants who use these tools and would not say so are absent from this strand by
construction, and that is the single largest gap in the study.
