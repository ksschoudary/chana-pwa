import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Configuration (Helvetica style)
st.set_page_config(page_title="Chana Intel", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="st-"] {
        font-family: 'Helvetica', 'Arial', sans-serif;
    }
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #5D4037;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header & Refresh
col_t, col_r = st.columns([4, 1])
with col_t:
    st.markdown('<p class="main-header">🌾 Chana Crop Intelligence Report</p>', unsafe_allow_html=True)
    st.caption(f"**Date:** {datetime.now().strftime('%B %d, %Y')} | **Scheduled Update:** 10:30 AM")
with col_r:
    if st.button("🔄 Refresh Now"):
        st.rerun()

# --- SECTION 1: PRICE TRACKER ---
st.header("📈 NCDEX Spot Price Tracker (Chana)")
st.write("Chana prices are seeing a bullish push this morning. Bikaner has gained significantly as the market reacts to the 'Short Spring' forecasts and potential yield hits in Central India.")

price_data = {
    "Location": ["Bikaner", "Delhi", "Akola"],
    "Today (₹/Q)": [5575.00, 5745.60, 5400.00],
    "Yesterday (₹/Q)": [5500.00, 5702.10, 5437.50],
    "% Change": ["+1.36%", "+0.76%", "-0.69%"],
    "Market Status": ["🟩 Strong Gain", "🟩 Firming Up", "🟦 Softening"]
}
st.table(pd.DataFrame(price_data))

# --- SECTION 2: WEATHER ANALYSIS ---
st.header("🌡️ Temperature & Weather Analysis")
st.write("Data from the IMD City Reports confirms a sharp rise in both day and night temperatures, tracking 3–5°C above normal in the rabi heartland.")

weather_data = {
    "Metric": ["Max Temp (Today)", "Min Temp (Today)", "Rainfall Outlook"],
    "Bikaner (Rajasthan)": ["31.0°C", "16.5°C (+3.7°C)", "Nil; Deficit"],
    "Sehore (MP)": ["33.0°C", "16.8°C (+2.5°C)", "Dry; Drought risk"]
}
st.table(pd.DataFrame(weather_data))

col_w1, col_w2 = st.columns(2)
with col_w1:
    st.info("**Bikaner:** Max temps hitting 32°C. Absence of winter rain is creating low-humidity (RH 28%), accelerating moisture loss.")
with col_w2:
    st.info("**Sehore:** Terminal heat is the primary concern. Temperatures breaching 32°C critical threshold, impacting grain-filling.")

# --- SECTION 3: CROP FRONT ---
st.header("🧬 Phenology & Crop Front Update")
st.write("The crop is currently in the **Reproductive to early Grain Filling** stage.")

st.markdown("#### ⚠️ Terminal Heat Stress")
st.write("According to ICAR-CRIDA, 'forced maturity' is active. Night temps >16°C prevent recovery, leading to a 10–12% reduction in seed weight.")

st.markdown("#### ⚠️ Forced Ripening")
st.write("In Sehore, crops are maturing **7–10 days ahead** of schedule. While this leads to early arrivals, it results in shriveled grains.")

# --- SECTION 4: ADVISORY ---
st.header("🩺 Agromet Advisory (Next 24-48 Hours)")
st.success("**Irrigation Intervention:** Light irrigation recommended to lower canopy temperature. Avoid over-watering to prevent root rot.")
st.warning("**Heat Mitigation:** Foliar spray of Potassium Nitrate (13-0-45) @ 1% to help the plant tolerate heat and improve grain quality.")
st.error("**Pest Monitoring:** Ideal weather for Pod Borer. Spray Indoxacarb if 1-2 larvae per meter row are found.")

st.divider()
st.caption("Data Sources: NCDEX, IMD, ICAR-CRIDA, AgPulse Analytica")
