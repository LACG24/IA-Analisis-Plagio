import time

def criba_eratostenes(n):
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i*i, n + 1, i):
                primos[j] = False
    return [i for i, es_primo in enumerate(primos) if es_primo]

def contar_primos_hasta(n):
    primos = criba_eratostenes(n)
    print(f"Total de primos hasta {n}: {len(primos)}")
    return primos

def menu():
    while True:
        print("\n--- Generador de Números Primos ---")
        try:
            n = int(input("Introduce un número entero mayor que 1: "))
            if n <= 1:
                print("El número debe ser mayor que 1.")
                continue
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

        inicio = time.time()
        primos = contar_primos_hasta(n)
        fin = time.time()

        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
        mostrar = input("¿Deseas mostrar los números primos? (s/n): ")
        if mostrar.lower() == "s":
            print(primos)

        otra = input("¿Deseas intentar con otro número? (s/n): ")
        if otra.lower() != "s":
            break

if __name__ == "__main__":
    menu()
