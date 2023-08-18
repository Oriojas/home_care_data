import os
import json
import base64
import requests
import pdfplumber
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="HealthVault",
                   page_icon="🏥",
                   layout="wide")


def load_image(image_f):
    img_f = Image.open(image_f)
    return img_f


st.markdown("### Sin alarmas vigentes 👨🏽‍⚕️")
st.markdown("* * *")
st.image("img/Recurso 1.png")
st.write("")
st.image("img/WhatsApp Image 2023-08-18 at 10.08.46 AM.jpeg")
st.markdown("* * *")

with st.sidebar:
    st.markdown("# Bienvenidos HealthVault 🏥")
    st.image("img/man.png")
    st.markdown("**Nombre:** Julio")
    st.markdown("**Apellidos:** del Padro Padilla")
    st.markdown("**Edad:** 28 años")
    st.markdown("**Peso:** 62 kg")
    st.markdown("**Altura:** 165 cm")
    st.image("img/Recurso 18.png")

    st.warning('Recuerda que para facilitar la gestión y procesamiento de'
               ' tu información, requerimos que compartas tus datos', icon="⚠️")

option = st.selectbox(
    'Selecciona el tipo de documento a analizar',
    ('imagen', 'pdf'))

st.write('Selección:', option)

if option == "pdf":
    uploaded_file = st.file_uploader('Sube un archivo .pdf', type="pdf")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            first_page = pdf.pages[0]
            st.write(first_page.chars[0])
else:
    image_file = st.file_uploader("Sube una imagen 'png', 'jpeg', 'jpg'", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        file_details = {"FileName": image_file.name, "FileType": image_file.type}
        # st.write(file_details)
        img = load_image(image_file)
        st.image(img)
        name = os.path.join("temp_data", image_file.name)
        with open(name, "wb") as f:
            f.write(image_file.getbuffer())
        st.success("Saved File")

        if st.button("Procesar"):
            with open(name, 'rb') as f:
                image = f.read()

            encoded_bytes = base64.b64encode(image)
            encoded_string = encoded_bytes.decode('utf-8')

            with open('temp_data/python-encoded.txt', 'w') as f:
                f.write(encoded_string)

            st.markdown("* * *")

            with open('data.json') as file:
                data = json.load(file)

                tratamiento = data.get("consulta").get("tratamiento")

                diagnostico = data.get("consulta").get("diagnostico")
                st.markdown("#### Diagnostico:")
                st.markdown(f"{diagnostico}")

                st.markdown("#### Tratamiento:")
                for i in range(len(tratamiento)):
                    if tratamiento[i].get("medicamento"):
                        st.write(tratamiento[i].get("medicamento"))
                        st.write(tratamiento[i].get("instrucciones"))

            with st.expander("Ver detalle documento"):
                st.write(data)

st.markdown("* * *")
