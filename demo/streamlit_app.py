import streamlit as st
import json

from app.core.agent import RevenueRecoveryAgent

st.set_page_config(page_title="Revenue Recovery AI Demo", layout="wide")

st.title("💰 Revenue Recovery AI – Interactive Demo")

uploaded_file = st.file_uploader("Upload CRM JSON", type=["json"])

agent = RevenueRecoveryAgent()

if uploaded_file:
    data = json.load(uploaded_file)

    st.subheader("Raw Input")
    st.json(data)

    if st.button("Run Analysis"):
        result = agent.run(data)

        st.subheader("Results")

        st.json(result)

        st.download_button(
            "Download CSV",
            data=result.get("csv", ""),
            file_name="revenue_recovery_report.csv",
            mime="text/csv"
        )
