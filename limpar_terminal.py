import os

def limpar_terminal():
    try:
        # Verificar o sistema operacional
        sistema_operacional = os.name

        if sistema_operacional == "posix" or "linux" in sistema_operacional.lower():
            # Sistema Unix (Linux, macOS)
            os.system("clear")
        elif sistema_operacional == "nt" or "windows" in sistema_operacional.lower():
            # Windows
            os.system("cls")
        else:
            # Se o sistema operacional não for reconhecido, usar sequência de escape ANSI para limpar
            print("\033c", end="")
    
    except Exception as e:
        print(f"Erro ao limpar o terminal: {e}")
