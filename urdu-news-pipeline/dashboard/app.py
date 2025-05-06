import os
import streamlit as st
import sqlalchemy
import pandas as pd
import plotly.express as px

# 1) Load DB URL from env
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://affan:pass123@localhost:5432/news_db")

# 2) Create SQLAlchemy engine
engine = sqlalchemy.create_engine(DATABASE_URL)

# 3) Fetch some dummy rows
@st.cache_data
def load_data(limit=20):
    query = "SELECT * FROM predictions ORDER BY id DESC LIMIT %s"
    return pd.read_sql(query, engine, params=(limit,))

df = load_data()

# 4) Display table
st.title("📊 Urdu News Predictions Dashboard")
st.write("Here's the latest predictions:")
st.dataframe(df)

# 5) Simple bar chart of labels
label_counts = df["predicted_label"].value_counts().reset_index()
label_counts.columns = ["Label", "Count"]
fig = px.bar(label_counts, x="Label", y="Count", title="Prediction Label Distribution")
st.plotly_chart(fig)