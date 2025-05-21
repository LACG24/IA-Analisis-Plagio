def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    pasos = 0
    while izq <= der:
        pasos += 1
        medio = (izq + der) // 2
        print(f"Paso {pasos}: Izq={izq}, Der={der}, Medio={medio}, Valor={lista[medio]}")
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

def menu():
    lista = list(range(0, 201, 5))  # Lista ordenada
    print("Lista de ejemplo:", lista)
    while True:
        try:
            objetivo = int(input("Valor a buscar: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        resultado = busqueda_binaria(lista, objetivo)
        if resultado != -1:
            print(f"Elemento encontrado en la posición {resultado}")
        else:
            print("Elemento no encontrado.")

        if input("¿Buscar otro valor? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    menu()
