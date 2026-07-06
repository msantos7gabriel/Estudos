vel = int(input('Qual sua Velocidade: '))
if vel > 80:
    print('Voce Foi Multado em R${}'.format((vel - 80)*7))
else:
    print('Você não foi multado')
