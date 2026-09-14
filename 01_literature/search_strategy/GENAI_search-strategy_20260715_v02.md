# Literature search strategy

Project `GENAI` · Version 02 · Searches run 10-15 July 2026 · Re-run due January 2027

## Research question

How do students and academic staff in higher education perceive the benefits and
risks of generative AI tools, and what factors explain whether they regard them as
predominantly beneficial ("boon") or harmful ("bane")?

## Concept blocks

| Block | Terms (OR within block) |
|---|---|
| A -- technology | "generative AI" OR "generative artificial intelligence" OR GenAI OR "large language model*" OR LLM OR ChatGPT OR "conversational agent*" |
| B -- setting | universit* OR "higher education" OR academic OR undergraduate OR postgraduate OR student* |
| C -- outcome | perception* OR attitude* OR adoption OR "academic integrity" OR ethic* OR trust OR "skill loss" OR deskilling |

Blocks combined as `A AND B AND C`.

## Databases and result counts

| Database | Interface | Date run | Query as entered | Results |
|---|---|---|---|---|
| Scopus | Elsevier | 2026-07-10 | `TITLE-ABS-KEY((A) AND (B) AND (C))` | 1,284 |
| Web of Science | Clarivate, Core Collection | 2026-07-10 | `TS=((A) AND (B) AND (C))` | 968 |
| ACM Digital Library | ACM | 2026-07-12 | Full text, `AllField` | 611 |
| IEEE Xplore | IEEE | 2026-07-12 | Metadata only | 342 |
| ERIC | ProQuest | 2026-07-14 | Descriptor + keyword | 287 |
| Google Scholar | -- | 2026-07-15 | First 100 results, grey-literature sweep only | 100 |

Total retrieved 3,592; 1,047 duplicates removed in Zotero; **2,545 unique records**
entered title/abstract screening.

## Limits applied

- Published 2022-11-30 onwards (public release of ChatGPT). Applied deliberately:
  earlier work on "AI in education" predates instruction-following models and does
  not address the phenomenon under study.
- English language only. Recorded as a limitation in the final report.
- Peer-reviewed journal articles, conference papers and books. Newspaper articles
  and institutional policy documents were captured separately as grey literature
  and are screened under a distinct set of criteria (see `../screening/`).

## Reproducibility notes

The exact strings above are stored verbatim so that a reader can reproduce the
counts. Where a database normalised the query on entry (Scopus expands `universit*`
differently from Web of Science) the string as the interface returned it was pasted
back into this file rather than the string as typed. Search alerts are active on
Scopus and Web of Science; new records arriving before submission are logged in
`../screening/` with a later screening date rather than being silently added.
