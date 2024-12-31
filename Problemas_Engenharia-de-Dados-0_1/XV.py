# Questão 15: Verificar se um número é primo.
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero_primo = 17
print(f"O número {numero_primo} é primo? {eh_primo(numero_primo)}")
