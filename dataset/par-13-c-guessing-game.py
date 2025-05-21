import random

def juego():
    objetivo = random.randint(1, 100)
    intento = 0
    maximo = 10
    print("¡Intenta adivinar el número entre 1 y 100!")

    while intento < maximo:
        entrada = input(f"Turno {intento + 1}/{maximo}: ")
        try:
            elegido = int(entrada)
        except ValueError:
            print("Eso no es un número.")
            continue

        intento += 1

        if elegido == objetivo:
            print(f"¡Ganaste en {intento} intentos!")
            return
        elif elegido < objetivo:
            print("Muy bajo.")
        else:
            print("Muy alto.")

    print(f"Fallaste. El número era {objetivo}.")

def repetir():
    while True:
        juego()
        de_nuevo = input("¿Jugar otra vez? (s/n): ")
        if de_nuevo.lower() != "s":
            break

if __name__ == "__main__":
    repetir()
