numeros = []
soma = 0
size = int(input())
for i in range(0, size):
    n = int(input())
    if n != 0:
        numeros.append(n)
    else:
        numeros.pop()

for num in numeros:
    soma += num
print(soma)
