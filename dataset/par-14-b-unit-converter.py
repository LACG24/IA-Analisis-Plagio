def convertir_longitud(valor, de, a):
    tabla = {"m": 1.0, "cm": 100.0, "km": 0.001}
    return valor / tabla[de] * tabla[a]

def convertir_peso(valor, de, a):
    tabla = {"kg": 1.0, "g": 1000.0, "lb": 2.20462}
    return valor / tabla[de] * tabla[a]

def convertir_temperatura(valor, de, a):
    if de == a:
        return valor
    if de == "C" and a == "F":
        return valor * 9/5 + 32
    elif de == "F" and a == "C":
        return (valor - 32) * 5/9
    else:
        raise ValueError("Conversión no soportada")

def menu():
    while True:
        print("\n--- CONVERSOR DE UNIDADES ---")
        print("1. Longitud")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Salir")
        op = input("Opción: ")

        if op == "1":
            v = float(input("Valor: "))
            d = input("Desde (m/cm/km): ")
            a = input("A (m/cm/km): ")
            print("Resultado:", convertir_longitud(v, d, a))
        elif op == "2":
            v = float(input("Valor: "))
            d = input("Desde (kg/g/lb): ")
            a = input("A (kg/g/lb): ")
            print("Resultado:", convertir_peso(v, d, a))
        elif op == "3":
            v = float(input("Valor: "))
            d = input("Desde (C/F): ")
            a = input("A (C/F): ")
            print("Resultado:", convertir_temperatura(v, d, a))
        elif op == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
