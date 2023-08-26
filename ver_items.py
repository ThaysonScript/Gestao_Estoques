# tela para mostrar que entrou no menu de visualizar items cadastrados
def menu_visualizar_items():
    print("\n'''''' MENU DE VISUALIZAR ITEMS CADASTRADOS ''''''''''")
    print("[1].VISUALIZAR SE O ITEM ESTA CADASTRADO")
    print("[2].VISUALIZAR ALGUMA PROPRIEDADE DE UM ITEM")
    print("[3].SAIR DO MENU DE VISUALIZAR ITEMS CADASTRADOS")
    
    
# tela para mostrar que o usuario deve escolher alguma das propriedades disponiveis
def menu_propriedades_busca():
    print("\n'''''' MENU DE VISUALIZAR PROPRIEDADES DE UM ITEM CADASTRADO ''''''''''")
    print("[1].VISUALIZAR POR MODELO")
    print("[2].VISUALIZAR POR SERIAL/CODIGO DO ITEM CADASTRADO")
    


#  2.3. Opção para buscar por itens cadastrados (e suas propriedades)
def visualizar_item():
    menu_visualizar_items()
    
    dados_totais = []
    with open('dados.txt', 'r') as dados:
        escolha = input('Digite alguma das opções acima: ')
        
        for dado in dados:
            fabricante, modelo, serial = dado.strip().split(',')
            
            dados_totais.append([fabricante, modelo, serial])
            
            
        if escolha == '1':
            nome_fabricante_buscar = input('Digite o nome da fabricante do seu item cadastrado: ')
            
            for dado in dados_totais:
                fabricante, modelo, serial = dado
            
                #  2.3.1. busca por nome do item
                if nome_fabricante_buscar == fabricante:
                    print(f'Seu item já esta cadastrado com sucesso com o nome da fabricante = {fabricante}')
                    
                    # 2.3.2. busca por propriedade do item
                    print('Deseja ver as propriedades desse item? ')
                    deseja_ver = input(f'Digite "s" ou "n" para consultar as propriedades da fabricante: {fabricante}').lower()
                    
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
                        print('Terminando consulta....')
                        
                        
        elif escolha == '2':
            menu_propriedades_busca()
            buscar_item_por_propriedade = input('Digite alguma das opções acima: ')
            
            if buscar_item_por_propriedade == '1':
                digitar_modelo = input('Digite o modelo do seu item cadastrado: ')
                
                deseja_ver_oque = input('Digite o que voce deseja ver a partir do seu modelo digitado ( fabricante ou serial ): ')
                
                for dado in dados_totais:
                    fabricante, modelo, serial = dado
                    
                    if deseja_ver_oque == 'fabricante' and digitar_modelo == modelo:
                        print(f'A fabricante do seu item com modelo = {digitar_modelo} é = {fabricante}')
                        
                    elif deseja_ver_oque == 'serial' and digitar_modelo == modelo:
                        print(f'O serial/codigo do seu item com modelo = {digitar_modelo} é = {serial}')
                        
                        
            elif buscar_item_por_propriedade == '2':
                digitar_serial = input('Digite o serial/codigo do seu item cadastrado: ')
                
                deseja_ver_oque = input('Digite o que voce deseja ver a partir do seu modelo digitado ( fabricante ou modelo ): ')
                
                for dado in dados_totais:
                    fabricante, modelo, serial = dado
                    
                    if deseja_ver_oque == 'fabricante' and digitar_serial == serial:
                        print(f'A fabricante do seu item com serial = {digitar_serial} é = {fabricante}')
                        
                    elif deseja_ver_oque == 'modelo' and digitar_serial == serial:
                        print(f'O modelo do seu item com serial = {digitar_serial} é = {modelo}')