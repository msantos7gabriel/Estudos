import datetime
nascimento = []
menor = 0
maior = 0
for i in range(0, 6):
    nascimento.append(int(input('Insira seu ano de nascimento: ')))
    idade = datetime.datetime.now().year - nascimento[i]
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Menores de idade: {}, Maiores de idade {}'.format(menor, maior))
