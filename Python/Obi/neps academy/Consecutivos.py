n = int(input())
numeros = list(map(int, input().split()))
pontos = repeticoes = 1
for i in range(0, n):
    if numeros[i] == numeros[i-1]:
        repeticoes += 1
        if repeticoes > pontos:
            pontos = repeticoes
    else:
        repeticoes = 1
print(pontos)
