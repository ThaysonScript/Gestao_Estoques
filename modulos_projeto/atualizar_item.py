# CARREGAR DADOS CADASTRADOS
def carregar_dados():
    with open('dados.csv', 'r') as dados:
        linhas = dados.readlines()
    return linhas

# REGISTRAR DADOS TOTAIS (ATUALIZADOS E ANTIGOS)
def salvar_dados(dados_atualizados):
    with open('dados.csv', 'w') as dados:
        dados.writelines(dados_atualizados)
        

# MOSTRAR MENU DE ESCOLHA PARA ATUALIZAR
def menu_tipo_atualizacao():
    print("\n''''''''''' MENU DE TIPOS DE ATUALIZAÇÕES ''''''''''''''''\n")
    print('[1].ATUALIZAR FABRICANTE, MODELO E CÓDIGO')
    print('[2].ATUALIZAR FABRICANTE ')
    print('[3].ATUALIZAR MODELO')
    print('[4].ATUALIZAR N° CODIGO DO ITEM')
    print('[5].SAIR DO MENU DE ATUALIZAÇÕES')
    print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")


# ATUALIZAR TODAS AS PROPRIEDADES
def atualizar_todas_propriedades():
    nova_fabricante = input('Digite a nova fabricante: ').strip()
    novo_modelo = input('Digite o novo modelo: ').strip()
    novo_codigo = input('Digite o novo codigo: ').strip()
    
    return f'{nova_fabricante},{novo_modelo},{novo_codigo}\n'

# ATUALIZAR SOMENTE A FABRICANTE
def atualizar_somente_fabricante(fabricante, modelo, codigo):
    fabricante_atual = input('Digite a fabricante atual do seu item: ')
    if fabricante_atual == fabricante:
        print(f"DADOS DO PRODUTO SELECIONADO: 'FABRICANTE': *{fabricante}, 'MODELO': {modelo}, ' N° codigo: {codigo} ")

        print(f'Atualmente o fabricante desse item é {fabricante}')
        
        novo_fabricante = input('Digite o novo fabricante que você quer inserir: ')
                              
        print('Sucesso! Seu fabricante foi atualizado com sucesso!')
        print(f"DADOS DO PRODUTO ATUALIZADOS: 'FABRICANTE': **{novo_fabricante}, 'MODELO': {modelo}, ' N° codigo: {codigo} ")
        
        return f'{novo_fabricante},{modelo},{codigo}\n'
        
        
# ATUALIZAR SOMENTE A MODELO
def atualizar_somente_modelo(fabricante, modelo, codigo):
    modelo_atual = input('Digite o seu modelo atual: ')
    
    print(f"DADOS DO PRODUTO SELECIONADO: 'FABRICANTE': {fabricante}, 'MODELO': *{modelo}, ' N° codigo: {codigo} ")
    print(f'Atualmente o modelo desse item é {modelo}')
    
    novo_modelo = input('Digite o novo modelo que você quer inserir:')
        
    print('Sucesso! Seu item foi atualizado com sucesso!')   
    
    print(f"DADOS DO PRODUTO ATUALIZADO: 'FABRICANTE': {fabricante}, 'MODELO': **{modelo}, ' N° codigo: {codigo} ")
    
    return f'{fabricante},{novo_modelo},{codigo}\n'
    
    
    
# ATUALIZAR SOMENTE A CODIGO
def atualizar_somente_codigo(fabricante, modelo, codigo):
    print('Recuperamos o seu código de produto atual digitado nesta sessão')
    
    print(f"DADOS DO PRODUTO SELECIONADO: 'FABRICANTE': {fabricante}, 'MODELO': {modelo}, ' N° codigo: *{codigo} ")
    
    print(f'Atualmente o modelo desse item é {modelo}')
    
    novo_codigo = input('Digite o novo codigo que você quer inserir:')
        
    print('Sucesso! Seu item foi atualizado com sucesso!')
    
    print(f"DADOS DO PRODUTO ATUALIZADO: 'FABRICANTE': {fabricante}, 'MODELO': **{modelo}, ' N° codigo: **{novo_codigo} ")
    
    return f'{fabricante},{modelo},{novo_codigo}\n'


# PROCURAR DADO A ATUALIZAR
def atualizar_dados():
    dados_cadastrados = carregar_dados()
    
    codigo_item_cadastrado = input('Digite o código do seu item cadastrado: ').strip()
    while True:
        menu_tipo_atualizacao()
        tipo_atualizar = int(input('Digite o tipo de atualização desejada: '))
        
        dados_atualizados = []
        
        for indice, linha in enumerate(dados_cadastrados):
            fabricante, modelo, codigo = linha.strip().split(',')
            if codigo_item_cadastrado == codigo:
                if tipo_atualizar == 1:
                    todas_propriedades = atualizar_todas_propriedades()
                    dados_atualizados.append(todas_propriedades)
                    
                elif tipo_atualizar == 2:
                    atualizar_fabricante = atualizar_somente_fabricante(fabricante, modelo, codigo)
                    
                    print(atualizar_fabricante)
                    input()
                    
                    dados_atualizados.append(atualizar_fabricante)
                        
                elif tipo_atualizar == 3:
                    atualizar_modelo = atualizar_somente_modelo(fabricante, modelo, codigo)
                    dados_atualizados.append(atualizar_modelo)
                    
                elif tipo_atualizar == 4:
                    atualizar_codigo = atualizar_somente_codigo(fabricante, modelo, codigo)
                    dados_atualizados.append(atualizar_codigo)    
                    
                    
            else:
                dados_atualizados.append(f'{fabricante},{modelo},{codigo}\n')
                    
        if tipo_atualizar == 5:
            print('SAINDO DO MENU DE ATUALIZAÇÕES....')
            break
                
        salvar_dados(dados_atualizados)
        
        
