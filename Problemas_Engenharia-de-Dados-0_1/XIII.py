# Questão 13: Verificar se uma string é um palíndromo.
def eh_palindromo(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

palavra = "A man, a plan, a canal, Panama"
print(f"A string é um palíndromo? {eh_palindromo(palavra)}")
