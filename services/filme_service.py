from models.filme import Filme

def adicionar_filme():
    titulo = input('Título: ')
    genero = input('Gênero: ')
    ano = int(input('Ano: '))
    filme = Filme(titulo, genero, ano)
    filme.salvar_filme()

def atualizar_filme():
    opcao = input('Informe a opção que deseja atualizar(titulo, genero, ano): ')
    nova_opcao = input('Informe a nova a atualização: ')
    Filme.atualizar(opcao, nova_opcao)

def excluir_filme():
    titulo = input('Informe o título: ')
    Filme.excluir(titulo)

def marcar_assistindo():
    titulo = input('Informe o título: ')
    Filme.marcar_assistido(titulo)

def desmarcar_assistindo():
    titulo = input('Informe o título: ')
    Filme.desmarcar_assistindo(titulo)
    
def avaliar_filme():
    id = int(input('Informe o Id: '))
    avaliacao = input('Digite a avaliação: ')
    Filme.avaliar(id, avaliacao)

def listar_filmes():
    Filme.listar()