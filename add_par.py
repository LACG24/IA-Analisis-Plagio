import os
import csv

CSV_FILE = "pares.csv"

def agregar_par(codigo_1, codigo_2, tipo_plagio):
    # Verifica si el archivo existe
    archivo_nuevo = not os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        # Escribe encabezado si es nuevo
        if archivo_nuevo:
            writer.writerow(["codigo_1", "codigo_2", "tipo_plagio"])

        writer.writerow([codigo_1, codigo_2, tipo_plagio])
        print(f"Par agregado: ({codigo_1}, {codigo_2}) - Tipo {tipo_plagio}")

# Ejemplo de uso manual:
if __name__ == "__main__":
    while True:
        print("\n--- Agregar nuevo par de código ---")
        archivo1 = input("Ruta del primer archivo .py: ")
        archivo2 = input("Ruta del segundo archivo .py: ")
        tipo = input("Tipo de plagio (1, 2, 3 o 4): ")

        if tipo not in {"1", "2", "3", "4"}:
            print("Tipo inválido.")
            continue

        if not (os.path.isfile(archivo1) and os.path.isfile(archivo2)):
            print("Uno o ambos archivos no existen.")
            continue

        agregar_par(archivo1, archivo2, tipo)

        continuar = input("¿Agregar otro par? (s/n): ").strip().lower()
        if continuar != 's':
            break
