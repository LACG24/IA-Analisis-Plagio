import csv

def leer_datos_csv(archivo):
    datos = []
    try:
        with open(archivo, newline='') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                datos.append({k: (float(v) if v.replace('.', '', 1).isdigit() else v)
                              for k, v in fila.items()})
    except FileNotFoundError:
        print(f"Archivo '{archivo}' no encontrado.")
    return datos

def promedio_columna(datos, columna):
    numeros = [fila[columna] for fila in datos if isinstance(fila[columna], float)]
    if not numeros:
        return None
    return sum(numeros) / len(numeros)

def contar_valores(datos, columna):
    conteo = {}
    for fila in datos:
        valor = fila[columna]
        conteo[valor] = conteo.get(valor, 0) + 1
    return conteo

def menu():
    archivo = input("Nombre del archivo CSV: ")
    datos = leer_datos_csv(archivo)
    if not datos:
        return
    while True:
        print("\nOpciones:")
        print("1. Promedio de una columna")
        print("2. Conteo de valores en columna")
        print("3. Salir")
        op = input("Selecciona: ")
        if op == "1":
            col = input("Nombre de la columna: ")
            prom = promedio_columna(datos, col)
            if prom is not None:
                print(f"Promedio de '{col}': {prom}")
            else:
                print("No se pudo calcular promedio.")
        elif op == "2":
            col = input("Columna a analizar: ")
            conteos = contar_valores(datos, col)
            for val, cnt in conteos.items():
                print(f"{val}: {cnt}")
        elif op == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
