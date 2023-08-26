def cadastrar_item():
    with open('dados.txt', 'a') as dados_txt, open('dados.csv', 'a') as dados_csv:
        fabricante_item = input('Digite o nome da fabricante do item: ')
        modelo_item = input('Digite o modelo item: ')
        serial_item = input('Digite o serial/codigo do item: ')
        
        dados_txt.write(f'{fabricante_item},{modelo_item},{serial_item}\n')
        dados_csv.write(f'{fabricante_item},{modelo_item},{serial_item}\n')
        
        
cadastrar_item()