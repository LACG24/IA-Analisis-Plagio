import time

def inicializar_vector(n):
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False
    return primos

def marcar_multiplos(primos, n):
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False

def extraer_primos(primos):
    return [i for i, v in enumerate(primos) if v]

def calcular_primos(n):
    p = inicializar_vector(n)
    marcar_multiplos(p, n)
    return extraer_primos(p)

def iniciar():
    while True:
        print("Primos hasta n")
        try:
            valor = int(input("n: "))
            if valor < 2:
                print("n debe ser mayor que 1.")
                continue
        except:
            print("Entrada inválida")
            continue

        inicio = time.time()
        resultado = calcular_primos(valor)
        fin = time.time()

        print(f"Total encontrados: {len(resultado)}")
        print(f"Tiempo: {fin - inicio:.4f}s")
        if input("Ver lista (s/n)? ").lower() == 's':
            print(resultado)
        if input("¿Nuevo intento? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    iniciar()
