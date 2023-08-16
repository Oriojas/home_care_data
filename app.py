import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Data Health Care",
                   page_icon="🏥",
                   layout="wide")

st.markdown("### **Paciente:** Juan Perez, **Documento:** 100000002")
st.markdown("#### Sin alarmas vigentes 👨🏽‍⚕️")
st.markdown("* * *")

with st.sidebar:
    st.markdown("# Bienvenidos a DHC 🏥")
    st.markdown("## Paciente")
    st.image("img/User-Profile-PNG.png")
    st.markdown("**Nombre:** Juan Perez")
    st.markdown("**Edad:** 49 años")
    st.markdown("**Documento:** 100000002")
    st.markdown("**Med. Tratante:** Dr. Julio Flores")
    st.warning('No olvidar verificar los datos del paciente', icon="⚠️")

with st.container():
    df = pd.read_csv("temp_data/temp_data.csv")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["date_c"], y=df["bpm"],
                             mode='lines',
                             name="bpm"))

    fig.add_trace(go.Scatter(x=df["date_c"], y=df["spo2"],
                             mode='lines',
                             name="spo2"))

    fig.update_layout(title='Ultimos datos pulsioximetría',
                      xaxis_title='Fecha',
                      yaxis_title='Valores')

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Información de los datos"):
        st.markdown("Esta información se genera según los datos que el paciente toma en su casa")

st.markdown("* * *")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Valores de BPM")
    col11, col12, col13 = st.columns(3)
    with col11:
        st.metric(label="Max",
                  value="70 BPM",
                  delta="1.2 BPM ")
    with col12:
        st.metric(label="MIN",
                  value="60 BPM",
                  delta="-1.2 BPM ")
    with col13:
        st.metric(label="PROM",
                  value="55 BPM",
                  delta="-1.2 BPM ")

with col2:
    st.markdown("### Valores de SPO2")
    col11, col12, col13 = st.columns(3)
    with col11:
        st.metric(label="Max",
                  value="95 SPO2",
                  delta="1.2 SPO2 ")
    with col12:
        st.metric(label="MIN",
                  value="90 SPO2",
                  delta="-1.2 SPO2 ")
    with col13:
        st.metric(label="PROM",
                  value="92 SPO2",
                  delta="-1.2 SPO2 ")
st.markdown("* * *")
