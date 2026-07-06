pessoas = []
dados = []
pesadas = []
leves = []
maior = menor = 0

while True:
    dados.append(str(input('\nNome: ').strip()))
    dados.append(int(input('Peso: ').strip()))
    pessoas.append(dados[:])
    if maior < dados[1]:
        maior = dados[1]
    if menor == 0:
        menor = dados[1]
    elif menor > dados[1]:
        menor = dados[1]

    dados.clear()

    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

for i in range(0, len(pessoas)):
    j = 1
    while j+1 < len(pessoas):
        if pessoas[i][j] == maior:
            pesadas.append(pessoas[i][j-1])
        j += 2

for i in range(0, len(pessoas)):
    j = 1
    while j+1 < len(pessoas):
        if pessoas[i][j] == menor:
            leves.append(pessoas[i][j-1])
        j += 2

print('=-'*20)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pesadas:
    print(f'[{p}]', end=" ")

print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')
for p in leves:
    print(f'[{p}]', end=" ")
