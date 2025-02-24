import sqlite3

conexao = sqlite3.connect('tabelas.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE filmes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT NOT NULL,
genero TEXT NOT NULL,
ano INT NOT NULL,
avaliacao REAL NOT NULL,
assistindo BOLLEAN NOT NULL
)
''')
conexao.commit()
conexao.close()