esquerda = int(input())
direita = int(input())

if esquerda > direita:
    resultado = esquerda + direita
else:
    resultado = 2 * (direita - esquerda)

print(resultado)
