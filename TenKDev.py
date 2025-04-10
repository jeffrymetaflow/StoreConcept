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
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["💰 Cost Simulator", "📊 KPI Tracker", "🧪 Scenario Simulator", "🧭 Strategy Overview", "🌍 Global Store Rollout Map", "💡 Cost Savings Tracker", "🔐 Cybersecurity Index"])

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

    if "kpi_data" not in st.session_state:
        st.session_state.kpi_data = []

    store_id = st.text_input("Store ID or Region:")
    uptime = st.slider("Network Uptime (%)", 90, 100, 99)
    latency = st.slider("Avg. Latency (ms)", 10, 200, 75)
    cx_score = st.slider("Customer Experience Index (1–10)", 1, 10, 8)

    def recommend_kpi_actions(row):
        recs = []
        if row["uptime"] < 95:
            recs.append("⚠️ Improve network reliability")
        if row["latency"] > 90:
            recs.append("🚀 Optimize app performance")
        if row["cx_score"] < 6:
            recs.append("📞 Investigate low CX feedback")
        return ", ".join(recs) if recs else "✅ No immediate action"

    if st.button("Add KPI Record"):
        new_row = {
            "store_id": store_id,
            "uptime": uptime,
            "latency": latency,
            "cx_score": cx_score
        }
        new_row["recommendation"] = recommend_kpi_actions(new_row)
        st.session_state.kpi_data.append(new_row)

    if st.session_state.kpi_data:
        df_kpi = pd.DataFrame(st.session_state.kpi_data)
        st.subheader("🔍 AI Recommendations")
        st.dataframe(df_kpi)

        st.subheader("📊 KPI Distribution Charts")
        st.bar_chart(df_kpi.set_index("store_id")["uptime"])
        st.bar_chart(df_kpi.set_index("store_id")["latency"])
        st.bar_chart(df_kpi.set_index("store_id")["cx_score"])

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
        st.image("images/strategy_modularity.png", caption="Modular Architecture Across Domains")
        st.write("The strategy is built on modular domains: network, security, edge, observability...")

    with st.expander("📈 Phased Rollout Model"):
        st.image("images/strategy_phased.png", caption="Phase 1 → Pilot | Phase 2 → Scale")
        st.write("From pilot deployment to full-scale rollout across 5,000 stores...")

    with st.expander("🔑 Success Metrics & Governance"):
        st.image("images/strategy_kpi.png", caption="Joint KPIs + Innovation Council")
        st.write("Joint KPIs, co-governance council, and quarterly reviews ensure value realization.")

    with st.expander("📦 Materials Module List"):
        st.image("images/module_materials_list.png", caption="Component Breakdown by Module")
        st.write("This list outlines required hardware, licenses, and software by strategic domain.")

    try:
        with open("Strategy Concept.pptx", "rb") as f:
            st.download_button("📥 Download Full Strategy Deck", f, file_name="Cisco_Walmart_Strategy_Concept.pptx")
    except:
        st.warning("⚠️ Strategy deck not found. Upload 'Strategy Concept.pptx' to your app directory.")

# --- Tab 5: Global Rollout Map ---
with tab5:
    st.header("🌍 Global Store Rollout Map")
    st.markdown("This live map shows store deployment status across global locations.")

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

st.markdown("---")
st.caption("Cisco Internal | Walmart Strategic Program Console")

# --- Tab 7: Cybersecurity Index ---
with tab7:
    st.header("🔐 Cybersecurity Maturity Index")
    st.markdown("Capability-based assessment from structured questionnaire responses.")

    try:
        df_questionnaire = pd.read_excel("cyber_index.xlsx", sheet_name="Client Questionnaire", skiprows=16)
        df_questionnaire = df_questionnaire.rename(columns={"Unnamed: 1": "Question", "Unnamed: 2": "Response"})
        df_questionnaire = df_questionnaire[["Question", "Response"]].dropna()

        # Define dynamic capability stage mapping
        capability_labels = ["Survival", "Measured", "Improving", "High Availability", "Optimized"]
        capability_size = len(df_questionnaire) // len(capability_labels)
        capability_map = []

        for label in capability_labels:
            capability_map += [label] * capability_size

        # Fill remaining rows
        capability_map += [capability_labels[-1]] * (len(df_questionnaire) - len(capability_map))
        df_questionnaire = df_questionnaire.copy()
        df_questionnaire["Capability Stage"] = capability_map
        df_questionnaire["Capability Stage"] = capability_map
        # Define function mapping based on number of questions
        functions = ["Identify", "Protect", "Detect", "Respond", "Recover", "CIS"]
        questions_per_function = len(df_questionnaire) // len(functions)
        function_map = []
        for idx in range(len(df_questionnaire)):
            function_idx = idx // questions_per_function
            function_map.append(functions[min(function_idx, len(functions) - 1)])
        df_questionnaire["Function"] = function_map

        st.subheader("📝 Interactive Questionnaire Editor")
        df_questionnaire["Response"] = df_questionnaire["Response"].fillna("NO").astype(str).str.upper()
        df_questionnaire["Question"] = df_questionnaire["Question"].fillna("Missing question text")

        for i in range(len(df_questionnaire)):
            question_label = f"{i+1}. {df_questionnaire.at[i, 'Question']}"
            current_response = str(df_questionnaire.at[i, 'Response']).strip().upper()
            if current_response not in ["YES", "NO"]:
                current_response = "NO"
            selected = st.radio(
                question_label,
                options=["YES", "NO"],
                index=0 if current_response == "YES" else 1,
                key=f"question_{i}"
            )
            df_questionnaire.at[i, 'Response'] = selected

        st.markdown("---")

        # Grouped stage-function summary
        stage_summary = df_questionnaire.groupby(["Function", "Capability Stage", "Response"]).size().unstack(fill_value=0)

        st.subheader("📊 Responses by Function & Capability Stage")
        st.dataframe(stage_summary)

        st.subheader("📈 YES Responses by Function")
        yes_summary = df_questionnaire[df_questionnaire["Response"] == "YES"].groupby("Function").size()
        st.bar_chart(yes_summary)

        st.subheader("📈 YES Responses by Capability Stage")
        stage_yes = df_questionnaire[df_questionnaire["Response"] == "YES"].groupby("Capability Stage").size()
        st.bar_chart(stage_yes)

        # Calculate maturity score per function
        st.subheader("📐 Maturity Score per Function")
        function_stage_weights = {"Survival": 1, "Measured": 2, "Improving": 3, "High Availability": 4, "Optimized": 5}
        df_questionnaire["Stage Weight"] = df_questionnaire["Capability Stage"].map(function_stage_weights)
        df_questionnaire["Score"] = df_questionnaire.apply(
            lambda row: row["Stage Weight"] if row["Response"] == "YES" else 0,
            axis=1
        )
    

        maturity_score = df_questionnaire.groupby("Function")["Score"].mean().round(2)
        import matplotlib.pyplot as plt

        # Color-coded bar chart for maturity scores
        st.subheader("🎨 Color-Coded Maturity Chart")
        fig, ax = plt.subplots()
        colors = []
        for score in maturity_score:
            if score <= 2:
                colors.append("red")
            elif score <= 3.5:
                colors.append("orange")
            else:
                colors.append("green")

        maturity_score.plot(kind='bar', color=colors, ax=ax)
        ax.set_ylabel("Average Score")
        ax.set_title("Maturity Score by Function")
        st.pyplot(fig)

        # Highlight dominant capability
        if not stage_yes.empty and stage_yes.sum() > 0:
            st.metric("🔐 Dominant Maturity Capability", stage_yes.idxmax())

    except Exception as e:
        st.warning(f"⚠️ Unable to load or analyze questionnaire data: {e}")

# --- Tab 6: Cost Savings Tracker ---
with tab6:
    st.header("💡 Cost Savings Tracker")
    st.markdown("Track cost savings progress store by store to support the $1B savings goal.")

    if "savings_data" not in st.session_state:
        st.session_state.savings_data = []

    savings_store = st.text_input("Store ID or Region (Savings Tab):")
    savings_amount = st.number_input("Estimated Savings for This Store ($)", min_value=0.0, step=1000.0)

    if st.button("Add Cost Savings Record"):
        st.session_state.savings_data.append({
            "store": savings_store,
            "savings": savings_amount
        })

    if st.session_state.savings_data:
        df_savings = pd.DataFrame(st.session_state.savings_data)
        total_savings = df_savings["savings"].sum()

        st.metric("💰 Cumulative Estimated Savings", f"${total_savings:,.0f}", help="Total across all stores")
        st.dataframe(df_savings)

        st.subheader("📊 Savings Distribution by Store")
        st.bar_chart(df_savings.set_index("store")['savings'])


        
