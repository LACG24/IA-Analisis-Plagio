def combinar(parte1, parte2):
    salida = []
    a = b = 0
    while a < len(parte1) and b < len(parte2):
        if parte1[a] <= parte2[b]:
            salida.append(parte1[a])
            a += 1
        else:
            salida.append(parte2[b])
            b += 1
    salida.extend(parte1[a:])
    salida.extend(parte2[b:])
    return salida

def mezcla_adaptativa(lista):
    if len(lista) <= 1:
        return lista
    if all(lista[i] <= lista[i+1] for i in range(len(lista)-1)):
        return lista
    mitad = len(lista) // 2
    izquierda = mezcla_adaptativa(lista[:mitad])
    derecha = mezcla_adaptativa(lista[mitad:])
    return combinar(izquierda, derecha)
