# Questão 9: Encontrar o segundo maior número em uma lista.
def segundo_maior(lista):
    primeiro, segundo = float('-inf'), float('-inf')
    for numero in lista:
        if numero > primeiro:
            segundo = primeiro
            primeiro = numero
        elif primeiro > numero > segundo:
            segundo = numero
    return segundo

lista = [10, 20, 30, 40, 50]
print(f"O segundo maior número é: {segundo_maior(lista)}")

