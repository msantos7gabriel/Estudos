letra = str(input())
palavras = list(map(str, input().split()))
vezes = 0

for p in palavras:
    if letra in p:
        vezes += 1

print(round(vezes/len(palavras)*100, 1))
