# walmart_cisco_streamlit_app.py

import streamlit as st
import pandas as pd
import time
import pydeck as pdk

# Page Config
st.set_page_config(
    page_title="Walmart–Cisco Platform Console",
    layout="wide"
)

st.title("📊 Walmart–Cisco Platform Rollout Console")

# Tabs for multiple functions
tab1, tab2, tab3, tab4 = st.tabs(["💰 Cost Simulator", "📊 KPI Tracker", "🧪 Scenario Simulator", "🧭 Strategy Overview"])

# --- Tab 1: Cost Simulator ---
# [Cost Simulator code here — omitted for brevity]

# --- Tab 2: KPI Tracker ---
# [KPI Tracker code here — omitted for brevity]

# --- Tab 3: Scenario Simulator ---
# [Scenario Simulator code here — omitted for brevity]

# --- Tab 4: Strategy Overview ---
with tab4:
    st.header("🧭 Strategic Framework Overview")
    st.markdown("This section outlines the platform strategy for Cisco + Walmart innovation.")

    with st.expander("🌐 Modular Platform Architecture"):
        try:
            st.image("images/strategy_modularity.png", caption="Modular Architecture Across Domains")
        except:
            st.info("Upload 'strategy_modularity.png' to the images folder")
        st.write("The strategy is built on modular domains: network, security, edge, observability...")

    with st.expander("📈 Phased Rollout Model"):
        try:
            st.image("images/strategy_phased.png", caption="Phase 1 → Pilot | Phase 2 → Scale")
        except:
            st.info("Upload 'strategy_phased.png' to the images folder")
        st.write("From pilot deployment to full-scale rollout across 5,000 stores...")

    with st.expander("🔑 Success Metrics & Governance"):
        try:
            st.image("images/strategy_kpi.png", caption="Joint KPIs + Innovation Council")
        except:
            st.info("Upload 'strategy_kpi.png' to the images folder")
        st.write("Joint KPIs, co-governance council, and quarterly reviews ensure value realization.")

    with st.expander("📦 Materials Module List"):
        try:
            st.image("images/module_materials_list.png", caption="Component Breakdown by Module")
        except:
            st.info("Upload 'module_materials_list.png' to the images folder")
        st.write("This list outlines required hardware, licenses, and software by strategic domain.")

    with st.expander("🌍 Global Store Rollout Map"):
        st.markdown("This live map shows store deployment status across global locations.")
        # Sample store data
        data = pd.DataFrame([
            {"store": "New York", "lat": 40.7128, "lon": -74.0060, "status": "Implemented"},
            {"store": "London", "lat": 51.5074, "lon": -0.1278, "status": "In Progress"},
            {"store": "Tokyo", "lat": 35.6895, "lon": 139.6917, "status": "Not Implemented"},
            {"store": "Chicago", "lat": 41.8781, "lon": -87.6298, "status": "Implemented"},
            {"store": "Paris", "lat": 48.8566, "lon": 2.3522, "status": "In Progress"},
            {"store": "Delhi", "lat": 28.6139, "lon": 77.2090, "status": "Not Implemented"},
            {"store": "Los Angeles", "lat": 34.0522, "lon": -118.2437, "status": "Implemented"},
            {"store": "Berlin", "lat": 52.5200, "lon": 13.4050, "status": "In Progress"},
            {"store": "Shanghai", "lat": 31.2304, "lon": 121.4737, "status": "Not Implemented"},
            {"store": "São Paulo", "lat": -23.5505, "lon": -46.6333, "status": "Implemented"},
        ])

        status_colors = {
            "Implemented": [0, 200, 0],
            "In Progress": [255, 215, 0],
            "Not Implemented": [255, 0, 0]
        }
        data["color"] = data["status"].apply(lambda x: status_colors[x])

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=data,
            get_position='[lon, lat]',
            get_color='color',
            get_radius=80000,
            pickable=True
        )

        view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1.3)

        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=view_state,
            layers=[layer],
            tooltip={"text": "{store}: {status}"}
        ))

    try:
        with open("Strategy Concept.pptx", "rb") as f:
            st.download_button("📥 Download Full Strategy Deck", f, file_name="Cisco_Walmart_Strategy_Concept.pptx")
    except:
        st.warning("⚠️ Strategy deck not found. Upload 'Strategy Concept.pptx' to your app directory.")

st.markdown("---")
st.caption("Cisco Internal | Walmart Strategic Program Console")
