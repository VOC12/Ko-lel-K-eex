import streamlit as st
import pandas as pd
import altair as alt

st.title("Visualizaciones Interactivas de lo q obtengamos de los datos")

# Datos de ejemplo
data = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valores': [4, 3, 7, 6]
})

# Gráfico de barras
chart = alt.Chart(data).mark_bar().encode(
    x='Categoría',
    y='Valores'
)

st.altair_chart(chart, use_container_width=True)
