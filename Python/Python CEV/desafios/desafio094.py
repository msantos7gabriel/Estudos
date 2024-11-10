pessoa = {}
grupo = []

while True:
    pessoa['nome'] = str(input('Nome: ').capitalize())
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        continuar = str(
            input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas.')
media = soma = 0

for g in grupo:
    soma += g['idade']

media = round(soma / len(grupo), 2)
print(f'- A média de idade é de {media} anos.')
print('- As Mulheres cadastradas foram: ', end=' ')

for g in grupo:
    if g['sexo'] == 'F':
        print(g['nome'], end=' ')

print()
print('- Lista das pessoas que estão em cima da média: ')

for g in grupo:
    if g['idade'] > media:
        print()
        print(f'nome = {g['nome']}; sexo = {g['sexo']}; idade = {g['idade']}')

print('<<< ENCERRADO >>>')
