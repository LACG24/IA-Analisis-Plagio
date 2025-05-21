class Nodo:
    def __init__(self, valor):
        self.izquierda = None
        self.derecha = None
        self.valor = valor

def agregar(arbol, elemento):
    if arbol is None:
        return Nodo(elemento)
    if elemento < arbol.valor:
        arbol.izquierda = agregar(arbol.izquierda, elemento)
    else:
        arbol.derecha = agregar(arbol.derecha, elemento)
    return arbol

def recorrido_inorden(nodo, acumulado):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda, acumulado)
        acumulado.append(nodo.valor)
        recorrido_inorden(nodo.derecha, acumulado)

def ordenar_por_arbol(lista):
    raiz = None
    for numero in lista:
        raiz = agregar(raiz, numero)
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado
