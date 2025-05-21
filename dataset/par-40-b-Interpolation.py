def busqueda_interpolada(lista, objetivo):
    inferior = 0
    superior = len(lista) - 1

    while inferior <= superior and objetivo >= lista[inferior] and objetivo <= lista[superior]:
        pos = inferior + ((objetivo - lista[inferior]) * (superior - inferior) // (lista[superior] - lista[inferior]))

        if lista[pos] == objetivo:
            return pos
        elif lista[pos] < objetivo:
            inferior = pos + 1
        else:
            superior = pos - 1
    return -1
