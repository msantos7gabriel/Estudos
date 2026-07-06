lista = []
for i in range(9):
    lista.append(int(input()))
print(f'Coluna 0: {lista[0]+lista[3]+lista[6]}')
print(f'Coluna 1: {lista[1]+lista[4]+lista[7]}')
print(f'Coluna 2: {lista[2]+lista[5]+lista[8]}')