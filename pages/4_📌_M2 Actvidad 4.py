
import streamlit as st
import pandas as pd
import numpy as np
import random
from faker import Faker

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad práctica, desarrollarás una aplicación web interactiva utilizando la librería Streamlit
 y la poderosa herramienta de manipulación de datos Pandas. El enfoque principal será el dominio de los 
métodos `.loc` e `.iloc` para realizar selecciones, filtrado y visualización de datos dentro de un DataFrame 
que contiene información sobre películas colombianas.A través de la creación de esta aplicación, explorarás cómo `.loc` permite
la selección de datos basada en etiquetas de filas y columnas, mientras que `.iloc` facilita la selección basada en índices
 enteros. Aprenderás a implementar controles interactivos en Streamlit que permitan a los usuarios experimentar con diferentes formas de
 consultar y explorar el conjunto de datos de películas, comprendiendo así la utilidad y la sintaxis de estos fundamentales métodos de Pandas.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Diferenciar y aplicar la selección de datos por etiquetas (`.loc`) y por posición (`.iloc`) en Pandas.
- Utilizar `.loc` para seleccionar datos por nombre y aplicar filtros.
- Utilizar `.iloc` para seleccionar datos por índice.
- Crear una aplicación Streamlit interactiva para explorar un DataFrame de películas con `.loc` e `.iloc`.
- Mostrar los resultados de las selecciones de datos en la aplicación Streamlit.
- Integrar Pandas y Streamlit para crear una interfaz de exploración de datos.
""")
import streamlit as st
import pandas as pd

# 1. Carga de datos (DataFrame de películas colombianas)
@st.cache_data
def cargar_datos():
    data = {
        'Título': ['La estrategia del caracol', 'El abrazo de la serpiente', 'Monos', 'Ciudad de perros', 'Los colores de la montaña',
                   'Sofía y el terco', 'La vendedora de rosas', 'El viaje', 'Paraíso Travel', 'Bolívar soy yo',
                   'Los viajes del viento', 'Gente de bien', 'Matar a Jesús', 'Climas', 'Memorias del calavero'],
        'Director': ['Sergio Cabrera', 'Ciro Guerra', 'Alejandro Landes', 'Tito Asorey', 'Carlos César Arbeláez',
                     'Andrés Burgos', 'Víctor Gaviria', 'Ernesto McCausland', 'Simón Brand', 'Jorge Alí Triana',
                     'Ciro Guerra', 'Franco Lolli', 'Laura Mora Ortega', 'Enrique Urbizu', 'Rubén Mendoza'],
        'Año': [1993, 2015, 2019, 2006, 2010,
                2012, 1998, 2001, 2008, 2002,
                2009, 2014, 2017, 2014, 2017],
        'Género': ['Comedia dramática', 'Aventura, Drama', 'Drama, Thriller', 'Drama', 'Drama',
                   'Drama, Comedia', 'Drama', 'Drama', 'Comedia, Drama', 'Comedia, Drama',
                   'Drama, Musical', 'Drama', 'Drama, Crimen', 'Drama', 'Comedia, Fantasía'],
        'Puntuación IMDB': [8.1, 7.8, 7.5, 7.2, 7.0,
                           6.8, 8.3, 7.1, 6.5, 6.9,
                           7.9, 7.3, 7.6, 6.7, 6.6]
    }
    df = pd.DataFrame(data)
    return df

df_peliculas_original = cargar_datos()

st.title('Explorador de Películas Colombianas')
st.subheader('Una aplicación interactiva con Streamlit y Pandas')

# 2. Sección para mostrar el DataFrame original
st.header('DataFrame Original de Películas')
st.dataframe(df_peliculas_original)

# 3. Sección para realizar selecciones con .loc
st.header('Selección de Películas (.loc)')

# Ejemplo 1: Selección por etiqueta (Título)
st.subheader('Seleccionar por Título')
titulo_seleccionado_loc = st.selectbox('Elige un título:', df_peliculas_original['Título'].unique())
if titulo_seleccionado_loc:
    pelicula_seleccionada = df_peliculas_original.loc[df_peliculas_original['Título'] == titulo_seleccionado_loc]
    st.write('Información de la película:')
    st.dataframe(pelicula_seleccionada)

# Ejemplo 2: Selección por múltiples criterios (Año y Puntuación)
st.subheader('Filtrar por Año y Puntuación')
año_filtro = st.slider('Selecciona un año mínimo:', df_peliculas_original['Año'].min(), df_peliculas_original['Año'].max(), df_peliculas_original['Año'].min())
puntuacion_minima = st.slider('Selecciona una puntuación mínima:', 0.0, 10.0, 7.0)
peliculas_filtradas_loc = df_peliculas_original.loc[(df_peliculas_original['Año'] >= año_filtro) & (df_peliculas_original['Puntuación IMDB'] >= puntuacion_minima)]
st.write(f'Películas estrenadas desde {año_filtro} con una puntuación mínima de {puntuacion_minima}:')
st.dataframe(peliculas_filtradas_loc)

# 4. Sección para realizar selecciones con .iloc
st.header('Selección de Películas (.iloc)')

# Ejemplo 3: Selección por rango de índices
st.subheader('Seleccionar por Rango de Índices')
indices_seleccionados = st.slider('Selecciona un rango de índices:', 0, len(df_peliculas_original) - 1, (0, 2))
inicio_indice, fin_indice = indices_seleccionados
peliculas_rango_iloc = df_peliculas_original.iloc[inicio_indice:fin_indice+1]
st.write(f'Películas en el rango de índices {inicio_indice} a {fin_indice}:')
st.dataframe(peliculas_rango_iloc)

# Ejemplo 4: Selección de filas y columnas específicas por índice
st.subheader('Seleccionar Filas y Columnas Específicas')
fila_indice = st.number_input('Índice de fila a mostrar:', 0, len(df_peliculas_original) - 1, 0)
columnas_indices = st.multiselect('Índices de columnas a mostrar:', range(len(df_peliculas_original.columns)), default=[0, 1])
if columnas_indices:
    columnas_seleccionadas = df_peliculas_original.columns[list(columnas_indices)].tolist()
    pelicula_iloc_especifica = df_peliculas_original.iloc[[fila_indice], df_peliculas_original.columns.get_indexer(columnas_seleccionadas)]
    st.write(f'Información de la película en el índice {fila_indice} y columnas con índices {columnas_indices}:')
    st.dataframe(pelicula_iloc_especifica)

st.sidebar.header('Opciones de Exploración')
st.sidebar.markdown('Utiliza los selectores y sliders para interactuar con los datos.')