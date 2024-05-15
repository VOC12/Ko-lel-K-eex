import streamlit as st

#background
background_image = "webApp/Images/BG.png"

# HTML y CSS 4 the bg
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#Tittle, I use a png as i wanted an specific typograpi
st.image("webApp/Images/tituloblanco.png", use_column_width=True)

# Espacio para los botones
st.markdown("<h2 style='text-align: center; color: white;'>Bienvenida a Ko'olel K'eex</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Accede a nuestros sitemas de ayuda en la siguiente barra.</p>", unsafe_allow_html=True)

# Botones de navegación con imágenes
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.image("webApp/Images/ENTERATE.png", use_column_width=True):
        st.experimental_set_query_params(page="visualizations")
        st.experimental_rerun()

with col2:
    if st.image("webApp/Images/hablaconmaya.png", use_column_width=True):
        st.experimental_set_query_params(page="chatbot")
        st.experimental_rerun()

with col3:
    if st.image("webApp/Images/celulasvioleta.png", use_column_width=True):
        st.experimental_set_query_params(page="map")
        st.experimental_rerun()

# Página principal
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["main"])[0]

if page == "main":
    st.write("Welcome to the main page. Use the buttons above to navigate.")
elif page == "visualizations":
    st.write("Visualizations page content goes here.")
elif page == "chatbot":
    st.write("Chatbot page content goes here.")
elif page == "map":
    st.write("Map page content goes here.")


