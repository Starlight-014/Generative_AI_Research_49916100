"""
00_generate_synthetic_data.py -- create the synthetic raw survey export.

This script exists only because the REIT6811 Applied Class 6 exercise needs a
realistic research repository without using real participant data. In a genuine
project this file would not exist: the raw export would come from the survey
platform and would never be generated.

Writes: ../data/raw/GENAI_survey-export_20260812_v01.csv

The seed is fixed so the file is reproducible. Five data-quality problems are
injected deliberately -- item non-response, a platform sentinel value, inconsistent
capitalisation, stray whitespace and a duplicate submission -- so that
01_clean_survey.py has something real to handle and the cleaning log is not empty.

Usage: python 00_generate_synthetic_data.py [output_path]
"""

from pathlib import Path
import csv, random, os, sys

random.seed(6811)
OUT = sys.argv[1] if len(sys.argv) > 1 else str(
    Path(__file__).resolve().parent.parent / "data" / "raw"
    / "GENAI_survey-export_20260812_v01.csv")

roles = ["Undergraduate"]*24 + ["Postgraduate (coursework)"]*14 + ["Postgraduate (research)"]*14 + ["Academic staff"]*8
disciplines = ["Engineering","Information Technology","Business","Health Sciences",
               "Humanities","Science","Education","Law"]
tools_pool = ["ChatGPT","Claude","Gemini","Copilot","Grammarly","DeepSeek"]

def lik(mu, lo=1, hi=5):
    v = round(random.gauss(mu, 1.05))
    return max(lo, min(hi, v))

rows = []
for i in range(1, 61):
    role = roles[i-1]
    disc = random.choice(disciplines)
    # heavier use among students than staff
    base = 4.0 if role.startswith("Under") else (3.6 if role.startswith("Postgraduate") else 2.7)
    freq = lik(base)
    ntools = 1 if freq <= 2 else random.choice([1, 2, 2, 3])
    tools = ";".join(sorted(random.sample(tools_pool, ntools)))
    # benefits scale with frequency of use
    ben_w = lik(1.6 + 0.62 * freq)
    ben_c = lik(1.3 + 0.60 * freq)
    # concerns are largely independent of use, accuracy concern is high across the board
    con_a = lik(3.9)
    con_i = lik(3.5)
    con_s = lik(3.4 + 0.10 * freq)
    trained = "Yes" if random.random() < (0.45 if role == "Academic staff" else 0.28) else "No"
    p_disc = 0.30 + 0.10 * (1 if trained == "Yes" else 0)
    disclosed = random.choices(["Always", "Sometimes", "Never"],
                               weights=[p_disc, 0.45, 0.55 - p_disc])[0]
    # stance: 1 = clearly a bane ... 5 = clearly a boon
    stance = lik(2.1 + 0.52 * ben_w - 0.28 * (con_a + con_i - 6) / 2)
    rows.append({
        "respondent_id": f"R{i:03d}",
        "role": role,
        "discipline": disc,
        "freq_use": freq,
        "tools_used": tools,
        "benefit_writing": ben_w,
        "benefit_coding": ben_c,
        "concern_accuracy": con_a,
        "concern_integrity": con_i,
        "concern_skill_loss": con_s,
        "training_received": trained,
        "disclosed_use": disclosed,
        "overall_stance": stance,
    })

# Inject the data-quality problems a raw export realistically contains, so that
# the cleaning script has something to do and the audit trail is visible.
rows[7]["freq_use"] = ""                 # item non-response
rows[18]["benefit_coding"] = "9"         # out-of-range sentinel for "not applicable"
rows[31]["role"] = "postgraduate (research)"   # inconsistent capitalisation
rows[44]["discipline"] = " Business "    # stray whitespace
rows.insert(45, dict(rows[44]))          # exact duplicate submission

hdr = list(rows[0].keys())
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=hdr)
    w.writeheader()
    w.writerows(rows)
print(f"wrote {OUT}: {len(rows)} rows (60 respondents + 1 duplicate)")
