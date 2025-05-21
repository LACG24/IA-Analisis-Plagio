import pandas as pd

def analizar_csv(ruta):
    try:
        df = pd.read_csv(ruta)
    except Exception as e:
        print(f"Error: {e}")
        return

    while True:
        print("\n1. Promedio de columna")
        print("2. Conteo de valores")
        print("3. Salir")
        op = input("Opción: ")

        if op == "1":
            col = input("Columna numérica: ")
            if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
                print("Promedio:", df[col].mean())
            else:
                print("Columna inválida.")
        elif op == "2":
            col = input("Columna categórica: ")
            if col in df.columns:
                print(df[col].value_counts())
            else:
                print("Columna inválida.")
        elif op == "3":
            break

if __name__ == "__main__":
    archivo = input("Nombre del archivo CSV: ")
    analizar_csv(archivo)