import pdfplumber
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

option = st.selectbox(
    'Selecciona el tipo de documento a analizar',
    ('imagen', 'pdf'))

st.write('You selected:', option)

if option == "pdf":
    uploaded_file = st.file_uploader('Sube un archivo .pdf', type="pdf")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            first_page = pdf.pages[0]
            st.write(first_page.chars[0])
else:
    uploaded_file = st.file_uploader("Sube una imagen 'png', 'jpeg', 'jpg'", type=['png', 'jpeg', 'jpg'])
    if uploaded_file is not None:
        st.image(uploaded_file)

st.markdown("* * *")
