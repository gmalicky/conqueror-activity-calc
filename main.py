import pandas as pd
import streamlit as st


def clear_values():
    st.session_state.h = 0
    st.session_state.m = 0


df = pd.read_csv("conversion_chart.csv")
df = df.set_index("Physical Activity")

st.set_page_config("Conqueror Activity Calculator", "🏅")
# styles
styles = """
    <style>
    .st-emotion-cache-h4xjwg {height: 0rem;}
    .stAppToolbar {visibility: hidden;}
    div.block-container {padding-top: 0.5rem;}
    </style>
"""
st.html(styles)
st.image("img/logo.svg", use_container_width=True)
activity = st.selectbox("Select Activity", df.index, placeholder="Select an activity")
hours = st.number_input("Hours", min_value=0, max_value=23, key="h")
minutes = st.number_input("Minutes", min_value=0, max_value=59, key="m")

if st.button("Calculate `km`"):
    total_minutes = hours * 60 + minutes
    conversion_factor_10min = df.at[activity, "km/10min"]
    conversion_factor_1min = df.at[activity, "km/min"]

    km = (total_minutes // 10) * conversion_factor_10min + (
        total_minutes % 10
    ) * conversion_factor_1min

    st.code(f"{km:.2f}")
st.button("Clear", on_click=clear_values)
