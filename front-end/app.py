import streamlit as st
import requests as rq

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de filmes", page_icon="💎")

#menu lateral = sidebar
menu = st.sidebar.radio("Navegação", ["Catálogo", "Inserir filmes", "Atualizar filme", "Deletar filme"])


if menu == "Catálogo":
    st.subheader("Todos os filmes")
    response = rq.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f" **{filme['titulo']}** / {filme['ano']} / {filme['genero']} / 👍 {filme['avaliacao']} 👎")
        else:
            st.info("Nenhum filme encontrado 📍" )

    else:
        st.error("Erro ao conectar API")

elif menu == "Inserir filmes":
    st.subheader("Inserir filme 🎞")
    titulo = st.text_input("Título do filme")
    genero = st.text_input("Gênero do filme")
    ano = st.number_input("Ano de lançamento", min_value=1950, max_value=2100, step=1 )
    avaliacao = st.number_input("0 a 10", min_value=0, max_value=10,  step=1)

    if st.button("Finalizar cadastro ✔"):
        params = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = rq.post(f"{API_URL}/filmes", params=params)
        if response.status_code == 200:
            st.success("Obra adicionada com sucesso! ✔")
        else:
            st.error("Error!")

elif menu == "Atualizar filme":
    st.subheader("Atualizar filme")
    id_movies = st.number_input("ID do Filme a atualizar", min_value=1, step=1)
    nova_avaliacao = st.number_input("Nova avaliação", min_value=0, max_value=10)
    if st.button("Atualizar"):
        params = {"nova_atualizacao": nova_avaliacao}
        response = rq.put(f"{API_URL}/filmes/{id_movies}", params=params)
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                st.warning(data["error"])         
            else:
                st.success("Obra atualizada com sucesso")
        else:
            st.error("Erro ao atualizar filme")

elif menu == "Deletar filme":
    st.subheader("Deletar filme ❌")
    identificacao = st.number_input("ID do filme e deletar")





 





