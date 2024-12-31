# Questão 1: Calcular a média de uma lista de números.
def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

numeros = [10, 20, 30, 40, 50]
print(f"A média é: {calcular_media(numeros)}")
