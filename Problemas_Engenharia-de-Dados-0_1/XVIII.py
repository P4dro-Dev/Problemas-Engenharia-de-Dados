# Questão 18: Verificar se uma lista está ordenada em ordem crescente.
def esta_ordenada(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

lista = [1, 2, 3, 4, 5]
print(f"A lista está ordenada? {esta_ordenada(lista)}")
