def fusion_bitonica(lista, inicio, tamaño, asc):
    if tamaño > 1:
        mitad = tamaño // 2
        for i in range(inicio, inicio + mitad):
            if (asc == 1 and lista[i] > lista[i + mitad]) or (asc == 0 and lista[i] < lista[i + mitad]):
                lista[i], lista[i + mitad] = lista[i + mitad], lista[i]
        fusion_bitonica(lista, inicio, mitad, asc)
        fusion_bitonica(lista, inicio + mitad, mitad, asc)

def ordenar_bitonicamente(lista, inicio, tamaño, asc):
    if tamaño > 1:
        mitad = tamaño // 2
        ordenar_bitonicamente(lista, inicio, mitad, 1)
        ordenar_bitonicamente(lista, inicio + mitad, mitad, 0)
        fusion_bitonica(lista, inicio, tamaño, asc)
