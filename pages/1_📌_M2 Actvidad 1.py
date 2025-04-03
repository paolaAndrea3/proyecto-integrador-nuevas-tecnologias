import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad, exploraremos la creación y manipulación de DataFrames en Pandas, utilizando Streamlit para visualizar los datos en una interfaz web. Se trabajará con diferentes fuentes de datos, como diccionarios, listas, archivos CSV, JSON, bases de datos SQLite, entre otros.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender cómo crear DataFrames a partir de diversas estructuras de datos.
- Aprender a visualizar DataFrames en una aplicación web con Streamlit.
- Manejar diferentes fuentes de datos como archivos, bases de datos y APIs.
- Aplicar estos conocimientos en un entorno interactivo.
""")

st.header("Solución")


# Título y descripción en Streamlit
st.title("Actividad 1 - Diccionario con DataFrame")
libros = {
    "Título": ["Crónica de una muerte anunciada", "El hobbit", "Matar a un ruiseñor"],
    "Autor": ["Gabriel García Márquez", "J.R.R. Tolkien", "Harper Lee"],
    "Año de Publicación": [1981, 1937, 1960],
    "Género": ["Realismo mágico", "Fantasía", "Drama"]
}

df_libros = pd.DataFrame(libros)
st.write("DataFrame de Libros")
st.dataframe(df_libros)

st.write("Código que genera el DataFrame de libros:")
code="""" 
libros = {
"Título": ["Crónica de una muerte anunciada", "El hobbit", "Matar a un ruiseñor"],
"Autor": ["Gabriel García Márquez", "J.R.R. Tolkien", "Harper Lee"],
"Año de Publicación": [1981, 1937, 1960],
"Género": ["Realismo mágico", "Fantasía", "Drama"]
}

df_libros = pd.DataFrame(libros)
st.write("DataFrame de Libros")
st.dataframe(df_libros)
"""
st.code(code, language='python')

st.title("Actividad 2 - Lista de diccionarios")

Ciudades = [
    {"Nombre": "Medellin", "Poblacion": 2500000, "País": "Colombia"},
    {"Nombre": "Madrid", "Poblacion": 3200000, "País": "España"},
    {"Nombre": "Cartagena", "Poblacion": 1065881, "País": "Colombia"},
    {"Nombre": "Barranquilla", "Poblacion": 1320000, "País": "Colombia"},
]
df_Ciudades = pd.DataFrame(Ciudades)
st.write("DataFrame de Ciudades")
st.dataframe(df_Ciudades)
st.write("Código que genera el DataFrame de ciudades:")
code = """
Ciudades = [
    {"Nombre": "Medellin", "Poblacion": 2500000, "País": "Colombia"},
    {"Nombre": "Madrid", "Poblacion": 3200000, "País": "España"},
    {"Nombre": "Cartagena", "Poblacion": 1065881, "País": "Colombia"},
    {"Nombre": "Barranquilla", "Poblacion": 1320000, "País": "Colombia"},
]
df_Ciudades = pd.DataFrame(Ciudades)
st.write("DataFrame de Ciudades")
st.dataframe(df_Ciudades)
"""
st.code(code, language='python')

st.title("Actividad 3 - Lista de listas")
productos = [
    ["Manzana", 2600,100],
    ["Pantalones", 45000, 50],
    ["Galletas", 134,20],
    ["Arroz", 2300, 200],
]
df_Productos = pd.DataFrame(productos, columns=["Nombre", "Precio", "Stock"])
st.write("DataFrame de Productos")
st.dataframe(df_Productos)
st.write("Código que genera el DataFrame de productos:")
code = """
productos = [
    ["Manzana", 2600,100],
    ["Pantalones", 45000, 50],
    ["Galletas", 134,20],
    ["Arroz", 2300, 200],
]
df_Productos = pd.DataFrame(productos, columns=["Nombre", "Precio", "Stock"])
st.write("DataFrame de Productos")
st.dataframe(df_Productos)
"""
st.code(code, language='python')

st.title("Actividad 4 - Series")

nombres = pd.Series(["Rosa", "Omaira", "Paola", "Dario"])
edades = pd.Series([67, 48, 18, 70])
ciudades = pd.Series(["Medellin", "Medellin", "Medellin", "Medellin"])

datos_personas = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}
# Crear un DataFrame a partir del diccionario
df_personas = pd.DataFrame(datos_personas)
st.write("Datos de Personas")
st.dataframe(df_personas)

st.write("Código que genera el DataFrame de personas")
code = """" 

nombres = pd.Series(["Rosa", "Omaira", "Paola", "Dario"])
edades = pd.Series([67, 48, 18, 70])
ciudades = pd.Series(["Medellin", "Medellin", "Medellin", "Medellin"])

datos_personas = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}
# Crear un DataFrame a partir del diccionario
df_personas = pd.DataFrame(datos_personas)
st.write("Datos de Personas")
st.dataframe(df_personas)
"""
st.code(code, language='python')