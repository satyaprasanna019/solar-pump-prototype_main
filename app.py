import streamlit as st
import time

# =========================
# Custom Inline CSS
# =========================
st.markdown(
    """
    <style>
    .card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-title {
        font-size: 16px;
        font-weight: 600;
        color: #374151;
    }
    .metric-value {
        font-size: 22px;
        font-weight: bold;
        color: #1e3a8a;
    }
    .big-metric {
        font-size: 48px;
        font-weight: bold;
        color: #1e40af;
    }
    .tag {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 13px;
        margin-top: 6px;
    }
    .tag-green {
        background-color: #dcfce7;
        color: #047857;
    }
    .tag-orange {
        background-color: #ffedd5;
        color: #c2410c;
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
    st.caption("Real-time water management and AI-powered insights")
    st.write("Last updated:", time.strftime("%B %d, %Y at %I:%M %p"))

    # --- AI Water Inflow Prediction ---
    st.subheader("AI Water Inflow Prediction")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="big-metric">2,847</div>
                <div>Gallons per minute (predicted)</div>
                <div class="tag tag-green">↑ 12% increase vs. last hour</div>
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

    # --- Pump Operations | Water Levels | System Status ---
    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown("### Pump Operations")
        st.toggle("Pump A-1 (1245 GPM)", value=True)
        st.toggle("Pump B-2 (987 GPM)", value=True)
        st.toggle("Pump C-3 (Maintenance)", value=False)

    with colB:
        st.markdown("### Water Levels")
        st.progress(78, text="Main Sump (24.5 ft depth)")
        st.progress(63, text="Secondary Sump (12.8 ft depth)")
        st.progress(11, text="Emergency Overflow (3.2 ft depth)")

    with colC:
        st.markdown("### System Status")
        st.markdown('<span class="metric-title">Overall Health</span>', unsafe_allow_html=True)
        st.markdown('<span class="tag tag-green">Optimal</span>', unsafe_allow_html=True)
        st.metric("Power Consumption", "847 kW")
        st.metric("Efficiency Rating", "94.2%")
        st.metric("Next Maintenance", "Oct 15, 2025")
        st.progress(92, text="Daily Performance")

    # --- Billing Summary ---
    st.markdown("### Billing Summary")
    st.caption("Current period water removal costs and projections")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="metric-value">$25,236</div>
                <div>Current Period</div>
                <div style="font-size:12px; color:gray;">Sep 1-21, 2025</div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="metric-value" style="color:#b45309;">$37,200</div>
                <div>Projected Monthly</div>
                <div style="font-size:12px; color:green;">↓ 8% under budget</div>
            </div>
            """, unsafe_allow_html=True)

    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="metric-value" style="color:#047857;">2.6M</div>
                <div>Gallons Processed</div>
                <div style="font-size:12px; color:gray;">This period</div>
            </div>
            """, unsafe_allow_html=True)

    with col4:
        st.markdown(
            """
            <div class="card">
                <div class="metric-value" style="color:#111827;">$0.0104</div>
                <div>Cost per Gallon</div>
                <div style="font-size:12px; color:green;">↓ 3% improvement</div>
            </div>
            """, unsafe_allow_html=True)

    billing_col1, billing_col2 = st.columns([1, 1])
    with billing_col1:
        period = st.selectbox("Billing Period:", ["Current Period", "Previous Period", "Year to Date"])
    with billing_col2:
        st.button("🔄 Refresh Data")

    # --- Quick Actions ---
    st.markdown("### Quick Actions")
    qa_col1, qa_col2, qa_col3 = st.columns(3)
    qa_col1.button("🌱 Carbon Credits")
    qa_col2.button("🔆 Solar Analytics")
    qa_col3.button("📄 Generate Report")

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
