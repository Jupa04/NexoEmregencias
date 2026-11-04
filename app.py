"""Nexo Emergencias: mockup de la consola de coordinación, servido con Streamlit.

El diseño vive en mockup/index.html y los datos de prueba en mockup/datos.json.
Al cargar la página, app.py inserta los datos en la plantilla y la muestra a pantalla completa.
"""
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent / "mockup"
ALTO = 1180  # alto del área del mockup en píxeles; dentro de él la página hace scroll

st.set_page_config(
    page_title="Nexo Emergencias",
    page_icon="🛟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Quita los márgenes y la barra de Streamlit para que el mockup ocupe toda la ventana
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"] {display: none !important;}
      .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {padding: 0 !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      [data-testid="stElementContainer"]:has(style) {display: none;}
      iframe {display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def cargar_pagina() -> str:
    plantilla = (BASE / "index.html").read_text(encoding="utf-8")
    datos = json.loads((BASE / "datos.json").read_text(encoding="utf-8"))
    return plantilla.replace("__DATOS__", json.dumps(datos, ensure_ascii=False))


components.html(cargar_pagina(), height=ALTO, scrolling=True)
