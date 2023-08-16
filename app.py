import numpy as np
import streamlit as st

st.set_page_config(page_title="Data Health Care",
                   page_icon="🏥",
                   layout="wide")

st.markdown("# Bienvenidos a DHC 🏥")

with st.sidebar:
    st.markdown("## Paciente")
    st.image("img/User-Profile-PNG.png")
    st.markdown("**Nombre:** Juan Perez")
    st.markdown("**Edad:** 49 años")
    st.markdown("**Documento:** 100000002")
    st.markdown("**Med. Tratante:** Dr. Julio Flores")

with st.container():
    st.write("### Ultima medición pulsioximetría")
    st.bar_chart(np.random.randn(50, 3))

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






