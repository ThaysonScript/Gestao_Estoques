import limpar_terminal

# CARREGAR DADOS CADASTRADOS
def carregar_items_armazenados():
    with open('dados.csv', 'r') as dados:
        return dados.readlines()

# REGISTRAR DADOS TOTAIS (ATUALIZADOS E ANTIGOS)
def salvar_items_armazenados(dados_atualizados):
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
    
def dado_a_ser_alterado_selecionado(fabricante, modelo, codigo):
    print(f"'''''''''DADOS DO PRODUTO SELECIONADO''''''''''")
    print(f'FABRICANTE: {fabricante}')
    print(f'MODELO: {modelo}')
    print(f'CÓDIGO: {codigo}')
    print("\n'''''''''''''''''''''''''''''''''''''''''''''''\n")
    
def dado_selecionado_foi_alterado(fabricante, modelo, codigo):
    print(f'DADOS DO PRODUTO ATUALIZADOS')
    print(f'FABRICANTE: {fabricante}')
    print(f'MODELO: {modelo}')
    print(f'CÓDIGO: {codigo}')

# ATUALIZAR TODAS AS PROPRIEDADES
def atualizar_todas_propriedades():
    nova_fabricante = input('Digite a nova fabricante: ').strip()
    novo_modelo = input('Digite o novo modelo: ').strip()
    novo_codigo = input('Digite o novo codigo: ').strip()
    return f'{nova_fabricante},{novo_modelo},{novo_codigo}\n'

# ATUALIZAR SOMENTE A FABRICANTE
def atualizar_somente_fabricante(fabricante, modelo, codigo):
    fabricante_atual = input('Digite a fabricante atual do seu item: ')

    dado_a_ser_alterado_selecionado(fabricante, modelo, codigo)
    novo_fabricante = input('Digite o novo fabricante que você quer inserir: ')
                            
    print('Seu fabricante foi atualizado com sucesso!')
    
    dado_selecionado_foi_alterado(novo_fabricante, modelo, codigo)
    return f'{novo_fabricante},{modelo},{codigo}\n'     
        
# ATUALIZAR SOMENTE O MODELO
def atualizar_somente_modelo(fabricante, modelo, codigo):
    modelo_atual = input('Digite o seu modelo atual: ')
    
    dado_a_ser_alterado_selecionado(fabricante, modelo, codigo)
    novo_modelo = input('Digite o novo modelo que você quer inserir:')
        
    print('Sucesso! Seu item foi atualizado com sucesso!')   
    
    dado_selecionado_foi_alterado(fabricante, novo_modelo, codigo)
    return f'{fabricante},{novo_modelo},{codigo}\n' 
    
# ATUALIZAR SOMENTE A CODIGO
def atualizar_somente_codigo(fabricante, modelo, codigo):
    print('Recuperamos o seu código de produto atual digitado nesta sessão')
    
    dado_a_ser_alterado_selecionado(fabricante, modelo, codigo)
    
    novo_codigo = input('Digite o novo codigo que você quer inserir:')
        
    print('Sucesso! Seu item foi atualizado com sucesso!')
    
    dado_selecionado_foi_alterado(fabricante, modelo, novo_codigo)
    return f'{fabricante},{modelo},{novo_codigo}\n'

# PROCURAR DADO A ATUALIZAR
def atualizar_dados():
    limpar_terminal.limpar_terminal()
    dados_cadastrados = carregar_items_armazenados()
    
    codigo_item_cadastrado = input('Digite o código do seu item cadastrado: ').strip()
    while True:
        menu_tipo_atualizacao()
        tipo_atualizar = int(input('Digite o tipo de atualização desejada: '))
        
        limpar_terminal.limpar_terminal()
        
        dados_atualizados = []
        
        for indice, linha in enumerate(dados_cadastrados):
            fabricante, modelo, codigo = linha.strip().split(',')
            if codigo_item_cadastrado == codigo:
                if tipo_atualizar == 1:
                    todas_propriedades = atualizar_todas_propriedades()
                    dados_atualizados.append(todas_propriedades)
                    limpar_terminal.limpar_terminal()
                    print('Atualizado com Sucesso!')
                    input('Pressione qualquer Tecla')                    
                    
                elif tipo_atualizar == 2:
                    atualizar_fabricante = atualizar_somente_fabricante(fabricante, modelo, codigo)
                    dados_atualizados.append(atualizar_fabricante)
                    limpar_terminal.limpar_terminal()
                    print('Atualizado com Sucesso!')
                    input('Pressione qualquer Tecla')                    
                        
                elif tipo_atualizar == 3:
                    atualizar_modelo = atualizar_somente_modelo(fabricante, modelo, codigo)
                    dados_atualizados.append(atualizar_modelo)
                    limpar_terminal.limpar_terminal()
                    print('Atualizado com Sucesso!')
                    input('Pressione qualquer Tecla')                    
                    
                elif tipo_atualizar == 4:
                    atualizar_codigo = atualizar_somente_codigo(fabricante, modelo, codigo)
                    dados_atualizados.append(atualizar_codigo) 
                    limpar_terminal.limpar_terminal() 
                    print('Atualizado com Sucesso!')
                    input('Pressione qualquer Tecla') 
                     
                    
            else:
                dados_atualizados.append(f'{fabricante},{modelo},{codigo}\n')
                    
        if tipo_atualizar == 5:
            print('SAINDO DO MENU DE ATUALIZAÇÕES....')
            break
                
        salvar_items_armazenados(dados_atualizados)
