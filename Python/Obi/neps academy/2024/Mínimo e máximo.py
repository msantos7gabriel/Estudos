s = int(input())
a = int(input())
b = int(input())

for i in range(a, b):
    soma = 0
    for j in range(len(str(i))):
        i = str(i)
        soma += int(i[j])
    if s == soma:
        menor = i
        break


for i in range(b, a, -1):
    soma = 0
    for j in range(len(str(i))):
        i = str(i)
        soma += int(i[j])
    if s == soma:
        maior = i
        break

print(menor)
print(maior)
