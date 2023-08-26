with open('dados.txt', 'r') as dados, open('dados.csv', 'w') as arquivo_csv:
    linhas_atualizadas = []
    item_atualizar = input('Digite o nome do item a ser atualizado: ')
    for linha in dados:
        fabricante, modelo, serial = linha.strip().split(",")
        
        if item_atualizar == fabricante:
            nova_fabricante = input('Digite a nova fabricante: ')
            novo_modelo = input('Digite o novo modelo: ')
            novo_serial = input('Digite o novo serial: ')
            
            fabricante = nova_fabricante
            modelo = novo_modelo
            serial = novo_serial
            
        linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
        
    arquivo_csv.writelines(linhas_atualizadas)
