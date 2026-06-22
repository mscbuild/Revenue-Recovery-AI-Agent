import streamlit as st
import requests
import json

API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="Revenue Recovery AI", layout="wide")

st.title("💰 Revenue Recovery AI Dashboard")

uploaded_file = st.file_uploader("Upload CRM JSON", type=["json"])

payload = None

if uploaded_file:
    try:
        payload = json.load(uploaded_file)

        st.subheader("Input Data")
        st.json(payload)

    except Exception as e:
        st.error(f"Invalid JSON file: {e}")

if payload:
    if st.button("Run Analysis"):

        try:
            with st.spinner("Calling AI backend..."):
                response = requests.post(
                    API_URL,
                    json=payload,
                    timeout=30
                )

            response.raise_for_status()

            result = response.json()

            st.success("Analysis complete!")

            # --- Risk Report ---
            st.subheader("Risk Report")
            st.json(result.get("risk_report", {}))

            # --- Priorities ---
            st.subheader("Priorities")
            st.json(result.get("priorities", []))

            # --- CSV Export ---
            csv_data = result.get("csv", "")

            st.subheader("CSV Export")

            st.text_area("CSV Output", csv_data, height=200)

            st.download_button(
                "Download CSV",
                data=csv_data,
                file_name="revenue_report.csv",
                mime="text/csv"
            )

        except requests.exceptions.Timeout:
            st.error("Backend timeout. Try again.")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to API. Is FastAPI running on port 8000?")

        except requests.exceptions.HTTPError as e:
            st.error(f"API error: {e.response.text}")

        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
