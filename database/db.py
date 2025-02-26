import sqlite3

conexao = sqlite3.connect('tabelas.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT NOT NULL,
genero TEXT NOT NULL,
ano INT NOT NULL,
avaliacao REAL NOT NULL,
assistindo BOOLEAN NOT NULL
)
''')

conexao.commit()
cursor.close()
conexao.close()

def conectar_banco_de_dados():
    conexao = sqlite3.connect('tabelas.db')
    return conexao