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
                    "ano lançamento": filme[3],
                     "avaliacao": filme[4] 
                     })
    return{"filmes": lista }