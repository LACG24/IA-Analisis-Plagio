def ajustar_heap(lista, tam, raiz):
    mayor = raiz
    izquierda = 2 * raiz + 1
    derecha = 2 * raiz + 2

    if izquierda < tam and lista[izquierda] > lista[mayor]:
        mayor = izquierda
    if derecha < tam and lista[derecha] > lista[mayor]:
        mayor = derecha

    if mayor != raiz:
        lista[raiz], lista[mayor] = lista[mayor], lista[raiz]
        ajustar_heap(lista, tam, mayor)

def ordenar_heap(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        ajustar_heap(lista, n, i)

    for j in range(n - 1, 0, -1):
        lista[j], lista[0] = lista[0], lista[j]
        ajustar_heap(lista, j, 0)
    return lista
