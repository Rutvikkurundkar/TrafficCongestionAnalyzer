import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Traffic Congestion Analyzer", layout="wide")

st.title("🚦 Traffic Congestion Analyzer")
st.markdown("### Real-time Traffic Analysis using PySpark + Streamlit")

# Display generated plots
figures = [
    ("Hourly Trend", "outputs/figures/hourly_trend.png"),
    ("Day of Week Trend", "outputs/figures/daily_trend.png"),
    ("Monthly Trend", "outputs/figures/monthly_trend.png")
]

for title, path in figures:
    if os.path.exists(path):
        st.subheader(title)
        st.image(Image.open(path), use_container_width=True)
    else:
        st.warning(f"⚠️ {title} not found. Run main.py first to generate it.")

st.markdown("---")
st.markdown("✅ Built By Rutvik")
