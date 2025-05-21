def mostrar_lista(texto, lista):
    print(texto, lista)

def ordenar_burbuja_mod(lista):
    cambios = 0
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                cambios += 1
    return lista, cambios

def entrada_manual():
    entrada = input("Ingrese números separados por espacio: ")
    return list(map(int, entrada.strip().split()))

def ejecutar():
    print("Opciones:\n1. Predefinido\n2. Manual")
    opcion = input("Seleccione: ")
    if opcion == "1":
        datos = [64, 34, 25, 12, 22, 11, 90, 55, 32, 78]
    elif opcion == "2":
        datos = entrada_manual()
    else:
        return

    mostrar_lista("Original:", datos)
    ordenado, total = ordenar_burbuja_mod(datos)
    mostrar_lista("Ordenado:", ordenado)
    print(f"Intercambios realizados: {total}")

if __name__ == "__main__":
    ejecutar()
