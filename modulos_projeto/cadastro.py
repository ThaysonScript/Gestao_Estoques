# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃               ┃╺┳╸┏━┓┏━┓━━━━━━━━━━━━  ** cadastro.py **  ━━━━━━━━━━━━━━┏━┓┏━┓                ┃
# ┃               ┃┃┃┃┃┃┃┏┛     VERSÃO: 1.0                             ┏━┓┏━┛┏━┛                ┃
# ┃                ┃┃┗┛┗┛┃┃      AUTORES:                                                        ┃
# ┃                                  Thayson Guedes de Medeiros                                  ┃
# ┃                                  Thiago Ferreira dos Santos                                  ┃
# ┃               ┗┻━┓┏┓┏━┛     DATA DE CRIAÇÃO:                       ┃┏━┛┃ ┃┃                  ┃
# ┃                 ┗━┛┗┛           08 de setembro de 2023                ┗┛ ┗┛                  ┃
# ┃                                                                                              ┃
# ┃  DESCRIÇÃO:                                                                                  ┃
# ┃  Este módulo executa [ O cadastro de itens (com ao menos 3 propriedades) ].                  ┃
# ┃                                                                                              ┃
# ┃  LINKS ÚTEIS:                                                                                ┃
# ┃  - Repositório do projeto: [ https://github.com/ThaysonScript/python_code ]                  ┃
# ┃  - Repositório do módulo: [ https://github.com/ThaysonScript/python_code/blob/main/modulos_projeto/cadastro.py ] ┃
# ┃  - Documentação de descrições e requisitos do projeto: [ pasta: descricao_projeto ]          ┃
# ┃                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# LIBS PARA GERAR CODIGO ALEATORIO
import random   # GERAR VALOR ALEATORIO
import string   # GERAR CARACTERES DE STRING

import limpar_terminal  # LIMPEZA DE TERMINAL

# MENU DE TIPOS DISPONIVEIS DE CADASTRO
def menu_cadastro():
    print("\n'''''' MENU DE CADASTRO DE ITEMS ''''''''''\n")
    print('         CADASTRE FABRICANTE                 ')
    print('         CADASTRE MODELO                     ')
    print('         CADASTRE CODIGO                     ')
    print("\n'''''''''''''''''''''''''''''''''''''''''''\n")
    
# GERANDO CODIGO ALEATORIO E RETORNANDO PARA A CHAMADA  
def gerando_codigo_aleatorio():
    caracteres_gerados = string.ascii_letters + string.digits
    codigo_aleatorio = ''.join(random.choice(caracteres_gerados) for _ in range(0, 5))
    return codigo_aleatorio

# DESEJA GERAR CODIGO ALEATORIO?
def criar_codigo_aleatorio():
    while True:
        gerar_aleatorio = input('Deseja gerar código aleatório? ( "s" ou "n" ): ').lower()
    
        if gerar_aleatorio == 's':
            codigo_aleatorio = gerando_codigo_aleatorio()
            print('\nCódigo Aleatório criado com Sucesso!\n')
            return codigo_aleatorio
        
        elif gerar_aleatorio == 'n':
            codigo_n_aleatorio = input('Digite o codigo do item: ')
            return codigo_n_aleatorio
        
        else:
            limpar_terminal.limpar_terminal()
            print('Digite uma Entrada Válida!\n')
            input('Digite "Enter" para Continuar')
            limpar_terminal.limpar_terminal()


# NOVO ITEM A SER CADASTRADO ( FABRICANTE, MODELO, CODIGO )
def novos_items_a_cadastrar():
    novo_fabricante = input('Digite o nome da fabricante do item: ')
    novo_modelo = input('Digite o modelo do item: ')
    novo_codigo = criar_codigo_aleatorio()
    return f'{novo_fabricante},{novo_modelo},{novo_codigo}\n'     

# 2.2 CADASTRAR ITEMS (COM 3 PROPRIEDADES - FABRICANTE, MODELO, CODIGO)
def cadastro():     # FUNCAO PRINCIPAL
    menu_cadastro()
    with open('dados.csv', 'a') as dados_csv:
        novos_cadastros = novos_items_a_cadastrar()
        novo = novos_cadastros.split(',')
        if novo[0] == '' or novo[1] == '' or novo[2] == 'None\n' or novo[2] == '\n':
            limpar_terminal.limpar_terminal()
            print('Não pode ser adicionado cadastros vazios!\n')
            
        else:
            dados_csv.write(novos_cadastros)
            print("*********** SEU ITEM FOI CADASTRADO! ***********\n")
            
    print('Redirecionando para o Menu Principal....\n')
    input('Digite "Enter" para Continuar')
