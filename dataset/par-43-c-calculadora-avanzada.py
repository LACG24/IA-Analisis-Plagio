import math

log = []

def procesar_entrada(expresion):
    try:
        resultado = eval(expresion, {"__builtins__": None}, vars(math))
        log.append((expresion, resultado))
        return resultado
    except Exception as err:
        return f"Error: {err}"

def ver_historial():
    print("\nRegistro:")
    for i, (e, r) in enumerate(log):
        print(f"{i + 1}. {e} = {r}")

def inicio():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Evaluar")
        print("2. Ver historial")
        print("3. Limpiar historial")
        print("4. Cerrar")

        eleccion = input("Elegir: ")
        if eleccion == "1":
            ex = input("Expresión: ")
            res = procesar_entrada(ex)
            print("Resultado:", res)
        elif eleccion == "2":
            ver_historial()
        elif eleccion == "3":
            log.clear()
            print("Historial eliminado.")
        elif eleccion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    inicio()
