# CARREGAR DADOS CADASTRADOS
def carregar_dados():
    with open('dados.csv', 'r') as dados:
        linhas = dados.readlines()
    return linhas


def menu_tipo_atualizacao():
    print("\n''''''''''' MENU DE TIPOS DE ATUALIZAÇÕES ''''''''''''''''\n")
    print('[1].ATUALIZAR FABRICANTE, MODELO E CÓDIGO')
    print('[2].ATUALIZAR FABRICANTE ')
    print('[3].ATUALIZAR MODELO')
    print('[4].ATUALIZAR N° CODIGO DO ITEM')
    print('[5].SAIR DO MENU DE ATUALIZAÇÕES')
    print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    

# REGISTRAR DADOS TOTAIS (ATUALIZADOS E ANTIGOS)
def salvar_dados(dados_atualizados):
    with open('dados.csv', 'w') as dados:
        dados.writelines(dados_atualizados)


# ENTRADA PARA NOVOS DADOS ATUALIZADOS E O RETORNO DELES
def novos_dados() -> str:
    nova_fabricante = input('Digite a nova fabricante: ').strip()
    novo_modelo = input('Digite o novo modelo: ').strip()
    novo_codigo = input('Digite o novo codigo: ').strip()
    
    return f'{nova_fabricante},{novo_modelo},{novo_codigo}\n'


# PROCURAR DADO A ATUALIZAR
def atualizar_dados():
    dados_cadastrados = carregar_dados()
    
    codigo_item_cadastrado = input('Digite o código do seu item cadastrado: ').strip()
    while True:
        menu_tipo_atualizacao()
        tipo_atualizar = int(input('Digite o tipo de atualização desejada: '))
        
        dados_atualizados = []
        
        for linha in dados_cadastrados:
            fabricante, modelo, codigo = linha.strip().split(',')
            if codigo_item_cadastrado == codigo:
                if tipo_atualizar == 1:
                    novos_items = novos_dados()
                    dados_atualizados.append(novos_items)
                    
                elif tipo_atualizar == 2:
                    fabricante_atual = input('Digite a fabricante atual do seu item: ')
                    if fabricante_atual == fabricante:
                        print(f"DADOS DO PRODUTO SELECIONADO: 'FABRICANTE': *{fabricante}, 'MODELO': {modelo}, ' N° codigo: {codigo} ")
                    
                        print(f'Atualmente o fabricante desse item é {fabricante}')
                        novo_fabricante = input('Digite o novo fabricante que você quer inserir: ')
                        
                        dados_atualizados.append(f'{novo_fabricante},{modelo},{codigo}\n')                       
                        print('Sucesso! Seu fabricante foi atualizado com sucesso!')
                        print(f"DADOS DO PRODUTO ATUALIZADOS: 'FABRICANTE': **{novo_fabricante}, 'MODELO': {modelo}, ' N° codigo: {codigo} ")
                        
                        
                elif tipo_atualizar == 3:
                    modelo_atual = input('Digite o seu modelo atual: ')
                    
                    print(f"DADOS DO PRODUTO SELECIONADO: 'FABRICANTE': {fabricante}, 'MODELO': *{modelo}, ' N° codigo: {codigo} ")
                    print(f'Atualmente o modelo desse item é {modelo}')
                    
                    novo_modelo = input('Digite o novo modelo que você quer inserir:')
                    
                    dados_atualizados.append(f'{fabricante},{novo_modelo},{codigo}\n')
                    
                    print('Sucesso! Seu item foi atualizado com sucesso!')   
                    print(f"DADOS DO PRODUTO ATUALIZADO: 'FABRICANTE': {fabricante}, 'MODELO': **{modelo}, ' N° codigo: {codigo} ") 
                    
                elif tipo_atualizar == 4:
                    print('Recuperamos o seu código de produto atual digitado nesta sessão')
                    
                    print(f"DADOS DO PRODUTO SELECIONADO: 'FABRICANTE': {fabricante}, 'MODELO': {modelo}, ' N° codigo: *{codigo} ")
                    print(f'Atualmente o modelo desse item é {modelo}')
                    
                    novo_codigo = input('Digite o novo codigo que você quer inserir:')
                    
                    dados_atualizados.append(f'{fabricante},{modelo},{novo_codigo}\n')
                    
                    print('Sucesso! Seu item foi atualizado com sucesso!')   
                    print(f"DADOS DO PRODUTO ATUALIZADO: 'FABRICANTE': {fabricante}, 'MODELO': **{modelo}, ' N° codigo: **{novo_codigo} ") 
                    
                else:
                    dados_atualizados.append(f'{fabricante},{modelo},{codigo}\n')
                    
                    
        if tipo_atualizar == 5:
            print('SAINDO DO MENU DE ATUALIZAÇÕES....')
            break
                
        salvar_dados(dados_atualizados)
