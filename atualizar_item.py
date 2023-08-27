def dados_armazenados():
    with open('dados.txt', 'r') as dados:
        linhas = dados.readlines()
        print(f'Items disponiveis: \n{linhas}')
        
    return linhas


def atualizar_dados():
    dados_cadastrados = dados_armazenados()
    
    item_atualizar = input('Digite o nome do item a ser atualizado: ')
    linhas_atualizadas = []
    for linha in dados_cadastrados:
        fabricante, modelo, serial = linha.strip().split(",")
        
        if item_atualizar == fabricante:
            nova_fabricante = input('Digite a nova fabricante: ')
            novo_modelo = input('Digite o novo modelo: ')
            novo_serial = input('Digite o novo serial: ')
            
            fabricante = nova_fabricante
            modelo = novo_modelo
            serial = novo_serial
            
        linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
        
    return linhas_atualizadas
        
     
        
with open('dados.txt', 'w') as dados:
    dados_atualizados = atualizar_dados()
    dados.writelines(dados_atualizados)