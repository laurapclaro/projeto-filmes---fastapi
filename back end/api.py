from fastapi import FastAPI
import funcao 
#ROda fastapi = python -m uvicorn api:app --reload
# /docs > documentaçãpo Swagger 
#redoc > Documentaçao Redoc


app = FastAPI(title="Gerenciador de Filmes")
#GET > pegar/listar
#POST > enviar/cadastrar
#PUT > atualizar
#DELETE > deletar


#API sempre retorna dados em json ( chave: valor)
@app.get("/")
def home():
    return {"mensagem": "Bem - vindo ao gerenciador de filmes! 🔑"}

@app.get("/filmes") 
def catalogo():
    filmes = funcao.listar_movies()
    lista = []
    for filme in filmes:
       lista.append( { "id": filme[0], 
                    "titulo": filme[1], 
                    "genero": filme[2],
                    "ano": filme[3],
                     "avaliacao": filme[4] 
                     })
    return{"filmes": lista }


@app.post("/filmes")
def adicionar_filme(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.criar_filme(titulo, genero, ano, avaliacao)
    return("mensagem: filme adicionado com sucesso!")