import streamlit as st
import requests as rq

API_URL = "http://http://127.0.0.1:8000/"

st.set_page_config(page_title="Gerenciador de filmes", page_icon="💎")

#menu lateral = sidebar
menu = st.sidebar.radio("Navegação", ["Catálogo"])


if menu == "Catálogo":
    st.subheader("Todos os filmes")
    response = rq.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            