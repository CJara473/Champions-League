import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
def load_data():
    file_path = "Datos_ML_con_Target.xlsx" # Ruta actualizada
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    df["Total Partidos"] = df["Victorias"] + df["Empates"] + df["Derrotas"]
    df["% Victorias"] = (df["Victorias"] / df["Total Partidos"]) * 100
    df["% Derrotas"] = (df["Derrotas"] / df["Total Partidos"]) * 100
    return df[["Club", "% Victorias", "% Derrotas"]]

df = load_data()

# Configuración de la aplicación Streamlit
st.title("Análisis de Resultados de Equipos")

# Selección del equipo
equipo = st.selectbox("Seleccione un equipo", df["Club"].unique())

data_equipo = df[df["Club"] == equipo]

# Mostrar estadísticas
st.write(f"### Estadísticas de {equipo}")
st.write(data_equipo)

# Gráfico de barras
fig = px.bar(
    data_equipo.melt(id_vars=["Club"], value_vars=["% Victorias", "% Derrotas"], var_name="Resultado", value_name="Porcentaje"),
    x="Resultado", y="Porcentaje", color="Resultado",
    title=f"Porcentaje de Victorias y Derrotas de {equipo}",
    text_auto=True
)

st.plotly_chart(fig)
