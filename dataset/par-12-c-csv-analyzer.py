import csv

def cargar_csv(nombre_archivo):
    registros = []
    try:
        with open(nombre_archivo, newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                registros.append({k: (float(v) if v.replace('.', '', 1).isdigit() else v)
                                  for k, v in fila.items()})
    except FileNotFoundError:
        print("Archivo no disponible:", nombre_archivo)
    return registros

def calcular_media(registros, campo):
    numeros = [r[campo] for r in registros if isinstance(r[campo], float)]
    if not numeros:
        return None
    return sum(numeros) / len(numeros)

def contar_categorias(registros, campo):
    conteos = {}
    for r in registros:
        valor = r[campo]
        conteos[valor] = conteos.get(valor, 0) + 1
    return conteos

def interfaz():
    archivo = input("Introduce el archivo .csv: ")
    data = cargar_csv(archivo)
    if not data:
        return
    while True:
        print("\nOpciones:")
        print("1. Calcular promedio")
        print("2. Contar valores")
        print("3. Salir")
        seleccion = input("Elige: ")
        if seleccion == "1":
            campo = input("Campo numérico: ")
            media = calcular_media(data, campo)
            if media is not None:
                print(f"Promedio de {campo}: {media}")
            else:
                print("No hay datos válidos.")
        elif seleccion == "2":
            campo = input("Campo categórico: ")
            resultado = contar_categorias(data, campo)
            for clave, cantidad in resultado.items():
                print(f"{clave}: {cantidad}")
        elif seleccion == "3":
            break
        else:
            print("Opción incorrecta")

if __name__ == "__main__":
    interfaz()
