# CARREGAR DADOS CADASTRADOS
def carregar_dados():
    with open('dados.csv', 'r') as dados:
        linhas = dados.readlines()
    return linhas

# REGISTRAR DADOS TOTAIS (ATUALIZADOS E ANTIGOS)
def salvar_dados(dados_atualizados):
    with open('dados.csv', 'w') as dados:
        dados.writelines(dados_atualizados)


# ENTRADA PARA NOVOS DADOS ATUALIZADOS E O RETORNO DELES
def novos_dados() -> str:
    nova_fabricante = input('Digite a nova fabricante: ').strip()
    novo_modelo = input('Digite o novo modelo: ').strip()
    novo_serial = input('Digite o novo serial: ').strip()
    
    return f'{nova_fabricante},{novo_modelo},{novo_serial}\n'


# PROCURAR DADO A ATUALIZAR
def atualizar_dados():
    dados_cadastrados = carregar_dados()
    print(f'Items disponiveis: \n{dados_cadastrados}')
    
    item_atualizar = input('Digite o nome do item a ser atualizado: ')
    linhas_atualizadas = []
    for linha in dados_cadastrados:
        fabricante, modelo, serial = linha.strip().split(',')
        
        if item_atualizar == fabricante:
            novos_items = novos_dados()
            linhas_atualizadas.append(novos_items)
            
        else:
            linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
        
    salvar_dados(linhas_atualizadas)
