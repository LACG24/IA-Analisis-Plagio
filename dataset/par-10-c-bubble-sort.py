def ordenar_burbuja(lista):
    longitud = len(lista)
    total_swaps = 0
    print("Lista original:", lista)
    for paso in range(longitud):
        print(f"\nIteración {paso + 1}:")
        for indice in range(0, longitud - paso - 1):
            print(f"  Comparando {lista[indice]} y {lista[indice+1]}")
            if lista[indice] > lista[indice + 1]:
                print(f"  Intercambiando {lista[indice]} y {lista[indice+1]}")
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                total_swaps += 1
            print("  Lista parcial:", lista)
        print(f"Fin de la iteración {paso + 1}: {lista}")
    print("\nLista ordenada:", lista)
    print("Número total de swaps:", total_swaps)
    return lista

def ejecutar_menu():
    print("Opciones de Bubble Sort")
    print("1. Lista por defecto")
    print("2. Ingresar lista")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        elementos = [64, 34, 25, 12, 22, 11, 90, 55, 32, 78]
    elif opcion == "2":
        datos = input("Introduce los números separados por espacio: ")
        elementos = list(map(int, datos.strip().split()))
    else:
        print("Selección inválida")
        return
    ordenar_burbuja(elementos)

if __name__ == "__main__":
    ejecutar_menu()
