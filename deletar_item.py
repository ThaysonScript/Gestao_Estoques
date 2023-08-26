deletar_item = input("Digite o nome do item que deseja excluir: ")

linhas_atualizadas = []
with open("dados.txt", "r") as dados:

    for linha in dados:
        print(linha)
        input()
        
        fabricante, modelo, serial = linha.strip().split(",")
        
        if fabricante != deletar_item:
            linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')

with open("dados.txt", "w") as arquivo_txt, open('dados.csv', 'w') as arquivo_csv:
    arquivo_txt.writelines(linhas_atualizadas)
    arquivo_csv.writelines(linhas_atualizadas)

print(f"Registro com o nome '{deletar_item}' foi excluído.")
