def combinar_bloques(parte1, parte2):
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

def mezcla_paralela(datos):
    if len(datos) <= 1:
        return datos
    mitad = len(datos) // 2
    izquierda = mezcla_paralela(datos[:mitad])
    derecha = mezcla_paralela(datos[mitad:])
    return combinar_bloques(izquierda, derecha)
