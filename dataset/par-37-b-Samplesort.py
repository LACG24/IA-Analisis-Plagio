def orden_muestreo(lista, divisiones=4):
    if not lista:
        return lista
    puntos = sorted(lista[::len(lista)//divisiones])
    grupos = [[] for _ in range(divisiones)]

    for elemento in lista:
        for i in range(len(puntos)):
            if elemento <= puntos[i]:
                grupos[i].append(elemento)
                break
        else:
            grupos[-1].append(elemento)

    resultado = []
    for grupo in grupos:
        resultado.extend(sorted(grupo))
    return resultado
