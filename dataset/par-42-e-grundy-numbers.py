memo = {}

def grundy(n, moves):
    if n in memo:
        return memo[n]
    posibles = set()
    for m in moves:
        if n >= m:
            posibles.add(grundy(n - m, moves))
    res = 0
    while res in posibles:
        res += 1
    memo[n] = res
    return res

def main():
    while True:
        try:
            piedras = int(input("Número de piedras: "))
            movs = list(map(int, input("Movimientos permitidos: ").split()))
        except:
            print("Entrada inválida.")
            continue

        g = grundy(piedras, movs)
        print("Valor Grundy:", g)
        print("Gana:", "Jugador 1" if g != 0 else "Jugador 2")

        if input("¿Nuevo juego? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()
