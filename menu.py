# Importar modulos do codigo
import cadastrar_item
import ver_items
import atualizar_item
import deletar_item

# 2.1. Menu inicial para o usuário selecionar a opção de interesse
def menu_usuario():
    print("\n'''''' ESCOLHA UMA OPÇÃO ''''''''''")
    print("[1].CADASTRAR ITEM")
    print("[2].BUSCAR ITEM")
    print("[3].EDITAR ITENS CADASTRADOS")
    print("[4].REMOVER ITEM CADASTRADO")
    print("[5].SAIR")
    
    
# selecionar a opção de interesse
def escolhas_usuario():
    while True:
        menu_usuario()
        escolha = input('Digite uma opção de escolha acima: ')
    
        if escolha == '1':
            cadastrar_item.cadastrar_item()
            
        elif escolha == '2':
            ver_items.visualizar_item()
            
        elif escolha == '3':
            atualizar_item.atualizar_item()
            
        elif escolha == '4':
            deletar_item.deletar_item()
            
        elif escolha == '5':
            print("\n'''''' SAINDO DO PROGRAMA ''''''''''\n")
            break
        
        else:
            print('Digite uma opção válida!')
            
            
if __name__ == '__main__':
    escolhas_usuario()