import limpar_terminal

# CARREGAR DADOS CADASTRADOS
def carregar_items_csv():
    with open('dados.csv', 'r') as dados:
        return [linha.strip().split(',') for linha in dados]

# MENU PARA ACESSAR TIPO DE VISUALIZACAO
def menu_tipo_visualizacao():
    print("\n'''''' MENU DE VISUALIZAR ITEMS CADASTRADOS ''''''''''\n")
    print("[1].VISUALIZAR SE O ITEM ESTA CADASTRADO")
    print("[2].VISUALIZAR ALGUMA PROPRIEDADE DE UM ITEM")
    print("[3].SAIR DO MENU DE VISUALIZAR ITEMS CADASTRADOS\n")
    print("\n'''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    
  
# MENU PARA VISUALIZAR POR UM DADO JA CADASTRADO E RETORNAR OUTRO, COMO, FABRICANTE -> MODELO/CODIGO  
def menu_visualizar_por_propriedade():
    print("\n'''''' MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ''''''''''\n")
    print("VISUALIZAR A PARTIR DE FABRICANTE ( DIGITE: fabricante )")
    print("VISUALIZAR A PARTIR DE MODELO ( DIGITE: modelo )")
    print("VISUALIZAR A PARTIR DE CODIGO DO ITEM CADASTRADO ( DIGITE: codigo )")
    print("SAIR DO MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ( DIGITE: sair )")
    print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    
    
# MENU DE CONSULTA QUE RETORNA O TIPO BUSCA QUE PODE SER ACESSADO
def tipo_disponivel_busca_propriedade(tipo):
    buscas = {
        'fabricante': 'MODELO OU CÓDIGO',
        'modelo': 'FABRICANTE OU CÓDIGO',
        'codigo': 'FABRICANTE OU MODELO',
        'sair': '[4].SAIR DO MENU DE TIPOS DE BUSCAS POR PROPRIEDADES DISPONIVEIS'
    }
    
    print("\n'''''' MENU DE TIPOS DE BUSCAS POR PROPRIEDADES DISPONIVEIS ''''''''''\n")
    
    if tipo in buscas:
        print(buscas[tipo])
        print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return buscas[tipo].lower()
    
    else:
        print("Opção inválida")
        
# MOSTRAR MENSAGEM DO FABRICANTE, CASO ENCONTRADO NO ESTOQUE
def resultado_por_nome(fabricante):
    print("\n''''''''''''' RESULTADO DA BUSCA POR NOME DA FABRICANTE ''''''''''''''\n")
    print(f'O item com nome de fabricante = {fabricante} se encontra cadastrada no sistema!')
    print("\n'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")    
    
# RETORNAR TODAS AS PROPRIEDADES CASO USUARIO DIGITAR S PARA VER PROPRIEDADES DAQUELA FABRICANTE CONSULTADA
def resultado_propriedades_nome(fabricante, modelo, codigo):
    print(f"\n''''''PROPRIEDADES DO ITEM '''''''''\n")
    print(f"  [1].FABRICANTE: '{fabricante}'")
    print(f"  [2].MODELO: '{modelo}'")
    print(f"  [3].CÓDIGO: '{codigo}'")
    print(f"\n'''''''''''''''''''''''''''''''''''\n")
     

# VER ITEMS CADASTRADOS POR NOME ( FABRICANTE )
def ver_por_nome(dados_totais):
    fabricante_do_usuario = input('\nDigite o nome da fabricante do seu item cadastrado: ')
            
    for fabricante, modelo, codigo in dados_totais:
        if fabricante_do_usuario == fabricante:
            resultado_por_nome(fabricante)
            
            print('Deseja ver as propriedades desse item? ')            
            visualizar_propriedades = input(f'Digite "s" ou "n" para consultar as propriedades da fabricante {fabricante}: ').strip().lower()
            
            if visualizar_propriedades == 's':
                resultado_propriedades_nome(fabricante, modelo, codigo)
                input('Pressione qualquer Tecla')
                
            elif visualizar_propriedades == 'n':
                print(f"\nSaindo da consulta de propriedade atrelada a fabricante: '{fabricante}'\n")
                input('Pressione qualquer Tecla')
            
            else:
                print('\nDigite somente "s" ou "n"')
              
                
#  VER PROPRIEDADE A PARTIR DE DADO DE ENTRADA ESPECIFICO (FABRICANTE, MODELO, CODIGO)
def tipo_busca_propriedade(dados_totais, tipo):
    busca_disponivel = tipo_disponivel_busca_propriedade(tipo)
    
    if tipo not in ['fabricante', 'modelo', 'codigo']:
        print('Digite somente "fabricante, modelo" ou "codigo"')
        
    elif tipo in ['fabricante', 'modelo', 'codigo']:
        tipo_acesso = input(f'Digite o tipo de acesso que deseja ver a partir da {tipo} do item ({busca_disponivel}): ')
        
        tipo_dado_armazenado = input(f'\nDigite o {tipo} do item: ').strip()
        
        limpar_terminal.limpar_terminal()
        
        for fabricante, modelo, codigo in dados_totais:
            if tipo == 'fabricante' and tipo_dado_armazenado == fabricante:
                if tipo_acesso == 'modelo':
                    print(f'O {tipo_acesso} do seu item com fabricante = {tipo_dado_armazenado} é = {modelo}')
                
                elif tipo_acesso == 'codigo':
                    print(f'O {tipo_acesso} do seu item com fabricante = {tipo_dado_armazenado} é = {codigo}')
                    
            elif tipo == 'modelo' and tipo_dado_armazenado == modelo:
                if tipo_acesso == 'fabricante':
                    print(f'A {tipo_acesso} do seu item com modelo = {tipo_dado_armazenado} é = {fabricante}')
                
                elif tipo_acesso == 'codigo':
                    print(f'O {tipo_acesso} do seu item com modelo = {tipo_dado_armazenado} é = {codigo}')
                    
            elif tipo == 'codigo' and tipo_dado_armazenado == codigo:
                if tipo_acesso == 'fabricante':
                    print(f'A {tipo_acesso} do seu item com codigo = {tipo_dado_armazenado} é = {fabricante}')
                
                elif tipo_acesso == 'modelo':
                    print(f'O {tipo_acesso} do seu item com codigo = {tipo_dado_armazenado} é = {modelo}')              
    else:
        print('Erro de tipo de acesso')
        
    input('Pressione qualquer Tecla: ')
    limpar_terminal.limpar_terminal()
   

# MOSTRAR PROPRIEDADE QUE PODE SER ACESSADA
def ver_por_propriedade(items_armazenados):
        menu_visualizar_por_propriedade()
        tipo_busca = input('Digite alguma das opções acima: ').strip()

        if tipo_busca in ['fabricante', 'modelo', 'codigo']:
            tipo_busca_propriedade(items_armazenados, tipo_busca)
            
        elif tipo_busca == 'sair':
            print('Saindo do menu de visualizar propriedades de um item cadastrado....')
            
        else:
            print('Digite uma opção acima válida')    
    

# CARREGAR FUNCAO PRINCIPAL QUE EXECUTA A VISUALIZACAO DE ITEMS CADASTRADOS
def ver_items():
    try:
        items_armazenados = carregar_items_csv()
        limpar_terminal.limpar_terminal()
        
        menu_tipo_visualizacao()
        tipo_de_visualizacao = int(input('Digite alguma das opções acima: '))
    
        if tipo_de_visualizacao == 1:
            limpar_terminal.limpar_terminal()
            ver_por_nome(items_armazenados)    
                        
        elif tipo_de_visualizacao == 2:
            limpar_terminal.limpar_terminal()
            ver_por_propriedade(items_armazenados)
            
        elif tipo_de_visualizacao == 3:
            limpar_terminal.limpar_terminal()
            print('Saindo do menu de visualizar items cadastrados....')
        
        else:
            print('Digite um valor válido! (somente numeros)')
            
    except FileNotFoundError:
        print('Arquivo.csv não existe, cadastre um novo item para executar essa consulta!')
        input('Pressione qualquer Tecla para Continuar')
