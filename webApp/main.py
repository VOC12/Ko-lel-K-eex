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


