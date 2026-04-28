import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="AI Strategic Energy Twin", layout="centered")

st.title("Strategic Energy Twin: AI-Driven Analytics")
st.write("---")

# Simulación de parámetros operativos
st.sidebar.header("Operational Parameters")
temp = st.sidebar.slider("Ambient Temperature (°C)", 10, 40, 24)
humidity = st.sidebar.slider("Relative Humidity (%)", 30, 90, 45)

# Lógica del Gemelo Digital (IA Prescriptiva)
predicted_load = 250 + (temp * 2.5) + (humidity * 0.2)
optimized_load = predicted_load * 0.88
savings = predicted_load - optimized_load

# Visualización de KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Predicted Load", f"{predicted_load:.1f} kWh")
col2.metric("Optimized Load", f"{optimized_load:.1f} kWh")
col3.metric("Cost Reduction", "12.0%")

st.info(f"**Strategic Insight:** System performance optimized. Operational overhead reduced by {savings:.1f} units.")

# Tu firma profesional
st.sidebar.markdown("---")
st.sidebar.write("### Author Details")
st.sidebar.info("Developed by **Mjgws96fsv**")
st.sidebar.caption("Specialist in AI & Digital Twin Strategic Solutions")
