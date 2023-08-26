# tela para mostrar que entrou no menu de cadastro de items
def menu_cadastrar_item():
    print("\n'''''' MENU DE CADASTRO DE ITEMS ''''''''''")


# 2.2. Opção para cadastrar itens (com ao menos 3 propriedades)
def cadastrar_item():
    menu_cadastrar_item()
    
    # adicionar alteracoes tanto em txt como csv
    with open('dados.txt', 'a') as dados_txt, open('dados.csv', 'a') as dados_csv:
        
        # 3 propriedades que podem ser cadastradas ( fabricante, modelo, serie/codigo do produto )
        fabricante_item = input('Digite o nome da fabricante do item: ')
        modelo_item = input('Digite o modelo item: ')
        serial_item = input('Digite o serial/codigo do item: ')
        
        # salvando alteracoes em txt e csv
        dados_txt.write(f'{fabricante_item},{modelo_item},{serial_item}\n')
        dados_csv.write(f'{fabricante_item},{modelo_item},{serial_item}\n')
        
    # sucesso ao cadastrar item
    print("\n'''''' ITEM CADASTRADO COM SUCESSO ''''''''''\n")
