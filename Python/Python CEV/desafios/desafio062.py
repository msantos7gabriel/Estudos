primeiro = int(input('Escreva o Primeiro termo da P.A.: '))
razao = int(input('Escreva a Razão da P.A.: '))
i = 0
while i < 11:
    print('{}. Termo: {} '.format(i, primeiro))
    primeiro += razao
    i += 1

termos = 1
while termos != 0:
    termos = int(input('Quantos termos a mais voce gostaria ?: '))
    if termos == 0:
        break
    termos += i
    while i < termos:
        print('{}. Termo: {} '.format(i, primeiro))
        primeiro += razao
        i += 1
