def cadastrar_item():
    print("\n'''''' MENU DE CADASTRO DE ITEMS ''''''''''")
    
    with open('dados.txt', 'a') as dados_txt:
        
        fabricante_item = input('Digite o nome da fabricante do item: ')
        modelo_item = input('Digite o modelo item: ')
        serial_item = input('Digite o serial/codigo do item: ')
        
        dados_txt.write(f'{fabricante_item},{modelo_item},{serial_item}\n')
        
    print("\n*********** ITEM CADASTRADO COM SUCESSO ***********")
