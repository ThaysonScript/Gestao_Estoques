def cadastrar_item():
    with open('dados.txt', 'a') as dados:
        fabricante_item = str(input('Digite o nome da fabricante do item: '))
        modelo_item = str(input('Digite o modelo item: '))
        serial_item = str(input('Digite o serial/codigo do item: '))
        
        dados.write(f'{fabricante_item},{modelo_item},{serial_item}\n')
        
        
cadastrar_item()



def ler_dados_txt():
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]



def escrever_dados_csv(dados):
    with open("dados.csv", "w") as arquivo:
        for linha in dados:
            arquivo.write(linha + '\n')
            
            
            
escrever_dados_csv(ler_dados_txt())
