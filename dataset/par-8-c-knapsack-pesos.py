def mochila_binaria(hijos, capacidad, val1, val2):
    base = sum(min(val1[n], val2[n]) for n in hijos)
    if base > capacidad:
        return -1
    margen = capacidad - base
    posibles = set([0])
    for n in hijos:
        diff = abs(val1[n] - val2[n])
        nuevos = set(posibles)
        for total in posibles:
            if total + diff <= margen:
                nuevos.add(total + diff)
        posibles = nuevos
    suma_total = sum(val1[n] + val2[n] for n in hijos)
    return suma_total - max(posibles) - base

N = int(input())
padres = list(map(int, input().split()))
pesos = list(map(int, input().split()))

estructura = [[] for _ in range(N + 1)]
for idx in range(2, N + 1):
    estructura[padres[idx - 2]].append(idx)

valorA = [0] + pesos
valorB = [0] * (N + 1)
resultado = "POSSIBLE"

for nodo in reversed(range(1, N + 1)):
    if len(estructura[nodo]) == 0:
        continue
    elif len(estructura[nodo]) == 1:
        hijo = estructura[nodo][0]
        if min(valorA[hijo], valorB[hijo]) > pesos[nodo - 1]:
            resultado = "IMPOSSIBLE"
            break
        elif max(valorA[hijo], valorB[hijo]) > pesos[nodo - 1]:
            valorB[nodo] = max(valorA[hijo], valorB[hijo])
        else:
            valorB[nodo] = min(valorA[hijo], valorB[hijo])
    else:
        carga = mochila_binaria(estructura[nodo], pesos[nodo - 1], valorA, valorB)
        if carga < 0:
            resultado = "IMPOSSIBLE"
            break
        valorB[nodo] = carga

print(resultado)
