from pathlib import Path

import pandas as pd


project_root = Path(__file__).resolve().parents[2]
entities_path = project_root / "data" / "raw" / "entities.csv"

entities = pd.read_csv(entities_path)

required_columns = {
    "name",
    "type",
    "youtube_url",
    "instagram_url",
    "x_url",
}

missing_columns = required_columns - set(entities.columns)

if missing_columns:
    raise ValueError(f"Missing columns: {sorted(missing_columns)}")

if entities.empty:
    raise ValueError("The entity list is empty.")

print(f"Successfully loaded {len(entities)} entities.")
print(entities[["name", "type"]].to_string(index=False))