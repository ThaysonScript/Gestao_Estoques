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
    while True:
        fabricante_atual = input('Digite a fabricante atual do seu item: ')

        if fabricante_atual != fabricante:
            print('Modelo atual incorreto! Por Favor digite o modelo correto do seu item cadastrado.')
            
        elif fabricante_atual == fabricante:
            dado_a_ser_alterado_selecionado(fabricante, modelo, codigo)
            novo_fabricante = input('Digite o novo fabricante que você quer inserir: ')
                                    
            print('Seu fabricante foi atualizado com sucesso!')
            
            dado_selecionado_foi_alterado(novo_fabricante, modelo, codigo)
            return f'{novo_fabricante},{modelo},{codigo}\n'     
        
# ATUALIZAR SOMENTE O MODELO
def atualizar_somente_modelo(fabricante, modelo, codigo):
    while True:
        modelo_atual = input('Digite o seu modelo atual: ')
        
        if modelo_atual != modelo:
            print('Modelo atual incorreto! Por Favor digite o modelo correto do seu item cadastrado.')
        
        elif modelo_atual == modelo:
            dado_a_ser_alterado_selecionado(fabricante, modelo, codigo)
            novo_modelo = input('Digite o novo modelo que você quer inserir:')
                
            print('Sucesso! Seu item foi atualizado com sucesso!')   
            
            dado_selecionado_foi_alterado(fabricante, novo_modelo, codigo)
            return f'{fabricante},{novo_modelo},{codigo}\n' 
    
# ATUALIZAR SOMENTE A CODIGO
def atualizar_somente_codigo(fabricante, modelo, codigo):
    print('Recuperamos o seu código de produto atual digitado nesta sessão\n')
    dado_a_ser_alterado_selecionado(fabricante, modelo, codigo)
    
    novo_codigo = input('Digite o novo codigo que você quer inserir:')
        
    print('Sucesso! Seu item foi atualizado!')
    
    dado_selecionado_foi_alterado(fabricante, modelo, novo_codigo)
    
    return f'{fabricante},{modelo},{novo_codigo}\n'


def tipo_escolha_atualizacao(dados_cadastrados, codigo_item_cadastrado, tipo_atualizar):
    dados_atualizados = []
    for linha in dados_cadastrados:
        fabricante, modelo, codigo = linha.strip().split(',')
        
        if codigo_item_cadastrado == codigo:
            if tipo_atualizar == '1':
                limpar_terminal.limpar_terminal()
                todas_propriedades = atualizar_todas_propriedades()
                dados_atualizados.append(todas_propriedades)
                limpar_terminal.limpar_terminal()
                print('Atualizado com Sucesso!')
                input('Pressione "Enter" para Continuar')                 
                
            elif tipo_atualizar == '2':
                limpar_terminal.limpar_terminal()
                atualizar_fabricante = atualizar_somente_fabricante(fabricante, modelo, codigo)
                dados_atualizados.append(atualizar_fabricante)
                limpar_terminal.limpar_terminal()
                print('Atualizado com Sucesso!')
                input('Pressione "Enter" para Continuar')                    
                    
            elif tipo_atualizar == '3':
                limpar_terminal.limpar_terminal()
                atualizar_modelo = atualizar_somente_modelo(fabricante, modelo, codigo)
                dados_atualizados.append(atualizar_modelo)
                limpar_terminal.limpar_terminal()
                print('Atualizado com Sucesso!')
                input('Pressione "Enter" para Continuar')                    
                
            elif tipo_atualizar == '4':
                limpar_terminal.limpar_terminal()
                atualizar_codigo = atualizar_somente_codigo(fabricante, modelo, codigo)
                dados_atualizados.append(atualizar_codigo) 
                limpar_terminal.limpar_terminal() 
                print('Atualizado com Sucesso!')
                input('Pressione "Enter" para Continuar')
                
        else:
            dados_atualizados.append(f'{fabricante},{modelo},{codigo}\n')
            
    return dados_atualizados    
    
# PROCURAR DADO A ATUALIZAR
def atualizar_dados(pesquisa_avancada=False):
    limpar_terminal.limpar_terminal()
    dados_cadastrados = carregar_items_armazenados()
    
    while True:    
        codigo_item_cadastrado = input('Digite o código do seu item cadastrado: ').strip()    
        if codigo_item_cadastrado != '':
            menu_tipo_atualizacao()
            tipo_atualizar = input('Digite o tipo de atualização desejada: ')
            
            if tipo_atualizar == '' or tipo_atualizar >= '6' or tipo_atualizar <= '0':
                limpar_terminal.limpar_terminal()
                print('\nDigite Somente Entradas Válidas!\n')
                print('Redirecionando para o Menu Principal....')
                input('\nPressione "Enter" para Continuar')
                limpar_terminal.limpar_terminal()
                break
        
            elif tipo_atualizar == '5':
                print('Saindo do Menu de Atualizações....')
                input('Pressione "Enter" para Continuar')
                break
            
            else:
                dados_atualizados = tipo_escolha_atualizacao(dados_cadastrados, codigo_item_cadastrado, tipo_atualizar)
                                            
                salvar_items_armazenados(dados_atualizados)
                limpar_terminal.limpar_terminal()
                break
                
        else:
            limpar_terminal.limpar_terminal()
            print('\nDigite um codigo válido!\n')
            input('Pressione "Enter" para Continuar')
            limpar_terminal.limpar_terminal()