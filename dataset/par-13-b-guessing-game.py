import random

def jugar():
    secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    print("¡Adivina el número entre 1 y 100!")

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos + 1}/{max_intentos}: ")
        try:
            numero = int(entrada)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        intentos += 1

        if numero == secreto:
            print(f"¡Felicidades! Lo adivinaste en {intentos} intentos.")
            return
        elif numero < secreto:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")

    print(f"Lo siento. El número correcto era {secreto}.")

def jugar_n_veces():
    while True:
        jugar()
        otra = input("¿Quieres jugar de nuevo? (s/n): ")
        if otra.lower() != "s":
            break

if __name__ == "__main__":
    jugar_n_veces()
