def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    total_lineas = len(lineas)
    total_palabras = 0
    total_letras = 0
    palabras_unicas = set()

    for linea in lineas:
        palabras = linea.strip().split()
        total_palabras += len(palabras)
        total_letras += sum(len(p) for p in palabras)
        palabras_unicas.update(palabras)

    print(f"Archivo: {nombre_archivo}")
    print(f"Total de líneas: {total_lineas}")
    print(f"Total de palabras: {total_palabras}")
    print(f"Total de letras: {total_letras}")
    print(f"Palabras únicas: {len(palabras_unicas)}")

def menu():
    while True:
        nombre = input("\nNombre del archivo a analizar: ")
        analizar_archivo(nombre)
        otra = input("¿Analizar otro archivo? (s/n): ")
        if otra.lower() != "s":
            break

if __name__ == "__main__":
    menu()
