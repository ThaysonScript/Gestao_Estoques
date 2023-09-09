# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃               ┃╺┳╸┏━┓┏━┓━━━━━━━━  ** deletar.py **  ━━━━━━━━━━━┏━┓┏━┓                        ┃
# ┃               ┃┃┃┃┃┃┃┏┛     VERSÃO: 1.0                             ┏━┓┏━┛┏━┛                ┃
# ┃                ┃┃┗┛┗┛┃┃      AUTORES:                                                        ┃
# ┃                                  Thayson Guedes de Medeiros                                  ┃
# ┃                                  Thiago Ferreira dos Santos                                  ┃
# ┃               ┗┻━┓┏┓┏━┛     DATA DE CRIAÇÃO:                       ┃┏━┛┃ ┃┃                  ┃
# ┃                 ┗━┛┗┛           08 de setembro de 2023                ┗┛ ┗┛                  ┃
# ┃                                                                                              ┃
# ┃  DESCRIÇÃO:                                                                                  ┃
# ┃  Este módulo executa [ a deletacao de items ].                                               ┃
# ┃                                                                                              ┃
# ┃  LINKS ÚTEIS:                                                                                ┃
# ┃  - Repositório do projeto: [ https://github.com/ThaysonScript/python_code ]                  ┃
# ┃  - Repositório do módulo: [ https://github.com/ThaysonScript/python_code/blob/main/modulos_projeto/deletar.py ] ┃
# ┃  - Documentação de descrições e requisitos do projeto: [ pasta: descricao_projeto ]          ┃
# ┃                                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# EFETUAR A REMOCAO DO ITEM A DELETAR
def carregar_items_delete(deletar_item):    #  2.6. Persistência dos dados em arquivo .csv contendo itens e suas propriedades
    with open("dados.csv", "r") as dados:
        return [linha for linha in dados if deletar_item not in linha]

# REGISTRAR A EXCLUSAO DE UM DADO
def registrar_delete(linhas_atualizadas):   #  2.6. Persistência dos dados em arquivo .csv contendo itens e suas propriedades
    with open("dados.csv", "w") as arquivo_csv:
            arquivo_csv.writelines(linhas_atualizadas)

# 2.5 OPCAO PARA REMOVER UM ITEM CADASTRADO
def deletar_item():
    try:
        deletar_item = input("Digite o nome do item que deseja excluir: ")
        linhas_atualizadas = carregar_items_delete(deletar_item)
        
        print(f"Registro com o nome '{deletar_item}' irá ser excluído.\n")  
    
        while True:
            escolha_delete = input('Deseja realmente excluir esse item s/n: ').lower()
            
            if escolha_delete == 's':
                registrar_delete(linhas_atualizadas)
                print('Seu item foi excluido com sucesso!')
                break
            
            elif escolha_delete == 'n':
                print('Redirecionando para menu principal')
                break
            
            else:
                print('Digite um valor válido')
            
        input('Pressione qualquer Tecla para Continuar')
        
    except FileNotFoundError:
        print('Arquivo.csv não existe, cadastre um novo item para executar essa consulta!')
        input('Pressione qualquer Tecla para Continuar')
