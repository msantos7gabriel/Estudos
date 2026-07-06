primeiro = int(input('Escreva o Primeiro termo da P.A.: '))
razao = int(input('Escreva a Razão da P.A.: '))
i = 0

while i != 11:
    print('{}. Termo: {} '.format(i, primeiro))
    primeiro += razao
    i += 1
