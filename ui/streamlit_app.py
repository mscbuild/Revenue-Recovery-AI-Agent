import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="Revenue Recovery AI", layout="wide")

st.title("💰 Revenue Recovery AI Dashboard")

uploaded_file = st.file_uploader("Upload CRM JSON", type=["json"])

if uploaded_file:
    payload = json.load(uploaded_file)

    st.subheader("Input Data")
    st.json(payload)

    if st.button("Run Analysis"):

        with st.spinner("Calling AI backend..."):
            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.success("Analysis complete!")

            st.subheader("Risk Report")
            st.json(result.get("risk_report"))

            st.subheader("Priorities")
            st.json(result.get("priorities"))

            st.subheader("CSV Export")
            st.text_area("CSV Output", result.get("csv"))

            st.download_button(
                "Download CSV",
                data=result.get("csv"),
                file_name="revenue_report.csv",
                mime="text/csv"
            )

        else:
            st.error(f"Error: {response.text}")
