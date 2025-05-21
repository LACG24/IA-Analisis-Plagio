import time

def es_primo(n):
    if n < 2:
        return False
    for div in range(2, int(n**0.5) + 1):
        if n % div == 0:
            return False
    return True

def obtener_primos(hasta):
    return [x for x in range(2, hasta + 1) if es_primo(x)]

def main():
    while True:
        try:
            limite = int(input("Introduce un número mayor que 1: "))
            if limite <= 1:
                print("Debe ser mayor que 1.")
                continue
        except:
            print("Entrada inválida.")
            continue

        inicio = time.time()
        resultado = obtener_primos(limite)
        fin = time.time()

        print(f"Primos encontrados: {len(resultado)}")
        print("Tiempo:", round(fin - inicio, 4), "segundos")
        if input("¿Mostrar lista? (s/n): ").lower() == 's':
            print(resultado)

        if input("¿Repetir? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    main()
