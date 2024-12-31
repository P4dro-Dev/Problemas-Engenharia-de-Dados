# Questão 6: Remover duplicatas de uma lista.
def remover_duplicatas(lista):
    return list(set(lista))

lista = [10, 20, 30, 40, 50, 10, 20, 10]
print(f"A lista sem duplicatas é: {remover_duplicatas(lista)}")
