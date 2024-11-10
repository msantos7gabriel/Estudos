n = int(input())
frase = list(str(input()))

for i in range(1, n):
    if frase[i] == frase[i-1]:
        frase[i] = frase[i].upper()
        frase[i-1] = frase[i-1].upper()

for f in frase:
    print(f, end='')
