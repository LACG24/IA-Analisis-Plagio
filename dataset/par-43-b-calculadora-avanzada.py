import math

historial = []

def evaluar_expresion(expr):
    try:
        resultado = eval(expr, {"__builtins__": None}, vars(math))
        historial.append((expr, resultado))
        return resultado
    except Exception as e:
        return f"Error: {e}"

def mostrar_historial():
    print("\nHistorial de operaciones:")
    for idx, (exp, res) in enumerate(historial):
        print(f"{idx + 1}. {exp} = {res}")

def menu():
    while True:
        print("\n--- CALCULADORA AVANZADA ---")
        print("1. Evaluar expresión")
        print("2. Mostrar historial")
        print("3. Borrar historial")
        print("4. Salir")

        op = input("Opción: ")
        if op == "1":
            expr = input("Introduce expresión (usa funciones de math, ej: sqrt(16)): ")
            resultado = evaluar_expresion(expr)
            print("Resultado:", resultado)
        elif op == "2":
            mostrar_historial()
        elif op == "3":
            historial.clear()
            print("Historial borrado.")
        elif op == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
