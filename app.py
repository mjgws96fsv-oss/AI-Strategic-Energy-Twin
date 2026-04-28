import streamlit as st import pandas as pd import numpy as np
st. set_page_config(page_title="AI Digital Twin", layout="centered"') st. title("AI Digital Twin for Energy Optimization")
# Controles interactivos
temp = st. slider("Temperature (°C)", 0, 40, 20)
humidity = st.slider("Humidity (%)"
, 0, 100, 50)
# Simulación de la IA
pred = 200 + temp * 5 + humidity * 2
if pred > 400:
action = "Reduce HVAC usage by 15%"
optimized = pred * 0.85
elif pred > 250:
action = "Optimize lighting systems"
optimized = pred * 0.92
else:
action = "System efficient"
optimized = pred 
# Mostrar métricas
coll, col2, col3 = st. columns (3)
col1 metric("Predicted", f"{pred: .2f}")
col2.metric("Optimized", f"{optimized: .2f}")
co13 metric("Saving", f"{pred - optimized: .2f}")
st. write("**Recommended Action:**", action)
