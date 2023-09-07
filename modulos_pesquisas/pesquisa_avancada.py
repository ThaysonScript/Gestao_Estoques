from modulos_projeto import ver

import platform
import os
import sys

import limpar_terminal


def tipo_operacao(tipo):
    if tipo == '1':
        ver.ver_items(pesquisa_avancada = True)
        
    elif tipo == '2':
        pass
    
    elif tipo == '3':
        pass
        
        
        
        
        
        
        

# Lista fictícia de produtos
# produtos = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5"]

produtos = []

def autocompletar(termo_pesquisa):
    termo_pesquisa = termo_pesquisa.lower()
    sugestoes = [produto for produto in produtos if termo_pesquisa in produto.lower()]
            
    return sugestoes

def confirmar_saida():
    while True:
        resposta = input("Deseja realmente sair? (S/N): ").strip().lower()
        
        if resposta == 's' or resposta == 'sim':
            return True
        
        elif resposta == 'n' or resposta == 'nao':
            return False
        
        else:
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")

def main(dados):
    if platform.system() == "Windows":
        import msvcrt
    else:
        import curses

    termo_pesquisa = ""
    opcao_selecionada = 0

    while True:
        limpar_terminal.limpar_terminal()

        if platform.system() != "Windows":
            stdscr = curses.initscr()
            curses.curs_set(1)  # Exibe o cursor

            altura, largura = stdscr.getmaxyx()

            stdscr.clear()
            stdscr.addstr(0, 0, f"Digite o nome do produto (ou 'q' para sair): {termo_pesquisa}")
        else:
            print(f"Digite o nome do produto (ou 'q' para sair): {termo_pesquisa}")

            if produtos == []:
                for dado in dados:
                    for indice, item in enumerate(dado):
                        if indice == 0:
                            produtos.append(item)

            sugestoes = autocompletar(termo_pesquisa)

        if not sugestoes:
            sugestoes = ["Nenhuma sugestão disponível"]

        for i, sugestao in enumerate(sugestoes):
            if platform.system() != "Windows":
                stdscr.addstr(i + 1, 0, f"{i + 1}: {sugestao}")
            else:
                print(f"{i + 1}: {sugestao}")

        if platform.system() != "Windows":
            stdscr.refresh()

        if platform.system() == "Windows":
            while msvcrt.kbhit():
                msvcrt.getch()

            char = msvcrt.getch().decode('utf-8')
        else:
            key = stdscr.getch()
            char = chr(key)

        if char.lower() == 'q' or char.lower() == 'quit':
            if confirmar_saida():
                break  # Sair do programa

        if char == '\r':
            if opcao_selecionada < len(sugestoes):
                produto_selecionado = sugestoes[opcao_selecionada]
                
                produtos.clear()
                
                return produto_selecionado  # Retorna o item selecionado
                
        elif char == '\x08':  # Backspace
            termo_pesquisa = termo_pesquisa[:-1]
            
        elif char.isprintable():
            termo_pesquisa += char
            
        elif char == 'A' and platform.system() != "Windows":
            opcao_selecionada = max(opcao_selecionada - 1, 0)
            
        elif char == 'B' and platform.system() != "Windows":
            opcao_selecionada = min(opcao_selecionada + 1, len(sugestoes) - 1)

    if platform.system() != "Windows":
        curses.endwin()
