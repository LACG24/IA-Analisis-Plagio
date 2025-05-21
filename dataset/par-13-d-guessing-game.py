import random

def intento(jugada, real):
    if jugada == real:
        return "¡Correcto!"
    elif jugada < real:
        return "Sube"
    else:
        return "Baja"

def juego_unico():
    objetivo = random.randint(1, 100)
    turnos = 0
    while turnos < 10:
        try:
            valor = int(input(f"Intento #{turnos + 1}: "))
        except:
            print("Número inválido")
            continue
        print(intento(valor, objetivo))
        turnos += 1
        if valor == objetivo:
            return
    print("Fallaste. Era:", objetivo)

def main():
    while True:
        juego_unico()
        if input("¿Repetir? s/n: ").lower() != 's':
            break

if __name__ == "__main__":
    main()
