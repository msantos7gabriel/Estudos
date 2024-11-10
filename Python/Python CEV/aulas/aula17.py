from ast import Del


num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
# num.pop(2)
# num.remove(2)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for i in range(0, len(valores)):
    valores.pop()

# for i in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a  # Cria uma ligação entre elas
print(f'\nLista A: {a}')
print(f'Lista B: {b}')
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')

b = a[:]  # Cria uma copia do valor de A para B
print(f'\nLista A: {a}')
print(f'Lista B: {b}')
b[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
