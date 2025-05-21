def dividir_y_ordenar(lista):
    if len(lista) <= 1:
        return lista

    centro = len(lista) // 2
    izquierda = dividir_y_ordenar(lista[:centro])
    derecha = dividir_y_ordenar(lista[centro:])
    return fusionar(izquierda, derecha)

def fusionar(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
