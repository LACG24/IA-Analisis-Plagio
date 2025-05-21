def orden_relampago(lista):
    tam = len(lista)
    if tam == 0:
        return lista

    m = int(0.45 * tam)
    max_indice = 0
    minimo = lista[0]
    for i in range(1, tam):
        if lista[i] < minimo:
            minimo = lista[i]
        if lista[i] > lista[max_indice]:
            max_indice = i

    if lista[max_indice] == minimo:
        return lista

    clases = [0] * m
    factor = (m - 1) / (lista[max_indice] - minimo)
    for i in range(tam):
        idx = int(factor * (lista[i] - minimo))
        clases[idx] += 1

    for i in range(1, m):
        clases[i] += clases[i - 1]

    lista[0], lista[max_indice] = lista[max_indice], lista[0]
    cambios = 0
    j = 0
    k = m - 1
    while cambios < tam - 1:
        while j > clases[k] - 1:
            j += 1
            k = int(factor * (lista[j] - minimo))
        valor = lista[j]
        while j != clases[k]:
            k = int(factor * (valor - minimo))
            destino = clases[k] - 1
            lista[destino], valor = valor, lista[destino]
            clases[k] -= 1
            cambios += 1

    for i in range(1, tam):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista
