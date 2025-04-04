import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime

# Database connection
def get_data():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="airflow",
        user="airflow",
        password="airflow"
    )
    query = "SELECT * FROM reddit_posts ORDER BY created_utc DESC LIMIT 100;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit UI
st.set_page_config(page_title="Reddit Dashboard", layout="wide")

st.title("📊 Reddit Post Dashboard")

df = get_data()

# Convert timestamp
df["created_utc"] = pd.to_datetime(df["created_utc"], unit='s')

# Sidebar filter
selected_subreddit = st.sidebar.multiselect("Select author", options=df["author"].unique(), default=df["author"].unique())
filtered_df = df[df["author"].isin(selected_subreddit)]

# Show table
st.subheader("Latest Posts")
st.dataframe(filtered_df[["title", "created_utc", "author"]])

# Basic bar chart
st.subheader("📈 Post Count by Subreddit")
post_count = filtered_df["author"].value_counts()
st.bar_chart(post_count)
