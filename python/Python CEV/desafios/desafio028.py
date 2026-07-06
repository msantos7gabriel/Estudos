from random import randint
from time import sleep

num = randint(0, 5)
user_input = int(input('Escreva Um Número'))
print("Processando...")
sleep(3)
if user_input == num:
    print('Você Venceu')
else:
    print('Você Perdeu')
