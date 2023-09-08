# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃               ┃╺┳╸┏━┓┏━┓━━━━━━━━━━━━━━  ** main.py **  ━━━━━━━━━━━━━━━━┏━┓┏━┓                ┃
# ┃               ┃┃┃┃┃┃┃┏┛     VERSÃO: 1.0                             ┏━┓┏━┛┏━┛                ┃
# ┃                ┃┃┗┛┗┛┃┃      AUTORES:                                                        ┃
# ┃                                  Thayson Guedes de Medeiros                                  ┃
# ┃                                  Thiago Ferreira dos Santos                                  ┃
# ┃               ┗┻━┓┏┓┏━┛     DATA DE CRIAÇÃO:                       ┃┏━┛┃ ┃┃                  ┃
# ┃                 ┗━┛┗┛           08 de setembro de 2023                ┗┛ ┗┛                  ┃
# ┃                                                                                              ┃
# ┃  DESCRIÇÃO:                                                                                  ┃
# ┃  Este módulo executa [ O início de toda a aplicação ].                                       ┃
# ┃                                                                                              ┃
# ┃  LINKS ÚTEIS:                                                                                ┃
# ┃  - Repositório do projeto: [ https://github.com/ThaysonScript/python_code ]                  ┃
# ┃  - Repositório do módulo: [ https://github.com/ThaysonScript/python_code/blob/main/main.py ] ┃
# ┃  - Documentação de descrições e requisitos do projeto: [ pasta: descricao_projeto ]          ┃
# ┃                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# --------------------- IMPORTAR PARTES DA APLICACAO --------------------------
from modulos_projeto import cadastro         # IMPORTAR CADASTROS
from modulos_projeto import ver              # IMPORTAR VISUALIZACOES
from modulos_projeto import atualizar        # IMPORTAR EDICOES
from modulos_projeto import deletar          # IMPORTAR DELETES
from modulos_pesquisas import menu_pesquisa  # IMPORTAR CONSULTAS MAIS RAPIDAS
import creditos                              # IMPORTAR CREDITOS DOS DESENVOLVEDORES
from time import sleep                       # IMPORTAR DELAY DE TEMPO
import limpar_terminal                       # IMPORTAR LIMPEZA DE TERMINAL

# 2.1. MENU INICIAL PARA O USUARIO SELECIONAR A OPCAO DE INTERESSE
def menu_principal():
    print("\n''''''''''''''' ESCOLHA UMA OPÇÃO '''''''''''''''''''\n")
    print("[1].CADASTRAR ITEM")
    print("[2].BUSCAR ITEM")
    print("[3].EDITAR ITENS CADASTRADOS")
    print("[4].REMOVER ITEM CADASTRADO")
    print("[5].REALIZAR PESQUISA AVANÇADA ( BETA )")
    print("[6].SAIR\n")
    print("[7].CREDITOS DOS DESENVOLVEDORES\n")
    print("''''''''''''''''''''''''''''''''''''")
    
# SELECIONAR A OPCAO DE INTERESSE
def escolha_interesse():    
    i = 0
    while True:
        if i == 0:
            # creditos.creditos()
            # sleep(3)
            i += 1
        else:
            limpar_terminal.limpar_terminal()
            
        print("\n'''''' BEM VINDO AO MENU INICAL DO USUÁRIO ''''''''''")
        menu_principal()  # CHAMAR MENU DE ESCOLHAS
        escolha = input('Digite uma opção de escolha acima: ')

        if escolha == '1':
            limpar_terminal.limpar_terminal()
            cadastro.cadastro()
            
        elif escolha == '2':
            limpar_terminal.limpar_terminal()
            ver.ver_items()
            
        elif escolha == '3':
            limpar_terminal.limpar_terminal()
            atualizar.atualizar_dados()
            
        elif escolha == '4':
            limpar_terminal.limpar_terminal()
            deletar.deletar_item()
            
        elif escolha == '5':
            limpar_terminal.limpar_terminal()
            menu_pesquisa.opcoes()
        
        elif escolha == '6':
            limpar_terminal.limpar_terminal()
            print("\n******** SAINDO DO PROGRAMA *********\n")
            break
        
        elif escolha == '7':
            limpar_terminal.limpar_terminal()
            creditos.creditos()
            input('Pressione "Enter" para Continuar')
            
        else:
            print('\nDigite uma opção válida!\n')
            input('Pressione qualquer Tecla para Continuar')
            
# EXECUTAR O INICIO DO PROGRAMA, EXECUTE DIRETAMENTE
if __name__ == '__main__':  # NAO EXECUTAVEL SE FOR MODULO
    escolha_interesse()
