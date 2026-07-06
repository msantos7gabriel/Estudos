lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno',
         15.90, 'Estojo', 25, 'Mochila', 120.32)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^30}')
print('-'*40)

for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}R${lista[i+1]:>7.2f}')
print('-'*40)
