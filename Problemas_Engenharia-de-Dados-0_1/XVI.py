# Questão 16: Implementar uma função para encontrar o enésimo número da sequência de Fibonacci.
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10
print(f"O {n}º número da sequência de Fibonacci é: {fibonacci(n)}")
