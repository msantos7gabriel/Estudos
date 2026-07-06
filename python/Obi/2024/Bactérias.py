maximo_bactérias = int(input())
n = int(input())
n1 = n
contador = 0

while True:
    if n <= maximo_bactérias:
        n *= n1
        contador += 1
    else:
        break
print(contador)
