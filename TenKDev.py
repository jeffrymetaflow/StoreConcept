# walmart_cisco_streamlit_app.py

import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Walmart–Cisco Platform Console",
    layout="wide"
)

st.title("📊 Walmart–Cisco Platform Rollout Console")

# --- Cost Simulator Section ---
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

# --- Downloads ---
st.header("📂 Download Resources")
with open("charter.pdf", "rb") as f:
    st.download_button("Download Innovation Charter (PDF)", f, file_name="Walmart_Cisco_Charter.pdf")

with open("cost_model.xlsx", "rb") as f:
    st.download_button("Download Cost Model (Excel)", f, file_name="Walmart_Cisco_Cost_Model.xlsx")

# --- Footer ---
st.markdown("---")
st.caption("Cisco Internal | Walmart Strategic Program Console")
