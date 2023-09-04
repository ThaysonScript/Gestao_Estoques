# GERAR CODIGO ALEATORIO
import random
import string


# MENU A SER MOSTRADO PARA O USUARIO AO ENTRAR EM CADASTRO DE ITEMS
def menu_cadastro():
    print("\n'''''' MENU DE CADASTRO DE ITEMS ''''''''''")
    
    
# OUTPUT DE ITEM COM SUCESSO AO CADASTRAR
def sucesso_ao_cadastrar():
    print("\n*********** ITEM CADASTRADO COM SUCESSO ***********")
    
    
#GERAR CODIGO ALEATORIO PARA UM ITEM A SER CADASTRADO    
def gerar_codigo_aleatorio():
    caracteres_gerados = string.ascii_letters + string.digits
    codigo_aleatorio = ''.join(random.choice(caracteres_gerados) for _ in range(0, 5))
    return codigo_aleatorio


# ITEM A SER CADASTRADO ( FABRICANTE, MODELO, CODIGO )
def items_entrada():
    fabricante = input('Digite o nome da fabricante do item: ')
    modelo = input('Digite o modelo do item: ')
    
    while True:
        cod_aleatorio = input('Deseja gerar código aleatório? ( "s" ou "n" ): ').lower()
        if cod_aleatorio == 's':
            codigo = gerar_codigo_aleatorio()
            break
        elif cod_aleatorio == 'n':
            codigo = input('Digite o codigo do item: ')
            break
        else:
            print('Entrada Inválida\n')
        
    return f'{fabricante},{modelo},{codigo}\n'
    
    
# 2.2 CADASTRAR ITEMS COM PELO MENOS 3 PROPRIEDADES
def cadastro():  
    menu_cadastro() 
    with open('dados.csv', 'a') as dados_csv:
        item_a_cadastrar = items_entrada()
        dados_csv.write(item_a_cadastrar)
        sucesso_ao_cadastrar()
