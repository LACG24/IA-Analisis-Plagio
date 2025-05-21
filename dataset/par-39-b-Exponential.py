def busqueda_binaria(lista, izq, der, objetivo):
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

def busqueda_exponencial(lista, valor):
    if lista[0] == valor:
        return 0
    indice = 1
    while indice < len(lista) and lista[indice] <= valor:
        indice *= 2
    return busqueda_binaria(lista, indice // 2, min(indice, len(lista) - 1), valor)
