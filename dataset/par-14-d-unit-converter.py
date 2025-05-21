def convertir(tipo, val, origen, destino):
    tablas = {
        "l": {"m": 1, "cm": 100, "km": 0.001},
        "p": {"kg": 1, "g": 1000, "lb": 2.20462}
    }

    if tipo == "t":
        if origen == destino:
            return val
        return val * 9 / 5 + 32 if origen == "C" else (val - 32) * 5 / 9
    elif tipo in tablas:
        return val / tablas[tipo][origen] * tablas[tipo][destino]
    else:
        raise Exception("Tipo inválido")

def pedir_valores():
    v = float(input("Cantidad: "))
    f = input("Desde: ")
    t = input("A: ")
    return v, f, t

def interfaz():
    while True:
        print("1. Longitud\n2. Peso\n3. Temperatura\n4. Salir")
        opc = input("Elige: ")
        if opc == "1":
            v, f, t = pedir_valores()
            print(convertir("l", v, f, t))
        elif opc == "2":
            v, f, t = pedir_valores()
            print(convertir("p", v, f, t))
        elif opc == "3":
            v, f, t = pedir_valores()
            print(convertir("t", v, f, t))
        elif opc == "4":
            break

if __name__ == "__main__":
    interfaz()
