
import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from firebase_admin import credentials, initialize_app, firestore
import firebase_admin
import json
import toml
import openpyxl
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

st.title("Actividad 5 - Archivo CSV")

df_csv = pd.read_csv("data.csv")
st.write("Datos desde CSV")
st.dataframe(df_csv)
st.write("Código que genera el Archivo CSV")
Code = """
df_csv = pd.read_csv("data.csv")
st.write("Datos desde CSV")
st.dataframe(df_csv)
""""" 
st.code(code, language='python')

st.title("Actividad 6 - Archivo Excel")
df_excel = pd.read_excel("data.xlsx")
st.write("Datos desde Excel")
st.dataframe(df_excel)
st.write("Código que genera el Archivo Excel")
code = """
df_excel = pd.read_excel("data.xlsx")
st.write("Datos desde Excel")
st.dataframe(df_excel)
"""
st.code(code, language='python')

st.title("Actividad 7 - Archivo JSON")
#creas un archivo llamado data.json y lo llamas con el suiguiente código
df_json = pd.read_json("data.json")
st.write("Datos de Usuarios desde JSON")
st.dataframe(df_json)
st.write("Código que genera el Archivo JSON")
code = """
#creas un archivo llamado data.json y lo llamas con el suiguiente código
df_json = pd.read_json("data.json")
st.write("Datos de Usuarios desde JSON")
st.dataframe(df_json)
"""
st.code(code, language='python')


st.title("Actividad 8 - URL")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"  # URL real de un archivo CSV
df_url = pd.read_csv(url)
st.dataframe(df_url)

st.header("Solución")
code="""
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"  # URL real de un archivo CSV
df_url = pd.read_csv(url)
st.dataframe(df_url)
"""
st.code(code, language='python')

st.title("Actividad 9 -Base de datos SQLite")

conn = sqlite3.connect("Estudiantes.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificacion INTEGER)")
conn.commit()
df_sqlite = pd.read_sql_query("SELECT * FROM Estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()
st.write("Código que genera la Base de datos SQLite")
code = """
import sqlite3  # Importar SQLite para trabajar con bases de datos

conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificacion INTEGER)")
cursor.execute("INSERT INTO estudiantes VALUES ('Tatiana', 4.5), ('Sebastian', 5), ('Marta', 3)")
conn.commit()
df_sqlite = pd.read_sql_query("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()
"""
st.code(code, language='python')

st.title("Actividad 10 - Array de NumPy")
array_numpy = np.array([
    [1, "Manzana", 2600],
    [2, "Pantalones", 45000],
    [3, "Galletas", 134]
])
df_numpy = pd.DataFrame(array_numpy, columns=["ID", "Producto", "Precio"])
st.write("Datos desde NumPy")
st.dataframe(df_numpy)
code = """
import numpy as np  # Importar NumPy para trabajar con arreglos

array_numpy = np.array([
    [1, "Manzana", 2600],
    [2, "Pantalones", 45000],
    [3, "Galletas", 134]
])
df_numpy = pd.DataFrame(array_numpy, columns=["ID", "Producto", "Precio"])
st.write("Datos desde NumPy")
st.dataframe(df_numpy)" \
"""
st.code(code, language='python')


st.title("Actividad 11 - Firebase")
def attrdict_to_dict(attrdict):
    """Convierte un objeto AttrDict a un diccionario Python estándar."""
    return dict(attrdict)

if not firebase_admin._apps:
    cred_toml = attrdict_to_dict(st.secrets["credentials"])
    cred_dict = toml.loads(toml.dumps(cred_toml))
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()
usuarios_ref = db.collection("usuarios")
usuarios = usuarios_ref.stream()
data = []
st.title("Usuarios de Firestore")

for usuario in usuarios:
    usuario_dict = usuario.to_dict()
    if "nombre" in usuario_dict and "edad" in usuario_dict: # Example of data validation.
        usuario_dict["ID"] = usuario.id
        data.append(usuario_dict)

df_firebase = pd.DataFrame(data)
st.write("Datos desde Firebase")
st.dataframe(df_firebase)


# Ejemplo: Agregar datos a Firestore

st.title("Agregar Nuevo Usuario")

nombre_nuevo = st.text_input("Nombre:")
edad_nueva = st.number_input("Edad:", min_value=0, step=1)

if st.button("Agregar Usuario"):
    if nombre_nuevo and edad_nueva >= 0:
        nuevo_usuario = {"nombre": nombre_nuevo, "edad": edad_nueva}
        db.collection("usuarios").add(nuevo_usuario)
        st.success("Usuario agregado correctamente.")
    else:
        st.warning("Por favor, ingresa un nombre y una edad válida.")