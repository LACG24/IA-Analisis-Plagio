def orden_digitos(lista, base):
    longitud = len(lista)
    resultado = [0] * longitud
    contador = [0] * 10

    for num in lista:
        idx = (num // base) % 10
        contador[idx] += 1

    for i in range(1, 10):
        contador[i] += contador[i - 1]

    for i in reversed(range(longitud)):
        idx = (lista[i] // base) % 10
        resultado[contador[idx] - 1] = lista[i]
        contador[idx] -= 1

    return resultado

def radix_orden(lista):
    mayor = max(lista)
    base = 1
    while mayor // base > 0:
        lista = orden_digitos(lista, base)
        base *= 10
    return lista
