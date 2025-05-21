def analizar(fichero):
    try:
        with open(fichero, encoding="utf-8") as doc:
            lineas = doc.readlines()
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return

    num_lineas = len(lineas)
    num_palabras = 0
    num_letras = 0
    vocabulario = set()

    for l in lineas:
        palabras = l.strip().split()
        num_palabras += len(palabras)
        num_letras += sum(len(p) for p in palabras)
        vocabulario.update(palabras)

    print("Archivo:", fichero)
    print("Líneas:", num_lineas)
    print("Palabras:", num_palabras)
    print("Letras:", num_letras)
    print("Vocabulario único:", len(vocabulario))

def lanzar():
    while True:
        nombre = input("Archivo a revisar: ")
        analizar(nombre)
        continuar = input("¿Analizar otro? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    lanzar()
