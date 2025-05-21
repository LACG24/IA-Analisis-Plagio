def conversion_universal(cantidad, origen, destino, tabla):
    return cantidad * tabla[origen] / tabla[destino]

def menu_conversor():
    tipos = {
        "longitud": {"m": 1, "cm": 100, "km": 0.001},
        "peso": {"kg": 1, "g": 1000, "lb": 2.20462},
        "temperatura": None
    }

    while True:
        print("\n1. Longitud\n2. Peso\n3. Temperatura\n4. Salir")
        op = input("Selecciona: ")

        if op == "1":
            t = tipos["longitud"]
            v = float(input("Cantidad: "))
            de = input("Desde (m/cm/km): ")
            a = input("A (m/cm/km): ")
            print("Resultado:", conversion_universal(v, de, a, t))
        elif op == "2":
            t = tipos["peso"]
            v = float(input("Cantidad: "))
            de = input("Desde (kg/g/lb): ")
            a = input("A (kg/g/lb): ")
            print("Resultado:", conversion_universal(v, de, a, t))
        elif op == "3":
            v = float(input("Cantidad: "))
            de = input("Desde (C/F): ")
            a = input("A (C/F): ")
            if de == a:
                print("Resultado:", v)
            elif de == "C" and a == "F":
                print("Resultado:", v * 9/5 + 32)
            elif de == "F" and a == "C":
                print("Resultado:", (v - 32) * 5/9)
            else:
                print("Conversión inválida.")
        elif op == "4":
            break

if __name__ == "__main__":
    menu_conversor()
