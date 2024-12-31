# Questão 10: Encontrar o elemento mais frequente em uma lista.
def elemento_mais_frequente(lista):
    frequencia = Counter(lista)
    return frequencia.most_common(1)[0][0]

lista = [10, 20, 30, 40, 50, 10, 20, 10]
print(f"O elemento mais frequente é: {elemento_mais_frequente(lista)}")

