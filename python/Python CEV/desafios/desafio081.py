valores = []
i = 0

while True:
    valores.append(int(input('Digite Um valor: ')))
    i += 1
    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

valores.sort(reverse=True)
print(f'\nVocê digitou {i} elementos')
print(f'Os Valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista!')
