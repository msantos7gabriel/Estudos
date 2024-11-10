matriz = []
linha = []
soma_principal = soma_invertida = 0

for i in range(3):
    for j in range(3):
        linha.append(int(input()))
    matriz.append(linha[:])
    linha.clear()

for i in range(3):
    for j in range(3):
        if i == j:
            soma_principal += matriz[i][j]

print(f'Diagonal principal: {soma_principal}')

i = 0
j = len(matriz)-1
while i != 3:
    soma_invertida += matriz[i][j]
    j -= 1
    i += 1
print(f'Diagonal secundaria: {soma_invertida}')
