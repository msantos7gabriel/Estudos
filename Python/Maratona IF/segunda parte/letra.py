letra = str(input())
frase = list(map(str, input().split()))
contador = 0
for f in frase:
    if letra in f:
        contador += 1

print(round(contador/len(frase) * 100, 1))
