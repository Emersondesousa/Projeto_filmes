from sqlite3 import Cursor, db
from database import db

class Filme:
    def __init__(self, titulo:str, genero:str, ano:int, avaliacao:float, assistindo: False):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.avaliacao = avaliacao
        self.assistindo = assistindo

    def salvar_filme(self):
        db.conectar_banco_de_dados()
        cursor = db.conexao.cursor()
        cursor.execute(f'''
        INSERT INTO filmes (titulo, genero, ano),
        '{self.titulo}', '{self.genero}', {self.ano}
        ''')
        db.conexao.commit()
        db.conexao.close()
        print(f'Filme {self.titulo} inserido na lista.')

    def atualizar(self, opcao_atualizar):
        db.conectar_banco_de_dados()
        cursor = db.conexao.cursor()
        cursor.execute(f'''
        UPDATE INTO filmes ({opcao_atualizar}),
        
        ''')


