def atualizar_item():
    with open('dados.txt', 'r') as dados:
        linhas = dados.readlines()
        print(f'Items disponiveis: \n{linhas}')
        
        item_atualizar = input('Digite o nome do item a ser atualizado: ')
        linhas_atualizadas = []
        for linha in linhas:
            fabricante, modelo, serial = linha.strip().split(",")
            
            if item_atualizar == fabricante:
                nova_fabricante = input('Digite a nova fabricante: ')
                novo_modelo = input('Digite o novo modelo: ')
                novo_serial = input('Digite o novo serial: ')
                
                fabricante = nova_fabricante
                modelo = novo_modelo
                serial = novo_serial
                
            linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')
            
    with open('dados.txt', 'w') as dados, open('dados.csv', 'w') as arquivo_csv:
        dados.writelines(linhas_atualizadas)
        arquivo_csv.writelines(linhas_atualizadas)
        