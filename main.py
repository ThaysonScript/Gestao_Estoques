# --------------------- IMPORTAR PARTES DA APLICACAO --------------------------
from modulos_projeto import cadastrar_item
from modulos_projeto import ver_items
from modulos_projeto import atualizar_item
from modulos_projeto import deletar_item
from modulos_projeto import persistencia_arquivo_csv


# 2.1. MENU INICIAL PARA O USUARIO SELECIONAR A OPCAO DE INTERESSE
def menu_usuario():
    print("\n'''''' ESCOLHA UMA OPÇÃO ''''''''''\n")
    print("[1].CADASTRAR ITEM")
    print("[2].BUSCAR ITEM")
    print("[3].EDITAR ITENS CADASTRADOS")
    print("[4].REMOVER ITEM CADASTRADO")
    print("[5].PERSISTIR DADOS EM ARQUIVO.CSV")
    print("[6].SAIR\n")
    print("''''''''''''''''''''''''''''''''''''")
    
    
#  SELECIONAR A OPCAO DE INTERESSE
def escolha_usuario():
    while True:
        menu_usuario()  # CHAMAR MENU PRINCIPAL
        escolha = input('Digite uma opção de escolha acima: ')

        if escolha == '1':
            cadastrar_item.cadastro()
            
        elif escolha == '2':
            ver_items.visualizar_item()
            
        elif escolha == '3':
            atualizar_item.atualizar_dados()
            
        elif escolha == '4':
            deletar_item.deletar_item()
            
        elif escolha == '5':
            persistencia_arquivo_csv.persistir_dados_arquivo_csv()
        
        elif escolha == '6':
            print("\n******** SAINDO DO PROGRAMA *********\n")
            break
        
        else:
            print('Digite uma opção válida!')
            
            
# EXECUTAR O INICIO DO PROGRAMA, EXECUTE DIRETAMENTE
if __name__ == '__main__':  # NAO EXECUTAVEL SE FOR MODULO
    escolha_usuario()