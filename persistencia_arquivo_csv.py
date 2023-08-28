def verificar_arquivo_csv_existe(arquivo_csv):
    return open(arquivo_csv, 'r')


def ler_arquivo_txt():
    linhas = []
    with open('dados.txt', 'r') as arquivo_txt:
        linhas.append(arquivo_txt.readlines())
        
    return linhas


def persistir_dados_arquivo_csv():
    dados_txt = ler_arquivo_txt()
    
    informar_arquivo_csv = input('Digite o seu arquivo com a extensão .csv, caso não tenha ( arquivo.csv ) digite enter: ')
    try:
        existencia = verificar_arquivo_csv_existe(informar_arquivo_csv)
        
        with open(informar_arquivo_csv, 'w') as arquivo_escrita_final:
            for dado in dados_txt:
                arquivo_escrita_final.writelines(dado)
            
        print('Dados foram salvos ( *persistidos* ) em arquivo csv com sucesso!')
            
    except FileNotFoundError:
        while True:
            print('Arquivo de geração .csv final não existe.\n')
            
            criar_csv_com_dados = input('Digite "s" ou "n" para criar arquivo .csv e amazenar seus items txt: ').lower()
            
            if criar_csv_com_dados == 's':
                nome_arquivo_csv = input('Digite o nome que quer dá ao seu arquivo.csv: ') + '.csv'
                
                with open(nome_arquivo_csv, 'w') as arquivo_escrita_final:
                    for dado in dados_txt:
                        arquivo_escrita_final.writelines(dado)
                print('Dados foram salvos ( *persistidos* ) em arquivo csv com sucesso!')
                
                break
            
            elif criar_csv_com_dados == 'n':
                print('OK, mas lembre-se de adicionar ou criar o seu arquivo.csv em algum momento não muito longo de tempo')
                break
                
    finally:
        print('\nObrigado pelo seu tempo!')
        