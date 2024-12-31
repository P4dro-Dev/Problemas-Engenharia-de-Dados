# Questão 8: Normalizar uma lista de números (min-max normalization).
def normalizar(numeros):
    min_val = min(numeros)
    max_val = max(numeros)
    return [(x - min_val) / (max_val - min_val) for x in numeros]

numeros = [10, 20, 30, 40, 50]
print(f"A lista normalizada é: {normalizar(numeros)}")
