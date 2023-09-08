# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃               ┃╺┳╸┏━┓┏━┓━━━━━━━━  ** limpar_terminal.py **  ━━━━━━━━━━━┏━┓┏━┓                ┃
# ┃               ┃┃┃┃┃┃┃┏┛     VERSÃO: 1.0                             ┏━┓┏━┛┏━┛                ┃
# ┃                ┃┃┗┛┗┛┃┃      AUTORES:                                                        ┃
# ┃                                  Thayson Guedes de Medeiros                                  ┃
# ┃                                  Thiago Ferreira dos Santos                                  ┃
# ┃               ┗┻━┓┏┓┏━┛     DATA DE CRIAÇÃO:                       ┃┏━┛┃ ┃┃                  ┃
# ┃                 ┗━┛┗┛           08 de setembro de 2023                ┗┛ ┗┛                  ┃
# ┃                                                                                              ┃
# ┃  DESCRIÇÃO:                                                                                  ┃
# ┃  Este módulo executa [ a limpeza do terminal ].                                              ┃
# ┃                                                                                              ┃
# ┃  LINKS ÚTEIS:                                                                                ┃
# ┃  - Repositório do projeto: [ https://github.com/ThaysonScript/python_code ]                  ┃
# ┃  - Repositório do módulo: [ https://github.com/ThaysonScript/python_code/blob/pesquisa-avancada/limpar_terminal.py ] ┃
# ┃  - Documentação de descrições e requisitos do projeto: [ pasta: descricao_projeto ]          ┃
# ┃                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

import os

def limpar_terminal():
    try:
        # VERIFICAR O SISTEMA OPERACIONAL
        sistema_operacional = os.name

        if sistema_operacional == "posix" or "linux" in sistema_operacional.lower():
            # SISTEMA UNIX (Linux, macOS)
            os.system("clear")
            
        elif sistema_operacional == "nt" or "windows" in sistema_operacional.lower():
            # WINDOWS
            os.system("cls")
            
        else:
            # USAR ESCAPE ANSI CASO SISTEMA NAO ENCONTRADO
            print("\033c", end="")
    
    except Exception as e:
        print(f"Erro ao limpar o terminal: {e}")
