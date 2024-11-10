numeros = []

for i in range(9):
    numeros.append(int(input()))

l1 = numeros[0]+numeros[1]+numeros[2]
l2 = numeros[3]+numeros[4]+numeros[5]
l3 = numeros[6]+numeros[7]+numeros[8]
print(f'Linha 0: {l1}')
print(f'Linha 1: {l2}')
print(f'Linha 2: {l3}')