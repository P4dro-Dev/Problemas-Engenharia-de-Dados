# Questão 11: Calcular a matriz de confusão para um conjunto de previsões e rótulos reais.
def calcular_matriz_confusao(previsoes, reais):
    matriz = {}
    for p, r in zip(previsoes, reais):
        if r not in matriz:
            matriz[r] = {}
        if p not in matriz[r]:
            matriz[r][p] = 0
        matriz[r][p] += 1
    return matriz

previsoes = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
reais = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
matriz_confusao = calcular_matriz_confusao(previsoes, reais)
print(f"A matriz de confusão é: {matriz_confusao}")
