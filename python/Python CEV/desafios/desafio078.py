números = []
pos_maior = []
pos_menor = []
for i in range(0, 5):
    números.append(int(input(f'Digite um valor para a Posição {i}: ')))
for i in range(0, len(números)):
    if números[i] == max(números):
        pos_maior.append(i)
    if números[i] == min(números):
        pos_menor.append(i)

print('=-'*15)
print(f'Você digitou os valores {números}')
print(f'O maior valor digitado foi {max(números)} nas posições ', end='')
for i in range(0, len(pos_maior)):
    print(f'{pos_maior[i]}...', end=' ')
print(f'\nO menor valor digitado foi {min(números)} nas posições ', end='')
for i in range(0, len(pos_menor)):
    print(f'{pos_menor[i]}...', end=' ')
