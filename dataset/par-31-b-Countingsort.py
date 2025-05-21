def conteo_ordenado(lista):
    mayor = max(lista)
    frecuencia = [0] * (mayor + 1)
    resultado = [0] * len(lista)

    for elemento in lista:
        frecuencia[elemento] += 1

    for i in range(1, len(frecuencia)):
        frecuencia[i] += frecuencia[i - 1]

    for elemento in reversed(lista):
        resultado[frecuencia[elemento] - 1] = elemento
        frecuencia[elemento] -= 1

    return resultado
