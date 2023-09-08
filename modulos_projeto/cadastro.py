# LIBS PARA GERAR CODIGO ALEATORIO
import random
import string

# MENU A SER MOSTRADO PARA O USUARIO AO ENTRAR EM CADASTRO DE ITEMS
def menu_cadastro():
    print("\n'''''' MENU DE CADASTRO DE ITEMS ''''''''''\n")
    print('         CADASTRE FABRICANTE                 ')
    print('         CADASTRE MODELO                     ')
    print('         CADASTRE CODIGO                     ')
    print("\n'''''''''''''''''''''''''''''''''''''''''''")
    
# GERANDO CODIGO ALEATORIO E RETORNANDO PARA A CHAMADA  
def gerando_codigo_aleatorio():
    caracteres_gerados = string.ascii_letters + string.digits
    codigo_aleatorio = ''.join(random.choice(caracteres_gerados) for _ in range(0, 5))
    return codigo_aleatorio

# DESEJA GERAR CODIGO ALEATORIO?
def criar_codigo_aleatorio():
    gerar_aleatorio = input('Deseja gerar código aleatório? ( "s" ou "n" ): ').lower()
    
    if gerar_aleatorio == 's':
        codigo_aleatorio = gerando_codigo_aleatorio()
        print('\nCódigo Aleatório criado com Sucesso!')
        return codigo_aleatorio
    
    elif gerar_aleatorio == 'n':
        codigo_n_aleatorio = input('Digite o codigo do item: ')
        return codigo_n_aleatorio
    
    else:
        print('Entrada Inválida\n')

# ITEM A SER CADASTRADO ( FABRICANTE, MODELO, CODIGO )
def novos_items_a_cadastrar():
    novo_fabricante = input('Digite o nome da fabricante do item: ')
    novo_modelo = input('Digite o modelo do item: ')
    novo_codigo = criar_codigo_aleatorio()
    return f'{novo_fabricante},{novo_modelo},{novo_codigo}\n'     

# 2.2 CADASTRAR ITEMS COM PELO MENOS 3 PROPRIEDADES
def cadastro():  
    menu_cadastro() 
    with open('dados.csv', 'a') as dados_csv:
        novos_cadastros = novos_items_a_cadastrar()
        novo = novos_cadastros.split(',')
        if novo[0] == '' or novo[1] == '' or novo[2] == 'None\n' or novo[2] == '\n':
            print('Não pode ser adicionado cadastros vazios!\n')
            
        else:
            dados_csv.write(novos_cadastros)
            print("\n*********** SEU ITEM FOI CADASTRADO! ***********\n")
            
    input('Pressione qualquer Tecla para Continuar')
