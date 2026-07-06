impares = []
pares = []

for i in range(10):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

for p in pares:
    print(p, end=' ')
print()
for i in impares:
    print(i, end=' ')
