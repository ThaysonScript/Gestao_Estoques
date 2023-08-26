deletar_item = input("Digite o nome do item que deseja excluir: ")

linhas_atualizadas = []
with open("dados.txt", "r") as dados:
    linhas = dados.readlines()

    for linha in linhas:
        fabricante, modelo, serial = linha.strip().split(",")
        
        
        if fabricante != deletar_item:
            linhas_atualizadas.append(f'{fabricante},{modelo},{serial}\n')

with open("dados.txt", "w") as dados:
    dados.writelines(linhas_atualizadas)

print(f"Registro com o nome '{deletar_item}' foi excluído.")



def ler_dados_txt():
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas]



def escrever_dados_csv(dados):
    with open("dados.csv", "w") as arquivo:
        for linha in dados:
            arquivo.write(linha + '\n')
            
            
            
escrever_dados_csv(ler_dados_txt())
