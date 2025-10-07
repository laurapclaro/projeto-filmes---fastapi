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



def listar_alunos():
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "SELECT * FROM alunos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_alunos(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "UPDATE alunos SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar um aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_aluno(id_aluno):
    conexao, cursor = conectar()
    if conexao:
        try: 
            cursor.execute(
                "DELETE FROM alunos WHERE id = %s", (id_aluno,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()
