primeiro = int(input('Escreva o Primeiro termo da P.A.: '))
razao = int(input('Escreva a Razão da P.A.: '))

for i in range(0, 11):
    print('{}. Termo: {} '.format(i, primeiro))
    primeiro += razao
