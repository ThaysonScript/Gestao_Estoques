def dados_items():
    dados_totais = []
    with open('dados.txt', 'r') as dados:
        for dado in dados:
            fabricante, modelo, serial = dado.strip().split(',')
            dados_totais.append([fabricante, modelo, serial])
    return dados_totais

#  2.3. Opção para buscar por itens cadastrados (e suas propriedades)
def visualizar_item():    # tela para mostrar que entrou no menu de visualizar items cadastrados
    dados_cadastrados = dados_items()
    print("\n'''''' MENU DE VISUALIZAR ITEMS CADASTRADOS ''''''''''")
    print("[1].VISUALIZAR SE O ITEM ESTA CADASTRADO")
    print("[2].VISUALIZAR ALGUMA PROPRIEDADE DE UM ITEM")
    print("[3].SAIR DO MENU DE VISUALIZAR ITEMS CADASTRADOS")
    
    while True:
        escolha = input('Digite alguma das opções acima: ')
    
        # 2.3.1. busca por nome do item
        if escolha == '1':
            visualizar_por_nome(dados_totais = dados_cadastrados)    
                        
        #  2.3.2. busca por propriedade do item
        elif escolha == '2':
            visualizar_por_propriedade(dados_totais = dados_items)
            
        elif escolha == '3':
            print('Saindo do menu de visualizar items cadastrados....')
            break
        
        else:
            print('Digite um valor válido!')
     
    
def visualizar_por_nome(dados_totais):
    nome_fabricante_buscar = input('Digite o nome da fabricante do seu item cadastrado: ')
            
    for fabricante, modelo, serial in dados_totais:
    
        #  verificar se o nome da fabricante de entrada é igual aos dados cadastrados no dados.txt
        if nome_fabricante_buscar == fabricante:
            print(f'Seu item já esta cadastrado com sucesso com o nome da fabricante = {fabricante}')
            
            # 2.3.2. busca por propriedade do item      !( a partir do nome da fabricante ja lido de entrada )!
            print('Deseja ver as propriedades desse item? ')
            while True:
                deseja_ver = input(f'Digite "s" ou "n" para consultar as propriedades da fabricante {fabricante}: ').lower()
                
                if deseja_ver == 's':
                    '''pergunta:
                    ao digitar s, buscar todas as propriedades daquele fabricante 
                    ou pedir para o usuario digitar que tipo de propriedade do fabricante deseja ver como ( modelo ou serial/codigo )
                    '''
                    break
                    
                elif deseja_ver == 'n':
                    # nao buscar item
                    break
                
                else:
                    print('Digite somente "s" ou "n"')
    
    
# tela para mostrar que o usuario deve escolher alguma das propriedades disponiveis
def visualizar_por_propriedade():
    dados_cadastrados = dados_items()
    print("\n'''''' MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ''''''''''")
    print("[1].VISUALIZAR POR MODELO")
    print("[2].VISUALIZAR POR SERIAL/CODIGO DO ITEM CADASTRADO")
    
    buscar_item_por_propriedade = input('Digite alguma das opções acima: ')

    # buscar por modelo e retornar fabricante ou serial do item ja cadastrado
    if buscar_item_por_propriedade == '1':
        buscar_por_modelo(dados_totais = dados_cadastrados)
                
    # buscar por serial/codigo do item ja cadastrado e retornar fabricante ou modelo          
    elif buscar_item_por_propriedade == '2':
        buscar_por_serial(dados_totais = dados_cadastrados)
        
    
def buscar_por_modelo(dados_totais):
    digitar_modelo = input('Digite o modelo do seu item cadastrado: ')
    while True:
        deseja_ver_oque = input('Digite o que voce deseja ver a partir do seu modelo digitado ( fabricante ou serial ): ')
    
        if deseja_ver_oque not in ['fabricante', 'serial']:
            print('Digite somente "fabricante" ou "serial"')
            
        else:
            for fabricante, modelo, serial in dados_totais:
            
                # retornar fabricante do modelo do item ja cadastrado
                if deseja_ver_oque == 'fabricante' and digitar_modelo == modelo:
                    print(f'A fabricante do seu item com modelo = {digitar_modelo} é = {fabricante}')
                    
                # retornar serial do modelo do item ja cadastrado
                elif deseja_ver_oque == 'serial' and digitar_modelo == modelo:
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
                
                # retornar fabricante a partir do serial
                if deseja_ver_oque == 'fabricante' and digitar_serial == serial:
                    print(f'A fabricante do seu item com serial = {digitar_serial} é = {fabricante}')
                    
                # retornar modelo a partir do serial
                elif deseja_ver_oque == 'modelo' and digitar_serial == serial:
                    print(f'O modelo do seu item com serial = {digitar_serial} é = {modelo}')
                    
            break
