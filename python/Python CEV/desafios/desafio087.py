num = []
coluna = []
soma_pares = soma_terceira = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        num.append(int(input(f'digite um valor para [{i}, {j}]: ')))
    coluna.append(num[:])
    num.clear()

print('-='*20)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {coluna[i][j]} ]', end=' ')
        if coluna[i][j] % 2 == 0:
            soma_pares += coluna[i][j]
        if j == 2:
            soma_terceira += coluna[i][j]
        if i == 1:
            if maior < coluna[i][j]:
                maior = coluna[i][j]
    if i != 2:
        print('\n')


print('\n')
print('-='*20)
print(f'A Soma dos valores pares é {soma_pares}.')
print(f'A Soma dos valores da terceira coluna é {soma_terceira}.')
print(f'O maior valor da segunda linha é {maior}.')
