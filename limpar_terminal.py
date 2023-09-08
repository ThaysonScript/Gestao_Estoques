import os

def limpar_terminal():
    try:
        # VERIFICAR O SISTEMA OPERACIONAL
        sistema_operacional = os.name

        if sistema_operacional == "posix" or "linux" in sistema_operacional.lower():
            # SISTEMA UNIX (Linux, macOS)
            os.system("clear")
            
        elif sistema_operacional == "nt" or "windows" in sistema_operacional.lower():
            # WINDOWS
            os.system("cls")
            
        else:
            # USAR ESCAPE ANSI CASO SISTEMA NAO ENCONTRADO
            print("\033c", end="")
    
    except Exception as e:
        print(f"Erro ao limpar o terminal: {e}")
