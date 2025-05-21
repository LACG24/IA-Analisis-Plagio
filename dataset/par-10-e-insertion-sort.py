def ordenar_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def menu_ordenamiento():
    print("1. Usar lista por defecto")
    print("2. Ingresar lista personalizada")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        valores = [64, 34, 25, 12, 22, 11, 90, 55, 32, 78]
    elif opcion == "2":
        entrada = input("Escribe los números separados por espacio: ")
        valores = list(map(int, entrada.split()))
    else:
        print("Opción inválida.")
        return
    print("Lista original:", valores)
    resultado = ordenar_insercion(valores)
    print("Lista ordenada:", resultado)

if __name__ == "__main__":
    menu_ordenamiento()
