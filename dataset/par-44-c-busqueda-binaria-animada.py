def buscar(lista, valor):
    ini = 0
    fin = len(lista) - 1
    contador = 0
    while ini <= fin:
        contador += 1
        medio = (ini + fin) // 2
        print(f"Iteración {contador}: ini={ini}, fin={fin}, medio={medio}, valor={lista[medio]}")
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            ini = medio + 1
        else:
            fin = medio - 1
    return -1

def menu_busqueda():
    datos = list(range(0, 201, 5))
    print("Lista:", datos)
    while True:
        try:
            objetivo = int(input("¿Qué número quieres buscar?: "))
        except:
            print("Entrada no válida.")
            continue

        pos = buscar(datos, objetivo)
        if pos != -1:
            print(f"Encontrado en índice {pos}")
        else:
            print("No está en la lista.")

        if input("¿Otra búsqueda? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    menu_busqueda()
