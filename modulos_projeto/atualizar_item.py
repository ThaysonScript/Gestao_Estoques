def dados_armazenados():
    with open('dados.csv', 'r') as dados:
        linhas = dados.readlines()
    return linhas

def novos_dados(nova_fabricante: str) -> str:
    nova_fabricante = input('Digite a nova fabricante: ').strip()
    novo_modelo = input('Digite o novo modelo: ').strip()
    novo_serial = input('Digite o novo serial: ').strip()
    
    return f'{nova_fabricante},{novo_modelo},{novo_serial}\n'

def atualizar_dados():
    dados_cadastrados = dados_armazenados()
    print(f'Items disponiveis: \n{dados_cadastrados}')
    
    item_atualizar = input('Digite o nome do item a ser atualizado: ')
    linhas_atualizadas = []
    for linha in dados_cadastrados:
        fabricante, modelo, serial = linha.strip().split(',')
        
        if item_atualizar == fabricante:
            novos_items = novos_dados(fabricante)
            linhas_atualizadas.append(novos_items)
            
        else:
            linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
        
    salvar_dados(linhas_atualizadas)
    
    
def salvar_dados(dados_atualizados):
    with open('dados.csv', 'w') as dados:
        dados.writelines(dados_atualizados)
