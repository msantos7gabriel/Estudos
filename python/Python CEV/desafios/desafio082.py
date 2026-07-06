valores = []

while True:
    valores.append(int(input('Digite Um valor: ')))
    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break


impar = []
par = []
for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        par.append(valores[i])
    else:
        impar.append(valores[i])

print('-='*15)
print(f'A Lista completa é {valores}')
print(f'A Lista de pares é {par}')
print(f'A Lista de ímpares é {impar}')
