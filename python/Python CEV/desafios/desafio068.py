from random import randint

print('=-'*15)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
print('=-'*15)
escolha = count = 0
while True:
    while True:
        escolha = int(input('Diga um valor: '))
        if escolha <= 10:
            break
        print('Escreva um valor entre 0 e 10 (não sei se vc sabe mas vc tem apenas 10 dedos na mão)\n')
    while True:
        impar_ou_par = str(input('Par Ou Ímpar ? [P/I] ')).strip().upper()[0]
        if impar_ou_par in 'PI':
            break
        print('Escreva um valor valido!')
    print('=-'*15)
    bot_number = randint(0, 10)
    verificar = escolha + bot_number
    print('Você Jogou {} e o computador {}. o Total de {}'.format(
        escolha, bot_number, verificar), end='')
    if verificar % 2 == 0:
        verificar = 'PAR'
    else:
        verificar = 'IMPAR'
    print(f' deu {verificar}')
    if impar_ou_par == verificar[0]:
        print("Voce Ganhou!")
        print("Vamos Jogar novamente...")
        count += 1
    else:
        print("Voce Perdeu!")
        break
    print('=-'*15)
print(f'GAME OVER! Você Venceu {count} vezes.')
