def mex(conj):
    m = 0
    while m in conj:
        m += 1
    return m

def calcular_grundy(n, movimientos):
    grundy = [0] * (n + 1)
    for i in range(1, n + 1):
        alcances = set()
        for m in movimientos:
            if i - m >= 0:
                alcances.add(grundy[i - m])
        grundy[i] = mex(alcances)
    return grundy

def imprimir_tabla(grundy):
    print("\nValor de Grundy por estado:")
    for i, val in enumerate(grundy):
        print(f"{i}: {val}")

def jugar_grundy(estado, movimientos):
    g = calcular_grundy(estado, movimientos)
    print(f"Grundy final para {estado} piedras:", g[estado])
    if g[estado] != 0:
        print("El primer jugador tiene una estrategia ganadora.")
    else:
        print("El segundo jugador tiene la ventaja.")

def menu():
    while True:
        print("\n--- Juego de Grundy ---")
        try:
            n = int(input("Cantidad inicial de piedras: "))
            mvs = input("Movimientos posibles (ej: 1 3 4): ")
            movimientos = list(map(int, mvs.strip().split()))
            if n < 1 or not movimientos:
                raise ValueError()
        except:
            print("Entrada inválida.")
            continue

        jugar_grundy(n, movimientos)

        if input("¿Otro juego? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    menu()
