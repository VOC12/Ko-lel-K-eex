import streamlit as st
import pydeck as pdk
import pandas as pd

st.title("Visualización del Mapa")

# Datos de ejemplo
data = pd.DataFrame({
    'lat': [37.7749, 34.0522, 40.7128],
    'lon': [-122.4194, -118.2437, -74.0060],
    'ciudad': ['San Francisco', 'Los Ángeles', 'Nueva York']
})

# Mapa
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=100000,
        ),
    ],
))
