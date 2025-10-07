import streamlit as st

def main():
    st.markdown(
        """
        <style>
        html, body, .stApp {
            background-color: #F07E69 !important;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Pesquisa de Filmes 🎬")

if __name__ == "__main__":
    main()