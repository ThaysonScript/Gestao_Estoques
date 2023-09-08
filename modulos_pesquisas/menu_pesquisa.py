from modulos_pesquisas import pesquisa_avancada

import limpar_terminal

def menu_pesquisa():
    print("\n'''''' OPÇÕES DE PESQUISA DISPONÍVEIS ''''''''''\n")
    print("[1].BUSCAR ITEM")
    print("[2].REMOVER ITEM CADASTRADO")
    print("[3].SAIR")
    print("\n''''''''''''''''''''''''''''''''''''\n")
    

def opcoes():
    while True:
        limpar_terminal.limpar_terminal()
        menu_pesquisa()
        
        escolha = input('Digite o tipo de pesquisa desejado: ')
        
        if escolha == '1':
            pesquisa_avancada.tipo_operacao(escolha)
        elif escolha == '2':
            pesquisa_avancada.tipo_operacao(escolha)
        elif escolha == '3':
            break
        else:
            print('\nDigite um valor válido!\n')
            input('Digite "Enter" para Continuar')