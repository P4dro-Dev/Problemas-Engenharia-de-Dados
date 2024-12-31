# Questão 7: Contar a frequência de cada elemento em uma lista.
from collections import Counter

def contar_frequencia(lista):
    return Counter(lista)

lista = [10, 20, 30, 40, 50, 10, 20, 10]
print(f"A frequência dos elementos é: {contar_frequencia(lista)}")
