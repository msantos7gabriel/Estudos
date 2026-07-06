nome = []
idade = []
sexo = []

for i in range(0, 4):
    nome.append(str(input('Insira seu nome: ')))
    idade.append(int(input('Insira sua idade: ')))
    sexo.append(int(input('Insira seu sexo:\n 1 - Masculino\n 2 - Feminino\n')))

media_idade = sum(idade) / len(idade)
print('\nA media de idade é de {}'.format(media_idade))

idade_velho = 0
marcador = 0
for i in range(0, 4):
    if idade[i] < idade_velho:
        idade_velho = idade[i]
        marcador = i

print('O nome do homem mais velho é: {}'.format(nome[marcador]))

marcador = 0
for i in range(0, 4):
    if sexo == 2:
        if idade < 20:
            marcador += 1

print('{} Mulheres tem menos de 20 anos' .format(marcador))
