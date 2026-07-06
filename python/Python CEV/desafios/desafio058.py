from random import randint
from time import sleep
print('-- Bem Vindo ao jogo da Adivinhação --')
sleep(1)
num = randint(0, 10)
print("Processando...")
sleep(3)
tentativas = 0
user_input = ''
while user_input != num:
    user_input = int(input('Escreva Um Número entre 1 e 10: '))
    if user_input == num:
        print('Você Acertou')
    else:
        if user_input < num:
            print("Mais... Tente Novamente")
        else:
            print('Menos... Tente Novamente')
    tentativas += 1
print('Você descobriu em: {}'.format(tentativas))
