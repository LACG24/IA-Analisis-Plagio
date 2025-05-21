def longitudes(valor, origen, destino):
    mapa = {"m": 1.0, "cm": 100.0, "km": 0.001}
    return valor / mapa[origen] * mapa[destino]

def pesos(valor, origen, destino):
    mapa = {"kg": 1.0, "g": 1000.0, "lb": 2.20462}
    return valor / mapa[origen] * mapa[destino]

def temperaturas(valor, origen, destino):
    if origen == destino:
        return valor
    if origen == "C" and destino == "F":
        return valor * 9/5 + 32
    elif origen == "F" and destino == "C":
        return (valor - 32) * 5/9
    else:
        raise ValueError("Conversión inválida")

def interfaz():
    while True:
        print("\n--- CONVERSOR ---")
        print("1. Longitud")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Terminar")
        opcion = input("Selecciona: ")

        if opcion == "1":
            val = float(input("Cantidad: "))
            ori = input("Desde (m/cm/km): ")
            dest = input("Hacia (m/cm/km): ")
            print("Resultado:", longitudes(val, ori, dest))
        elif opcion == "2":
            val = float(input("Cantidad: "))
            ori = input("Desde (kg/g/lb): ")
            dest = input("Hacia (kg/g/lb): ")
            print("Resultado:", pesos(val, ori, dest))
        elif opcion == "3":
            val = float(input("Cantidad: "))
            ori = input("Desde (C/F): ")
            dest = input("Hacia (C/F): ")
            print("Resultado:", temperaturas(val, ori, dest))
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    interfaz()
