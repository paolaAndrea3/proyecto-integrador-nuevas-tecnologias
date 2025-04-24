import streamlit as st
# Importar bibliotecas
import pandas as pd
import numpy as np
from faker import Faker
import random
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")


st.subheader("Actividad 1: Practica de filtrado en Pandas (Google Colab)")   

st.link_button("Google Colab", "https://colab.research.google.com/drive/1T0VhaE8ZMRShSYLbfAlMxFEz3-PrQZwl?usp=sharing")