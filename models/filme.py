from database import db

class Filme:
    def __init__(self, titulo:str, genero:str, ano:int, avaliacao=None, assistindo=False):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.avaliacao = avaliacao
        self.assistindo = assistindo

    def salvar_filme(self):
        if not self.titulo or not self.genero or not self.ano:
            print('Preencha todos os campos.')
            return
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f''' SELECT titulo FROM filmes WHERE titulo = '{self.titulo}' ''')
        resultado = cursor.fetchone()
        if resultado:
            print('Este filme já foi cadastrado.')
        else:
            cursor.execute(f'''
            INSERT INTO filmes (titulo, genero, ano, avaliacao, assistindo) VALUES
            ('{self.titulo}', '{self.genero}', {self.ano}, '{self.avaliacao}', '{self.assistindo}')''')
            conexao.commit()
            print('Filme adicionado com sucesso!')
        cursor.close()
        conexao.close()

    def atualizar(self, id_filme, opcao_atualizar, novo_atributo ):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f''' SELECT id FROM filmes WHERE id = {id_filme} ''')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Filme não encontrado.')
        else:
            cursor.execute(f'''
            UPDATE filmes SET {opcao_atualizar} = '{novo_atributo}' WHERE id = {id_filme}
            ''')
            conexao.commit()
            print('Filme atualizado com sucesso!')  
        cursor.close()
        conexao.close()

    def excluir(self, titulo_filme):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f'''SELECT titulo FROM filmes WHERE titulo = '{titulo_filme}' ''')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Filme não encontrado.')
        else:    
            cursor.execute(f'''
            DELETE FROM filmes WHERE titulo = '{titulo_filme}' ''')
            conexao.commit()
            print('Filme deletado com sucesso!')
        cursor.close()
        conexao.close()

    def marcar_assistido(self, titulo_filme):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f'''SELECT titulo FROM filmes WHERE titulo = '{titulo_filme}' ''')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Filme não encontrado.')
        else:
            cursor.execute(f'''
            UPDATE filmes SET assistindo = '{True}' WHERE titulo = '{titulo_filme}' ''')
            conexao.commit()
            print('Marcação concluida com sucesso!')
        cursor.close()
        conexao.close()

    def desmarcar_assistindo(self, titulo_filme):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f'''SELECT titulo FROM filmes WHERE titulo = '{titulo_filme}' ''')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Filme não encontrado.')
        else:    
            cursor.execute(f'''
            UPDATE filmes SET assistindo = '{False}' WHERE titulo = '{titulo_filme}' ''')
            conexao.commit()
            print('Filme desmarcado com sucesso!')
        cursor.close()
        conexao.close()

    def avaliar(self, id, avaliacao):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f'''SELECT id FROM filmes WHERE id = {id}''')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Id não encontrado')
        else:    
            cursor.execute(f'''
            UPDATE filmes SET avaliacao = '{avaliacao}' WHERE id = {id} ''')
            conexao.commit()
            print('Avaliação atualizada com sucesso!')
        cursor.close()
        conexao.close()
        

    def listar(self):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute('''SELECT * FROM filmes''')
        filmes = cursor.fetchall()
        cursor.close()
        conexao.close()
        if not filmes:
            print('Não há filme cadastrado.')
        else:
            for i in filmes:
                print(i)

    def buscar_filme(self, nome_filme):
        conexao = db.conectar_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute(f''' SELECT * FROM filmes WHERE titulo = '{nome_filme}' ''')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Filme não encontrado')
        else:
            print(f'Filme encontrado: {resultado}')
            conexao.commit()
        cursor.close()
        conexao.close()    
