num = []
coluna = []

for i in range(0, 3):
    for j in range(0, 3):
        num.append(int(input(f'digite um valor para [{i}, {j}]: ')))
    coluna.append(num[:])
    num.clear()
print('-='*20)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {coluna[i][j]:^5} ]', end=' ')
    print('\n')
