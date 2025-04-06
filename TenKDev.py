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
tab1, tab2, tab3, tab4 = st.tabs(["💰 Cost Simulator", "📊 KPI Tracker", "🧪 Scenario Simulator", "🧭 Strategy Overview"])

# --- Tab 1: Cost Simulator ---
with tab1:
    st.header("💰 Cost Model Simulator")
    st.markdown("""
    Adjust the number of stores and discount rate to estimate the total program cost.
    """)

    store_count = st.slider("Number of Stores", 100, 5000, 1000, step=100)
    discount = st.selectbox("Discount Level", ["None", "30%", "40%", "55%"])

    discount_map = {"None": 0.00, "30%": 0.30, "40%": 0.40, "55%": 0.55}

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
            progress_text = [
                "Step 1/5: Incident Detected",
                "Step 2/5: Cisco AIOps Tools Engaged",
                "Step 3/5: Root Cause Identified",
                "Step 4/5: Remediation Triggered",
                "Step 5/5: Issue Resolved ✅"
            ][i-1]
            progress_bar.progress(i * 20, text=progress_text)

        st.success("🎉 Scenario Completed Successfully!")
        st.markdown("---")
        st.subheader("📊 Outcome")
        if scenario == "Checkout Latency Spike":
            st.write("- AppDynamics flagged latency > 4s")
            st.write("- Intersight auto-scaled checkout app")
            st.write("- Transaction time reduced from 5.2s to 2.3s")
            try:
                st.image("images/latency_spike_appd.png", caption="AppDynamics: Latency Spike in Checkout Flow")
            except Exception:
                st.warning("⚠️ Image failed to load. Please check file format and path.")
        elif scenario == "WAN Link Failure":
            st.write("- ThousandEyes detected outage")
            st.write("- SD-WAN rerouted traffic automatically")
            st.write("- No impact to store operations")
            try:
                st.image("images/wan_outage_path.png", caption="ThousandEyes: Path Outage Detected and Rerouted")
            except Exception:
                st.warning("⚠️ Image failed to load. Please check file format and path.")
        elif scenario == "Unauthorized IoT Device":
            st.write("- SecureX flagged unknown MAC address")
            st.write("- Device quarantined within 45 seconds")
            st.write("- No lateral movement detected")
            try:
                st.image("images/iot_securex_alert.png", caption="SecureX: IoT Device Quarantined")
            except Exception:
                st.warning("⚠️ Image failed to load. Please check file format and path.")

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

    try:
        with open("Strategy Concept.pptx", "rb") as f:
            st.download_button("📥 Download Full Strategy Deck", f, file_name="Cisco_Walmart_Strategy_Concept.pptx")
    except:
        st.warning("⚠️ Strategy deck not found. Upload 'Strategy Concept.pptx' to your app directory.")

st.markdown("---")
st.caption("Cisco Internal | Walmart Strategic Program Console")
