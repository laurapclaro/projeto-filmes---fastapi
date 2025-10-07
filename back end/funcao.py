from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id SERIAL PRIMARY KEY ,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL )


""")
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela {erro}")
        finally:
            cursor.close()
            conexao.close()


criar_tabela()

#--------------

def criar_filme(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "INSERT INTO movies (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()



criar_filme("Avatar", "Ação", 2009, 10.0)

#-----------

def listar_movies():
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "SELECT * FROM movies ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

filmes = listar_movies()
print(filmes)

#-----------------

def atualizar_movies(id_movie, nova_avaliacão):
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "UPDATE movies SET avaliacão = %s WHERE id = %s",
                (nova_avaliacão, id_movie)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar a nota: {erro}")
        finally:
            cursor.close()
            conexao.close()


#--------

def deletar_movie(id_movie):
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "DELETE FROM movies WHERE id = %s", (id_movie,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()


#----------------

def pesquisar_filme(titulo_parcial):
    conexao, cursor = conectar()
    if conexao:
        try:
            # Usa LIKE para buscar títulos que contenham a string (case insensitive)
            cursor.execute(
                "SELECT * FROM movies WHERE titulo ILIKE %s ORDER BY id",
                (f"%{titulo_parcial}%",)
            )
            resultados = cursor.fetchall()
            return resultados
        except Exception as erro:
            print(f"Erro ao pesquisar filme: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

