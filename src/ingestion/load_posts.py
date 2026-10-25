from pathlib import Path

import pandas as pd


project_root = Path(__file__).resolve().parents[2]
posts_path = project_root / "data" / "raw" / "sample_posts.csv"

posts = pd.read_csv(posts_path)

required_columns = {
    "entity_name",
    "platform",
    "post_url",
    "published_at",
    "collected_at",
    "views",
    "likes",
    "comments",
    "shares",
}

missing_columns = required_columns - set(posts.columns)

if missing_columns:
    raise ValueError(f"Missing columns: {sorted(missing_columns)}")

if posts.empty:
    raise ValueError("The posts list is empty.")

print(f"Successfully loaded {len(posts)} posts.")
print(posts[["entity_name", "platform","views", "likes", "comments"]].to_string(index=False))