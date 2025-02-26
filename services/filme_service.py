from models.filme import Filme

filme = Filme('','',0)
def adicionar_filme():
    titulo = input('Título: ')
    genero = input('Gênero: ')
    ano = int(input('Ano: '))
    filme = Filme(titulo, genero, ano)
    filme.salvar_filme()

def atualizar_filme():
    id_filme = int(input('Informe o id do filme: '))
    opcao = input('Informe a opção que deseja atualizar(titulo, genero, ano): ')
    nova_opcao = input('Informe a nova a atualização: ')
    filme.atualizar(id_filme, opcao, nova_opcao)

def excluir_filme():
    titulo = input('Informe o título: ')
    filme.excluir(titulo)

def marcar_assistindo():
    titulo = input('Informe o título: ')
    filme.marcar_assistido(titulo)

def desmarcar_assistindo():
    titulo = input('Informe o título: ')
    filme.desmarcar_assistindo(titulo)
    
def avaliar_filme():
    id = int(input('Informe o Id: '))
    avaliacao = input('Digite a avaliação: ')
    filme.avaliar(id, avaliacao)

def listar_filmes():
    filme.listar()

def bucar_filme():
    nome_filme = input('Informe o nome do filme: ')
    filme.buscar_filme(nome_filme)