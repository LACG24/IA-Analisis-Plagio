def buscar_en_lista(datos, objetivo):
    inicio, fin = 0, len(datos) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        print(f"Revisando índice {medio}: {datos[medio]}")
        if datos[medio] == objetivo:
            return medio
        elif datos[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def simulacion_busqueda():
    elementos = [i for i in range(0, 201, 5)]
    print("Lista disponible.")
    while True:
        try:
            valor = int(input("Buscar: "))
        except:
            print("Número inválido.")
            continue
        r = buscar_en_lista(elementos, valor)
        print("Resultado:", f"Índice {r}" if r != -1 else "No encontrado")
        if input("¿Otro intento? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    simulacion_busqueda()
