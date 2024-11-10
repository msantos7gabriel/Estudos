from random import randint
valores = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram', end=' ')
for i in range(0, len(valores)):
    print(valores[i], end=' ')
print(f'\nO Maior valor sorteado foi {max(valores)}')
print(f'O Menor valor sorteado foi {min(valores)}')
