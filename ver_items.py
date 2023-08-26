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
