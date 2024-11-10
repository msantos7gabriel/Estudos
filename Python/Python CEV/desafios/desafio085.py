number = []
pares = []
impares = []
for i in range(0, 7):
    number.append(int(input(f'Digite o {i+1}°. Valor: ')))
    if number[0] % 2 == 0:
        pares.append(number[0])
    else:
        impares.append(number[0])
    number.clear()
pares.sort()
impares.sort()
print('-='*20)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
