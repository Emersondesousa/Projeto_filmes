import time
from services import filme_service

while True:

    print('Filmes e Séries')
    print('Menu:  ')
    print('1 -- Adicionar filme')
    print('2 -- Listar filmes')
    print('3 -- Buscar filme')
    print('4 -- Atualizar filme')
    print('5 -- Excluir filme')
    print('6 -- Marcar como assistido')
    print('7 -- Desmarcar como assistido')
    print('8 -- Avaliar filme')
    print('9 -- Sair')
    
    opcao = input('Informe o número da opção desejada: ')

    match opcao:
        
        case '1':
            filme_service.adicionar_filme()
            time.sleep(1)

        case '2':
            filme_service.listar_filmes()
            time.sleep(1)

        case '3':
            filme_service.bucar_filme()
            time.sleep(1)

        case '4':
            filme_service.atualizar_filme()
            time.sleep(1)

        case '5':
            filme_service.excluir_filme()
            time.sleep(1)

        case '6':
            filme_service.marcar_assistindo()
            time.sleep(1)

        case '7':        
            filme_service.desmarcar_assistindo()
            time.sleep(1)

        case '8':
            filme_service.avaliar_filme()
            time.sleep(1)

        case '9':
            print('Programa encerrado.')
            break

        case _:
            print('Erro, digite uma opção válida.')
            time.sleep(1)