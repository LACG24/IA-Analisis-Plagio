import csv

def cargar(archivo):
    try:
        with open(archivo) as f:
            lector = csv.DictReader(f)
            return [
                {k: float(v) if v.replace('.', '', 1).isdigit() else v for k, v in fila.items()}
                for fila in lector
            ]
    except:
        return []

def promedio(col, datos):
    valores = [r[col] for r in datos if isinstance(r[col], float)]
    return round(sum(valores) / len(valores), 2) if valores else None

def frecuencias(col, datos):
    salida = {}
    for r in datos:
        salida[r[col]] = salida.get(r[col], 0) + 1
    return salida

def ciclo_menu(datos):
    while True:
        print("1. Promedio\n2. Frecuencias\n3. Fin")
        op = input("> ")
        if op == "1":
            c = input("Columna: ")
            r = promedio(c, datos)
            print("Resultado:", r if r is not None else "No válido")
        elif op == "2":
            c = input("Columna: ")
            for k, v in frecuencias(c, datos).items():
                print(f"{k}: {v}")
        elif op == "3":
            break

def main():
    archivo = input("Archivo CSV: ")
    datos = cargar(archivo)
    if datos:
        ciclo_menu(datos)

if __name__ == "__main__":
    main()
