import random

def jugar_rondas():
    numero_secreto = random.randint(1, 100)
    puntos = 100
    for turno in range(1, 11):
        try:
            valor = int(input(f"Intento {turno}: "))
        except:
            print("Entrada inválida")
            continue
        if valor == numero_secreto:
            print(f"¡Acertaste con {puntos} puntos!")
            return
        elif valor < numero_secreto:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")
        puntos -= 10
    print(f"No lograste adivinar. El número era {numero_secreto}.")

def juego_principal():
    while True:
        jugar_rondas()
        if input("¿Jugar otra vez? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    juego_principal()
