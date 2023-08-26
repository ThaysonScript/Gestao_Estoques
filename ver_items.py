escolha = str(input('Digite o item a ser consultado ( por nome ou propriedade ): '))

with open('dados.txt', 'r') as dados:
    for dado in dados:
        fabricante, modelo, serial = dado.strip().split(',')
        
        if escolha == fabricante:
            print(f'Sua marca de fabricante é: {fabricante}')
            
        elif escolha == modelo:
            print(f'Seu modelo de item é: {modelo}')
            
        elif escolha == serial:
            print(f'O codigo serial do seu item é: {serial}')
            
            
            
def ler_dados_txt():
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]



def escrever_dados_csv(dados):
    with open("dados.csv", "w") as arquivo:
        for linha in dados:
            arquivo.write(linha + '\n')
            
            
            
escrever_dados_csv(ler_dados_txt())