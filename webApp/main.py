import streamlit as st

st.title("Ko'olel-K'eex")

# Estilo CSS para el fondo de color morado con un borde
st.markdown("""
    <style>
    .main {
        background-color: #d8b4e2;
        padding: 20px;
        border: 5px solid #8a2be2;
        border-radius: 10px;
    }
    .title {
        color: #4b0082;
        text-align: center;
        font-size: 2em;
    }
    .sidebar .sidebar-content {
        background-color: #d8b4e2;
    }
    </style>
    """, unsafe_allow_html=True)

# Contenido de la página principal
st.markdown("""
<div class="main">
    <h1 class="title">Bienvenidos a Ko'olel K'eex</h1>
    <p>We are a collective and an amazing web app for women. Use the sidebar to navigate between the different sections.</p>
</div>
""", unsafe_allow_html=True)

# Agregar una imagen en la página principal
st.image("webApp/Images/KKLOGO.png", caption="Nuestro logo", use_column_width=True)

# Sidebar
st.sidebar.title("Naviagte")
st.sidebar.markdown("Choose an option for help")

# Agregar otra imagen en la barra lateral
st.sidebar.image("webApp/Images/KKLOGO.png", caption="Otra descripción", use_column_width=True)
