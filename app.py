import streamlit as st
import datetime
import os

# Load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def compute_prediction(weather_impact, geo_perm, season_factor):
    base = 2500
    return int(round(base * weather_impact * geo_perm * season_factor))

def main():
    st.set_page_config(page_title="Mining Operations Dashboard", layout="wide")

    # load CSS
    local_css(os.path.join("assets", "styles.css"))

    # header
    st.title("Mining Operations Dashboard")
    st.caption("Real-time water management and AI-powered dewatering insights")
    now = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")
    st.markdown(f"**Last updated:** {now}")

    st.markdown("---")

    # Prediction section
    st.subheader("AI Water Inflow Prediction")
    st.write("Machine learning analysis of mine water patterns.")

    # Inputs
    weather_impact = st.slider("Weather Impact Factor", 0.5, 2.0, 1.2, 0.1)
    geo_perm = st.slider("Geological Permeability", 0.5, 2.0, 0.9, 0.1)
    season = st.selectbox("Seasonal Adjustment", ["Wet Season (1.3x)", "Dry Season (0.8x)", "Normal (1.0x)"])

    if "Wet" in season:
        season_factor = 1.3
    elif "Dry" in season:
        season_factor = 0.8
    else:
        season_factor = 1.0

    # Prediction button
    if st.button("Update Prediction"):
        prediction = compute_prediction(weather_impact, geo_perm, season_factor)
    else:
        prediction = compute_prediction(weather_impact, geo_perm, season_factor)

    # Display card
    st.markdown(f'''
    <div class="card">
      <div class="metric-value">{prediction:,}</div>
      <div>Gallons per minute (predicted)</div>
      <div class="delta-green">↑ 12% vs last hour</div>
    </div>
    ''', unsafe_allow_html=True)

    # other cards
    cols = st.columns(3)
    titles = ["Pump Operations", "Water Levels", "System Status"]
    for col, title in zip(cols, titles):
        with col:
            st.markdown(f'<div class="card"><h3>{title}</h3></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
