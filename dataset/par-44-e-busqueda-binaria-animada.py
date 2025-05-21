def buscar_lineal(lista, x):
    for i, val in enumerate(lista):
        print(f"Probando índice {i}: {val}")
        if val == x:
            return i
    return -1

def interfaz():
    datos = list(range(0, 201, 5))
    print("Lista:", datos)
    while True:
        try:
            objetivo = int(input("Buscar: "))
        except:
            print("Entrada inválida.")
            continue
        r = buscar_lineal(datos, objetivo)
        if r != -1:
            print(f"Encontrado en posición {r}")
        else:
            print("No está.")
        if input("¿Otra búsqueda? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    interfaz()
