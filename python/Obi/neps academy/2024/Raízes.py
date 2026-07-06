from math import sqrt

int(input())
numeros = list(map(float, input().split()))
for n in numeros:
    print(f'{sqrt(n):.4f}')
