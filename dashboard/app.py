
import streamlit as st
import requests

st.set_page_config(
    page_title="Central Bank AI",
    page_icon="🏦",
    layout="wide"
)

st.title("CENTRAL BANK AI")
st.subheader(
    "Monetary Policy & Financial Stability Simulator"
)

st.warning(
    "Research prototype. Outputs are not official "
    "monetary policy recommendations."
)

st.sidebar.header("Forecast Configuration")

variable = st.sidebar.selectbox(
    "Economic Variable",
    ["inflation", "gdp_growth", "unemployment"]
)

horizon = st.sidebar.slider(
    "Forecast Horizon",
    min_value=1,
    max_value=12,
    value=4
)

raw_values = st.text_area(
    "Enter historical observations (comma separated)",
    "4.2, 4.5, 4.1, 3.9, 4.0, 4.3, 4.1, 3.8, 4.0, 4.2, 4.1, 4.3"
)

if st.button("Generate Forecast"):

    try:
        series = [
            float(value.strip())
            for value in raw_values.split(",")
        ]

        response = requests.post(
            "http://127.0.0.1:8000/api/v1/forecast",
            json={
                "series": series,
                "horizon": horizon,
                "variable_name": variable
            },
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        st.success("Forecast generated")

        st.metric(
            "Latest Forecast",
            result["predictions"][-1]
        )

        st.write("Forecast Results")

        st.line_chart(
            result["predictions"]
        )

        st.json(result)

    except ValueError:
        st.error("Enter valid numeric observations.")

    except requests.RequestException as error:
        st.error(f"API connection failed: {error}")
