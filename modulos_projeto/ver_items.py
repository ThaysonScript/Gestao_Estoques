import limpar_terminal

# CARREGAR DADOS CADASTRADOS
def carregar_dados():
    dados_totais = []
    with open('dados.csv', 'r') as dados:
        for dado in dados:
            fabricante, modelo, codigo = dado.strip().split(',')
            dados_totais.append([fabricante, modelo, codigo])
    return dados_totais

# MENU PARA ACESSAR TIPO DE VISUALIZACAO
def menu_ver_items():
    print("\n'''''' MENU DE VISUALIZAR ITEMS CADASTRADOS ''''''''''\n")
    print("[1].VISUALIZAR SE O ITEM ESTA CADASTRADO")
    print("[2].VISUALIZAR ALGUMA PROPRIEDADE DE UM ITEM")
    print("[3].SAIR DO MENU DE VISUALIZAR ITEMS CADASTRADOS\n")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    
  
# MENU PARA VISUALIZAR POR UM DADO JA CADASTRADO E RETORNAR OUTRO, COMO, FABRICANTE -> MODELO/CODIGO  
def menu_visualizar_por_propriedade():
    print("\n'''''' MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ''''''''''\n")
    print("VISUALIZAR A PARTIR DE FABRICANTE ( DIGITE: fabricante )")
    print("VISUALIZAR A PARTIR DE MODELO ( DIGITE: modelo )")
    print("VISUALIZAR A PARTIR DE CODIGO DO ITEM CADASTRADO ( DIGITE: codigo )")
    print("SAIR DO MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ( DIGITE: sair )")
    print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    
    
# MENU DE CONSULTA QUE RETORNA O TIPO BUSCA QUE PODE SER ACESSADO
def menu_disponivel_busca_por_propriedades(tipo):
    print("\n'''''' MENU DE TIPOS DE BUSCAS POR PROPRIEDADES DISPONIVEIS ''''''''''\n")
    
    if tipo == 'fabricante':
        print("MODELO OU CÓDIGO")
        print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return 'modelo ou codigo'
        
    elif tipo == 'modelo':
        print("FABRICANTE OU CÓDIGO")
        print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return 'fabricante ou codigo'
        
    elif tipo == 'codigo':
        print("FABRICANTE OU MODELO")
        print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return 'fabricante ou modelo'
        
    elif tipo == 'sair':
        print("[4].SAIR DO MENU DE TIPOS DE BUSCAS POR PROPRIEDADES DISPONIVEIS")
        
    

# MOSTRAR MENSAGEM DO FABRICANTE, CASO ENCONTRADO NO ESTOQUE
def resultado_busca_por_nome(fabricante):
    print(f"\n''''''''''''' RESULTADO DA BUSCA POR NOME DA FABRICANTE ''''''''''''''\n")
    print(f'O item com nome de fabricante = {fabricante} se encontra cadastrada no sistema!')
    print("\n'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    
    print('Deseja ver as propriedades desse item? ')  # VER PROPRIEDADES DA FABRICANTE CONSULTADA
    
    
# RETORNAR TODAS AS PROPRIEDADES CASO USUARIO DIGITAR S PARA VER PROPRIEDADES DAQUELA FABRICANTE CONSULTADA
def resultado_busca_propriedades_fabricante(fabricante, modelo, codigo):
    print(f"\n''''''PROPRIEDADES DO ITEM '''''''''\n")
    print(f"  [1].FABRICANTE: '{fabricante}'")
    print(f"  [2].MODELO: '{modelo}'")
    print(f"  [3].CÓDIGO: '{codigo}'")
    print(f"\n'''''''''''''''''''''''''''''''''''")
    
# CARREGAR FUNCAO PRINCIPAL QUE EXECUTA A VISUALIZACAO DE ITEMS CADASTRADOS
def ver_items():
    dados_armazenados = carregar_dados()
    while True:
        limpar_terminal.limpar_terminal()
        menu_ver_items()
        escolha = int(input('Digite alguma das opções acima: '))
    
        if escolha == 1:
            limpar_terminal.limpar_terminal()
            ver_por_nome(dados_armazenados)    
                        
        elif escolha == 2:
            limpar_terminal.limpar_terminal()
            ver_por_propriedade(dados_armazenados)
            
        elif escolha == 3:
            limpar_terminal.limpar_terminal()
            print('Saindo do menu de visualizar items cadastrados....')
            break
        
        else:
            print('Digite um valor válido! (somente numeros)')
     

# VER ITEMS CADASTRADOS POR NOME ( FABRICANTE )
def ver_por_nome(dados_totais):
    buscar_fabricante = input('\nDigite o nome da fabricante do seu item cadastrado: ')
            
    for fabricante, modelo, codigo in dados_totais:
        if buscar_fabricante == fabricante:
            resultado_busca_por_nome(fabricante)
            
            ver_propriedades_fabricante = input(f'Digite ( s/n ) para consultar as propriedades da fabricante {fabricante}: ').strip().lower()
            
            if ver_propriedades_fabricante == 's':
                resultado_busca_propriedades_fabricante(fabricante, modelo, codigo)
                input('Pressione qualquer Tecla: ')
                break
                
            elif ver_propriedades_fabricante == 'n':
                print(f"\nSaindo da consulta de propriedade atrelada a fabricante: '{fabricante}'\n")
                input('Pressione qualquer Tecla: ')
                break
            
            else:
                print('\nDigite somente ( s/n )')

   
# MOSTRAR PROPRIEDADE QUE PODE SER ACESSADA
def ver_por_propriedade(dados_armazenados):
    while True:
        menu_visualizar_por_propriedade()
        buscar_item_por_propriedade = input('Digite alguma das opções acima: ').strip()

        if buscar_item_por_propriedade in ['fabricante', 'modelo', 'codigo']:
            tipo_busca_propriedade(dados_armazenados, buscar_item_por_propriedade)
            
        elif buscar_item_por_propriedade == 'sair':
            print('Saindo do menu de visualizar propriedades de um item cadastrado....')
            break
        else:
            print('Digite uma opção acima válida')
 
 
#  VER PROPRIEDADE A PARTIR DE DADO DE ENTRADA ESPECIFICO (FABRICANTE, MODELO, CODIGO)
def tipo_busca_propriedade(dados_totais, tipo):
    menu_disponivel = menu_disponivel_busca_por_propriedades(tipo)
    
    if tipo not in ['fabricante', 'modelo', 'codigo']:
        print('Digite somente "fabricante, modelo" ou "codigo"')
        
    elif tipo in ['fabricante', 'modelo', 'codigo']:
        tipo_acesso = input(f'Digite o tipo de acesso que deseja ver a partir da {tipo} do item ({menu_disponivel}): ')
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