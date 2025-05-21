def minimo_excluyente(conjunto):
    x = 0
    while x in conjunto:
        x += 1
    return x

def obtener_grundy(maximo, opciones):
    tabla = [0] * (maximo + 1)
    for pos in range(1, maximo + 1):
        alcances = set()
        for paso in opciones:
            if pos - paso >= 0:
                alcances.add(tabla[pos - paso])
        tabla[pos] = minimo_excluyente(alcances)
    return tabla

def desplegar_tabla(valores):
    print("\nValores Grundy por estado:")
    for pos, g in enumerate(valores):
        print(f"{pos}: {g}")

def simular_juego(inicial, saltos):
    resultado = obtener_grundy(inicial, saltos)
    print(f"Grundy final para {inicial} piedras:", resultado[inicial])
    if resultado[inicial] != 0:
        print("Jugador 1 tiene ventaja.")
    else:
        print("Jugador 2 tiene ventaja.")

def menu_grundy():
    while True:
        print("\n--- Juego Grundy ---")
        try:
            cantidad = int(input("Número de piedras: "))
            lista = input("Movimientos (ej: 1 3 4): ")
            pasos = list(map(int, lista.strip().split()))
            if cantidad < 1 or not pasos:
                raise ValueError()
        except:
            print("Error en entrada.")
            continue

        simular_juego(cantidad, pasos)

        if input("¿Intentar otra vez? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    menu_grundy()
