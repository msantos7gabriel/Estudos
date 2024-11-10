pessoas_sexo = []
pessoas_idade = []
while True:
    print('-'*30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-'*30)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('Escreva um valor valido!')
    pessoas_sexo.append(sexo)
    pessoas_idade.append(idade)
    print('-'*30)
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Escreva um valor valido!')
    if continuar == 'N':
        break

n = count = 0
while len(pessoas_idade) > n:
    if pessoas_idade[n] > 18:
        count += 1
    n += 1
print(f'Total de pessoas com mais de 18 anos: {count}')

n = count = 0
while len(pessoas_sexo) > n:
    if pessoas_sexo[n] == 'M':
        count += 1
    n += 1
print(f'Ao todo temos {count} Homens cadastrados')

n = count = 0
while len(pessoas_sexo) > n:
    if pessoas_sexo[n] == 'F':
        if pessoas_idade[n] < 20:
            count += 1
    n += 1
print(f'E temos {count} Mulheres com menos de 20 anos')
