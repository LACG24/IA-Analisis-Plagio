def minimo_excluido(s):
    val = 0
    while val in s:
        val += 1
    return val

def calcular_tabla_grundy(n, reglas):
    resultados = [0] * (n + 1)
    for pos in range(1, n + 1):
        alcanzables = {resultados[pos - r] for r in reglas if pos - r >= 0}
        resultados[pos] = minimo_excluido(alcanzables)
    return resultados

def jugar(piedras, reglas):
    tabla = calcular_tabla_grundy(piedras, reglas)
    ganador = "Jugador 1" if tabla[piedras] != 0 else "Jugador 2"
    print("Grundy:", tabla[piedras])
    print("Gana:", ganador)

def bucle_principal():
    while True:
        try:
            total = int(input("N° piedras: "))
            pasos = list(map(int, input("Movimientos: ").split()))
        except:
            print("Error en entrada.")
            continue
        jugar(total, pasos)
        if input("¿Otra partida? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    bucle_principal()
