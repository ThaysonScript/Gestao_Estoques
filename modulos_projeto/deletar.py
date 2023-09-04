def carregar_items(deletar_item):    
    with open("dados.csv", "r") as dados:
        return [linha for linha in dados if deletar_item not in linha]

# REGISTRAR A EXCLUSAO DE UM DADO
def registrar_delete(linhas_atualizadas):
    with open("dados.csv", "w") as arquivo_csv:
            arquivo_csv.writelines(linhas_atualizadas)


# CARREGAR DADOS CADASTRADOS E PROCURAR DADO ESPECIFICO PARA EXCLUIR
def deletar_item():
    deletar_item = input("Digite o nome do item que deseja excluir: ")
    linhas_atualizadas = carregar_items(deletar_item)
                
    try:
        print(f"Registro com o nome '{deletar_item}' irá ser excluído.\n")  
    
        while True:
            escolha_delete = input('Deseja realmente excluir esse item s/n: ').lower()
            
            if escolha_delete == 's':
                registrar_delete(linhas_atualizadas)
                print('Seu item foi excluido com sucesso!')
                break
            
            elif escolha_delete == 'n':
                print('Redirecionando para menu principal')
                break
            
            else:
                print('Digite um valor válido')
            
        input('Pressione qualquer Tecla para Continuar')
        
    except FileNotFoundError:
        print('Arquivo.csv não existe, cadastre um novo item para executar essa consulta!')
        input('Pressione qualquer Tecla para Continuar')