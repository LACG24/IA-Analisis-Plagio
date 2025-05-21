def ordenar_shell(lista):
    longitud = len(lista)
    salto = longitud // 2

    while salto > 0:
        indice = salto
        while indice < longitud:
            valor = lista[indice]
            pos = indice
            while pos >= salto and lista[pos - salto] > valor:
                lista[pos] = lista[pos - salto]
                pos -= salto
            lista[pos] = valor
            indice += 1
        salto //= 2
    return lista
