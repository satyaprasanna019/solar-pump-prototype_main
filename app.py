import streamlit as st
import numpy as np
import time

# =========================
# Custom Inline CSS
# =========================
st.markdown(
    """
    <style>
    .card {
        background-color: #eff6ff;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 48px;
        font-weight: bold;
        color: #1e40af;
    }
    .delta-green {
        color: #047857;
        background-color: #dcfce7;
        padding: 4px 8px;
        border-radius: 999px;
        font-size: 14px;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Sidebar Navigation
# =========================
st.sidebar.title("DAAS Dashboard")
page = st.sidebar.radio("Navigation", ["Dashboard", "Billing & Credits", "Solar & Optimization"])

# =========================
# Dashboard Page
# =========================
if page == "Dashboard":
    st.title("Mining Operations Dashboard")
    st.caption("Real-time water management and AI-powered dewatering insights")
    st.write("Last updated:", time.strftime("%B %d, %Y at %I:%M %p"))

    st.subheader("AI Water Inflow Prediction")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="metric-value">2,847</div>
                <div>Gallons per minute (predicted)</div>
                <div class="delta-green">↑ 12% increase vs. last hour</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        weather = st.slider("Weather Impact Factor", 0.5, 2.0, 1.2)
        geo = st.slider("Geological Permeability", 0.5, 2.0, 0.9)
        season = st.selectbox("Seasonal Adjustment", ["Dry Season (0.7x)", "Normal (1.0x)", "Wet Season (1.3x)"])
        if st.button("Update Prediction"):
            st.success("Prediction updated with new parameters!")

    st.subheader("Pump Operations")
    st.progress(70)

    st.subheader("Water Levels")
    st.metric("Reservoir Level", "65%", "↓ 5% vs. last day")

    st.subheader("System Status")
    st.success("All systems operational ✅")

# =========================
# Billing & Credits Page
# =========================
elif page == "Billing & Credits":
    st.title("Billing & Credits")
    st.info("Here you can manage billing, usage credits, and subscription details.")
    st.metric("Current Balance", "$120")
    st.metric("Credits Remaining", "450 kWh")

# =========================
# Solar & Optimization Page
# =========================
elif page == "Solar & Optimization":
    st.title("Solar & Optimization")
    st.info("AI-driven solar power optimization and energy efficiency insights.")
    st.metric("Solar Power Generated", "1,250 kWh", "+8% vs. last week")
    st.metric("Optimization Savings", "$340", "+12% vs. last month")
