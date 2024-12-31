# Questão 14: Calcular o fatorial de um número.
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = 5
print(f"O fatorial de {numero} é: {calcular_fatorial(numero)}")
