def busqueda_ternaria(lista, izq, der, objetivo):
    if der >= izq:
        tercio1 = izq + (der - izq) // 3
        tercio2 = der - (der - izq) // 3

        if lista[tercio1] == objetivo:
            return tercio1
        if lista[tercio2] == objetivo:
            return tercio2

        if objetivo < lista[tercio1]:
            return busqueda_ternaria(lista, izq, tercio1 - 1, objetivo)
        elif objetivo > lista[tercio2]:
            return busqueda_ternaria(lista, tercio2 + 1, der, objetivo)
        else:
            return busqueda_ternaria(lista, tercio1 + 1, tercio2 - 1, objetivo)
    return -1
