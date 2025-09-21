import streamlit as st

st.set_page_config(page_title="Solar & Optimization")

st.title("Solar & Optimization")
st.write("☀️ Insights into solar energy savings and system optimization.")

# Example: efficiency metrics
st.metric("Solar Contribution", "35%", "+5% vs last month")
st.metric("Energy Cost Savings", "$4,200", "+8%")

# Example: chart
import pandas as pd
import numpy as np

days = pd.date_range("2025-09-01", periods=10)
data = pd.DataFrame({"Solar Output (kWh)": np.random.randint(200, 500, size=10)}, index=days)
st.line_chart(data)
