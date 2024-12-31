# Questão 4: Calcular a mediana de uma lista de números.
def calcular_mediana(numeros):
    numeros.sort()
    n = len(numeros)
    meio = n // 2
    if n % 2 == 0:
        return (numeros[meio - 1] + numeros[meio]) / 2
    else:
        return numeros[meio]

numeros = [10, 20, 30, 40, 50]
print(f"A mediana é: {calcular_mediana(numeros)}")
