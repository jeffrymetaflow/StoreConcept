# walmart_cisco_streamlit_app.py

import streamlit as st
import pandas as pd
import time

# Page Config
st.set_page_config(
    page_title="Walmart–Cisco Platform Console",
    layout="wide"
)

st.title("📊 Walmart–Cisco Platform Rollout Console")

# Tabs for multiple functions
tab1, tab2, tab3 = st.tabs(["💰 Cost Simulator", "📊 KPI Tracker", "🧪 Scenario Simulator"])

# --- Tab 1: Cost Simulator ---
with tab1:
    st.header("💰 Cost Model Simulator")
    st.markdown("""
    Adjust the number of stores and discount rate to estimate the total program cost.
    """)

    store_count = st.slider("Number of Stores", 100, 5000, 1000, step=100)
    discount = st.selectbox("Discount Level", ["None", "30%", "40%", "55%"])

    discount_map = {"None": 0.00, "30%": 0.30, "40%": 0.40, "55%": 0.55}

    # Estimated base cost per module per store (list price)
    base_cost_per_store = {
        "Network Modernization": 7000,
        "Edge Compute + 5G": 45000,
        "Security & Zero Trust": 3800,
        "AIOps & Observability": 3000,
        "Cloud Integration": 1000,
        "Dev Enablement": 1000
    }

    def calculate_cost(store_count, discount_pct):
        breakdown = {}
        total = 0
        for module, cost in base_cost_per_store.items():
            module_total = store_count * cost
            discounted_total = module_total * (1 - discount_pct)
            breakdown[module] = discounted_total
            total += discounted_total
        return total, breakdown

    total_cost, module_breakdown = calculate_cost(store_count, discount_map[discount])

    st.subheader("📈 Estimated 3-Year Program Cost")
    st.metric("Total Cost", f"${total_cost:,.0f}", help="Includes all selected modules")

    # Module Breakdown Chart
    st.bar_chart(pd.Series(module_breakdown))

    st.header("📂 Download Resources")
    try:
        with open("charter.pdf", "rb") as f:
            st.download_button("Download Innovation Charter (PDF)", f, file_name="Walmart_Cisco_Charter.pdf")
    except FileNotFoundError:
        st.warning("⚠️ Charter PDF not found. Upload to GitHub or disable this feature.")

    try:
        with open("cost_model.xlsx", "rb") as f:
            st.download_button("Download Cost Model (Excel)", f, file_name="Walmart_Cisco_Cost_Model.xlsx")
    except FileNotFoundError:
        st.warning("⚠️ Cost model file not found. Upload to GitHub or disable this feature.")

# --- Tab 2: KPI Tracker ---
with tab2:
    st.header("📊 Pilot KPI Dashboard")
    st.markdown("Enter real or test data to simulate pilot rollout metrics.")

    store_id = st.text_input("Store ID or Region:")
    uptime = st.slider("Network Uptime (%)", 90, 100, 99)
    latency = st.slider("Avg. Latency (ms)", 10, 200, 75)
    cx_score = st.slider("Customer Experience Index (1–10)", 1, 10, 8)

    st.subheader("🧾 Summary:")
    st.write(f"**Store ID**: {store_id}")
    st.write(f"**Network Uptime**: {uptime}%")
    st.write(f"**Latency**: {latency} ms")
    st.write(f"**CX Score**: {cx_score}/10")

# --- Tab 3: Scenario Simulator ---
with tab3:
    st.header("🧪 Scenario Simulator")
    st.markdown("Simulate a real-world issue and how Cisco AIOps responds.")

    scenario = st.selectbox("Choose a Scenario", [
        "Checkout Latency Spike",
        "WAN Link Failure",
        "Unauthorized IoT Device"
    ])

    if st.button("Run Simulation"):
        st.subheader("🚦 Incident Simulation")

        progress_text = "⏳ Starting scenario simulation..."
        progress_bar = st.progress(0, text=progress_text)

        for i in range(1, 6):
            time.sleep(1)
            if i == 1:
                progress_text = f"Step {i}/5: Incident Detected"
            elif i == 2:
                progress_text = f"Step {i}/5: Cisco AIOps Tools Engaged"
            elif i == 3:
                progress_text = f"Step {i}/5: Root Cause Identified"
            elif i == 4:
                progress_text = f"Step {i}/5: Remediation Triggered"
            else:
                progress_text = f"Step {i}/5: Issue Resolved ✅"
            progress_bar.progress(i * 20, text=progress_text)

        st.success("🎉 Scenario Completed Successfully!")

        st.markdown("---")
        st.subheader("📊 Outcome")
        if scenario == "Checkout Latency Spike":
            st.write("- AppDynamics flagged latency > 4s")
            st.write("- Intersight auto-scaled checkout app")
            st.write("- Transaction time reduced from 5.2s to 2.3s")
            st.image("images/latency_spike_appd.png", caption="AppDynamics: Latency Spike in Checkout Flow")
        elif scenario == "WAN Link Failure":
            st.write("- ThousandEyes detected outage")
            st.write("- SD-WAN rerouted traffic automatically")
            st.write("- No impact to store operations")
            st.image("images/wan_outage_path.png", caption="ThousandEyes: Path Outage Detected and Rerouted")
        elif scenario == "Unauthorized IoT Device":
            st.write("- SecureX flagged unknown MAC address")
            st.write("- Device quarantined within 45 seconds")
            st.write("- No lateral movement detected")
            st.image("images/iot_securex_alert.png", caption="SecureX: IoT Device Quarantined")

st.markdown("---")
st.caption("Cisco Internal | Walmart Strategic Program Console")

