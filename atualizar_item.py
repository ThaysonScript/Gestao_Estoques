with open('dados.txt', 'r') as dados:
    linhas = dados.readlines()
    
    print(f'Items disponiveis: \n{linhas}')
    
    linhas_atualizadas = []
    item_atualizar = str(input('Digite o nome do item a ser atualizado: '))
    for linha in linhas:
        fabricante, modelo, serial = linha.strip().split(",")
        
        if item_atualizar == fabricante:
            nova_fabricante = str(input('Digite a nova fabricante: '))
            novo_modelo = str(input('Digite o novo modelo: '))
            novo_serial = str(input('Digite o novo serial: '))
            
            fabricante = nova_fabricante
            modelo = novo_modelo
            serial = novo_serial
            
        linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
        
        
with open('dados.txt', 'w') as dados:
    dados.writelines(linhas_atualizadas)
    
    
    
def ler_dados_txt():
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]



def escrever_dados_csv(dados):
    with open("dados.csv", "w") as arquivo:
        for linha in dados:
            arquivo.write(linha + '\n')
            
            
            
escrever_dados_csv(ler_dados_txt())
