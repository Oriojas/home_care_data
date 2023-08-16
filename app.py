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

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.write(df)

st.markdown("* * *")
