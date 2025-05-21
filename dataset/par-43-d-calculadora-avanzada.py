import math

memoria = []

def procesar(entrada):
    try:
        r = eval(entrada, {"__builtins__": None}, vars(math))
        memoria.append((entrada, r))
        return r
    except Exception as e:
        return f"ERROR: {e}"

def historial():
    for i, (e, r) in enumerate(memoria, 1):
        print(f"{i}) {e} = {r}")

def limpiar():
    memoria.clear()

def iniciar_calculadora():
    while True:
        print("1) Evaluar\n2) Historial\n3) Limpiar\n4) Salir")
        opc = input("Elige: ")
        if opc == "1":
            exp = input("Expresión: ")
            print("→", procesar(exp))
        elif opc == "2":
            historial()
        elif opc == "3":
            limpiar()
        elif opc == "4":
            break

if __name__ == "__main__":
    iniciar_calculadora()
