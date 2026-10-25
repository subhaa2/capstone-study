from pathlib import Path

import pandas as pd
import streamlit as st

project_root = Path(__file__).resolve().parents[1]
posts = pd.read_csv(project_root / "data/raw/sample_posts.csv")

st.title("Social Media Engagement Dashboard")

brand = st.selectbox("Choose a brand or event", posts["entity_name"].unique())
filtered = posts[posts["entity_name"] == brand]

views, likes, comments = st.columns(3)

views.metric("Views", f"{filtered['views'].sum():,.0f}")
likes.metric("Likes", f"{filtered['likes'].sum():,.0f}")
comments.metric("Comments", f"{filtered['comments'].sum():,.0f}")

st.subheader("Posts")
st.dataframe(filtered, use_container_width=True)