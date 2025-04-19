import streamlit as st
import pandas as pd
import io
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad tiene como objetivo introducir a los estudiantes en el análisis y visualización de datos utilizando Python, las 
bibliotecas Pandas y Streamlit. A través de la carga y manipulación de un conjunto de datos de estudiantes colombianos.

""")

st.header("Objetivos de aprendizaje")

st.markdown("""
-Cargar y visualizar datos desde archivos CSV.

-Explorar y resumir datos utilizando métodos como .head(), .tail(), .info() y .describe().

-Seleccionar y filtrar columnas específicas del DataFrame.

-Aplicar filtros interactivos basados en criterios definidos por el usuario, como el promedio de calificaciones.
""")

st.header("Solución")
# Cargar el archivo CSV y mostrarlo como un DataFrame
df = pd.read_csv("estudiantes_colombia.csv")
st.dataframe(df)

st.markdown('<p style="font-size:16px; font-weight:bold;">Código que genera el Archivo CSV</p>', unsafe_allow_html=True)

code="""
df = pd.read_csv("estudiantes_colombia.csv")
st.dataframe(df)

# Si no sabes como crear un archivo CSV, aquí tienes un ejemplo:
#📄 Paso 1: Crear un archivo CSV en excel con datos de ejemplo
Primero, creamos un archivo CSV llamado estudiantes_colombia.csv que 
contiene información de estudiantes. Este archivo debe tener un formato similar al siguiente:

id,nombre,edad,ciudad,promedio,asistencia
1,Juan Pérez,17,Bogotá,4.5,0.95
2,María Gómez,16,Medellín,3.8,0.88
3,Carlos López,18,Cali,4.2,0.92
4,Ana Martínez,15,Barranquilla,3.5,0.85
5,Pedro Sánchez,19,Cartagena,4.8,0.97
Luego lo guardas como archivo CSV y lo agregas a la raiz del proyecto 
"""
st.code(code, language='python')
#Mostrar las primeras y últimas 5 filas del DataFrame
st.title("Primeras 5 filas del DataFrame")
st.dataframe(df.head())

#Mostrar las últimas 5 filas del DataFrame
st.title("Últimas 5 filas del DataFrame")
st.dataframe(df.tail())

st.markdown('<p style="font-size:16px; font-weight:bold;">Código que muestras las primeras y últimas 5 filas del DataFrame</p>', unsafe_allow_html=True)

code="""
st.title("Primeras 5 filas del DataFrame")
st.dataframe(df.head())
st.write("Últimas 5 filas del DataFrame")
st.dataframe(df.tail())
"""
st.code(code, language='python')

# Se muestra Resumen general del DataFrame con .info()

st.title("Información general del DataFrame con .info()")
buffer = io.StringIO()
df.info(buf=buffer)
info_string = buffer.getvalue()

st.write("Información del dataset:")
st.text(info_string)

st.markdown('<p style="font-size:16px; font-weight:bold;">Código que muestra Resumen general del DataFrame con .info()</p>', unsafe_allow_html=True)
code="""
st.title("Información general del DataFrame")
buffer = io.StringIO()
df.info(buf=buffer)
info_string = buffer.getvalue()

st.write("Información del dataset:")
st.text(info_string)
"""
st.code(code, language='python')


# Se muestra Resumen general del DataFrame con describe().
st.title("Se muestra Resumen general del DataFrame con describe()")
st.dataframe(df.describe())
st.markdown('<p style="font-size:16px; font-weight:bold;">Código que muestra Resumen general del DataFrame con describe().</p>', unsafe_allow_html=True)
code="""
st.dataframe(df.describe())
"""
st.code(code, language='python')


#--- Seleccionar columnas específicas (ej. "nombre", "edad", "promedio") para mostrarlas.
st.title("Seleccionar columnas específicas.")
st.subheader("Seleccionar columnas para mostrar")
# Obtenemos la lista de todas las columnas de todo el datset.
columnas= df.columns.to_list()

# Usamos un widget de Streamlit llamado multiselect para que el usuario pueda
# elegir qué columnas quiere ver.
columnas_seleccionadas = st.multiselect("Seleccionamos las columnas que queremos ver:", columnas, default=["nombre", "edad", "promedio"])

# Si el usuario selecciona alguna columna, las mostramos.
if columnas_seleccionadas:
    st.write("Columnas seleccionadas:")
    st.dataframe(df[columnas_seleccionadas])
else:
    st.info("Por favor seleccionar almenos una columna para mostrar.")

st.markdown('<p style="font-size:16px; font-weight:bold;">Código para crear la parte de seleccionar almenos una o varial columnas para mostrar</p>', unsafe_allow_html=True)
code="""
st.title("Seleccionar columnas específicas.")
st.subheader("Seleccionar columnas para mostrar")
# Obtenemos la lista de todas las columnas de todo el datset.
columnas= df.columns.to_list()

# Usamos un widget de Streamlit llamado multiselect para que el usuario pueda
# elegir qué columnas quiere ver.
columnas_seleccionadas = st.multiselect("Seleccionamos las columnas que queremos ver:", columnas, default=["nombre", "edad", "promedio"])

# Si el usuario selecciona alguna columna, las mostramos.
if columnas_seleccionadas:
    st.write("Columnas seleccionadas:")
    st.dataframe(df[columnas_seleccionadas])
else:
    st.info("Por favor seleccionar almenos una columna para mostrar.")
"""
st.code(code, language='python')


#Filtrar estudiantes por promedio
st.title("Filtrar estudiantes por promedio")

# Encontramos el promedio maximo para establecer el rango del slider.
max_promedio = float(df['promedio'].max())

# Creamos un slider (una barra deslizante) para que el usuario pueda elegir
# el valor mínimo de promedio que quiere ver.

promedio_minimo = st.slider("Mostrar estudiantes co promedio mayor o igual a:", 0.0, max_promedio, 3.0)

# Filtramos el dataset para mostrar solo los estudiantes con un promedio mayor o igual al valor del slider.
estudiantes_filtrados = df[df['promedio'] >= promedio_minimo]

# Mostramos lo estudiantes filtrados.
st.write(f"Estudiantes con promedio mayor o igual a {promedio_minimo}:")
st.dataframe(estudiantes_filtrados)

st.markdown('<p style="font-size:16px; font-weight:bold;">Código para Filtrar estudiantes por promedio</p>', unsafe_allow_html=True)
code="""
#Filtrar estudiantes por promedio
st.title("Filtrar estudiantes por promedio")

# Encontramos el promedio maximo para establecer el rango del slider.
max_promedio = float(df['promedio'].max())

# Creamos un slider (una barra deslizante) para que el usuario pueda elegir
# el valor mínimo de promedio que quiere ver.

promedio_minimo = st.slider("Mostrar estudiantes co promedio mayor o igual a:", 0.0, max_promedio, 3.0)

# Filtramos el dataset para mostrar solo los estudiantes con un promedio mayor o igual al valor del slider.
estudiantes_filtrados = df[df['promedio'] >= promedio_minimo]

# Mostramos lo estudiantes filtrados.
st.write(f"Estudiantes con promedio mayor o igual a {promedio_minimo}:")
st.dataframe(estudiantes_filtrados)
"""
st.code(code, language='python')