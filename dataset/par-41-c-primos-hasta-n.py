import time

def generar_primos(hasta):
    marcados = [True] * (hasta + 1)
    marcados[0] = marcados[1] = False
    for candidato in range(2, int(hasta ** 0.5) + 1):
        if marcados[candidato]:
            for multiple in range(candidato * candidato, hasta + 1, candidato):
                marcados[multiple] = False
    return [i for i, es_primo in enumerate(marcados) if es_primo]

def contar_total_primos(hasta):
    lista_primos = generar_primos(hasta)
    print(f"Cantidad de primos hasta {hasta}: {len(lista_primos)}")
    return lista_primos

def interfaz_primos():
    while True:
        print("\n*** Calculadora de Números Primos ***")
        try:
            numero = int(input("Número máximo: "))
            if numero <= 1:
                print("Debe ser mayor que 1.")
                continue
        except ValueError:
            print("Valor inválido.")
            continue

        t0 = time.time()
        resultado = contar_total_primos(numero)
        t1 = time.time()

        print(f"Tiempo: {t1 - t0:.6f} s")
        ver = input("¿Mostrar los primos? (s/n): ")
        if ver.lower() == "s":
            print(resultado)

        repetir = input("¿Otro intento? (s/n): ")
        if repetir.lower() != "s":
            break

if __name__ == "__main__":
    interfaz_primos()