valores = []

while True:
    val = int(input("\nDigite um valor: "))
    if val not in valores:
        valores.append(val)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')
