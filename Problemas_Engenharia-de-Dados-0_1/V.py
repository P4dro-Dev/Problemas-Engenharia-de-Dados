# Questão 5: Calcular a moda de uma lista de números.
from collections import Counter

def calcular_moda(numeros):
    frequencia = Counter(numeros)
    moda = frequencia.most_common(1)[0][0]
    return moda

numeros = [10, 20, 30, 40, 50, 10, 20, 10]
print(f"A moda é: {calcular_moda(numeros)}")
