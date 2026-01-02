import json
import pandas as pd
import re

INPUT_PATH = r"C:\Users\sonia\Desktop\acm_open_project\data\problems_data.jsonl"
OUTPUT_PATH = r"C:\Users\sonia\Desktop\acm_open_project\data\processed_data.csv"

rows = []

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)

        title = data.get("title", "")
        desc = data.get("description", "")
        inp = data.get("input_description", "")
        out = data.get("output_description", "")

        full_text = f"{title} {desc} {inp} {out}".lower()
        full_text = re.sub(r"[^a-z0-9\s]", " ", full_text)
        full_text = re.sub(r"\s+", " ", full_text).strip()

        rows.append({
            "text": full_text,
            "class": data["problem_class"],
            "score": data["problem_score"]
        })

df = pd.DataFrame(rows)
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Preprocessing completed")
print(df.head())
