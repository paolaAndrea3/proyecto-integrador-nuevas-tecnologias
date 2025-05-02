import streamlit as st
# Importar bibliotecas
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import date

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad se desarrolla una aplicación interactiva en Streamlit que permite aplicar filtros 
dinámicos a un conjunto de datos. Se utilizan diferentes técnicas de filtrado en Python y Pandas, 
controladas desde la barra lateral, para explorar la información de manera flexible e intuitiva.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
-Aplicar filtros dinámicos sobre datos con Pandas.

-Usar componentes interactivos en Streamlit.

-Reforzar el uso de estructuras de datos y operadores en Python.

-Desarrollar pensamiento lógico para el análisis de datos.
""")

st.header("Solución")


st.subheader("Actividad 1: Practica de filtrado en Pandas (Google Colab)")   

st.link_button("Google Colab", "https://colab.research.google.com/drive/1T0VhaE8ZMRShSYLbfAlMxFEz3-PrQZwl?usp=sharing")


#----------------------------------------------------------

# --- Configurar Faker para Colombia ---
fake = Faker('es_CO')
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# --- Crear datos falsos ---
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',
            'Cali', 'Quibdó', 'Buenaventura',
            'Villavicencio', 'Yopal',
            'Leticia', 'Puerto Inírida'
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

df_nuevo = pd.DataFrame(data)
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])



# --- INTERFAZ STREAMLIT ---
st.title("Filtros Dinámicos sobre Personas en Colombia")
st.sidebar.header("Configuración de Filtros")

# Copia para aplicar filtros
df_filtrado = df_nuevo.copy()

# 1. Filtro por rango de edad
if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (20, 50))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios
if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales',
        'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'
    ]
    seleccionados = st.sidebar.multiselect("Selecciona municipios", municipios)
    if seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(seleccionados)]

# 3. Filtro por ingreso mensual mínimo
if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mensual mínimo (COP)", 800000, 12000000, 1000000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_min]

# 4. Filtro por ocupación
if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
        'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
        'Emprendedor', 'Obrero'
    ]
    seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombres que contienen una cadena
if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Ingrese texto a buscar en nombre")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

# 7. Filtro por año de nacimiento
if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    anios = list(range(1949, 2010))
    anio = st.sidebar.selectbox("Selecciona el año", anios)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == anio]

# 8. Filtro por acceso a internet
if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("Acceso a internet", ["Sí", "No"])
    valor = True if acceso == "Sí" else False
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == valor]

# 9. Filtro por ingresos nulos
if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", value=date(1950, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha de fin", value=date(2005, 12, 31))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

# Mostrar resultados
st.subheader("Resultados filtrados")
st.dataframe(df_filtrado)

st.caption(f"Total de registros mostrados: {len(df_filtrado)}")

st.subheader("Codigo que genera el Dataframe y los filtros")
code = """

# --- Configurar Faker para Colombia ---
fake = Faker('es_CO')
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# --- Crear datos falsos ---
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',
            'Cali', 'Quibdó', 'Buenaventura',
            'Villavicencio', 'Yopal',
            'Leticia', 'Puerto Inírida'
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

df_nuevo = pd.DataFrame(data)
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])



# --- INTERFAZ STREAMLIT ---
st.title("Filtros Dinámicos sobre Personas en Colombia")
st.sidebar.header("Configuración de Filtros")

# Copia para aplicar filtros
df_filtrado = df_nuevo.copy()

# 1. Filtro por rango de edad
if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (20, 50))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios
if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales',
        'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'
    ]
    seleccionados = st.sidebar.multiselect("Selecciona municipios", municipios)
    if seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(seleccionados)]

# 3. Filtro por ingreso mensual mínimo
if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mensual mínimo (COP)", 800000, 12000000, 1000000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_min]

# 4. Filtro por ocupación
if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
        'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
        'Emprendedor', 'Obrero'
    ]
    seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombres que contienen una cadena
if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Ingrese texto a buscar en nombre")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

# 7. Filtro por año de nacimiento
if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    anios = list(range(1949, 2010))
    anio = st.sidebar.selectbox("Selecciona el año", anios)
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == anio]

# 8. Filtro por acceso a internet
if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("Acceso a internet", ["Sí", "No"])
    valor = True if acceso == "Sí" else False
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == valor]

# 9. Filtro por ingresos nulos
if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", value=date(1950, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha de fin", value=date(2005, 12, 31))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

# Mostrar resultados
st.subheader("Resultados filtrados")
st.dataframe(df_filtrado)

st.caption(f"Total de registros mostrados: {len(df_filtrado)}")

"""
st.code(code, language='python')