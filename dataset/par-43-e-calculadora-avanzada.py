hist = []

def evaluar(expr):
    try:
        res = eval(expr, {"__builtins__": None})
        hist.append((expr, res))
        return res
    except:
        return "Expresión inválida."

def mostrar():
    for i, (e, r) in enumerate(hist, 1):
        print(f"{i}. {e} = {r}")

def menu():
    while True:
        print("1. Calcular")
        print("2. Historial")
        print("3. Borrar")
        print("4. Salir")
        opc = input(">> ")
        if opc == "1":
            ex = input("Expresión (usa +, -, *): ")
            print("Resultado:", evaluar(ex))
        elif opc == "2":
            mostrar()
        elif opc == "3":
            hist.clear()
        elif opc == "4":
            break

if __name__ == "__main__":
    menu()
