# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃               ┃╺┳╸┏━┓┏━┓━━━━━━━━  ** menu_pesquisa.py **  ━━━━━━━━━━━┏━┓┏━┓                  ┃
# ┃               ┃┃┃┃┃┃┃┏┛     VERSÃO: 1.0                             ┏━┓┏━┛┏━┛                ┃
# ┃                ┃┃┗┛┗┛┃┃      AUTORES:                                                        ┃
# ┃                                  Thayson Guedes de Medeiros                                  ┃
# ┃                                  Thiago Ferreira dos Santos                                  ┃
# ┃               ┗┻━┓┏┓┏━┛     DATA DE CRIAÇÃO:                       ┃┏━┛┃ ┃┃                  ┃
# ┃                 ┗━┛┗┛           08 de setembro de 2023                ┗┛ ┗┛                  ┃
# ┃                                                                                              ┃
# ┃  DESCRIÇÃO:                                                                                  ┃
# ┃  Este módulo executa [ o menu da pesquisa melhorada de items ].                              ┃
# ┃                                                                                              ┃
# ┃  LINKS ÚTEIS:                                                                                ┃
# ┃  - Repositório do projeto: [ https://github.com/ThaysonScript/python_code ]                  ┃
# ┃  - Repositório do módulo: [ https://github.com/ThaysonScript/python_code/blob/main/modulos_pesquisas/menu_pesquisa.py ] ┃
# ┃  - Documentação de descrições e requisitos do projeto: [ pasta: descricao_projeto ]          ┃
# ┃                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from modulos_pesquisas import pesquisa_avancada

import limpar_terminal

def menu_pesquisa():
    print("\n'''''' OPÇÕES DE PESQUISA DISPONÍVEIS ''''''''''\n")
    print("[1].BUSCAR ITEM")
    print("[2].SAIR")
    print("\n''''''''''''''''''''''''''''''''''''\n")
    

def opcoes():
    while True:
        limpar_terminal.limpar_terminal()
        menu_pesquisa()
        
        escolha = input('Digite o tipo de pesquisa desejado: ')
        
        if escolha == '1':
            pesquisa_avancada.tipo_operacao(escolha)
        elif escolha == '2':
            break
        else:
            print('\nDigite um valor válido!\n')
            input('Digite "Enter" para Continuar')