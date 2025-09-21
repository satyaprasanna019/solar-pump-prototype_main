import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------
# Page config
# -------------------
st.set_page_config(page_title="Operations Command Center", layout="wide")

st.title("🚀 Operations Command Center Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
date_filter = st.sidebar.date_input("Select Date Range")
category_filter = st.sidebar.selectbox("Category", ["All", "Solar", "Wind", "Hydro"])

# Dummy Data (replace with your own)
data = {
    "Category": ["Solar", "Wind", "Hydro", "Solar", "Wind"],
    "Value": [40, 30, 20, 50, 35],
    "Region": ["North", "South", "East", "West", "Central"]
}
df = pd.DataFrame(data)

# Filtered Data
if category_filter != "All":
    df = df[df["Category"] == category_filter]

# -------------------
# Layout
# -------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Category Distribution")
    fig1 = px.pie(df, names="Category", values="Value", title="Energy Breakdown")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🌍 Regional Analysis")
    fig2 = px.bar(df, x="Region", y="Value", color="Category", title="Region-Wise Performance")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 Detailed Data")
st.dataframe(df, use_container_width=True)
