# --------------------- IMPORTAR PARTES DA APLICACAO --------------------------
from modulos_projeto import cadastro
from modulos_projeto import ver
from modulos_projeto import atualizar
from modulos_projeto import deletar
from modulos_pesquisas import menu_pesquisa

import limpar_terminal

# 2.1. MENU INICIAL PARA O USUARIO SELECIONAR A OPCAO DE INTERESSE
def menu_principal():
    print("\n'''''' ESCOLHA UMA OPÇÃO ''''''''''\n")
    print("[1].CADASTRAR ITEM")
    print("[2].BUSCAR ITEM")
    print("[3].EDITAR ITENS CADASTRADOS")
    print("[4].REMOVER ITEM CADASTRADO")
    print("[5].REALIZAR PESQUISA AVANÇADA ( BETA )")
    print("[6].SAIR\n")
    print("''''''''''''''''''''''''''''''''''''")
    
#  SELECIONAR A OPCAO DE INTERESSE
def escolha_interesse():
    while True:
        limpar_terminal.limpar_terminal()
        menu_principal()  # CHAMAR MENU PRINCIPAL
        escolha = input('Digite uma opção de escolha acima: ')

        if escolha == '1':
            limpar_terminal.limpar_terminal()
            cadastro.cadastro()
            
        elif escolha == '2':
            limpar_terminal.limpar_terminal()
            ver.ver_items()
            
        elif escolha == '3':
            limpar_terminal.limpar_terminal()
            atualizar.atualizar_dados()
            
        elif escolha == '4':
            limpar_terminal.limpar_terminal()
            deletar.deletar_item()
            
        elif escolha == '5':
            limpar_terminal.limpar_terminal()
            menu_pesquisa.opcoes()
        
        elif escolha == '6':
            limpar_terminal.limpar_terminal()
            print("\n******** SAINDO DO PROGRAMA *********\n")
            break
        
        else:
            print('\nDigite uma opção válida!\n')
            input('Pressione qualquer Tecla para Continuar')
            
# EXECUTAR O INICIO DO PROGRAMA, EXECUTE DIRETAMENTE
if __name__ == '__main__':  # NAO EXECUTAVEL SE FOR MODULO
    escolha_interesse()
