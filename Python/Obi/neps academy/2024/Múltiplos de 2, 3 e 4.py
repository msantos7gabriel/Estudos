numeros = []
n = int(input())

m2 = m3 = m4 = 0

for i in range(n):
    numeros.append(int(input()))

for n in numeros:
    if n % 2 == 0:
        m2 += 1
    if n % 3 == 0:
        m3 += 1
    if n % 4 == 0:
        m4 += 1
print(m2)
print(m3)
print(m4)