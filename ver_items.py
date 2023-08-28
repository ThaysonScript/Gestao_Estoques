def dados_items():
    dados_totais = []
    with open('dados.txt', 'r') as dados:
        for dado in dados:
            fabricante, modelo, serial = dado.strip().split(',')
            dados_totais.append([fabricante, modelo, serial])
    return dados_totais

def visualizar_item():
    dados_cadastrados = dados_items()
    while True:
        print("\n'''''' MENU DE VISUALIZAR ITEMS CADASTRADOS ''''''''''\n")
        print("[1].VISUALIZAR SE O ITEM ESTA CADASTRADO")
        print("[2].VISUALIZAR ALGUMA PROPRIEDADE DE UM ITEM")
        print("[3].SAIR DO MENU DE VISUALIZAR ITEMS CADASTRADOS\n")
        print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        
        escolha = input('Digite alguma das opções acima: ')
    
        if escolha == '1':
            visualizar_por_nome(dados_cadastrados)    
                        
        elif escolha == '2':
            visualizar_por_propriedade(dados_cadastrados)
            
        elif escolha == '3':
            print('Saindo do menu de visualizar items cadastrados....')
            break
        
        else:
            print('Digite um valor válido!')
     
    
def visualizar_por_nome(dados_totais):
    nome_fabricante_buscar = input('\nDigite o nome da fabricante do seu item cadastrado: ')
            
    for fabricante, modelo, serial in dados_totais:
    
        if nome_fabricante_buscar == fabricante:
            print(f"\n''''''''''''' RESULTADO DA BUSCA POR NOME DA FABRICANTE ''''''''''''''\n")
            print(f'O item com nome de fabricante = {fabricante} se encontra cadastrada no sistema!')
            print("\n'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
            
            print('\nDeseja ver as propriedades desse item? ')
            while True:
                deseja_ver = input(f'Digite "s" ou "n" para consultar as propriedades da fabricante {fabricante}: ').lower()
                
                if deseja_ver == 's':
                    print(f"\n''''''PROPRIEDADES DO ITEM '''''''''\n")
                    print(f"  [1].FABRICANTE: '{fabricante}'")
                    print(f"  [2].MODELO: '{modelo}'")
                    print(f"  [3].SERIAL/CÓDIGO: '{serial}'")
                    print(f"\n'''''''''''''''''''''''''''''''''''")

                    break
                    
                elif deseja_ver == 'n':
                    print(f"Saindo da consulta de propriedade atrelada a fabricante: '{fabricante}'")
                    break
                
                else:
                    print('\nDigite somente "s" ou "n"')
    
    
def visualizar_por_propriedade(dados_cadastrados):
    while True:
        print("\n'''''' MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ''''''''''\n")
        print("[1].VISUALIZAR POR MODELO")
        print("[2].VISUALIZAR POR SERIAL/CODIGO DO ITEM CADASTRADO")
        print("[3].SAIR DO MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO")
        print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        
        buscar_item_por_propriedade = input('Digite alguma das opções acima: ')

        if buscar_item_por_propriedade == '1':
            buscar_por_modelo(dados_totais = dados_cadastrados)
                            
        elif buscar_item_por_propriedade == '2':
            buscar_por_serial(dados_totais = dados_cadastrados)
            
        elif buscar_item_por_propriedade == '3':
            print('Saindo do menu de visualizar propriedades de um item cadastrado....')
            break
        else:
            print('Digite uma opção acima válida')
        
    
def buscar_por_modelo(dados_totais):
    digitar_modelo = input('Digite o modelo do seu item cadastrado: ')
    while True:
        deseja_ver_oque = input('Digite o que voce deseja ver a partir do seu modelo digitado ( fabricante ou serial ): ')
    
        if deseja_ver_oque not in ['fabricante', 'serial']:
            print('Digite somente "fabricante" ou "serial"')
            
        else:
            for fabricante, modelo, serial in dados_totais:
                if deseja_ver_oque == 'fabricante':
                    if digitar_modelo == modelo:
                        print(f'A fabricante do seu item com modelo = {digitar_modelo} é = {fabricante}')
                    
                elif deseja_ver_oque == 'serial':
                    if digitar_modelo == modelo:
                        print(f'O serial/codigo do seu item com modelo = {digitar_modelo} é = {serial}')
                    
            break
            
            
def buscar_por_serial(dados_totais):
    digitar_serial = input('Digite o serial/codigo do seu item cadastrado: ')
    
    while True:
        deseja_ver_oque = input('Digite o que voce deseja ver a partir do seu serial/codigo do item digitado ( fabricante ou modelo ): ')
        
        if deseja_ver_oque not in ['fabricante', 'modelo']:
            print('Digite somente "fabricante" ou "modelo"')
            
        else:
            for fabricante, modelo, serial in dados_totais:
                if deseja_ver_oque == 'fabricante':
                    if digitar_serial == serial:
                        print(f'A fabricante do seu item com serial = {digitar_serial} é = {fabricante}')
                    
                elif deseja_ver_oque == 'modelo':
                    if digitar_serial == serial:
                        print(f'O modelo do seu item com serial = {digitar_serial} é = {modelo}')
                    
            break
